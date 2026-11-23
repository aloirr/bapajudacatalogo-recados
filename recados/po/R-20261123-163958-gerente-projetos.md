---
id: R-20261123-163958-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0029
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T16:39:58+00:00
---
# Autorização de merge: PRs #179 e #180 (T-0029, Portfólio 2027)

Peço a autorização de merge dos 2 PRs da T-0029, aprovada no R-20261123-162032-po (7a e 15a).

1) PR #179, branch catalogo-grafico/T-0029-portfolio-2027
- Head: ee49e32bb917b1ac9e08a524abb06ed85958216e
- Arquivos, todos do catalogo-grafico: catalogo_grafico/gerador/portfolio.py, taxo.py, LEIA_GERADOR.md e catalogo_grafico/entregas/Portfolio_Produtos_BAP_AUTOPARTS.pdf (87 págs., sha256 14d24e81701acb8c23ae7c1894d8e61485b86f8cec29d8790fe866f0efeab410, mesmo nome)
- A entrega é igual à simulação aprovada (6d8f143), menos a pág. 2: 'bom custo-benefício' (15a). A4, Digital e Linha Moto continuam iguais ao main.
- CI no ee49e32: verde (conferir, site e GitGuardian)
- testes: PASSOU (#180, no 0133f6f; o PDF é o mesmo no ee49e32)
- designer-ux e design-de-marca: entrega final LIBERADA (MC-0017 fechado)
- revisor-codigo: APROVADA PELA REVISÃO (reteste às 12:37, no ee49e32)
- corretor-redundancias: LIBERADO no reteste. RD-0547 a RD-0549 CORRIGIDOS. RD-0550 e RD-0551 (montadora repetida ou com 2 grafias no PDF) e RD-0552 (regra própria de pesado no Kit Filtros) ficam ABERTOS na fila, com simulação.
- Merge: squash com expectedHeadSha, 'Agente: catalogo-grafico' e 'Tarefa: T-0029'

2) PR #180, branch testes/T-0029-portfolio
- Head: 148c048b15b26cf78386e2d223596817b68d0a03
- Arquivos: testes/prints/T-0029/ (testes)
- CI verde; revisor: APROVADA PELA REVISÃO
- Merge: squash com expectedHeadSha, 'Agente: testes' e 'Tarefa: T-0029'

Observação do revisor, que não trava: o mês da capa vem do dia em que o PDF é gerado (edicao()). Qualquer regeração a partir de dezembro muda a capa para 'Dezembro de 2026' sem nova aprovação. Se preferir fixar, vai para a fila.
