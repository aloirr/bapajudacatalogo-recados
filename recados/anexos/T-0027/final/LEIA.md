# T-0027 · entrega final do "1 item" (RD-0510)

22/11/2026 07:24 (Manaus) · catalogo-grafico · decisão R-20261122-112104-po: 1a ("1 / ITEM" no painel) e 2a (o Portfólio fica fora).

## O que muda
- Os 3 PDFs em `catalogo_grafico/entregas/`, com os mesmos nomes: A4 gráfica, Completo Digital e Linha Moto.
- Gerados do commit `2164a2d` (gerador), com `PYTHONHASHSEED=0`.
- "1 itens" passa a "1 item" e "1 / ITENS" passa a "1 / ITEM". Nada mais muda.

## Prova pixel a pixel (150 ppi, entregas do main `0fb9453` × entregas novas)
- Linha Moto: mudam as págs. 2, 3 e 5 de 17.
- Completo Digital: mudam as págs. 2, 300 e 302 de 311.
- A4 gráfica: muda a pág. 50 de 56 (múltiplo de 4).
- Total: 7 de 384 páginas. Em cada uma, o texto muda numa palavra só. O número de páginas e o título dos metadados não mudam.

## Arquivos
- `<pdf>-pNN-prancha.png`: a página inteira, antes e depois lado a lado, a 150 ppi.
- `<pdf>-pNN-zoom.png`: o recorte do trecho que muda, antes e depois, a 300 ppi.
