---
id: R-20261124-213133-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: null
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-24T21:31:33+00:00
---
# Regra nova do Alexandre: toda sessão com Opus 5.5 e esforço médio (PR #192, governança)

O Alexandre escreveu direto na sessão do gerente (24/11/2026, ~17:40 Manaus), literal: "crie todas as sessoes com opus 5.5 médio. bote como regra".

Feito:
- PR #192 (governança, CLAUDE.md), head 0babecb8f342faa14bfcc47548da04599a4e1f9e: na seção Sessões e recados, toda sessão nova (create_session) com model claude-opus-5-5 e effort medium.
- O revisor-codigo já está revisando. Quando ele aprovar, peço a sua autorização de merge (número e SHA).

Para você, que cria as sessões: a regra já vale a partir de agora, ao criar qualquer sessão (model "claude-opus-5-5", effort "medium").
[SUPOSIÇÃO] Os subagentes dentro das sessões continuam como estão; se o Alexandre quiser o mesmo neles, é outra mudança, nos .claude/agents.
