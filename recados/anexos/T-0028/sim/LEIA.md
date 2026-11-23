# T-0028 · Simulação: Portfólio e capa da Linha Moto

`catalogo-grafico`, 23/11/2026 07:35 (Manaus); ajuste do parecer de UX às 07:50. Branch `catalogo-grafico/T-0028-entregas`, head `6c035be` (2 commits sobre o main `15c3d8d`: `223ce6b` e `6c035be`).
Decisões 9a e 11a do R-20261123-112006-alexandre. Nada foi gravado em `catalogo_grafico/entregas/`.

## O que muda
- **`plural.py` (novo):** o `plural()` sai do `digital2.py`, que passa a importá-lo de lá. O `portfolio.py` (RD-0527), o `lista_aplicacoes_site.py` e o `kitfiltros/kit.py` (RD-0526) usam a mesma função, sem cópia. O patch está em `diff-gerador.patch`.
- **Portfólio:** "1 itens" → "1 item". Antes saía em 2 págs. da entrega (69 e 76); agora sai "1 item" em 3 págs., porque o Filtro de Ar Moto é página nova. O `portfolio.py` passa a ler a base de `dados/` (v27), como os 3 PDFs; antes lia a v11 de `saidas/`, que não está no Git.
- **Linha Moto, capa:** "7 famílias · 75 itens para motocicletas" → "7 linhas · 75 itens para motocicletas" (MC-0015). Ver `moto-p01-capa-zoom-*.png`.

## Prova pixel a pixel (150 ppi na Moto e na lista; 100 ppi no resto; texto pelo PyMuPDF)
| PDF | Comparação | Págs. | Resultado |
|---|---|---|---|
| A4 | gerado × entrega | 56 = 56 | nenhuma página difere (texto e pixel) |
| Completo Digital | gerado × entrega | 311 = 311 | nenhuma página difere |
| Linha Moto | gerado × entrega | 17 = 17 | só a pág. 1 (capa) difere; as outras 16 são iguais |
| Lista de aplicações do site | código novo × código do main | 21 = 21 | nenhuma página difere |
| Kit Filtros | não roda nesta nuvem | – | Os caminhos fixos do `kit.py` e do `parse.py` (`/home/claude/...` e `/mnt/user-data/uploads/...`) não existem aqui. Só muda o "N veículo(s)" do cabeçalho, e o `plural()` dá o mesmo texto de antes para n de 0 a 4999 (teste feito) |
| Portfólio, variante a (código do `223ce6b`) | código novo × código do main, as duas na v27 | 94 = 94 | só mudam as págs. 78, 79 e 88 ("1 itens" → "1 item") |

## Portfólio: entrega (82 págs., 23/10, v11) × regerado
- **Regerado pela v27, como está no commit (a): 94 págs., e não 88.**
  - A v27 divide os Rolamentos em 3 sistemas: Transmissão, Motor e Rodagem.
  - Cada linha ganha cartões de "Rolamentos" em Transmissão e em Motor, sob o título "Cubos e Rolamentos".
  - O Universal ganha um sistema "Transmissão" com 2 rolamentos.
  - A lista da divisória da Linha Leve (pág. 4) passa do limite de baixo (aviso `ATENÇÃO: lista passou da página`). Encosta no rodapé, mas não cobre o nº da página.
- **As 88 págs. esperadas são a variante b** (`diff-variante-b.patch`, 3 linhas no `dados()`, fora do commit): os Rolamentos ficam no sistema em que o Catálogo BAP (A4 e Digital) os mostra, Rodagem; o resto segue o SISTEMA da v27. A v11 também dá 88 págs.
- **Páginas de produto que mudam (b × entrega; na a, as mesmas contagens, com as págs. deslocadas, mas 12 novas: 5 das novas da b e 7 de Rolamentos em Transmissão ou Motor):**
  - 13 iguais;
  - 9 mudam só no nº de itens;
  - 45 mudam no nº e nas "Principais aplicações";
  - 7 mudam só nas aplicações;
  - 6 são novas: Pesada Bieletas, Pesada Caixa de Direção, Pesada Cubo de Roda, Moto Filtros de Ar, Moto Filtros de Óleo e Universal Rolamentos;
  - nenhuma sai.
- **Por quê:** os números e as aplicações vêm do catálogo de hoje (com os complementos e as correções desde 23/10) e da base v27. O "+2.700 itens no catálogo" da pág. 2 passa a "+4.500".
- **Divisórias (págs. 3, 4, 44, 70 e 78 na b):** novos totais.
  - Linha Moto: 4 sistemas, com Filtração.
  - Universal: 4 sistemas, com Rodagem.
  - Ver `port-sumario-*.png`.
