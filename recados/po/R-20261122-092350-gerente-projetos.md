---
id: R-20261122-092350-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0024
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T09:23:50+00:00
---
# Autorização de merge: PR #134 (página T-0024), head b3fde044cba4be2bfdfa2cb73d0bcb5f4c2de92b

PR #134 · branch web-site/T-0024-pagina · head b3fde044cba4be2bfdfa2cb73d0bcb5f4c2de92b · mergeable clean.
Arquivos (5, todos do web-site): site/admin/pdfs/pdfs.js, site/admin/pdfs/index.html, site/admin/admin.css, site/conta.js e site/styles.css.
CI no head: conferir, site e GitGuardian verdes.

Revisões:
- designer-ux LIBERADO e design-de-marca LIBERADO: página final igual à v2 aprovada; o ajuste depois disso só tirou CSS sem efeito, com as caixas dos botões iguais.
- testes PASSOU: bateria com o #133 e o #134 juntos, mais a prova negativa.
- revisor-codigo LIBERADO (reteste 05:23): sem regressão, com estados, servidor antigo e escape conferidos no Chromium. O teste antigo do main continua passando sobre main + #133 + #134.
- corretor-redundancias LIBERADO (reteste 05:19): RD-0479 a RD-0482 corrigidos.

Peço a autorização: squash, expectedHeadSha, 'Agente: web-site', T-0024.
Com ela, executo em seguida o #133 (já autorizado no 4d4ffa8) e o #134, nessa ordem.

Depois vem o #138 (testes/login.mjs, head 4595275, revisor e corretor LIBERADO): trago o main para o branch, espero o CI verde e peço a autorização com o SHA novo. Por último, o #135.
