# T-0019 · PDFs 2027 com a base v23

Autorização: R-20261120-235000-alexandre, com aprovação antecipada nesta rodada. Gerado com `PYTHONHASHSEED=0`, um processo por PDF, sobre o main `2945a37` (base v23) mais o ajuste "DE" antes do ano (`2fe2940`).

- **Antes:** os PDFs do main `2945a37` em `catalogo_grafico/entregas/` (gerados com a v21, #77).
- **Depois:** os PDFs novos, já em `catalogo_grafico/entregas/`.

## O que mudou no gerador
- `gerador/digital_data.json`, que é entrada fixa (extraída do catálogo digital de 13/10). A aplicação dos itens antigos vem dele, e não da base. Três textos ficaram iguais aos da base v23:
  - CRU100: "Hyunday HR (07/2017)" → "Hyundai HR 2.5 4x2 (04/2007–12/2017)";
  - SCE14002: "1929–1932" "1934" → "1929 · 1932 · 1934";
  - FAC6108: "Eclipse Cross 1.5 L 16V · em Diante ·" → "Eclipse Cross 1.5 L 16V ·" (sem ano, como a base).
- Nenhum script mudou nesta geração.

## Diferenças de texto (PyMuPDF, página a página)
| PDF | Página | Antes | Depois |
|---|---|---|---|
| A4 | 19 | Hyunday HR (07/2017), Kia Motors Bongo 2500 (07/2017) | Hyundai HR 2.5 4x2 (04/2007–12/2017), Kia Motors Bongo 2500 (07/2017) |
| A4 | 21 (destaque) | 1630 1929–19321934 LS1941 | 1630 1929 · 1932 · 1934 LS1941 |
| Digital | 105 | Hyunday HR (07/2017), Kia Motors Bongo 2500 (07/2017) | Hyundai HR 2.5 4x2 (04/2007–12/2017), Kia Motors Bongo 2500 (07/2017) |
| Digital | 110 (destaque e tabela) | … LS 1630 1929–19321934 LS1941 … | … LS 1630 1929 · 1932 · 1934 LS1941 … |
| Digital | 141 (ELE1068, v22 P2) | Uno 1.1 Brio/1.3/1.5/1.6R 19/84->1995 | Uno 1.1 Brio/1.3/1.5/1.6R 1984–1995 |
| Digital | 206 | Cross 1.5 L 16V · em Diante · Outlander | Cross 1.5 L 16V · Outlander |
| Linha Moto | — | nenhuma | nenhuma |

As outras mudanças da v22 e da v23 estão na aba VEICULOS, que os PDFs não leem.

## Conferência
- Páginas: A4 56 (múltiplo de 4), Digital 308 e Moto 17, iguais ao main. Nenhuma linha muda de página.
- Tamanho: A4 13,2 MB, Digital 5,9 MB e Moto 0,8 MB.
- Aviso de uso interno em todas as páginas (56 / 308 / 17).
- Texto sobreposto: nada novo. O detector acha 3 casos no A4, p. 20, iguais aos do main: a tag NOVO encosta na montadora (EMB3400700639R, 648R e 649R).
- Palavras proibidas (preço, R$, USD, estoque, fornecedor, AUTOIMPACT, SUNRISE, #N/A, FOB, MOQ, ranking, custo, duvidoso, "nan"): 0. Os falsos positivos são os mesmos de antes: "preço acessível/competitivo" (texto institucional do A4) e "consulte o vendedor BAP" (catálogo interno).
- O "em Diante" solto do Digital (FAC6108): 1 → 0.
- O PDF da Linha Moto tem o mesmo texto do main. Mudam só a data e o ID, por isso ele não foi trocado em `entregas/`.

## Pranchas (150 ppi, antes à esquerda e depois à direita)
- `01_A4_p019_CRU100.png`
- `02_A4_p021_SCE14002.png`
- `03_Digital_p105_CRU100.png`
- `04_Digital_p110_SCE14002.png`
- `05_Digital_p141_ELE1068.png`
- `06_Digital_p206_FAC6108.png`
