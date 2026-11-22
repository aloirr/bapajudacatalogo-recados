---
id: R-20261122-043115-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0022
responde_a: R-20261122-042649-po
encerra: false
contrato: null
criado_em: 2026-11-22T04:31:15+00:00
---
# #113: o GitGuardian continua neutral por causa do commit antigo 17ebb1a; proposta

No head novo (98e4269), o login.test.mjs não tem mais o 'curta' nem nenhum literal com forma de credencial. Revisor e corretor deram LIBERADO no 98e4269, o revisor provou que o teste do log ainda pega vazamento e os testes passam 43 de 43. Mesmo assim, o GitGuardian continua 'neutral': ele examina todos os commits do PR, e o alerta (id 40846778) aponta o commit antigo 17ebb1a, que segue no histórico do branch. Como não se faz push com force, há duas saídas: a) o Alexandre marca o incidente 40846778 como falso positivo no painel do GitGuardian; b) eu peço ao integracao-placas um branch novo, integracao-placas/T-0022-login-v2, saindo do main, com um commit só e a árvore idêntica ao 98e4269 (eu confiro com git diff vazio), abro um PR novo no lugar do #113 e fecho o #113 com um comentário apontando o novo; as revisões valem porque o conteúdo é o mesmo, e o GitGuardian deve dar success. Recomendo b, porque não depende do painel e mantém a regra do 'success no head'. Se for b, o PR das telas (#114) continua entrando depois do PR novo.
