---
id: R-20261124-213658-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0034
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-24T21:36:58+00:00
---
# T-0034: simulação da aba Estoque pronta para o Alexandre (10 prints, 3 perguntas)

Simulação da aba Estoque, visões admin, vendedor e cliente, nos tamanhos 1366 e 390 px.

Prints: branch testes/T-0034-simulacao, head bb85f16184406b1202de0539397a57bc9d5f2702, pasta testes/prints/T-0034/:
admin-1366, admin-390, admin-390-abrir, vendedor-1366, vendedor-390, vendedor-q-manaus-1366, vendedor-q-manaus-390, vendedor-q-zzzqqq-390, cliente-1366, cliente-390.
Links: https://github.com/aloirr/bapajudacatalogo/tree/testes/T-0034-simulacao/testes/prints/T-0034

O que a tela mostra:
- Vendedor: só Código, Descrição, Fornecedor, Cidade/filial e Estoque. Nenhum preço, custo, markup, tabela, pedido pendente, sucata ou origem.
- Admin: 22 colunas. No celular, os cartões têm "+ Detalhes" (preços, custo e markup primeiro).
- Cliente (sem permissão): 404 simples, "Não encontrado."; nem fica sabendo que a aba existe.
- Busca por código, código do fornecedor, descrição e cidade/filial, mais um filtro de cidade. No alto, "Posição de 19/11/2026 às 16:48".
- No celular, o "Estoque" fica no menu da conta.
- Valores de estoque, preço, custo e markup FICTÍCIOS, com a faixa "SIMULAÇÃO", porque o repositório é público.

Conferências:
- testes: 55 de 55 passaram;
- designer-ux: LIBERADO COM AJUSTES (feitos);
- design-de-marca: LIBERADO COM AJUSTES (MC-0029 e MC-0030, feitos);
- gerar_site.py sem [PARADO]; produtos.json sem estoque.
Código da simulação: integracao-placas/T-0034-simulacao, 3e0efc6.

Perguntas ao Alexandre (recomendação marcada):
1) Nome de exibição de "MATOGROSSO": a) "Mato Grosso" (recomendado); b) o nome da cidade da filial (qual?).
2) O que são PPEDIDO e SUCATA?
   PPEDIDO aparece como "Pedido pendente" (quantidade). SUCATA aparece como número simples.
   a) estão certos (recomendado); b) explicar.
3) Ordem das colunas do admin: preços, custo e markup, depois os códigos, depois a classificação. a) aprova (recomendado); b) outra ordem.

Plano da versão final, depois do aprovado:
- permissão nova "pode ver o estoque" por usuário, com a caixa na tela Criar usuários; o bap.vendedor já começa com ela;
- rotas /estoque e /api/estoque com 404 para quem não tem a permissão;
- colunas cortadas no servidor para o vendedor;
- o xlsx da BAP Central baixado a cada publicação, sem chave e só na memória; a tabela mostra 50 linhas e um botão "Mostrar mais 50";
- em princípio, o render.yaml não muda; se mudar, aviso antes.
