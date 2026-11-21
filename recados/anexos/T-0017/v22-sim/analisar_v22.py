"""T-0017 v22 (simulação): a faixa 'AAAA->AAAA' (e variações) da APLICACAO que virou ano aberto na VEICULOS.

Lê a base (só leitura) e grava analise_v22.json com, para cada linha da VEICULOS de ANO_FIM vazio cujo modelo tem
pelo menos um trecho com a faixa de seta, os trechos da APLICACAO desse modelo e a decisão automática.
Uso: python3 -I analisar_v22.py <base.xlsx> <saida.json>
"""
import json
import re
import sys
import unicodedata

import openpyxl

ANO = r"(?:\d{1,2}/)?(?:19|20)\d{2}(?!\d)"
SETA = r"(?:-\s*>|–\s*>|=\s*>|→|>)"
TOKEN = re.compile(
    rf"(?<![\d.,/])(?P<fechada>{ANO}\s*(?P<sep>{SETA}|–|-|\ba\b|até|/)\s*{ANO})"
    rf"|(?<![\d.,/])(?P<aberta>{ANO}\s*(?:{SETA}|\+|em\s+diante))"
    rf"|(?P<ate>(?:(?<=\s)|^)(?:>|até)\s*{ANO})"
    rf"|(?<![\d.,/])(?P<solto>{ANO})", re.I)
ANO_RE = re.compile(r"(?:19|20)\d{2}(?!\d)")


def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return s


def trechos(texto):
    """[(veículo, tipo, ini, fim, forma, trecho)] na ordem do texto."""
    out, pos = [], 0
    for m in TOKEN.finditer(texto):
        veic = texto[pos:m.start()]
        tok = m.group(0)
        anos = [int(a) for a in ANO_RE.findall(tok)]
        if m.group("fechada"):
            sep = re.sub(r"\s", "", m.group("sep"))
            seta = bool(re.fullmatch(SETA.replace(r"\s*", ""), sep)) or sep in ("->", "–>", "=>", "→", ">")
            tipo, ini, fim, forma = "fechada", anos[0], anos[1], sep
            if not seta:
                forma = sep
        elif m.group("aberta"):
            tipo, ini, fim, forma = "aberta", anos[0], None, re.sub(r"\s", "", tok[len(m.group(0).split()[0]):]) or ">"
        elif m.group("ate"):
            tipo, ini, fim, forma = "ate", None, anos[0], ">AAAA"
        else:
            tipo, ini, fim, forma = "solto", anos[0], anos[0], ""
        out.append((veic, tipo, ini, fim, forma, (veic.strip(" ,;·\n") + " " + tok).strip()))
        pos = m.end()
    return out


def eh_seta(forma):
    return forma in ("->", "–>", "=>", "→", ">")


def casa(modelo, veic):
    return re.search(rf"(?<![a-z0-9]){re.escape(norm(modelo))}(?![a-z0-9])", norm(veic)) is not None


def main(base, saida):
    wb = openpyxl.load_workbook(base, read_only=True)
    wp = wb["PRODUTOS"]
    cab = [c.value for c in next(wp.iter_rows(max_row=1))]
    ia = cab.index("APLICACAO")
    aplic = {str(r[0]).strip(): str(r[ia] or "") for r in wp.iter_rows(min_row=2, values_only=True) if r[0] is not None}
    wv = wb["VEICULOS"]
    cabv = [c.value for c in next(wv.iter_rows(max_row=1))]
    veics = {}
    for n, r in enumerate(wv.iter_rows(min_row=2, values_only=True), 2):
        veics.setdefault(str(r[0]).strip(), []).append((n, dict(zip(cabv, r))))
    wb.close()
    sem_veic, linhas = [], []
    com_seta = {c: t for c, t in aplic.items() if any(x[1] == "fechada" and eh_seta(x[4]) for x in trechos(t))}
    for cod, texto in sorted(com_seta.items()):
        rows = veics.get(cod, [])
        if not rows:
            sem_veic.append(cod)
            continue
        tr = trechos(texto)
        modelos = sorted({v["MODELO"] for _, v in rows if v["MODELO"]}, key=lambda s: -len(s))
        # cada trecho vai para o modelo mais longo que casa, e para a versão que casa (ou a sem versão)
        dono = []
        for t in tr:
            m = next((md for md in modelos if casa(md, t[0])), None)
            alvo = None
            if m:
                cands = [(n, v) for n, v in rows if v["MODELO"] == m]
                comv = [(n, v) for n, v in cands if v["VERSAO"] and casa(v["VERSAO"], t[0])]
                semv = [(n, v) for n, v in cands if not v["VERSAO"]]
                alvo = (comv or semv or [None])[0]
            dono.append(alvo[0] if alvo else None)
        for n, v in rows:
            if v["ANO_FIM"] is not None:
                continue
            meus = [t for t, d in zip(tr, dono) if d == n]
            if not any(t[1] == "fechada" and eh_seta(t[4]) for t in meus):
                continue
            motivo, fim = [], None
            if any(t[1] in ("aberta", "ate") for t in meus):
                motivo.append("o mesmo veículo tem outro trecho aberto ou sem início no texto")
            inis = [t[2] for t in meus if t[2] is not None]
            fins = [t[3] for t in meus if t[3] is not None]
            if inis and min(inis) != v["ANO_INICIO"]:
                motivo.append(f"o ANO_INICIO de hoje ({v['ANO_INICIO']}) não é o do texto ({min(inis)})")
            if fins:
                fim = max(fins)
                if not any(t[1] == "fechada" and t[3] == fim for t in meus):
                    motivo.append(f"o ano final ({fim}) vem de um ano solto, não de uma faixa")
            if v["ANO_DUVIDA"]:
                motivo.append("a linha tem ANO_DUVIDA")
            if v["SITUACAO"] != "separado":
                motivo.append(f"SITUACAO '{v['SITUACAO']}'")
            linhas.append({"linha": n, "cod": cod, "fab": v["FABRICANTE"], "modelo": v["MODELO"],
                           "versao": v["VERSAO"], "ini": v["ANO_INICIO"], "fim": fim,
                           "situacao": v["SITUACAO"], "ano_duvida": v["ANO_DUVIDA"],
                           "formas": sorted({t[4] for t in meus if t[1] == "fechada"}),
                           "trechos": [t[5] for t in meus], "motivo": motivo})
    json.dump({"codigos_com_seta": sorted(com_seta), "sem_veiculos": sem_veic, "linhas": linhas}, open(saida, "w"),
              ensure_ascii=False, indent=1)
    for l in linhas:
        print(l["linha"], l["cod"], l["modelo"], l["versao"] or "", l["ini"], "->", l["fim"], l["situacao"][:3],
              l["formas"], "|", " ‖ ".join(l["trechos"])[:160], "|", "; ".join(l["motivo"]))
    print("códigos com seta:", len(com_seta), "sem VEICULOS:", sem_veic)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
