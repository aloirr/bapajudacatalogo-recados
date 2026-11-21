"""T-0017 v22 (SIMULAÇÃO, nada é gravado na base): monta SIMULACAO_v22_T-0017.xlsx e numeros_v22.json.

Uso: python3 -I simular_v22.py <base.xlsx> <analise_v22.json> <pasta_saida>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

TAREFA, DATA = "T-0017", "21/11/2026"
ORIGEM = "R-20261120-221700-alexandre ('1) a')"
P1_COD = "ELE1092"                     # 4 linhas já 'duvidoso' (marca: 'VOLKSWAGEM'/FORD), a faixa é provada
P2 = ("ELE1068", "Uno", 2700, "19/84->1995", "1984->1995", 1995, 1984, 1995)


def limpa(t):
    return re.sub(r"\s+", " ", re.sub(r"(^|\n)\s*T\s*\n", r"\1", t)).strip(" T")


def main(base, analise, saida):
    saida = Path(saida)
    a = json.load(open(analise))
    wb = openpyxl.load_workbook(base, read_only=True)
    apl = {str(r[0]).strip(): str(r[2] or "") for r in wb["PRODUTOS"].iter_rows(min_row=2, values_only=True)
           if r[0] is not None}
    vrow = {n: r for n, r in enumerate(wb["VEICULOS"].iter_rows(min_row=2, values_only=True), 2) if n == P2[2]}
    wb.close()
    sha = hashlib.sha256(Path(base).read_bytes()).hexdigest()

    muda, ficam = [], []
    for l in a["linhas"]:
        prova = " ‖ ".join(limpa(t) for t in l["trechos"])
        so_duv = l["motivo"] == ["SITUACAO 'duvidoso'"]
        if not l["motivo"] or (so_duv and l["cod"] == P1_COD):
            muda.append(dict(l, prova=prova, entra="sim" if not l["motivo"] else "só com P1 = a"))
        else:
            ficam.append(dict(l, prova=prova))
    # P2: Uno do ELE1068 ('19/84->1995')
    v = vrow[P2[2]]
    assert (v[0], v[2], v[3], v[4], v[5]) == (P2[0], P2[1], None, P2[5], None), v
    assert apl[P2[0]].count(P2[3]) == 1

    cel = []   # (cod, aba, linha, coluna, fab, modelo, versao, ini, antes, depois, forma, prova, situacao, entra)
    for m in muda:
        cel.append((m["cod"], "VEICULOS", m["linha"], "ANO_FIM", m["fab"], m["modelo"], m["versao"], m["ini"], None,
                    m["fim"], ", ".join(m["formas"]), m["prova"], m["situacao"], m["entra"]))
    tre = "Uno 1.1 Brio/1.3/1.5/1.6R 19/84->1995"
    cel.append((P2[0], "PRODUTOS", None, "APLICACAO", None, None, None, None, tre, tre.replace("19/84", "1984"),
                "->", "'19/84' -> '1984' (só esse trecho da célula muda)", None, "só com P2 = a"))
    cel.append((P2[0], "VEICULOS", P2[2], "ANO_INICIO", v[1], v[2], None, P2[5], P2[5], P2[6], "->", tre, v[7],
                "só com P2 = a"))
    cel.append((P2[0], "VEICULOS", P2[2], "ANO_FIM", v[1], v[2], None, P2[5], None, P2[7], "->", tre, v[7],
                "só com P2 = a"))

    log = []
    for c in cel:
        cod, aba, n, col, fab, mod, ver, ini, antes, depois, forma, prova, sit, entra = c
        q = "" if entra == "sim" else f" [{entra}]"
        if aba == "PRODUTOS":
            obs = (f"APLICACAO: '{antes}' -> '{depois}' (ano de 4 dígitos digitado como '19/84'; o resto da célula não "
                   f"muda).")
            tipo = "CORRECAO_APLICACAO"
        else:
            nome = mod + (f" {ver}" if ver else "")
            if col == "ANO_FIM" and cod != P2[0]:
                obs = (f"ANO_FIM do {nome} (linha {n}): vazio (= em diante, {ini}+) -> {depois} ({ini}–{depois}). "
                       f"Prova na APLICACAO: '{prova}' (o '{forma}' entre dois anos é a faixa).")
            elif col == "ANO_INICIO":
                obs = (f"ANO_INICIO do {nome} (linha {n}): {antes} -> {depois}. Prova na APLICACAO: '{prova}' "
                       f"('19/84' é 1984).")
            else:
                obs = (f"ANO_FIM do {nome} (linha {n}): vazio (= em diante) -> {depois} ({P2[6]}–{depois}). Prova "
                       f"na APLICACAO: '{prova}'.")
            tipo = "CORRECAO_VEICULO"
        log.append((tipo, aba, cod, None, f"{obs} Nada marcado como duvidoso. Aprovado em <recado do Alexandre>"
                    f"{q}. {TAREFA} (v22), {DATA}"))

    sem_veic = [(c, "; ".join(m.group(0) for m in re.finditer(
        r"[^,;\n|]{0,40}(?:19|20)\d{2}\s*(?:-\s*>|–\s*>|→|>)\s*(?:19|20)\d{2}", apl[c]))) for c in a["sem_veiculos"]]
    formas = {"->": 0, ">": 0, "> (com espaço)": 0, "→": 0, "- > / –>": 0}
    cods_forma = {k: set() for k in formas}
    for c, t in apl.items():
        for m in re.finditer(r"(?<!\d)(?:19|20)\d{2}(\s*(?:-\s*>|–\s*>|→|>)\s*)(?:19|20)\d{2}", t):
            s = m.group(1)
            k = ("->" if s == "->" else ">" if s == ">" else "> (com espaço)" if s.strip() == ">" else
                 "→" if "→" in s else "- > / –>")
            formas[k] += 1
            cods_forma[k].add(c)

    n_sim = sum(1 for c in cel if c[-1] == "sim")
    num = {"base_sha256": sha, "codigos_com_seta": len(a["codigos_com_seta"]),
           "ocorrencias_por_forma": formas, "codigos_por_forma": {k: len(v) for k, v in cods_forma.items()},
           "celulas_sim": n_sim, "linhas_veiculos_sim": n_sim, "codigos_sim": len({c[0] for c in cel if c[-1] == "sim"}),
           "celulas_P1": sum(1 for c in cel if c[-1] == "só com P1 = a"),
           "celulas_P2": sum(1 for c in cel if c[-1] == "só com P2 = a"),
           "ficam": len(ficam), "codigos_sem_veiculos": len(sem_veic), "log_previsto": len(log)}

    out = openpyxl.Workbook()
    b = Font(bold=True)
    amarelo = PatternFill("solid", fgColor="FFF2CC")
    ws = out.active
    ws.title = "LEIA"
    leia = [
        [f"SIMULAÇÃO da v22 da base unificada ({TAREFA}). Nada foi gravado: sem versão nova, sem commit."],
        [f"Fonte: v21 (main 39477d6), sha256 {sha[:8]}…{sha[-4:]}. Data: {DATA} (Manaus). Pedido: {ORIGEM}."],
        ["O que muda: na aba VEICULOS, o ANO_FIM das linhas em que a faixa 'AAAA->AAAA' (e variações: 'AAAA>AAAA', "
         "'AAAA - > AAAA', 'AAAA→AAAA') da APLICACAO virou ano aberto (ANO_FIM vazio = em diante)."],
        ["Regra (R-20261120-213300): nada novo marcado nem escrito como duvidoso; o fim só entra quando o texto "
         "prova a faixa. Por isso fica como está a linha em que o mesmo veículo tem outro trecho aberto no texto "
         "(ex.: 'Fiorino 1992>' e 'Fiorino 750 kg 2008>2010'), e o ANO_FIM é o maior fim das faixas do veículo."],
        ["ENTRA: 'sim' = entra com o aprovado; 'só com P1 = a' / 'só com P2 = a' = depende da pergunta (RESUMO.md)."],
        ["Sem preço, sem fornecedor e sem DADOS_ADICIONAIS nesta planilha."],
        [],
        ["ABA", "LINHAS", "CÓDIGOS", "O QUE É"],
        ["ANTES_DEPOIS", len(cel), len({c[0] for c in cel}), f"uma linha por célula: {n_sim} entram com o aprovado, "
         f"{num['celulas_P1']} dependem da P1 e {num['celulas_P2']} da P2"],
        ["FICAM", len(ficam), len({f['cod'] for f in ficam}), "linhas com a faixa de seta que NÃO mudam (o mesmo "
         "veículo tem outro trecho aberto no texto): informação"],
        ["SEM_VEICULOS", len(sem_veic), len(sem_veic), "códigos com a faixa de seta no texto, mas sem linha na "
         "VEICULOS: nada muda (informação)"],
        ["LOG_CORRECOES_PREVISTO", len(log), len({l[2] for l in log}), "uma linha por célula, como a P14 da v21"],
        [],
        ["FORMA NO TEXTO", "OCORRÊNCIAS", "CÓDIGOS", ""],
    ] + [[k, formas[k], len(cods_forma[k]), ""] for k in formas]
    for r in leia:
        ws.append(r)
    for r in (8, 14):
        for c in ws[r]:
            c.font = b
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["D"].width = 110

    cab = ["CODIGO_BAP", "ABA", "LINHA", "COLUNA", "FABRICANTE", "MODELO", "VERSAO", "ANO_INICIO_HOJE", "ANTES",
           "DEPOIS", "FORMA", "PROVA_NA_APLICACAO", "SITUACAO", "ENTRA"]
    ad = out.create_sheet("ANTES_DEPOIS")
    ad.append(cab)
    for c in cel:
        ad.append(["(vazio)" if (x is None and i == 8) else x for i, x in enumerate(c)])
        if c[-1] != "sim":
            for x in ad[ad.max_row]:
                x.fill = amarelo
    fi = out.create_sheet("FICAM")
    fi.append(["CODIGO_BAP", "LINHA", "FABRICANTE", "MODELO", "VERSAO", "ANO_INICIO", "ANO_FIM", "SITUACAO",
               "TRECHOS_DO_VEICULO", "POR QUE FICA"])
    for f in ficam:
        fi.append([f["cod"], f["linha"], f["fab"], f["modelo"], f["versao"], f["ini"], "(vazio)", f["situacao"],
                   f["prova"], "; ".join(f["motivo"])])
    sv = out.create_sheet("SEM_VEICULOS")
    sv.append(["CODIGO_BAP", "TRECHOS_COM_SETA"])
    for r in sem_veic:
        sv.append(list(r))
    lg = out.create_sheet("LOG_CORRECOES_PREVISTO")
    lg.append(["TIPO", "ABA", "CODIGO_ANTES_OU_NOVO", "CODIGO_REFERENCIA", "OBSERVACAO"])
    for r in log:
        lg.append(list(r))
    for s in out.worksheets[1:]:
        for c in s[1]:
            c.font = b
        s.freeze_panes = "A2"
        s.auto_filter.ref = s.dimensions
        for col in s.columns:
            w = max(len(str(x.value or "")) for x in col)
            s.column_dimensions[col[0].column_letter].width = min(max(10, w + 2), 90)
        for row in s.iter_rows(min_row=2):
            for x in row:
                x.alignment = Alignment(vertical="top", wrap_text=True)
    out.save(saida / "SIMULACAO_v22_T-0017.xlsx")
    json.dump(num, open(saida / "numeros_v22.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps(num, ensure_ascii=False))
    for c in cel:
        print(c[0], c[2], c[3], c[5], c[6] or "", c[8], "->", c[9], c[-1])


if __name__ == "__main__":
    main(*sys.argv[1:4])
