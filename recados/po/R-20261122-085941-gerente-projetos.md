---
id: R-20261122-085941-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: revisao
prioridade: normal
tarefa: T-0024
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T08:59:41+00:00
---
# PR #135 (b4405eb): volta para ajuste de 1 linha de comentário no render.yaml:50

Revisor: VOLTA PARA AJUSTE. Corretor: LIBERADO, com o RD-0455 (baixa).
O buildFilter está certo: os globs casam exatamente os 7 arquivos de entregas/ e não pegam .xlsx, .png nem Aplicacoes_*.pdf. Catalogo_BAP_*_...pdf cobre os anos seguintes. YAML válido, sem segredo, preço nem estoque.

Ajuste pedido (os dois apontam a mesma linha, render.yaml:50, que o PR não tinha mexido):
- Antes: '# Login do catálogo (T-0022): serve o site/ inteiro só com login. Sem rootDir: lê site/ e os 2 PDFs de catalogo_grafico/entregas/.'
- Depois (recomendo a do corretor, sem contagem, para não envelhecer de novo): '# Login do catálogo (T-0022, T-0024): serve o site/ inteiro só com login. Sem rootDir: lê site/ e os arquivos do admin de catalogo_grafico/entregas/ (lista PDFS do server.mjs).'

Com o commit novo, mande o SHA: eu peço o reteste rápido. O merge continua depois do #133 e do #134.
