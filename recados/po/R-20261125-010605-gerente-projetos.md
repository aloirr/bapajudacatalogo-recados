---
id: R-20261125-010605-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0034
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-25T01:06:05+00:00
---
# T-0034: autorização de merge dos registros #197, #198, #199 e #200

PRs só de documentos (passam só pelo revisor-codigo, R-20261123-112006-alexandre), todos APROVADOS PELA REVISÃO:
- #197 designer-ux (docs/ux/pareceres/T-0034-*.md): head 806480d8190d1ba1d249a50b51fd46c3c75b0805
- #198 design-de-marca (docs/marca/pareceres/T-0034-*.md): head 7c741198f9827493866e54087434d9e67adc527f
- #199 corretor-redundancias (docs/qualidade/redundancias/T-0034.md e CATALOGO.md): head a6f607b1e823c6b8c8adcc32f3a3c648c6a75e7a
- #200 gerente-projetos (.coord/tarefas/T-0034.md, quadro e docs/ROADMAP.md): head 45a9706953340a5d7916cea9666aa831fadfe857. Os achados 1, 2 e 4 do revisor já foram aplicados e revisados.
A ordem não importa: são pastas diferentes. Confira o CI antes de autorizar.

Pergunta (achado 3 do revisor; recomendo a):
a) deixar como registro histórico. Os registros citam números reais que não são preço nem estoque: a contagem de 18.274 linhas (na tarefa e no UX), a posição de 19/11/2026 16:48 (na marca) e um trecho de ID de produto (no UX da simulação). A BAP Central já é pública.
b) trocar por textos genéricos antes do merge, como foi feito no LEIA.md.

Depois dos merges: PAUSA.
