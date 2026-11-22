# T-0023 · Simulação da grafia "BAP AUTOPARTS" (antes × depois)

Gerada em 22/11/2026 03:08 (Manaus), no branch `catalogo-grafico/T-0023-grafia`, com `PYTHONHASHSEED=0`.
Só as páginas mudadas; as entregas oficiais (`catalogo_grafico/entregas/`) **não** foram geradas de novo.

Grafia seguida: `docs/marca/manual.md:10-14`: "BAP AUTOPARTS", tudo em maiúsculas e sem espaço, também no texto
corrido (o manual não abre exceção para o texto corrido; "BAP Autoparts" está na lista do errado).
O domínio `bapautoparts.com.br` e o `@bapautoparts` não mudaram.

## O que ver (PNG em `png/`, 150 ppi; o recorte da barra a 300 ppi)

Cada item tem `_antes.png`, `_depois.png` e `_par.png` (os dois juntos, ANTES à esquerda ou em cima).

| | Página | Arquivo do par | O que mudou |
|---|---|---|---|
| (a) | A4, barra do topo (recorte da pág. 2) | `png/a_A4_barra_do_topo_par.png` | "BAP AUTO PARTS" → "BAP AUTOPARTS" (barra preta, à direita) e o sobretítulo verde logo abaixo |
| (b) | A4, pág. 2 "Por que BAP?" | `png/b_A4_pag02_institucional_par.png` | barra do topo, sobretítulo e "A BAP AUTOPARTS é uma empresa…" |
| (c) | Lubrificantes (PDF), capa | `png/c1_Lubrificantes_PDF_capa_par.png` | nada visível (a capa não tem o nome escrito; só o Author do arquivo muda) |
| (c) | Lubrificantes (PDF), pág. 2 "Quem somos" | `png/c2_Lubrificantes_PDF_quem_somos_par.png` | cabeçalho "BAP AUTOPARTS" e título "A BAP AUTOPARTS" |
| (c) | Lubrificantes (PDF), pág. 11 contato | `png/c3_Lubrificantes_PDF_gerente_comercial_par.png` | "Gerente Comercial · BAP AUTOPARTS" |
| (c) | Lubrificantes (.pptx), capa | `png/c4_Lubrificantes_PPTX_capa_par.png` | nada visível |
| (c) | Lubrificantes (.pptx), slide 2 | `png/c5_Lubrificantes_PPTX_quem_somos_par.png` | o mesmo do PDF |
| (c) | Lubrificantes (.pptx), slide 11 | `png/c6_Lubrificantes_PPTX_gerente_comercial_par.png` | o mesmo do PDF |

Observações da simulação (iguais no antes e no depois, não são mudança):
- As fotos de produto da apresentação em PDF vêm de `entradas/bap/`, que não está na nuvem: no lugar de cada foto há
  um quadro cinza. A entrega final usa as fotos.
- O .pptx foi gerado sem o `apply_theme.js` (opcional, não está no repositório) e desenhado pelo LibreOffice para
  virar PNG: as cores dos textos com cor do tema (azul, amarelo, laranja) são do tema padrão, não da BAP.
  [SUPOSIÇÃO] no PowerPoint, com o tema aplicado como na entrega de outubro, as cores são as da BAP.

## Metadados (Author)

| Arquivo | Script | Antes | Depois |
|---|---|---|---|
| Catálogo A4 (gráfica) | `print_cat.py` | BAP Auto Parts | BAP AUTOPARTS |
| Catálogo Completo Digital | `digital2.py` | BAP Auto Parts | BAP AUTOPARTS |
| Catálogo Linha Moto (usa a classe do digital) | `digital2.py` | BAP Auto Parts | BAP AUTOPARTS |
| Lubrificantes e Químicos (PDF) | `apres_bemol.py` | BAP Auto Parts | BAP AUTOPARTS |
| Lubrificantes e Químicos (.pptx): `dc:creator` e `cp:lastModifiedBy` | `apres_ppt.js` | BAP Auto Parts | BAP AUTOPARTS |
| Kit Filtros (PDF) | `kitfiltros/kit.py` | BAP Auto Parts | BAP AUTOPARTS (*) |
| Kit Filtros 32 pág. (versão 1, antiga) | `kitfiltros/kit_v1_32pag.py` | BAP Auto Parts | BAP AUTOPARTS (*) |
| Simulação do detalhe (script antigo) | `simulacao_detalhe/print_cat.py` | BAP Auto Parts | BAP AUTOPARTS (*) |

Os cinco primeiros foram lidos dos arquivos gerados nesta simulação (antes e depois).
(*) Só no código: o `kit.py` não roda na nuvem (caminho fixo `/home/claude/catalogo/...` para as fontes e as entradas,
como diz o `LEIA_GERADOR.md`); o antes é o da entrega atual (`Kit_Filtros_BAP.pdf`, Author "BAP Auto Parts").
O Portfólio já estava em "BAP AUTOPARTS".

## Conferência

- `grep -rni "auto parts" catalogo_grafico/gerador`: **0** (fora o `__pycache__`, apagado).
- Texto inteiro, página a página, antes × depois, trocando só a grafia: **0 página com outra diferença**
  (A4 pág. 2; Lubrificantes PDF, 11 páginas; Lubrificantes .pptx, 11 slides). Mesmo número de páginas.
- Pixels: só mudam as áreas da grafia (a capa não muda nenhum pixel).

## Diagramação

Nenhuma quebra de linha mudou e nada se sobrepôs; só a largura das palavras:
- A4, barra do topo: "BAP AUTOPARTS" fica 3 pt mais curto (alinhado à direita: começa 3 pt mais à direita).
- A4, sobretítulo verde: 2,8 pt mais curto.
- A4, "Quem somos": a 1ª linha fica 5,3 pt mais larga ("AUTOPARTS" em maiúsculas), cabe na coluna; o parágrafo
  continua com 3 linhas e as mesmas quebras.
- Lubrificantes, cabeçalho "BAP AUTOPARTS": 3,4 pt (PDF) e 4,6 pt (.pptx) mais curto.
- Lubrificantes, título "A BAP AUTOPARTS" (30 pt): 20,8 pt (PDF) e 32,2 pt (.pptx) mais largo; continua numa linha só.
- Lubrificantes, "Gerente Comercial · BAP AUTOPARTS": 6 pt (PDF) e 16 pt (.pptx) mais largo, dentro do cartão.

## Entregas atuais (antes de gerar de novo, depois do "aprovado")

Ainda com a grafia antiga: A4 (texto 2 + Author), Digital, Linha Moto e Kit Filtros (Author),
Lubrificantes PDF (texto 2 + Author) e .pptx (3 no texto + Author).
