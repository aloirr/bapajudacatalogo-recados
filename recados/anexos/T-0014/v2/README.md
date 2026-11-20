# T-0014 · Simulação v2: janela no computador, foto menor com "Clique na foto para ampliar.", celular A e B

Branch `web-site/T-0014-cartao-pdf`, servido com `python3 -m http.server 8098 -d site`. Prints do Playwright (Chromium), deviceScaleFactor 2.
Texto do produto 30% menor, com piso de 12 px (título 21 px no computador e 16,8 px no celular; o resto 12 px).
Foto do produto: computador 200 × 200 px (55% menor que os 440 px da janela de antes); celular 129 × 129 px em 390 px (60% menor que os 322 px de hoje).
Foto ampliada: 648 × 648 px no computador (1366 × 768) e 358 × 358 px no celular (390 px). Fecha com X, Esc, clique fora e o voltar.

| Arquivo | O que é |
|---|---|
| 1366-janela-CL14.png | Computador: o CL14 aberto da lista "palheta", na janela por cima da lista |
| 1366-janela-CL14-foto-ampliada.png | Computador: a foto do CL14 ampliada por cima da janela (foco no X) |
| 390-janela-CL14.png | Celular, versão janela (B, `?v=B`, o padrão da simulação): o CL14 aberto da lista |
| 390-janela-CL14-foto-ampliada.png | Celular, versão janela: a foto ampliada |
| 390-pagina-CL14.png | Celular, versão página (A, `?v=A`): o CL14 com "Voltar aos resultados" |
| 390-pagina-CL14-inteira.png | Celular, versão página: a página toda, de cima a baixo |
| 390-pagina-CL14-foto-ampliada.png | Celular, versão página: a foto ampliada |
| 1366-cartao-OEM-bieleta.png | Computador: lista "bieleta"; o 1º cartão (BIE20000) começa pelos códigos OEM 1J04-228.04A e 6Q04.113.15C |
| 390-cartao-OEM-bieleta.png | Celular: o mesmo cartão (OEM primeiro, depois "+8") |
| PDF-CL14-da-janela.pdf | "Salvar em PDF" do CL14 a partir da janela: 1 página A4, sem a lista por trás |
| PDF-CL14-da-janela-A4.png | A mesma folha A4 em imagem |
