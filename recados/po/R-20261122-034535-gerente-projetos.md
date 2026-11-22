---
id: R-20261122-034535-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0022
responde_a: R-20261122-034324-po
encerra: false
contrato: null
criado_em: 2026-11-22T03:45:35+00:00
---
# Pedido de autorização de merge: PR #110 no 7a6ba83 e PR #111 no 5a344ba

# Pedido de autorização de merge: PR #110 no commit 7a6ba8370ebbf55e8d6afc13304f3e7039f54983 e PR #111 no commit 5a344baf5f1a5f36cb4bbd1e4e78e3068df6f7e2

Ordem: primeiro o #110, depois o #111. O RD-0326 fica CORRIGIDO quando os dois estiverem no main.

## PR #110 (governança parte 1, 'Agente: alexandre')
- **Head:** 7a6ba8370ebbf55e8d6afc13304f3e7039f54983. O merge-tree com o main c9975a5 não mostra conflito.
- **Arquivos (4):**
  - .coord/donos.json, com servicos/login/** para o integracao-placas;
  - .claude/agents/integracao-placas.md;
  - .claude/agents/gerente-projetos.md;
  - CLAUDE.md.
- **CI no head:** conferir, site e GitGuardian em success.
- **Revisões no 7a6ba83:**
  - revisor-codigo: LIBERADO (reteste);
  - corretor-redundancias: LIBERADO, desde que o #111 também entre (reteste).

## PR #111 (registro da T-0022, 'Agente: gerente-projetos')
- **Head:** 5a344baf5f1a5f36cb4bbd1e4e78e3068df6f7e2.
- **Arquivos (3), só em .coord/:**
  - README.md:14, com servicos/login/ (a parte do RD-0326 que cabe ao gerente);
  - quadro.md;
  - tarefas/T-0022.md.
- **CI no head:** conferir, site e GitGuardian em success.
- **Revisões no 5a344ba:**
  - revisor-codigo: LIBERADO (reteste);
  - corretor-redundancias: LIBERADO (reteste; RD-0331 a RD-0333 corrigidos).

## Merge
Com a sua autorização, faço o squash com expectedHeadSha nos dois PRs:
- **#110:** "T-0022: servicos/login/ com dono integracao-placas (governança parte 1) (T-0022)" e 'Agente: alexandre'.
- **#111:** "T-0022: registro do passo 2 e servicos/login/ no README do quadro (T-0022)" e 'Agente: gerente-projetos'.
