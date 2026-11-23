# T-0029 · Rodada final do Portfólio 2027, com a base v28

- Branch `catalogo-grafico/T-0029-portfolio-2027`, head `bf89f50d1f5186cb4ef462092361a8dbeed1b385`.
- Base usada: a v28 do `catalogo-dados/T-0031-v28` (1a4afa4). Copiei o arquivo só para gerar e não fiz commit dela.
- Gerado com `PYTHONHASHSEED=0`; imagens a 150 ppi.
- O "antes" é a simulação aprovada (61ac7ed, base v27). O "depois" é esta rodada.
- O PDF completo está nesta pasta, com o mesmo nome da entrega: `Portfolio_Produtos_BAP_AUTOPARTS.pdf`. Ele ainda não foi gravado em `entregas/`.

**Contagem: 88 → 87 páginas.** Some a pág. 46 (Pesada, Bieletas).

## Arquivos

- Cada página que muda tem dois arquivos: `antes-pNN_depois-pMM-<motivo>-ANTES.png` e `...-DEPOIS.png`.
  - NN é o número na simulação aprovada; MM, o número nesta rodada.
- A página que sai tem um arquivo só: `antes-p46-v28-bieletas-pesada-SAI.png`.

## O que muda, pelo número de antes → número de agora

**v28**
- p03: contagens. Leve 4.048 → 4.050 itens. Pesada 25 → 24 produtos e 513 → 508 itens.
- p04 (divisória da Leve): 4.048 → 4.050 itens.
- p07: 124 → 125 itens.
- p08: 30 → 31 itens.
- p44 (divisória da Pesada): 20 famílias, 24 produtos e 508 itens; Bieletas sai da lista.
- p45 (Pesada, Amortecedores): 5 → 3 itens; "Fiat Dobló" sai.
- p46 (Pesada, Bieletas): sai, porque ficou com menos de 3 itens.

**Selo de volta a "NOVIDADE 2026" (9a)**
- Páginas de antes: 08, 24, 29, 34, 37, 38, 39, 40, 52, 53, 55, 61, 62, 63, 64, 65, 71, 73 e 74.
- Depois da pág. 46 elas passam a 51, 52, 54, 60, 61, 62, 63, 64, 70, 72 e 73.

**ProActive e Shiftease (10a)**
- p75 → 74 e p79 → 78: "proactive" → "ProActive".
- p80 → 79: "shiftease" → "Shiftease".

**Pesada só com veículo pesado (16a)**
- Páginas: p48 → 47, 54 → 53, 55 → 54, 57 → 56, 61 → 60, 62 → 61, 64 → 63, 67 → 66 e 69 → 68.
- Nessas páginas, o veículo leve de um item LEVE E PESADA sai da lista. Entram os próximos veículos da ordem do catálogo.

**Só o número muda**
- As páginas 47 e 56 a 88 de antes, menos as listadas acima, passam a 46 e 55 a 87.

## O que não mudou

- A4, Completo Digital e Linha Moto, gerados com a v28 no branch, saem iguais aos da main, pixel a pixel a 150 ppi:
  - A4: 56 páginas;
  - Completo Digital: 311 páginas;
  - Linha Moto: 17 páginas.
- Não houve `[PARADO]` na geração.
- No texto do Portfólio não aparece preço, estoque nem palavra interna.
