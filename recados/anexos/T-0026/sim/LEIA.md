# T-0026 · Simulação: RD-0498 e RD-0499 (repetições no A4, no Completo Digital e na Linha Moto)

| Campo | Valor |
|---|---|
| Quem | catalogo-grafico |
| Quando | 22/11/2026 06:32 (Manaus) |
| Base | origin/main `1255bbe` (worktree, sem commit e sem PR) |
| Decisão | R-20261122-102147-po, pela delegação R-20261122-090651 (conservadora: só tirar repetição e corrigir o que está errado) |
| Geração | `PYTHONHASHSEED=0`, A4, Completo Digital e Linha Moto inteiros, antes e depois, 150 ppi |
| Entregas | `catalogo_grafico/entregas/` não mudou |

## O que muda
1. **A4, pág. 2 (RD-0498).** "Quem somos" fica só com a primeira frase. As linhas (leve, pesada e moto) vão para "Por que vender BAP", e sai de lá o "preço competitivo sem abrir mão da qualidade", que o "Quem somos" já diz. Cada fato fica uma vez, e nenhum se perde. O texto é o do corretor.
2. **A4, págs. 3 e 4 e anotações (RD-0499).** O lado direito da barra fica vazio, como na pág. 2 (RD-0429, já aprovado). Na pág. 4 e nas anotações, o sobretítulo "CATÁLOGO 2027" vira "BAP AUTOPARTS", também como na pág. 2. A pág. 3 mantém o "GUIA RÁPIDO".
3. **Sumário do Completo Digital (RD-0499).** O lado direito da barra fica vazio, e o sobretítulo passa a ser "BAP AUTOPARTS". O texto não muda.
4. **Sumário da Linha Moto (RD-0499).** Muda o mesmo que no Completo. Saem também os 2 erros:
   - o "CATÁLOGO COMPLETO" da barra;
   - o texto, que agora diz "Todas as linhas BAP **para motocicletas** com as aplicações completas. Toque no nome da linha para ir direto à página."

A marca, as fontes, as cores e o resto do texto institucional não mudam.

**Correção do achado.** O RD-0499 diz que a barra do Sumário do digital tem "CATÁLOGO DE PRODUTOS 2027" e "CATÁLOGO 2027". No PDF de hoje, ela tem "CATÁLOGO COMPLETO 2027" à esquerda e "CATÁLOGO COMPLETO" à direita, e o sobretítulo repete "CATÁLOGO COMPLETO 2027". A repetição é a mesma, só muda o texto.

## Prova de que nenhuma outra página muda (`prova_pixel_a_pixel.txt`)
| PDF | Páginas (antes = depois) | Iguais pixel a pixel | Mudam |
|---|---|---|---|
| A4 | 56 (múltiplo de 4) | 53 | 2, 3 e 4 |
| Completo Digital | 311 | 310 | 2 (Sumário) |
| Linha Moto | 17 | 16 | 2 (Sumário) |

- A pág. 3 muda só na barra, a pág. 4 só na barra e no sobretítulo, e os sumários do digital só no topo (caixas no relatório).
- O texto que sai e o que entra em cada página estão no relatório e batem com a lista acima.
- **Anotações:** o A4 de hoje tem 56 páginas e não usa nenhuma página de anotações. Por isso, gerei a página à parte (`anotacoes()`, com o código do main e com o da simulação; o "57" do rodapé é só de exemplo).
- A trava não deu `[PARADO]`, e os 23 testes do gerador passam.
- Nenhum texto fica sobreposto (conferido nos PNGs).

## Sem preço e sem estoque
Procurei no texto das 6 páginas (`textos_paginas.txt`) "R$", preço com número, estoque, saldo, quantidade e unidade: **0 achados**. O "preço acessível" do "Quem somos" é texto institucional, sem valor.

## A pág. 2 do A4 e o vazio embaixo (nota 5.1 do designer-ux na T-0025)
Do fim dos números ao rodapé:

| Versão | Vazio |
|---|---|
| Antes | 324 pt, 38% da altura |
| Depois | 352 pt, 41% da altura (2 linhas a mais) |

A variante de espaçamento (`A4_pag02_variante_espacamento.png`) abre 13 pt entre os blocos e devolve os números ao lugar de antes: o vazio volta a ser de 323 pt. Ela não tem texto novo. A comparação das 4 versões está em `A4_pag02_opcoes.png`.

