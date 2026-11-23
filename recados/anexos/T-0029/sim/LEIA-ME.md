# T-0029 · Simulação do Portfólio 2027 e das siglas de montadora

Branch `catalogo-grafico/T-0029-portfolio-2027`, head `61ac7ed2b769ab4230a10e81ca21080d6a3a4bb4`. Gerado com `PYTHONHASHSEED=0` e PNG a 150 ppi.
Cada página que muda tem dois arquivos: `port-pNN-<motivo>-antes.png` (main 9f37e19) e `port-pNN-<motivo>-depois.png` (branch).

O Portfólio continua com 88 páginas. Mudam 26 delas:

- **p01, capa:** "PORTFÓLIO DE PRODUTOS 2027". O mês sai como "Novembro de 2026": é o mês em que o PDF é gerado, por extenso.
- **p03, nosso portfólio:**
  - "conforme o Catálogo BAP 2027";
  - a frase "sistema do veículo → família → produto" saía sem as setas, porque a Poppins não tem o "→". Agora sai "sistema do veículo, família e produto".
- **p88, contracapa:** "PORTFÓLIO DE PRODUTOS 2027".
- **Selo "NOVIDADE 2026" trocado por "NOVIDADE 2027" (19 páginas):** p08, 24, 29, 34, 37, 38, 39, 40, 52, 53, 55, 61, 62, 63, 64, 65, 71, 73 e 74.
- **Siglas (MC-0017):** "Vw" passa a "VW" 3 vezes e "Gm" passa a "GM" 5 vezes:
  - p21: "VW/Ford";
  - p34: "Fiat/GM/VW/Toyota";
  - p42: "GM/GM", "VW/Ford" e "Ford/GM/Dodge/Troller";
  - p67: "Ford/GM/Dodge/Troller".
- **p81:** "Balde óleo effitech" passa a "Balde óleo Effitech".

O texto de todas as outras páginas é igual ao da main.

Nesta fase:
- A4, Completo Digital e Linha Moto saem iguais à main, pixel a pixel a 150 ppi.
- Os arquivos de `entregas/` não foram regravados.
- No texto do PDF não aparece preço, estoque nem palavra interna.
