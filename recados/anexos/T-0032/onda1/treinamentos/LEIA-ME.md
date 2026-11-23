# T-0032 · Onda 1: os 3 treinamentos atualizados e a Mecânica Básica final (SIMULAÇÃO)

Decisões do Alexandre (R-20261123-162032-po): 1a, 2a, 3a, 4a, 5a e 6b. Nada foi para `entregas/`: os 3 atualizados passam antes pelo designer-ux e pelo Alexandre.

Cada pasta tem o .pptx, o PDF de apoio (S9, LibreOffice), `slides/` (PNG a 100 ppi), `mosaico_8_slides.png` e `comparativo_original_x_novo.png` (8 pares).

| Pasta | Slides | Com imagem no slide | Imagens | Notas |
|---|---|---|---|---|
| `mecanica_basica/` | 45 | 35 (45 com o logo do layout) | 156 | 45 |
| `baterias/` | 47 (o original tem 47) | 36 | 152 | 47 |
| `linha_moto/` | 41 (40 + "preparado para") | 30 | 96 | 41 |
| `lubrificantes/` | 47 (43 + módulo 04 Químicos) | 33 | 127 | 47 |

Em todos: Arial (nenhum "Calibri" no pacote), "uso interno" no rodapé, verde do logo `#59BA61` no tema, "Novembro de 2026" na capa, notas no formato do original (MENSAGEM-CHAVE, COMO CONDUZIR...), nenhum "estoque" nem "R$" (o gerador para se aparecer), todo código citado conferido na base v28 (existe e está ATIVO), e o .pptx sai igual byte a byte a cada geração.

## Rodada 2: pareceres de UX e de marca (MC-0023 e MC-0024)

Mecânica Básica e Linha Moto foram liberados e não mudaram (regerados idênticos, byte a byte).

| Deck · slide | O que mudou |
|---|---|
| Baterias 22 | O logo do YouTube saiu; entrou o ícone de vídeo do padrão (câmera branca no círculo verde `#59BA61`). O QR e o link ficam. O link agora quebra entre palavras: no LibreOffice ele era um bloco só e cortava "c om" e "cel ular". |
| Baterias 41 | Título em 1 linha: "Velas: partida difícil nem sempre é a bateria". |
| Lubrificantes 3 | Grade 5 × 2 com o cartão "✓ Fechamento" de volta (2 colunas, no fim). |
| Lubrificantes 20 a 23 e 27 | Texto vermelho sobre fundo claro passou a `#8A3F00` ("Fora do portfólio", "Não indicar"...). |
| Lubrificantes 27 | "DIE5500 · 500 ml" em verde-escuro, como os outros códigos. |
| Guia | `PADRAO_TREINAMENTO.md`: vermelho `#D64545` no ícone de sinal grave, na faixa que reprova (Baterias 29) e na escala de leitura (Baterias 23); amarelo `#F2C14E` só na escala de leitura, com texto escuro. Os dois "a aprovar pelo Alexandre". |

Na fila, sem fazer agora: "1L" → "1 L".

## Rodada 3: mídia órfã fora do pacote

O gerador agora tira do .pptx toda mídia que nenhum slide, layout ou master usa (a imagem trocada ou a forma apagada deixava o arquivo antigo dentro do pacote, como o logo do YouTube em Baterias). Mídias órfãs que saíram: Mecânica Básica 40, Baterias 1 (o logo do YouTube), Linha Moto 4, Lubrificantes 1. Conferido com `gerador/treinamento_orfas.py`: 0 órfãs nos 4. Os PNGs dos 180 slides saem iguais, pixel a pixel, aos do c75390d.

## Como foi feito

O `treinamento_molde.py` abre o próprio original de cada um e regera todos os slides dele, na ordem. O JSON (`gerador/treinamentos/<nome>.json`) só diz o que muda em cada slide (`editar`) e o que entra (`inserir_depois`). O que não está no JSON fica como no original.

## O que mudou em relação ao original

**Baterias**
- Tabela do portfólio (14) pela base: 6 linhas (TF, EFB, LP, MX leve, MX…F, MX pesada) com a faixa de Ah dos códigos ATIVOS. O original tinha 5 linhas ("B", "BF") e faixas que não batem com a base.
- CCA da 60D-LP-18 pela base: 485 A (o original dizia 430 A) nos slides 15 e 24; a conta do teste passa a 243 A. A "LP70" das notas virou a 70D-MXP-12 (CCA 560 A, 280 A).
- "estoque" saiu (S2): "falta do modelo" no fechamento e no Não fechou; armazenagem fala em prateleira.
- Slide 31: "Terminais oxidados / ou soltos" (com Arial, o título ia a 2 linhas e encostava).
- Notas dos slides 43 e 44 no formato do original.

