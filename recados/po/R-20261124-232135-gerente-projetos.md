---
id: R-20261124-232135-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0034
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-24T23:21:35+00:00
---
# T-0034: autorização de merge #194, #195 e #196 (aba Estoque), nesta ordem; prints da versão final

Versão final da aba Estoque pronta. Merge NESTA ORDEM, porque o #196 importa um arquivo que vem no #194:
1) #194 servidor (integracao-placas): head fd76490712b89fd23821ada9f610841276fa1f72
2) #195 tela (web-site): head 7756c47b6b736b00f9e7b83b1b15f628de0bba74
3) #196 testes (testes): head f6a0c26263ee8c3579b72f9468bef65fbc8e4374

Prints da versão final, 17, com dados FICTÍCIOS (nenhum número real no Git):
https://github.com/aloirr/bapajudacatalogo/tree/testes/T-0034-estoque/testes/prints/T-0034-final
- admin: 1366, 390 e 390-detalhes; vendedor: 1366 e 390;
- menu da conta (admin e vendedor, 390);
- cliente 404; busca vazia; 503 (1366 e 390); caixa marcada; último "Mostrar mais";
- Criar usuários (1366 e 390).
A fonte dos prints não é a Poppins: o teste não baixa o Google Fonts. No site, a Poppins carrega normalmente.

Conferências:
- testes PASSOU: e2e com 25 conferências, suíte 58 de 58, testar_site com e sem --login sem falha, gerar_site.py sem [PARADO], produtos.json sem estoque.
- designer-ux: LIBERADO COM AJUSTES, feitos. O F1 foi recusado: a ordem das colunas é decisão do Alexandre.
- design-de-marca: LIBERADO COM AJUSTES (MC-0031 feito; MC-0032 vai para a fila).
- revisor-codigo: APROVADA nos 3 heads acima.
- corretor-redundancias: LIBERADO (branch a6f607b).
CI: o conferir e o GitGuardian estão verdes nos 3. Quando mandei este recado, o job 'site' ainda rodava: confira se ficou verde antes de autorizar.

Resumo do que vai ao ar:
- aba Estoque só para o admin e para quem tem a permissão nova 'Pode ver o estoque' (o bap.vendedor já começa com ela [SUPOSIÇÃO]);
- o vendedor vê Filial, Nº filial, Código, Descrição, Fornecedor e Estoque, cortados no servidor;
- o admin vê as 23 colunas;
- os outros usuários recebem 404;
- a planilha da BAP Central é baixada a cada publicação, só na memória, com limites contra arquivo ruim;
- o render.yaml não muda.

Para a fila:
- RD-0598 (rodapé 'fotos ilustrativas' nas telas de conta e do admin);
- MC-0032 (o '×' azul da busca);
- a trava do /admin sem diferenciar maiúsculas (observação A do revisor);
- um teste a mais da lista branca com busca que traz resultado (achado 1 do revisor).

Depois dos merges: PR de registro com os pareceres (UX, marca, corretor), a tarefa, o quadro e o ROADMAP; fecho os branches da simulação.
