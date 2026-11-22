---
id: R-20261122-071124-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0022
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T07:11:24+00:00
---
# Pedido de merge: PR #125 (catálogo de RD-0401 a RD-0414), head e27f5e5235ac77f43d34963ed8f840ecd64e4ace

Peço autorização para o merge do PR #125. O merge vem DEPOIS do #124, porque o catálogo cita o 480b157 do #124.

- Head: e27f5e5235ac77f43d34963ed8f840ecd64e4ace. Branch: corretor-redundancias/T-0022-T-0023-catalogo-rd. São 2 commits sobre o main 582c38b.
- Arquivos: docs/qualidade/redundancias/CATALOGO.md, T-0022.md (§12 a §15) e T-0023.md (novo). Todos são do corretor-redundancias.
- Conteúdo:
  - MANTIDOS: RD-0401 a RD-0403 (#120) e RD-0409 e RD-0410 (#123).
  - CORRIGIDOS: RD-0404 e RD-0405 (#121), RD-0406 a RD-0408 e RD-0411 (#122), e RD-0412 a RD-0414 (480b157, #124).
  - O próximo número livre é o RD-0415.
- revisor-codigo: LIBERADO no 8b4c375 e LIBERADO no delta até o e27f5e5. Ele confirmou as linhas citadas, a numeração sem buraco e o formato.
- CI no e27f5e5: site, conferir e GitGuardian em success.
- Merge: squash com expectedHeadSha e 'Agente: corretor-redundancias'.

Para você saber: a simulação da T-0023 está pronta (branch catalogo-grafico/T-0023-grafia, 7c7c4db). O design-de-marca e o designer-ux estão revisando. Mando o pacote para o Alexandre logo depois.
