---
id: R-20261123-191148-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0032
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T19:11:48+00:00
---
# T-0032 onda 1: autorização do #186 (6ae0331) e do #189 (a1620f8)

Pedido de autorização para os 2 últimos merges da onda 1 da T-0032, nesta ordem (squash, com expectedHeadSha):

1) **#186, a lista de materiais do servidor (integracao-placas)**
   - Head: 6ae033144003cca5da993eed8706cc7769d810c9. É o f04c6a7 aprovado, mais o merge do main a0dc065, sem rebase.
   - CI verde: conferir, site e GitGuardian. O "site" passou agora que o #188 está no main.
   - Revisor APROVADA no f04c6a7. Corretor LIBERADO (RD-0567, RD-0568 e RD-0572).
   - O merge do main não mudou nenhum arquivo do dono. No 6ae0331, `verificar --base origin/main` deu OK e o login.test.mjs passou 21/21.
2) **#189, o registro no quadro (gerente-projetos, só documentos)**
   - Head: a1620f80b01da7b67e7e6b6907e6d4c6ea6242c3.
   - O registro diz: T-0032 "ONDA 1 CONCLUÍDA (o #186 entra antes deste registro); ONDA 2 PAUSADA", e o item 0 da fila mostra onde a onda 2 parou.
   - Revisor APROVADA no a1620f8.
   - CI: conferir e GitGuardian verdes. O "site" ainda estava rodando às 15:11; só faço o merge com ele verde.

Depois desses dois merges, aviso uma vez e fico parado até você chamar, como você pediu.
