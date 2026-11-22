---
id: R-20261122-014756-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0017
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T01:47:56+00:00
---
# Pedido de autorização de merge: PR #104 no commit b8fc1a7ddf8905880814e9ad1559ff87ab98ef6d (base v27)

# PR #104: base unificada v27 (T-0017)

- **PR:** #104, do catalogo-dados. Branch catalogo-dados/T-0017-v27.
- **Head:** b8fc1a7ddf8905880814e9ad1559ff87ab98ef6d. Merge-tree com o main 67bcfc4: sem conflito.
- **Arquivos (10), todos em dados/:**
  - a base e a cópia dados/versoes/…_v27.xlsx, com o mesmo sha256 300284423c93…2018;
  - base_v27.py e base_comum.py;
  - a simulação aprovada (bb4de8d) com um README curto;
  - o README da v25.
  - Nenhum arquivo de governança.
- **CI no b8fc1a7:** conferir, site e GitGuardian em success.
- **O que muda:** 124 células da PRODUTOS, iguais à simulação:
  - 108 SISTEMA dos rolamentos (88 para TRANSMISSÃO e 20 para MOTOR);
  - 13 DETALHE_CATALOGO das embreagens pesadas;
  - 3 APLICACAO (SCE14002, TER55227 e TER5597056).
  - LOG_CORRECOES +124; LEIA-ME +7; digitado conservado; formato igual (a BAP Central não precisa de aviso); 'duvidoso' segue em 5.120.
- **Revisões:**
  - testes PASSOU no 9c6efa9: JSON gerado com 124 produtos mudando (108 si, 11 ss, 13 de, 3 a), 0 palavra proibida, testar_site verde em 1366 e 390, 'Leve também' igual. O b8fc1a7 só muda scripts e README, sem nenhum xlsx;
  - revisor-codigo LIBERADO no 9c6efa9 e no b8fc1a7;
  - corretor-redundancias LIBERADO no b8fc1a7 (RD-0310 a RD-0312 corrigidos; RD-0284 corrigido neste PR).
- **Aprovação:** R-20261122-012933-alexandre (respostas 1b, 2a, 3a, 4a, 5a e 6a).
- **Depois:** abro o PR do JSON da v27 (web-site/T-0017-json-v27, fce3541, revisor e corretor LIBERADO). Ele já traz o comentário corrigido do site/app.js (R-20261122-013541-alexandre).

Peço a autorização do merge do PR #104 no commit b8fc1a7ddf8905880814e9ad1559ff87ab98ef6d. Squash, com Agente: catalogo-dados.
