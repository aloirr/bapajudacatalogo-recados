# T-0027 · simulação do "1 item" (RD-0510)

22/11/2026 07:17 (Manaus) · catalogo-grafico · commit local `2164a2d` (sobre o main `ab9b8f0`), sem push e sem PR.

## O que muda
- O singular fica num lugar só: `plural(n, um='item', varios='itens')` no `digital2.py`, junto do `ANO`.
- A função é usada nos 7 pontos que escrevem "N itens" ou "N linhas": `digital2.py` (continuação da tabela, sumário, página de sistema), `print_cat.py` (painel do cabeçalho e "Mais N … desta linha") e `catalogo_moto.py` (capa).
- Sai o `cover_page` do `digital2.py`, código morto que nenhum arquivo chamava.
- Não mudam: a marca, o texto institucional, o layout e os nomes das entregas. Diff: `diff-gerador.patch`.

| PDF | Pág. | Antes | Depois |
|---|---|---|---|
| Linha Moto | 2 (Sumário, Lâmpadas Moto) | 1 itens | 1 item |
| Linha Moto | 3 (Sistema Elétrica, Lâmpadas Moto) | 1 itens | 1 item |
| Linha Moto | 5 (Lâmpadas Moto, painel) | 1 / ITENS | 1 / ITEM |
| Completo Digital | 2 (Sumário, Lâmpadas Moto) | 1 itens | 1 item |
| Completo Digital | 300 (Seção Linha Moto, Lâmpadas Moto) | 1 itens | 1 item |
| Completo Digital | 302 (Lâmpadas Moto, painel) | 1 / ITENS | 1 / ITEM |
| A4 gráfica | 50 (Lâmpadas Moto, painel) | 1 / ITENS | 1 / ITEM |

## Prova pixel a pixel (150 ppi, `PYTHONHASHSEED=0`, main `ab9b8f0` × `2164a2d`)
- Linha Moto: mudam as págs. 2, 3 e 5 de 17.
- Completo Digital: mudam as págs. 2, 300 e 302 de 311.
- A4 gráfica: muda a pág. 50 de 56 (múltiplo de 4).
- Total: 7 de 384 páginas. Em cada uma, o texto muda numa palavra só ("itens" → "item", "ITENS" → "ITEM").
- Os PDFs "antes" têm o texto igual ao das entregas atuais, página por página.

## Arquivos
- `<pdf>-pNN-antes.png` e `-depois.png`: a página inteira, a 150 ppi.
- `-zoom-antes.png` e `-zoom-depois.png`: o recorte do trecho, a 300 ppi.

## Perguntas ao PO
1. **O painel do cabeçalho com 1 item** (A4 pág. 50, Completo pág. 302, Moto pág. 5): a) "1 / ITEM" ► recomendado (é o singular correto e o alinhamento à direita não muda); b) manter "1 / ITENS".
2. **O Portfólio (material para cliente) também tem "1 itens"**: págs. 69 (Elétrica, Linha Moto) e 76 (Lubrificantes), no `portfolio.py:257`. O mesmo molde sem singular está em `portfolio.py:154` e `:180`. Ele está fora dos 3 PDFs desta tarefa. a) fica fora da T-0027, num RD novo para a fila do Alexandre ► recomendado (critério conservador; a T-0027 fecha sem mexer em material de cliente); b) entra nesta tarefa, com nova simulação do Portfólio.
