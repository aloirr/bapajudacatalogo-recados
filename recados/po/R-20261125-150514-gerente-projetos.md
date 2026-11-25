---
id: R-20261125-150514-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0038
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-25T15:05:14+00:00
---
# T-0038: autorização de merge dos registros #213, #214, #215 e #216

Peço autorização para o merge dos registros da T-0038. São PRs só de documentos e passam só pelo revisor-codigo (R-20261123-112006-alexandre). Merge squash com expectedHeadSha, nesta ordem:

1. #213 designer-ux · head cc24b95eb0020f2f9df7da1d87f34e79ae52efd1 · docs/ux/pareceres/T-0038-simulacao.md
2. #214 design-de-marca · head 78738b54e6b64a6179cd3e27f9b37ab38b89cf4a · docs/marca/pareceres/T-0038-simulacao.md
3. #215 corretor-redundancias · head 93991883f61665ba384fe1f8e3e7cf4ea4c2e5db · docs/qualidade/redundancias/T-0038.md e CATALOGO.md (próximo número livre: RD-0645)
4. #216 gerente-projetos · head d18a9a5d8f99e253c61bac985c35ea806d12d43d · .coord/tarefas/T-0038.md e .coord/quadro.md

Situação dos 4:
- CI verde (site, conferir e GitGuardian);
- revisor-codigo: APROVADO PELA REVISÃO;
- sem conflito com o main bd332c4.

Obs.: o branch da T-0033 usa os números RD-0624 a RD-0638, com achados diferentes dos da T-0038. A T-0033 renumera quando entrar.
