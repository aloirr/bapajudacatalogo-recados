# T-0045 · PR da tela nova: prints para o Alexandre antes do merge

Branch `web-site/T-0045-sim-site`, head b518dc7. O branch tem os commits 1023320, ec9c7fb e 31451b9, mais o merge do main 8179d82 (T-0043 e v31), que entrou sem conflito. Mudam só o site/app.js e o site/styles.css. Os dados não mudam.

Aprovação: R-20261127-200014-alexandre, item 1 ("aprovado, com ajuste": título da tabela fora da caixa e cabeçalho das colunas com fundo e destaque).

## O que muda na tela
- **Botões:** uma barra só no rodapé, com Copiar código, Salvar em PDF e Voltar juntos. Ela fica presa no fim da tela e, no fim da página, encosta no fim do bloco. Na janela do produto, a barra vai no rodapé, e o ✕ fica em cima.
- **Largura:** é a mesma em todas as telas (1334 px úteis em 1366 e 1848 em 1920), com o conteúdo alinhado ao logo.
- **Aplicação:** ocupa a largura toda. Referências e Ficha ficam lado a lado embaixo.
- **Tabelas:**
  - o título fica fora da caixa;
  - o cabeçalho das colunas da Aplicação ganha fundo verde-claro, com uma linha verde embaixo;
  - as linhas são alternadas.
- **Letra do produto:** segue a escala única, de 12, 13, 15, 17 e 20 px.
- **"Salvar em PDF" (A4):** igual ao de hoje, sem botões.

## Conferido
- A tabela de aplicação dos 4.419 produtos sai idêntica à do main (sha256 igual). O merge não mexeu na T-0043.
- O testar_site passou.

## Prints, só da tela visível
`antes-` (main 8179d82) e `depois-` (b518dc7), em 1366, 390 e 1920:
- VEL7520 e BIE20014: topo, meio e fim;
- janela do TER552120: topo e fim;
- início, busca e Sobre: topo.

`antes-VEL7520-A4.pdf` e `depois-VEL7520-A4.pdf`: o "Salvar em PDF".