**Linha Moto**
- Coluna "Estoque" fora das 6 tabelas (pneus, câmaras, químicos, fluido de freio, velas, rolamentos 2) e as notas "Estoque somado em 13/10/2026" fora.
- Lâmpada: "4.261 unidades em estoque" fora. Filtro de ar: o FAR6365 está "SEM ESTOQUE NO ARQUIVO" na base, então o cartão virou "Filtro de ar" com "Confira a aplicação no Catálogo BAP".
- Óleos 4T: os números de unidades saíram.
- Novo slide 4, "Ao final… você estará preparado para" (S4), no molde do de Baterias.
- Notas: as soltas do original ganharam o formato; os 5 slides sem nota (4, 7, 19, 26, 33 do original) ganharam notas.
- Grafia ProActive. Arquivo sem a data: `Treinamento_Linha_Moto_BAP_Vendedores`.

**Lubrificantes**
- Módulo 04 Químicos (novo, 4 slides: divisória, 4 famílias, tabela com código e quando oferecer, onde oferecer); os módulos seguintes passam a 05–08 e os Tópicos a 8 cartões. Códigos AER, SIL, FLU, RAD e DIE da base; a dica diz quantos químicos ATIVOS há na base.
- "Toda a linha ativa tem estoque nas 7 filiais" fora (slide 17, texto e notas); a nota do Mix sem "volume em estoque das filiais".
- Pela base: ProActive 200 10W-40 é API SN (o original dizia SM); Shiftease 120 85W-140 é sintético (o original dizia mineral); fluido de radiador vai de 1 L a 20 L ATIVOS (o original dizia até 1.000 L).
- S7: a SQ (31/03/2025, ILSAC GF-7) ficou. O "CL-4 (PC-12), licenças a partir de 01/01/2027" virou "PC-12: nova categoria diesel, com licenças previstas para 2027". [SUPOSIÇÃO: sem internet neste ambiente para conferir na API; o nome final da categoria não foi confirmado, por isso saiu.]
- Grafia ProActive, Shiftease e Effitech (o kicker continua em caixa alta). "estoque" fora (armazenagem, Não fechou: "falta do produto"). Notas dos slides 38 a 40 no formato.

**Mecânica Básica (final)**: regerada pelo mesmo gerador; já tinha "uso interno" e o `#59BA61`; o único ajuste é a lista de fontes do pacote (docProps), que também passa a Arial.

## Dados sem fonte na base (mantidos)

- Baterias: +150 pontos de venda, +30 linhas, +200 mil produtos/mês, "entre os 5 maiores fabricantes"; medidas das caixas LP60BFD/LP60AFD (238 × 175 × 175/189 mm) e o código de fábrica; tabela de tempo de recarga; ½ vida útil a cada +8 °C e 2 a 4 anos (fontes citadas no slide); 6 a 8 e ~200 partidas por dia (Heliar).
- Linha Moto: emplacamentos (Abraciclo, Fenabrave); medida e óleo de fábrica por moto; aplicação típica dos pneus; referência NGK das velas; medidas dos rolamentos; índices de carga e velocidade; ebulição do fluido DOT (FMVSS 116); "kit relação chegando" (não está na base).
- Lubrificantes: registro ANP, viscosidade a 100 °C e ponto de escoamento (ficha técnica e FDS); exemplos de veículos do "Onde oferecer"; data da SQ e da PC-12 (S7, acima); CEATOX e normas de segurança.

## Sobreposição

A conferência automática (PyMuPDF) aponta 4 casos por deck atualizado (Baterias 6 e 36, Moto 29, Lubrificantes 7 e 12). Olhei cada um: são blocos de texto vizinhos que o PDF agrupa; nos PNGs não há texto sobre texto.

## Nomes finais propostos (render.yaml e página de Materiais)

- `Treinamento_Mecanica_Basica_BAP_Vendedores.pptx` e `.pdf`
- `Treinamento_Baterias_BAP_Vendedores.pptx` e `.pdf`
- `Treinamento_Linha_Moto_BAP_Vendedores.pptx` e `.pdf` (sem o "_27-10" do original)
- `Treinamento_Lubrificantes_BAP_Vendedores.pptx` e `.pdf`

## Como gerar

```
cd catalogo_grafico/gerador
PYTHONHASHSEED=0 python treinamento_molde.py <mecanica_basica|baterias|linha_moto|lubrificantes> --sim PASTA
```