## Perguntas ao PO (► = recomendação)
1. **RD-0498, texto de "Quem somos" e "Por que vender BAP".**
   - ► a) O do corretor (está na simulação). Quem somos: "A BAP AUTOPARTS é uma empresa brasileira fundada em 2021 para oferecer componentes automotivos de qualidade, com segurança e preço acessível." Por que vender BAP: "Portfólio robusto para as linhas leve, pesada e moto: suspensão, direção, freio, arrefecimento, motor, transmissão, elétrica e acessórios. Produtos com padrão OEM, testados para máxima performance."
   - b) As linhas ficam em "Quem somos" (`A4_pag02_variante_texto.png`). Quem somos: "…com segurança e preço acessível, nas linhas leve, pesada e moto." Por que vender BAP: "Portfólio robusto para suspensão, direção, freio, arrefecimento, motor, transmissão, elétrica e acessórios. Produtos com padrão OEM, testados para máxima performance."
   - c) Deixar como está.
2. **RD-0498, o vazio maior embaixo da pág. 2.**
   - ► a) Deixar como sai. São 2 linhas a mais de vazio (de 38% para 41% da altura), e preencher a página fica para a tarefa futura da nota 5.1.
   - b) Ajustar só o espaçamento: 13 pt a mais entre os blocos, e os números voltam ao lugar de antes (`A4_pag02_variante_espacamento.png`).
   - Em nenhum caso entra texto novo.
3. **RD-0499, lado direito da barra (A4 págs. 3, 4 e anotações e Sumário do Completo e da Linha Moto).**
   - ► a) Vazio, como na pág. 2 (RD-0429, aprovado na T-0025). Nas páginas de linha, o lado direito continua com o grupo.
   - b) Outro rótulo (ex.: "SUMÁRIO", "GUIA RÁPIDO"), que repetiria o título ou o sobretítulo da faixa logo abaixo.
4. **RD-0499, sobretítulo do Sumário (A4, Completo e Linha Moto) e das Anotações (A4).**
   - ► a) "BAP AUTOPARTS", igual ao da pág. 2 (está na simulação). Não muda o layout: só troca o texto.
   - b) Sem sobretítulo. No A4, a faixa recentraliza sozinha se o `hero` ganhar o caso "sem sobretítulo". No digital, o título e o texto precisam subir cerca de 10 pt. São 2 mudanças de layout pequenas.
   - c) Manter "CATÁLOGO 2027" no sobretítulo e só esvaziar a barra. O ano continuaria 2 vezes (barra e sobretítulo).
5. **RD-0499, texto do Sumário da Linha Moto.**
   - ► a) "Todas as linhas BAP para motocicletas com as aplicações completas. Toque no nome da linha para ir direto à página." É a menor correção, e "linha" é o mesmo termo do Completo (está na simulação).
   - b) "Todas as famílias para motocicletas com as aplicações completas. Toque no nome da família para ir direto à página." É o termo da capa da Linha Moto ("7 famílias").
6. **Fora dos achados, mas errado na mesma página: "1 itens".** Aparece "Lâmpadas Moto · 1 itens" ou "1 ITENS" em 6 páginas:
   - na Linha Moto, nas págs. 2 (Sumário), 3 (sistema Elétrica) e 5 (Lâmpadas Moto);
   - no Completo Digital, nas págs. 2 (Sumário), 300 (sistema Linha Moto) e 302 (Lâmpadas Moto).
   - ► a) Fica fora desta rodada: abrir um achado (RD) para "1 item" no singular nos 3 PDFs. Assim, esta simulação continua só com as repetições.
   - b) Corrigir já nesta tarefa. Isso muda mais páginas (sumários, páginas de sistema e capa da família) e pede nova simulação.

## Arquivos
- **Antes e depois, lado a lado:** `A4_pag02_antes_depois.png`, `A4_pag03_antes_depois.png`, `A4_pag04_antes_depois.png`, `A4_anotacoes_antes_depois.png`, `Digital_pag02_sumario_antes_depois.png` e `Moto_pag02_sumario_antes_depois.png`.
- **Avulsos:** `*_antes.png` e `*_depois.png` das mesmas 6 páginas.
- **Opções da pág. 2:** `A4_pag02_opcoes.png`, `A4_pag02_variante_espacamento.png` e `A4_pag02_variante_texto.png`. As variantes não estão no diff.
- **Prova pixel a pixel e texto das páginas:** `prova_pixel_a_pixel.txt` e `textos_paginas.txt`.
- **Diff do gerador:** `T-0026-simulacao.diff` (3 arquivos, +13 −10: `print_cat.py`, `digital2.py` e `catalogo_moto.py`).
