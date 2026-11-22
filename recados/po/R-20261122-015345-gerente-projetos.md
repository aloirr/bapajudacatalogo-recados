---
id: R-20261122-015345-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0017
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T01:53:45+00:00
---
# Pedido de autorização de merge: PR #106 no commit fce3541fa2e13d772b4126bfb6a7ab785e714ea1 (JSON da v27)

# PR #106: JSON do site com a base v27 (T-0017)

- **PR:** #106, do web-site. Branch web-site/T-0017-json-v27.
- **Head:** fce3541fa2e13d772b4126bfb6a7ab785e714ea1. Merge-tree com o main 9268f42, que já tem a v27 pelo #104: sem conflito.
- **Arquivos (4):** site/data/produtos.json, docs/DADOS_DO_SITE.md, scripts/gerar_site.py (só comentário) e site/app.js (só comentário). Nenhum de governança.
- **CI no fce3541:** conferir, site e GitGuardian em success.
- **JSON:** mudam 124 produtos (108 si, 11 ss, 13 de, 3 a); nenhum entra ou sai; 0 SUNRISE, ESTOQUE, R$, USD, FOB, BAP BOX e 'duvidoso'. O arquivo é reproduzível com a v27.
- **Revisões:**
  - testes: a bateria do #104 com o mesmo JSON passou, com 0 falha em 1366 e 390 e o 'Leve também' igual;
  - revisor LIBERADO no 7357708 (o fce3541 só muda comentários);
  - corretor LIBERADO no fce3541 (RD-0313 e RD-0314).
- **Aprovações:** R-20261122-012933-alexandre (v27) e R-20261122-013541-alexandre (o código sobre a foto fica, e só o comentário muda).

Peço a autorização do merge do PR #106 no commit fce3541fa2e13d772b4126bfb6a7ab785e714ea1. Squash, com Agente: web-site.
