# T-0006, fase 1 (baterias): simulação para o Alexandre

Pedido: R-20261123-112006-alexandre, decisão 5a. Proposta aprovada: R-20261123-095435-alexandre (PR #157).
Prints do site de verdade (branch `web-site/T-0006-fase1-baterias`), servido no computador, sem selo de simulação. Ainda não está no ar.

## O que muda
- Busca "bateria": 2 grupos novos na coluna de filtros (no celular, no painel "Filtrar"), depois da Família:
  - **Amperagem**: 13 opções em Ah, do menor ao maior (40 Ah ... 220 Ah);
  - **Partida a frio (CCA)**: as 5 faixas aprovadas (até 400, 401 a 500, 501 a 600, 601 a 800, acima de 800).
- Os grupos só aparecem quando a lista tem bateria. Funcionam como os outros filtros: etiqueta com o X ("Amperagem: 60 Ah"), "Filtrar (1)", opção com 0 em cinza e endereço (`ah=60`, `cca=401-500`).
- Busca "60ah", "60 ah", "60Ah" e "bateria 60ah": agora acham as 8 baterias de 60 Ah (antes, só 4).

## O que entrou no JSON
Nada. O site lê o Ah e o CCA da ficha técnica que o site já tinha (C20(AH) e CCA-18°). A base não muda.
Não há preço nem estoque.

## Testes
- `gerar_site.py`: sem [PARADO] (4.419 produtos).
- `testar_site.mjs --conhecidos`: PASSOU, sem falha nova.
- Contagens iguais às do levantamento: 60 Ah = 8; CCA 15/6/11/8/6; 60 Ah + 401 a 500 = 5.
- As outras buscas não mudaram: "amortecedor" 710, "gol 2010 amortecedor" 5, "AMT7115" 1, "TRW 16900255S" 2, "90/90-18" 3, "6203" 4.
- No celular (390 px), a tela não rola para o lado.

## Prints (1366 px e 390 px)
- 01: antes (o site de hoje), busca "bateria";
- 02 e 02b: busca "bateria" com os 2 grupos abertos;
- 03: os 2 grupos fechados;
- 04: faixa de CCA "401 a 500" marcada (6 produtos);
- 05: busca "60ah" (8 produtos);
- 06: painel "Filtrar" no celular, com 60 Ah marcado ("Ver 8 produtos").

## Pergunta ao Alexandre
1. **Lista longa da Amperagem (13 opções).**
   - Opção a) **(recomendo)**: mostrar as 13 opções, como nos prints. É o padrão de hoje: Linha, Categoria e Sistema aparecem inteiras.
   - Opção b): mostrar só as 8 primeiras e um botão "Ver mais".
