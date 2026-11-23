---
id: R-20261123-143346-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0030
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T14:33:46+00:00
---
# Autorização de merge: PRs #173 e #174 (T-0030)

Peço a autorização de merge dos 2 PRs da T-0030 (rótulos 'Ah' e 'CCA' na ficha da bateria, aprovados no 12a do R-20261123-141744-po).

1) PR #173, branch web-site/T-0030-rotulos-bateria
- Head: ceb297cd268668e0e87cbcbcf9cf93621e444d4c
- Arquivos: site/app.js e docs/DADOS_DO_SITE.md (web-site)
- CI no ceb297c: verde (conferir, site e GitGuardian)
- revisor-codigo: APROVADA PELA REVISÃO (reteste às 10:30)
- corretor-redundancias: LIBERADO (reteste às 10:30). RD-0541 MANTIDO pelo seu R-20261123-142842-po; RD-0542 e RD-0543 CORRIGIDOS
- testes: PASSOU. Do 3da35c1 ao ceb297c mudaram só um comentário e uma linha do doc
- FICHA, TRAVA e produtos.json sem mudança
- Merge: squash com expectedHeadSha, 'Agente: web-site' e 'Tarefa: T-0030'

2) PR #174, branch testes/T-0030-rotulos
- Head: 01fc11d9f3eb5d6b9d39193e7f63b0cb07f165f3
- Arquivos: testes/prints/T-0030/ (testes)
- CI no 01fc11d: verde
- revisor: APROVADA PELA REVISÃO; corretor: LIBERADO
- Merge: squash com expectedHeadSha, 'Agente: testes' e 'Tarefa: T-0030'

Também em andamento:
- T-0031: o #175 (catalogo-dados, base v28) e o #176 (testes) estão com o revisor e o corretor. O testes deu PASSOU.
- T-0029 final: gerada com a v28, com 87 págs. O 16a ainda tem uma variante em teste, porque a 1ª regra também tirava tratores e colheitadeiras da Pesada.
- T-0032 passo 1: o padrão de treinamento está pronto e com o UX e a marca. Os 2 portfólios de amostra estão sendo gerados.
