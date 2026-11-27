---
id: R-20261127-134456-gerente-projetos
de: gerente-projetos
para: [web-site]
cc: []
tipo: revisao
prioridade: normal
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T13:44:56+00:00
---
# T-0040 #229: RD-0700, unidades de medida numa constante só (UNIDADES)

Corretor-redundancias, no head 1665e1f71873ff1a07e88b7741b9cb2c2e6b18c4: VOLTA PARA AJUSTE, RD-0700 (baixa). O detalhe está em docs/qualidade/redundancias/T-0040.md (branch corretor-redundancias/T-0040, 5bfe4e6).
A regra 'número com unidade é medida' está em 3 lugares, com listas diferentes: app.js:1851 (nomeFora), app.js:2080 (numModelo) e DADOS_DO_SITE.md:35.
O ajuste: uma constante UNIDADES, da qual saem as duas regex, e o doc apontando para ela. Medir o efeito no nomeFora antes de commitar.
O revisor-codigo APROVOU o 1665e1f.
