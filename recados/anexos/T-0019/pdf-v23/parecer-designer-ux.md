# T-0019 · Parecer de UX · PDFs 2027 com a base v23

- Branch `catalogo-grafico/T-0019-pdf-v23`, head `52772d1`. Rodada R-20261120-235000-alexandre (aprovação antecipada, sem mudança de layout).
- Conferido: as 6 pranchas em `catalogo_grafico/simulacoes/T-0019-pdf-v23/` e os PDFs de `entregas/` (antes = `2945a37`), comparados linha a linha com PyMuPDF.

## Resultado: LIBERADO

| Página | Item | Cabe? | Formato | Leitura |
|---|---|---|---|---|
| A4 p.19 | CRU100 | 🟢 1 linha, termina em x=377, coluna vizinha em 432,8 | 🟢 "(04/2007–12/2017)" com travessão, como "(1987–1998)" | 🟢 "Hyunday" virou "Hyundai" |
| A4 p.21 (destaque) | SCE14002 | 🟢 mesma linha, mesma altura | 🟢 "1929 · 1932 · 1934" | 🟢 melhor que "1929–19321934" |
| Digital p.105 | CRU100 | 🟢 1 linha, até x=360,7 (vizinha em 401,8) | 🟢 | 🟢 |
| Digital p.110 (destaque e tabela) | SCE14002 | 🟢 1 linha, até x=394,4, folga de 7,4 pt até a coluna vizinha | 🟢 | 🟢 |
| Digital p.141 | ELE1068 | 🟢 continua em 2 linhas: "Uno Mille" sobe e a 2ª linha encurta | 🟢 "1984–1995" no lugar de "19/84->1995" | 🟢 |
| Digital p.206 | FAC6108 | 🟢 a linha encurta | 🟢 | 🟢 sai o "em Diante" solto |

- Só as 6 páginas mudam de texto (A4: 19 e 21; Digital: 105, 110, 141 e 206). O número de linhas e as alturas (y) de todas as linhas são iguais aos de antes, então nada é empurrado.
- O ano segue em cinza `#5b5f5b` sobre o texto `#161816` (contraste de cerca de 6,4:1, acima de 4,5:1).
- Sem preço e sem estoque.

## Observações (não seguram o PR)
1. 🟡 SCE14002, "Mbb LS 1630 1929 · 1932 · 1934 LS1941": [SUPOSIÇÃO] 1929, 1932 e 1934 parecem ser modelos Mercedes (LS 1929, LS 1932, LS 1934), não anos. O gerador pinta os três de cinza, a cor de ano. O PDF segue a base v23, mas vale o `catalogo-dados` confirmar. Se forem modelos, o texto fica "LS 1630 · LS 1929 · LS 1932 · LS 1934 · LS 1941".
2. 🟡 CRU100: na mesma linha, "Kia Motors Bongo 2500 (07/2017)" continua com uma data só, sem dizer se é "de" ou "até", ao lado do intervalo novo do Hyundai. É dado (`catalogo-dados`), fora deste PR.

## A4 p.20 · tag NOVO encostada na montadora (já existia no main)
- Recomendo **virar tarefa** (🟡, do `catalogo-grafico`). Não é só encostar: a tag tapa o nome.
  - EMB3400700639R: a tag (x 115,7–131,5) cobre o "MB" (a aplicação começa em x=127).
  - EMB3400700648R e 649R: a tag (até x≈132) cobre o "V" de "VOLVO".
- Nos códigos curtos a tag cabe (termina em x≈101–113). O problema está só nos códigos de 14 caracteres.
- Proposta: quando o código e a tag não couberem antes da coluna de aplicação, a tag desce para a linha da descrição curta, sem mudar a largura das colunas. Antes de virar PDF, simular a p.20 em A4.
