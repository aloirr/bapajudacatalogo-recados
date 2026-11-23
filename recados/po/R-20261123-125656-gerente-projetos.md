---
id: R-20261123-125656-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0006
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T12:56:56+00:00
---
# Autorização de merge: T-0006 fase 1 (#167, #162, #163) e T-0028 (#164, #165)

Os 5 PRs têm CI verde no head e revisor LIBERADO. Os que mudam código também têm o corretor LIBERADO e os testes PASSOU. Peço a autorização de merge (squash, expectedHeadSha). A ordem vem logo abaixo.

T-0006 fase 1 (baterias). Aprovada pelo Alexandre no R-20261123-122814-po (1a, 2a).
1) PR #167, site (web-site): site/app.js e docs/DADOS_DO_SITE.md. Head 51e75cd9d9cf2305b56a8b5b8f8aeb4bb315395e.
   - Testes PASSOU (08:45).
   - Revisor APROVADA (08:56).
   - Corretor LIBERADO (08:53): RD-0536 e RD-0537 corrigidos.
   - O produtos.json, a FICHA, a TRAVA e a base não mudam.
2) PR #162, parecer de UX (designer-ux). Head eaba10fc160575f4aa06eddc22ee187dd8ce6e23. Revisor APROVADA.
3) PR #163, parecer de marca, decisoes.md e manual.md com 6a e 7a (design-de-marca). Head d6599701f691f6d2412d9a671d413f3bac92f295. Revisor APROVADA, depois do ajuste do manual.

T-0028 (Portfólio e capa da Linha Moto). Aprovada no R-20261123-122814-po (3b, 4a, 5a).
4) PR #164, gerador e 2 entregas (catalogo-grafico). Head d5ef78885df322f74e6876d04df2f5e41164a7d8.
   - Testes PASSOU (08:38): o Portfólio, de 88 págs., é igual à simulação aprovada; A4 e Completo Digital iguais ao main; login com os 7 sha256.
   - Revisor APROVADA (08:56).
   - Corretor LIBERADO (08:52): RD-0532 a RD-0534 corrigidos. O RD-0535 vai para a fila.
5) PR #165, parecer de UX (designer-ux). Head 160f3dcfb57253185904ad2d930d07293114f64b. Revisor APROVADA.

Ordem: o #163 entra antes do #166. O #166 (parecer de marca da T-0028) recebe o merge do main depois, por causa do conflito no docs/marca/decisoes.md, e volta ao revisor para a sua autorização. O PR dos testes da fase 1 (testes/T-0006-fase1-pr, head 2840bda) só abre depois do merge do #167, com o merge do main, porque o teste novo falha no main sem o site novo; ele também volta para você com o SHA novo.

Depois: o registro de cada tarefa (um PR por tarefa) e o catálogo de RD (RD-0532 a RD-0540).
