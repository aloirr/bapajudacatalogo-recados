# T-0017 · v23 da base unificada: SIMULAÇÃO

Pedido: R-20261120-235000-alexandre, item 1.3 ("v23: CRU100 com os dados do LOG da v21, SCE14002 '1929–19321934' e FAC6108 'em Diante' sem ano").
- Base de partida: v22 do main 6f7b7af (sha256 `0c403c37…54ba`).
- Aprovação antecipada desta rodada: a simulação segue a recomendação do dono e do gerente.
- Regra fixa (R-20261120-213300): nada novo marcado nem escrito como duvidoso.

## Antes e depois (4 células, 2 códigos)

| Código | Aba · linha | Coluna | Antes | Depois |
|---|---|---|---|---|
| CRU100 | PRODUTOS · 2447 | APLICACAO | Hyunday HR (07/2017), Kia Motors Bongo 2500 (07/2017) | Hyundai HR 2.5 4x2 (04/2007–12/2017), Kia Motors Bongo 2500 (07/2017) |
| FAC6108 | VEICULOS · 8950 (MITSUBISHI Eclipse Cross) | ANO_INICIO | 2009 | (vazio) |
| FAC6108 | VEICULOS · 8950 | ANO_FIM | 2012 | (vazio) |
| FAC6108 | VEICULOS · 8950 | ANO_DUVIDA | herdado: o ano vem depois de outro modelo da lista | (vazio) |

## Os três casos

**1. CRU100: entra (a).**
- O LOG_CORRECOES da v21 guarda, na linha LINHA_REMOVIDA "HYUNDAI", a tabela de aplicação de origem: HR, Ano 04/07 - 12/17, Tração 4x2, Motor 2.5.
- a) Trocar só o trecho da Hyundai: "Hyunday HR (07/2017)" → "Hyundai HR 2.5 4x2 (04/2007–12/2017)". **Recomendo**: o ano, a tração e o motor vêm da tabela de origem. "Hyunday" é a grafia errada de Hyundai, já apontada na T-0007.
- b) Deixar como está.
- O trecho da Kia ("Kia Motors Bongo 2500 (07/2017)") fica. A linha KIA MOTORS da origem (Bongo, K2500, Cardan A) não tem ano.

**2. SCE14002: nada muda na base.**
- O "1929–19321934" já virou "1929 · 1932 · 1934" na v21 (P2 a, com a linha no LOG_CORRECOES). O texto de hoje é "Servo Embreagem Mbb LS 1630 1929 · 1932 · 1934 LS1941 Vwc 16210 17240 1730 · 111693".
- A VEICULOS (LS 1630 e LS 1941) não tem texto quebrado.
- O texto antigo só continua em `catalogo_grafico/gerador/digital_data.json` (do `catalogo-grafico`), lido pelo `digital2.py`. O mesmo vale para o "Eclipse Cross 1.5 L 16V · em Diante" do FAC6108.

**3. FAC6108: entra a forma neutra (b).**
- O "em Diante" sem ano já saiu da APLICACAO na v21 (P5 a: "o veículo fica sem ano"). O texto não tem ano para a Eclipse Cross.
- Na VEICULOS, a Eclipse Cross ficou com 2009–2012, que é o ano da Outlander, a seguinte na lista ("Eclipse Cross 1.5 L 16V · Outlander 2.0 L 16V 2009–2012").
- a) Pôr um ano inicial. Não há ano no texto.
- b) Forma neutra: ANO_INICIO, ANO_FIM e ANO_DUVIDA vazios, e a Eclipse Cross fica sem ano, como a APLICACAO. **Recomendo**: não inventa ano e não marca nada novo.
- O site não leva os anos da VEICULOS: o `produtos.json` não muda por causa disso.

## Ficam de fora (para a volta do Alexandre)
- **CRU100, trecho da Kia:** o "(07/2017)" fica. Não há fonte para ele nem para outro ano.
- **CRU100, Hyundai HR na VEICULOS:** não há linha da HR. Pôr uma linha nova é a decisão da P12 da v21 (linhas novas na VEICULOS), que não entrou.
- **CRU100, Embalagem (90 x 90 x 35 mm) e Cardan (- e A):** não são aplicação. Continuam só no LOG_CORRECOES.
- **SCE14002, LS 1929, 1932 e 1934 na VEICULOS:** seriam linhas novas (P12 da v21).

## Formato
- Mesmas abas e colunas da v22. Nenhuma linha nova na VEICULOS e nenhum produto sai.
- Previsto no LOG_CORRECOES: 4 linhas, uma por célula.
- O LEIA-ME ganha o bloco da v23 no topo.

## Arquivos
- `SIMULACAO_v23_T-0017.xlsx`, com as abas LEIA, ANTES_DEPOIS (lida pelo `dados/scripts/base_v23.py`) e FORA.
- `numeros_v23.json`: as contagens.
- `simular_v23.py`: o script, que só lê a base (`python3 -I simular_v23.py <base.xlsx> <pasta_saida>`).
