---
id: R-20261123-113852-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: alta
tarefa: T-0006
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T11:38:52+00:00
---
# T-0006 fase 1 (baterias): simulação para o Alexandre, 1 pergunta (recomendação 1a)

Merges: #160 → 6dcee05 e #161 → 0d13520 (R-20261123-113806-po); #159 → 81f42d7 (R-20261123-113426-po).

T-0006 fase 1 (baterias), pedido 5a do R-20261123-112006-alexandre.
- Simulação nos recados: recados/anexos/T-0006/fase1-sim/ (commit 1a09ed2). São 12 prints, 1366 e 390 px, antes e depois, mais o LEIA.md.
- Implementação: branch web-site/T-0006-fase1-baterias, head 5a46510 (site/app.js e docs/DADOS_DO_SITE.md).

O que muda na tela:
- Na busca 'bateria' aparecem 2 grupos de filtro novos, depois da Família: 'Amperagem' (13 opções, de 40 Ah a 220 Ah) e 'Partida a frio (CCA)' (5 faixas: até 400, 401 a 500, 501 a 600, 601 a 800, acima de 800). Funcionam como os filtros de hoje: etiqueta com X, 'Filtrar (n)' e 'Limpar tudo'.
- A busca acha '60ah', '60 ah', '60Ah' e 'bateria 60ah'. Hoje acha 4 produtos; agora acha os 8 de 60 Ah.
- O produtos.json não muda: o site lê o Ah e o CCA da ficha técnica que já existe. A FICHA, a TRAVA e a base não mudam.
- Testes: gerar_site sem [PARADO]; testar_site PASSOU, sem falha nova; as buscas geral, por veículo e por código ou referência não mudaram.
- Pareceres: UX LIBERADO (designer-ux/T-0006-fase1, eaba10f) e marca LIBERADO (design-de-marca/T-0006-fase1, 78a3a08).

Notas, sem pergunta:
- Marca, MC-0016 (baixa, fora da fase 1): a ficha técnica da bateria mostra 'C20(ah)' e 'Cca-18°', enquanto o filtro diz 'Ah' e 'CCA'. Vai para a fila do Alexandre. Se o rótulo mudar, o filtro muda no mesmo PR.
- UX: em 1366 px, os grupos novos ficam abaixo de Categoria, Sistema e Família, que na busca 'bateria' têm uma opção só. Fica como ideia de layout para o futuro, com simulação.

Pergunta ao Alexandre (o po leva no formato do R-20261123-111806, com o bloco para copiar):
1) 'Ver mais' na Amperagem, que tem 13 opções.
   a) mostrar as 13, como nos prints ► recomendado (UX e marca). É o padrão de hoje, nenhum grupo tem 'Ver mais', e cortar em 8 esconderia as baterias de 90 a 220 Ah, entre elas as 9 da Linha Pesada.
   b) mostrar 8 e um botão 'Ver mais'.
   Além disso, o 'aprovado' da simulação.

Com o 'aprovado': testes (os casos novos de bateria no testar_site), revisor, corretor, PR do web-site e do testes, e os pareceres. A T-0028 (Portfólio e capa da Linha Moto) vem em recado próprio quando saírem os pareceres de UX e de marca. Ela tem 2 perguntas, uma delas porque o Portfólio pela v27 dá 94 páginas, e não 88.
