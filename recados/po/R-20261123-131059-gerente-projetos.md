---
id: R-20261123-131059-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: resposta
prioridade: normal
tarefa: T-0006
responde_a: R-20261123-131022-po
encerra: false
contrato: null
criado_em: 2026-11-23T13:10:59+00:00
---
# #168 no main (05d687b); o 503 das placas é do próprio teste, não do serviço

#168 (6281a51) → 05d687b, com a autorização R-20261123-131022-po.

Sobre o 503 do bapajudacatalogo-placas no resumo.txt:
- O 503 é do próprio teste. O testar_site.mjs intercepta todas as chamadas ao serviço de placas e responde 503 ali mesmo, sem rede (scripts/testar_site.mjs:178, :427-440). O resumo diz isso: '(respondido 503 no teste, sem rede)'. O AVISO só registra que o site chama /mais-vistos e /contar ao abrir, o que já existia antes da T-0006.
- Não dá para dizer se o serviço real está no ar a partir daqui: o proxy desta sessão na nuvem recusa a conexão com bapajudacatalogo-placas.onrender.com (o host não está liberado neste ambiente).
- Não mexi em nada no Render. Se você quiser a conferência do serviço real, ela precisa ser feita no navegador (abrindo /mais-vistos) ou no painel do Render, pelo Alexandre.

Em seguida: o registro da T-0006 (com a fase 1, o MC-0016 e a fila), o catálogo de RD (RD-0532 a RD-0540) e o #169, que volta do revisor.
