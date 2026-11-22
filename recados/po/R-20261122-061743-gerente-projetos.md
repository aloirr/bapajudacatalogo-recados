---
id: R-20261122-061743-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: normal
tarefa: T-0023
responde_a: R-20261122-061514-po
encerra: false
contrato: null
criado_em: 2026-11-22T06:17:43+00:00
---
# T-0023: a especificação deixa de fora outras formas da grafia antiga; ampliar?

O revisor do PR #122 (tarefa da T-0023) bloqueou por causa do escopo. Trocar só a forma 'BAP AUTO PARTS' nos 4 arquivos não fecha o critério '0 BAP AUTO PARTS nas entregas'.

1) A topbar: print_cat.py:480 chama topbar(dc, 'BAP Auto Parts') e a função faz .upper(). Por isso o A4 gráfico mostra 'BAP AUTO PARTS' em quase todas as páginas. O mesmo acontece em simulacao_detalhe/print_cat.py:424.
2) Texto visível 'BAP Auto Parts' ('A BAP Auto Parts é uma empresa…', 'Gerente Comercial · BAP Auto Parts'): print_cat.py:483, simulacao_detalhe/print_cat.py:427, apres_bemol.py:119 e :257, apres_ppt.js:66 e :208. Aparece no PDF e no .pptx de Lubrificantes e Químicos. O docs/marca/manual.md:12-14 diz que a grafia é toda em maiúsculas e sem espaço.
3) O autor nos metadados (setAuthor 'BAP Auto Parts'): print_cat.py:39, digital2.py:158, apres_bemol.py:28, apres_ppt.js:11, kitfiltros/kit.py:193, kitfiltros/kit_v1_32pag.py:189 e simulacao_detalhe/print_cat.py:49. Fica nas propriedades dos PDFs (A4, Completo Digital, Linha Moto, Kit Filtros e Lubrificantes) e do .pptx.

Minha recomendação: [a] ampliar a especificação para todas as formas, 1, 2 e 3. O critério passa a ser '0 auto parts com espaço, em qualquer caixa, no gerador e nas entregas', sem contar o domínio bapautoparts.com.br. Tudo continua com simulação antes. A alternativa [b] é fazer só 1 e 2, deixando os metadados fora do escopo, registrados na tarefa.

Com a sua resposta, atualizo a T-0023 no mesmo PR #122. Os RD-0406 a RD-0408 do corretor já estão aplicados (head novo a seguir).
