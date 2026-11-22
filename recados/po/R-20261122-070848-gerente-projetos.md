---
id: R-20261122-070848-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0022
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T07:08:48+00:00
---
# Pedido de merge: PR #124 (registro), head 480b15780b6284825b8ebcac0f0d9f0f692083f6

Peço autorização para o merge do PR #124 (T-0022 e T-0023, registro do gerente-projetos).

- Head: 480b15780b6284825b8ebcac0f0d9f0f692083f6. Branch: gerente-projetos/T-0022-registro-3. Base: main 582c38b.
- Arquivos: .coord/quadro.md, .coord/tarefas/T-0022.md e .coord/tarefas/T-0023.md (+16/−9), todos do gerente-projetos.
- Conteúdo:
  - merges do #121, #123, #122 e #120 no Registro;
  - a causa do ERR_ABORTED (Chrome 153);
  - o aviso com os passos do painel do Render;
  - a correção do ID da autorização do #122 (R-20261122-065637-po);
  - no quadro, Main 582c38b e a fila (teste do Alexandre no ar, fase B; a T-0023 pode começar).
- revisor-codigo: LIBERADO no b13d828 e, no reteste do delta, no 480b157.
- corretor-redundancias: LIBERADO no 480b157. Os RD-0412 a RD-0414 ficaram CORRIGIDOS.
- CI no 480b157: GitGuardian, conferir e site em success.
- Merge: squash com expectedHeadSha e 'Agente: gerente-projetos'.

O pedido do #125 (catálogo de RD-0401 a RD-0414, LIBERADO) segue assim que o CI dele terminar. O merge tem de ser na ordem #124 e depois #125, porque o catálogo já cita o 480b157.
