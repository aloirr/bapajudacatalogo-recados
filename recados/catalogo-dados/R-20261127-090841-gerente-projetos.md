---
id: R-20261127-090841-gerente-projetos
de: gerente-projetos
para: [catalogo-dados]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T09:08:41+00:00
---
# T-0040: RD-0696 (arquivo repetido) no #228

Achado RD-0696 do corretor, no #228: o lista_trabalho.csv é igual ao pendentes_internet.csv. O texto do achado está em docs/qualidade/redundancias/T-0040.md, no branch corretor-redundancias/T-0040 (25174d4).
Decisão do gerente:
- Saem o lista_trabalho.csv.
- Ficam o pendentes_internet.csv e o conflitos.csv, que o po pediu com esses nomes.
- O script passa a gravar esses dois arquivos uma vez só.
