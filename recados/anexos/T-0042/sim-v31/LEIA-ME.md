# T-0042 · simulação da v31 (correções pontuais da base)

Branch `catalogo-dados/T-0042-v31`, commit f6e8957. É só simulação: a base real continua na v30 e não há v31 em `dados/versoes/`.

## Arquivos
- `antes_depois_v31.xlsx`: abas RESUMO, MUDANCAS (antes, depois e fonte de cada célula), SEM_FONTE, DO_SITE, PONTOS_ALEXANDRE (P1 a P10, com a/b) e EFEITO_SITE.
- Prints (antes = site da v30; depois = simulação), em 1366 e 390 px:
  - `antes-/depois-<CÓDIGO>-<largura>.png`: LAM2004, POL1712, CRU5280, CRU512022;
  - `…-v2.png`: VEL7520, ROL15106 (ROL15106/15250) e SFR30034, mais as buscas "vela palio 2005", "vela astra 2010", "rolamento a-40 1990" e "bongo k-2700 2000".

## Resumo
- 61 células da VEICULOS mudam, saem 2 linhas e entram 6; a PRODUTOS e a APLICACAO não mudam.
- A marca da revisão da P12 cai de 5.397 para 5.382, e nada novo é marcado.
- A simulação mostra a opção a) de todos os pontos.
- No site mudam 7 produtos: LAM2004, POL1712, VEL7520, ROL15106/15250, CRU5280, CRU512022 e SFR30034.
- Observação: no SFR30034, o print do "depois" não mostra o "K-2400", porque o site corta esse texto da Versão (aba DO_SITE).
