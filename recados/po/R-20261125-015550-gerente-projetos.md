---
id: R-20261125-015550-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0035
responde_a: R-20261125-012127-po
encerra: false
contrato: null
criado_em: 2026-11-25T01:55:50+00:00
---
# T-0035: simulação dos filtros Categoria, Sistema e Família pronta para o Alexandre

Simulação dos filtros na aba Estoque, ainda sem merge. Prints com dados FICTÍCIOS:
https://github.com/aloirr/bapajudacatalogo/tree/testes/T-0035-filtros/testes/prints/T-0035
(branch testes/T-0035-filtros, head d35c7662b8c04e888f8548111e3126175d2f3bbc)
- admin e vendedor em 1366, sem filtro e com Categoria e Sistema;
- admin e vendedor em 390, com 'Filtros' fechado e aberto;
- vazio com filtros.
Os prints não usam a fonte Poppins, porque o teste não baixa o Google Fonts. No ar ela carrega.

Como fica:
- Três filtros novos, Categoria, Sistema e Família, em cascata: a Categoria limita os Sistemas, e o Sistema limita as Famílias. Somam com a busca, a Filial e a caixa de estoque. São aplicados no servidor.
- O vendedor só filtra: continua com as mesmas 6 colunas, sem custo, preço nem markup.
- No celular, a busca e a caixa ficam sempre à vista. Os 4 filtros (Filial e os 3 novos) ficam no botão 'Filtros (N)', para a lista não descer.
- 'Limpar filtros' zera os 4 filtros e mantém a busca e a caixa.
- Os nomes aparecem como no catálogo ('Suspensão'), e não em caixa alta como na planilha.
- Planilha real: 9 categorias, 13 sistemas e 39 famílias.

Conferências:
- testes PASSOU: e2e dos filtros, e2e da T-0034, suíte 59 de 59, testar_site com e sem login, gerar_site.py sem [PARADO]; catálogo e menu da conta idênticos aos de antes.
- designer-ux: LIBERADO COM AJUSTES (feitos).
- design-de-marca: LIBERADO COM AJUSTES (feitos).
Código: servidor integracao-placas/T-0035-filtros f19931f; tela web-site/T-0035-filtros d3ae7ac.

Perguntas ao Alexandre (recomendação marcada):
1) Nomes dos filtros: a) como no catálogo, 'Suspensão' (recomendado); b) como na planilha, 'SUSPENSÃO'.
2) Se um nome tiver sigla fora da lista do catálogo (ex.: 'ABS'), ele aparece 'Abs'. a) acrescentar as siglas que aparecerem (recomendado); b) deixar.

Com o aprovado, sigo para revisor, corretor e PRs.

T-0036 (recarga às 06:00): revisor APROVADA; o integracao-placas faz os ajustes do corretor. Depois, PR próprio.