- **Material para cliente:** a busca no texto (ranking, vendedor, MOQ, FOB, fornecedor, estoque, uso interno, R$, custo, margem, nome de fornecedor e de concorrente) não acha nada nas 2 variantes.
  - O "preço acessível" do "Quem somos" é o texto institucional que já estava na entrega e que a marca aceitou na T-0026.
  - Nenhum texto sobreposto novo: só os 3 falsos positivos da capa, que já estavam na entrega.

## Perguntas ao Alexandre
1. **Como agrupar os Rolamentos no Portfólio?** Na v27, eles estão em 3 sistemas. A decisão 9a falou em 88 págs.
   - a) SISTEMA da v27 como está: 94 págs. Rolamentos em Transmissão, Motor e Rodagem em cada linha, com "Universal · Transmissão" de 2 itens. A lista da Linha Leve encosta no rodapé, e precisaria de um ajuste de layout com simulação própria.
   - **b) Rolamentos em Rodagem, como no Catálogo BAP; o resto pelo SISTEMA da v27: 88 págs., sem o aviso de lista longa. (recomendado)**
   - c) Voltar à v11: 88 págs., mas com a classificação de outubro, fora da base atual.
2. **Datas do Portfólio:** a capa diz "PORTFÓLIO DE PRODUTOS 2026" e "Outubro de 2026", a pág. 3 diz "conforme o Catálogo BAP 2026" e a contracapa repete o "2026". Estes textos não mudaram nesta simulação.
   - **a) Ficam como estão nesta tarefa; a troca vai para a fila, com simulação própria. (recomendado: a 9a não pediu a troca)**
   - b) Trocar já para "Novembro de 2026" e "Catálogo BAP 2027", com uma nova rodada de simulação.

Observação, sem pergunta: algumas "Principais aplicações" saem com a grafia da base ("Gm/Gm Corsa", "Vw/Ford Gol") ou cortadas sem "…" ("Volkswagen / Chevrolet / Ford VW Fus", pág. 42 da b). Já acontecia na entrega e não muda aqui.

## Ajuste do parecer de UX (`6c035be`, 07:50)
- **O problema:** o `aplicacoes()` do `portfolio.py` juntava as linhas da APLICACAO da v27. A quebra de linha ia para o PDF como glifo vazio, que a Poppins não tem, e 2 aplicações ficavam coladas ("HONDA CG 125 CARGO ESD - 2014–2015¤HONDA CG 12…").
- **A correção:**
  - Cada linha passa a ser uma aplicação.
  - A linha quebrada no meio na base ("…SUSPENSÃO" + "PNEUMÁTICA 4X2…") continua a de cima: a de cima não termina em ano e esta não começa por uma 1ª palavra já vista.
  - O " - " antes do ano sai junto com o ano.
- **O "depois" × o "antes" (o `223ce6b`):** só mudam 6 págs. em cada variante, conferidas pixel a pixel e no texto.
  - Variante a: 39, 42, 47, 66, 68 e 79.
  - Variante b: 37, 40, 45, 62, 64 e 73.
  - Por quê, na b:
    - 37, 62 e 73 tinham o glifo vazio;
    - 40 e 64 (Filtros de Óleo) tinham a mesma cola, escondida pelo corte "…": a lista ganha as linhas separadas;
    - 45 (Amortecedores da Pesada) muda de "MB OF1724 -" para "MB OF1724".
  - Imagens: `port-aplic-<variante>-pNN-<produto>-antes.png` e `-depois.png`. Os 2 PNGs do Filtro de Ar Moto também foram refeitos.
- **Glifo vazio no Portfólio inteiro (PyMuPDF):**
  - Antes do ajuste, o detector achou 5 em cada variante: 3 nas aplicações e 2 na seta da pág. 3.
  - Depois do ajuste, **0 nas aplicações** nas 2 variantes. Restam só os 2 da seta "→" da pág. 3, "Linha → sistema → família → produto" (`portfolio.py:406`). A entrega de 23/10 também tem esses 2. Eles ficam como estão, por decisão do gerente: a troca é da marca.
- **Para a seta, a Poppins (Regular, Medium e Bold) não tem nenhuma seta** (nem U+2192, nem ➔, ⟶ ou ►). Ela tem `›` (U+203A), `»` (U+00BB), `>`, `–` (U+2013), `—` (U+2014), `•`, `·` e `/`.
- **Os outros PDFs:** foram regerados no `6c035be`.
  - A4 e Completo Digital: iguais à entrega, pixel a pixel.
  - Linha Moto: só a capa difere da entrega, e é igual à da 1ª rodada.
  - Lista de aplicações: igual.
- **Variante b:** o `diff-variante-b.patch` foi refeito sobre o `6c035be`, com o mesmo conteúdo. Não foi aplicada no branch.
- **Observação, sem pergunta:** o Filtro de Ar Moto mostra só "HONDA CG 125 CARGO ESD". O produto tem 27 linhas, todas CG 125, 150 e 160. A regra antiga do `aplicacoes()` não repete a 1ª palavra, que nas linhas da v27 é a montadora. Não mexi nessa regra.
