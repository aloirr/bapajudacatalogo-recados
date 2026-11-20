# T-0014 · Simulação: cartão com referências, "Salvar em PDF" (A4), página compacta, "Voltar" (A) e janela (B)

Branch `web-site/T-0014-cartao-pdf` (worktree /home/user/wt-T-0014), servido com `python3 -m http.server 8098 -d site`.
"Antes" = main 340fa20. Medidas tiradas pelo Playwright (Chromium), deviceScaleFactor 1. Console sem erro em todas as telas.

## Como abrir cada variante (parâmetros só da simulação)
- `?v=A` (padrão): página do produto com o botão "Voltar".  `?v=B`: o produto abre numa janela por cima da lista.
- `?t=30`: texto da página/janela do produto 30% menor.  `?t=50`: 50% menor.  Sem `?t`: o tamanho de hoje.
- Ex.: http://localhost:8098/?v=B&t=30#/busca?q=palheta e http://localhost:8098/?v=A&t=50#/produto/CL14

## Cartão do resultado (busca "palheta", 1º cartão BS10)
| | 1366 px | 390 px |
|---|---|---|
| foto antes | 287 × 288 px | 172 × 173 px |
| foto depois | 287 × 150 px (−48% de altura) | 172 × 110 px (−36%) |
| altura do cartão antes | 453 px | 348 px |
| altura do cartão depois | 319 px (−30%) | 289 px (−17%) |
| linha "ACESSÓRIOS · LEVE" (11 px, verde #3E8F2B no branco, contraste 4,1:1) | sai | sai |
| etiquetas das referências (11 px, #1F2422 em #F4F5F4, contraste 14,4:1; "+N" em #2E6B1F, 5,8:1) | até 2 linhas | até 2 linhas |

Exemplo com muitas referências (busca "bieleta", BIE20000): 1366 px mostra `01.10 009 1J04-228.04A 6Q04.113.15C N1068 BTC01106 +4`; 390 px mostra `01.10 009 1J04-228.04A +7`.
Ficam fora das etiquetas o código da própria BAP (marca "BAP PN_2", "BAPTA PN" ou o código igual ao do produto).

## Página do produto CL14 (versão A)
| | 1366 px | 390 px |
|---|---|---|
| foto antes | 530 × 530 px | 358 × 358 px |
| foto depois | 477 × 477 px (−10%) | 322 × 322 px (−10%) |
| referências e ficha | embaixo da aplicação | embaixo (igual) |
| referências e ficha depois | **ao lado** da aplicação (2 colunas) | uma embaixo da outra |
| altura da página antes | 4.345 px | 5.020 px |
| altura depois, texto 100% (só o layout) | 3.384 px (−22%) | 4.414 px (−12%) |
| altura depois, texto −30% | 2.634 px (−39%) | 3.563 px (−29%) |
| altura depois, texto −50% | 2.192 px (−50%) | 3.031 px (−40%) |
| rolagem para o lado | não (1366) | não (scrollWidth 390) |

Janela (versão B), altura do conteúdo que rola dentro dela: 1366 px 2.208 px (−30%) e 1.750 px (−50%); 390 px 3.005 px (−30%) e 2.473 px (−50%). Foto na janela de 1366: 440 × 440 px.

## Tamanho do texto (px, página e janela)
| texto | hoje | −30% | −50% |
|---|---|---|---|
| código (título), 1366 / 390 | 30 / 24 | 21 / 16,8 | 15 / 12 |
| descrição | 17 | 11,9 | 8,5 |
| aplicação (lista) | 15 | **10,5** | **7,5** |
| tabelas (referências, ficha) | 14 | **9,8** | **7** |
| título das caixas ("APLICAÇÃO") | 13 | 9,1 | 6,5 |
| aviso "Confira sempre a aplicação…" | 12,5 | 8,75 | 6,25 |
| selos (Acessórios, Palhetas…) | 12 | 8,4 | 6 |
| botões (Voltar, Copiar código, Salvar em PDF) | 14, altura 44 | 14, altura 44 | 14, altura 44 |

Abaixo de 12 px no celular: na −50%, **todos** os textos menos o título (12 px) ficam abaixo de 12 px; a aplicação vai a 7,5 px e a tabela a 7 px, ilegível no celular.
Na −30%, a aplicação (10,5 px), as tabelas (9,8 px), os selos e o aviso também ficam abaixo de 12 px; só o título e a descrição (11,9) ficam perto.
Os botões não diminuem (alvo de toque de 44 px).

## Folha A4 ("Salvar em PDF")
- Solução: sem biblioteca. O botão chama `window.print()` e o `styles.css` tem `@page { size: A4 }` e `@media print`; o vendedor escolhe "Salvar como PDF".
- A folha tem: logo BAP, código, descrição, foto, referências cruzadas, ficha técnica, aplicação (em 3 colunas), o aviso "As fotos são ilustrativas. Confira sempre a aplicação antes da compra." e o link do produto. Saem: menu, rodapé, botões, selos, "Voltar", "Ofereça junto" e "Itens parecidos". "Diferencial BAP" entra quando existe.
- Os PDFs de exemplo, pelo Playwright (`page.pdf`, A4): todos com **1 página** A4 (595 × 842 pt). Sem "preço", "estoque", "custo", "MOQ", "fornecedor", "ranking", "origem" nem "R$" no texto (pdftotext).
  - CL14 (5 referências, 8 campos de ficha, 93 linhas de aplicação);
  - FAC6000 (o produto com **mais referências**: 23; sem foto, sai "Foto em breve");
  - BIE20014 (o com mais referências **e** foto: 12);
  - CL14 aberto pela janela (versão B): sai igual, sem a lista por trás.

## Voltar (A) e janela (B)
- A: lista "palheta" com 48 cartões carregados, rolada até o 30º (MF19), abre o produto e "Voltar aos resultados": volta com os 48 cartões, a mesma rolagem (1366: 3.168 px; 390: 4.664 px), o mesmo endereço e o foco no cartão MF19.
- B: fecha com X, com Esc e com o voltar do navegador; a lista fica na mesma rolagem (1366: 712 px; 390: 1.044 px) e o foco volta ao cartão CL14. O foco vai ao X ao abrir; 40 Tabs seguidos não saem da janela. O endereço muda para #/produto/CL14 enquanto ela está aberta (o link serve para mandar).
- Link direto #/produto/CL14 na B: abre a **página** (com "Voltar", que vai ao início quando não há tela anterior).

## Arquivos
- Cartão: antes-cartao-palheta-1366.png, antes-cartao-palheta-390.png, depois-cartao-palheta-1366.png, depois-cartao-palheta-390.png, depois-cartao-bieleta-1366.png, depois-cartao-bieleta-390.png
- Página antes: antes-pagina-CL14-1366.png, antes-pagina-CL14-390.png (+ -inteira.png, a página toda)
- A, −30% e −50%: depois-A-pagina-t30-CL14-1366.png, depois-A-pagina-t30-CL14-390.png, depois-A-pagina-t50-CL14-1366.png, depois-A-pagina-t50-CL14-390.png (+ -inteira.png)
- A, volta à lista: depois-A-voltar-lista-1366.png, depois-A-voltar-lista-390.png
- B, −30% e −50%: depois-B-janela-t30-CL14-1366.png, depois-B-janela-t30-CL14-390.png, depois-B-janela-t50-CL14-1366.png, depois-B-janela-t50-CL14-390.png
- A4: depois-PDF-CL14.pdf, depois-PDF-CL14-A4.png, depois-PDF-FAC6000.pdf, depois-PDF-FAC6000-A4.png, depois-PDF-BIE20014.pdf, depois-PDF-BIE20014-A4.png, depois-PDF-CL14-da-janela.pdf, depois-PDF-CL14-da-janela-A4.png
- Medidas brutas: antes-medidas.json, depois-medidas.json
