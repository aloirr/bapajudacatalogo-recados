---
id: R-20261124-214608-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0034
responde_a: R-20261124-214137-po
encerra: false
contrato: null
criado_em: 2026-11-24T21:46:08+00:00
---
# T-0034: nova simulação da aba Estoque pronta (respostas do Alexandre aplicadas)

Simulação refeita com as respostas do Alexandre.
Prints: branch testes/T-0034-simulacao, head 721065f334d4bef4b1c9fa39492fc6b8b14a2602, pasta testes/prints/T-0034/ (os mesmos 10 arquivos).
https://github.com/aloirr/bapajudacatalogo/tree/testes/T-0034-simulacao/testes/prints/T-0034
Código da simulação: integracao-placas/T-0034-simulacao, 11da4b9.

O que mudou:
- "Mato Grosso". A busca acha "mato grosso" e "matogrosso".
- PPEDIDO = "Custo do produto" e CUSTO_TOTAL = "Custo total" (custo + sucata), os dois em R$. Os valores continuam fictícios.
- Admin: Cidade/filial, Código, Descrição, Estoque, Custo do produto, Custo total, Preço capital, Preço interior, Markup capital, Markup interior e depois as outras 12 colunas.
  - No celular, o cartão mostra filial, código, estoque e descrição; "+ Detalhes" abre as outras 18, a partir dos custos.
- Vendedor: Cidade/filial, Código, Descrição, Fornecedor e Estoque, sem custo, preço, markup nem "R$".

Testes: 66 de 66 passaram.

Para o Alexandre:
- aprovado da simulação?
- [SUPOSIÇÃO] o rótulo da 1ª coluna ficou "Cidade / filial" nas duas visões; se ele quiser só "Filial", é um ajuste pequeno.
Com o aprovado, começo a versão final (servidor de login, permissão nova, 404, corte das colunas no servidor e o xlsx baixado a cada publicação).

PR #192: sigo travado. O controle de permissões desta sessão negou duas vezes a assinatura "Agente: alexandre". Só destrava se o Alexandre autorizar direto nesta sessão ou se ele mesmo fizer o commit.
