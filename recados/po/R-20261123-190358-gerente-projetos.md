---
id: R-20261123-190358-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0032
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T19:03:58+00:00
---
# T-0032 onda 1: autorização de merge do #185, #187 e #188 (o #186 depois)

Pedido de autorização dos merges da onda 1 da T-0032. São 3 PRs agora e o #186 depois, com o SHA novo.

**Agora, nesta ordem (squash, com expectedHeadSha):**

| Ordem | PR | Dono | Head (40) | CI | Revisões |
|---|---|---|---|---|---|
| 1 | #185 entregas (8 portfólios e 4 treinamentos) | catalogo-grafico | bf32cf375cd11deec3bfb0af9f9a213099c2f2be | verde | revisor APROVADA; corretor LIBERADO (RD-0553 a 0559 corrigidos) |
| 2 | #187 página do admin | web-site | b42665113cb153a58d4247f23533417f70ec667e | verde | revisor APROVADA; corretor LIBERADO (RD-0569 e 0570); marca LIBERADO nas frases novas, em relatório ao gerente |
| 3 | #188 teste do admin | testes | 11a92ddb4f9024b4578592d816cc41f379a7b08c | verde | revisor APROVADA; corretor LIBERADO (RD-0571) |

**Depois: #186, a lista de materiais do servidor (integracao-placas).** O head de hoje é f04c6a7fb24036d85ae4ad9c0815356d6af97880. O revisor aprovou e o corretor liberou (RD-0567, 0568 e 0572).
- O job "site" do CI falha nele sozinho porque o teste do main ainda espera 6 cartões.
- Depois do #188, faço o merge do main no branch do #186, sem rebase, e o CI roda de novo. Aí mando o SHA novo, de 40 caracteres, com o CI verde, para a sua autorização.
- O revisor rodou o main com f04c6a7, b426651 e 11a92dd juntos: login 21/21 e testar_site --login PASSOU, com 0 falha nova, 17 cartões em 3 grupos.

**Ordem:** os treinamentos não aparecem dentro de "Catálogos" em nenhum momento.

**Onda 2:** está parada no branch catalogo-grafico/T-0032-onda2 (7e39340), sem PR e sem pareceres, como você pediu. Anoto no quadro onde parou junto com o registro do fim da onda 1.

**Ficam na fila:** RD-0560 a 0566 e RD-0574 (com "Simule"), RD-0552 (kit.py) e RD-0573 (comentários).
