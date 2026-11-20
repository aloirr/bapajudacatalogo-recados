# T-0019 · Simulação "OFEREÇA JUNTO" → "LEVE TAMBÉM" no catálogo em PDF

Decisão: R-20261120-141600-alexandre, item 3. Isto é só a simulação: nada foi gravado no repositório e nada foi commitado.

## Imagens (150 dpi, antes e depois)
| Página | O que mostra |
|---|---|
| `A4_impresso_p023_*.png` | A4 da gráfica 2027, pág. 23 (Sapata de Freio): cabeçalho da coluna, faixa e o texto `coluna "Leve também"` dentro da faixa |
| `A4_impresso_p003_*.png` | A4 2027, pág. 3 ("Como consultar"): passo 04 com o título e o texto |
| `Digital_p005_*.png` | Digital 2027, pág. 5 (Amortecedores): cabeçalho da coluna |

Como a simulação foi feita: o gerador não roda nesta nuvem, porque faltam o `ESTOQUE_BAP.xlsx` e as fotos (`entradas/bap/`), que vêm do PC do Alexandre. Então o "depois" é o PDF entregue em 13/11 com só o rótulo trocado no mesmo lugar, na mesma fonte Poppins, no mesmo corpo, na mesma cor e com o mesmo espaçamento (`sim_leve_tambem.py`). O PDF final sai do gerador, com o texto refluído e o impresso em CMYK.

## Arquivos que mudam (`catalogo_grafico/gerador/`, diff em `geradores.diff`)
- `print_cat.py`: o rótulo da faixa (A4) e o passo 04 do "Como consultar" (título e texto).
- `digital2.py`: o rótulo da faixa da capa de linha. Hoje nenhuma página do digital mostra essa faixa, mas o código está no caminho da geração.
- `oferta.py`, `cross.py`, `pneus_fix.py`, `moto.py`: o nome da coluna (`extra_col`).
- `cross.py` e `moto.py`: nos textos das faixas, `coluna "Ofereça junto"` passa a ser `coluna "Leve também"` (Sapata, Bomba de Óleo, Kit de Distribuição, Velas, Pneus e câmaras, Câmaras e Pneus moto). Isso vai além do rótulo; se o GP preferir, dá para tirar.
- Ficam como estão: os comentários e docstrings (`oferta.py` l.1, `moto.py` l.105/107, `catalogo_moto.py` l.3) e a coluna `OFERECA_JUNTO` da base, que é de `dados/`.

Geradores que são só histórico, sem mudança:
- `simulacao_detalhe/`: cópia de uma simulação antiga.
- `portfolio_v1_por_sistema.py`: só tem a palavra "oferecer", não o rótulo, e o portfólio em uso é o `portfolio.py`.
- `lista_aplicacoes_site.py`: gerou o PDF Antes/Depois de 12/11.
- `auditoria_catalogo.py`: planilha de 23/10.
- `encartelados.py`: planilha interna, não é PDF.
- `base_v*.py`: geravam as versões da base.

O Portfólio, o Kit Filtros e a apresentação de lubrificantes não têm o rótulo (0 ocorrências).

## Cabe no mesmo espaço?
Sim, e sobra espaço (largura com Poppins Bold e o espaçamento do gerador):

| Onde | Antes | Depois | Espaço |
|---|---|---|---|
| Cabeçalho da coluna no A4 (7,6 pt) | 72,6 pt | 61,0 pt | coluna de 78 pt |
| Cabeçalho da coluna no digital e no Moto (8 pt) | **75,9 pt** | 63,7 pt | coluna de 74 pt |
| Faixa do A4 (9 pt) | 90,6 pt | 76,1 pt | 126 pt até o texto |

Hoje o rótulo antigo passa 1,9 pt da coluna no digital e invade o espaço entre as colunas. Com "LEVE TAMBÉM", isso deixa de acontecer.

## Quantas páginas têm o bloco (PDFs de 13/11, 2027)
- A4 da gráfica: 51 de 56 páginas, com 96 ocorrências (cabeçalhos, 15 faixas e o "Como consultar").
- Digital: 299 de 317 páginas (cabeçalho da coluna).
- Linha Moto: 8 de 17 páginas.

## Tempo depois do "aprovado"
[SUPOSIÇÃO] Uns 30 a 40 minutos para os três PDFs:
- uns 5 minutos para gerar o A4, o digital e o Moto;
- o resto para conferir o número de páginas, comparar o texto com a versão de 13/11, procurar texto sobreposto e checar o tamanho do arquivo.

O prazo depende de ter os mesmos `ESTOQUE_BAP.xlsx` e fotos usados em 13/11. Com outro estoque, a ordem dos destaques muda e a comparação mostra mais do que o rótulo.
