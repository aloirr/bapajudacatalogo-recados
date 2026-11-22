---
id: R-20261122-080801-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0022
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T08:08:01+00:00
---
# Pedido de merge: PR #127 (arremates da placa), head d3ebb6592e35592d7495784154e016eb5c70d959

Peço autorização para o merge do PR #127 (T-0022, arremates).

- Head: d3ebb6592e35592d7495784154e016eb5c70d959. Branch: integracao-placas/T-0022-arremates. Base: main 548ce73.
- Arquivos (5): servicos/login/login.test.mjs, servicos/placas/server.mjs, contador.mjs, README.md e teste.test.mjs. Todos são do integracao-placas.
- O que muda:
  - teste novo: o /interno/codigos responde com o serviço fechado e a chave certa, e responde 401 com a errada;
  - sai a reserva da placa sem as 2 variáveis, que deixou de servir com o catálogo fechado. No ar nada muda, porque as 2 variáveis já chegam pelo #126.
- revisor-codigo: LIBERADO no 60a1fcc e no reteste do d3ebb65. Os casos sem chave, vazia e errada seguem cobertos no teste do /interno/codigos, e a chave fora do log segue coberta no teste do log.
- corretor-redundancias: LIBERADO no d3ebb65 (RD-0418 a RD-0421 CORRIGIDOS).
- Testes: 44/44. CI no d3ebb65: conferir, site e GitGuardian em success.
- Merge: squash com expectedHeadSha e 'Agente: integracao-placas'.

Ponto do #128 para o Alexandre: o testes viu que as 21 imagens PNG do .pptx de Lubrificantes ganharam uma credencial C2PA. É um metadado de origem de conteúdo, assinado pela Anthropic, que diz que o arquivo veio do Claude. Os pixels são iguais e não há dado interno nem 'auto parts'.
Pergunta:
1) O .pptx pode ir ao cliente com esse metadado nas imagens?
   a) Pode.
   b) Tirar o bloco C2PA das PNG antes do merge, sem mexer nos pixels. (RECOMENDADO, para o arquivo ficar igual ao de outubro fora a grafia)
O testes também anotou, como anterior à tarefa: o PDF da Linha Moto tem o título 'Catálogo BAP 2027 — Completo (uso interno)' nos metadados.
