# T-0019 · RD-0293 · composição do kit de embreagem uma vez só (simulação)

Só simulação: nada foi para `catalogo_grafico/entregas/`. Gerado com `PYTHONHASHSEED=0`, um processo por PDF, numa pasta temporária. **Antes:** o main `409d137` (base v27). **Depois:** o mesmo main com a correção do `detalhe.essencial` (branch `catalogo-grafico/T-0019-rd0293-sim`).

## O que muda
Nas embreagens remanufaturadas, o subtítulo do PDF repetia a composição do kit: a sobra da DESCRICAO ("plato/disco/mancal") e o rótulo do `detalhe.essencial` ("c/ platô, disco, rol. e mancal"). Agora o rótulo entra e a sobra sai:

- antes: "395MM 18 estrias plato/disco/mancal · c/ platô, disco, rol. e mancal"
- depois: "395MM 18 estrias · c/ platô, disco, rol. e mancal" (igual ao DETALHE_CATALOGO da base v27)

Só a família Embreagem Remanufaturada muda. Nenhum outro produto, nenhuma aplicação, referência ou "Leve também".

## Códigos afetados (15)
| Código | Depois |
|---|---|
| EMB1047071R | 395MM 10 estrias · c/ platô, disco, rol. e mancal (antes "plato/disco/ro/mancal") |
| EMB3400700639R | 395MM 18 estrias · c/ platô, disco, rol. e mancal |
| EMB6085R | 330MM 10 estrias · c/ platô, disco, rol. e mancal |
| EMB6126R | 330MM 10 estrias · c/ platô, disco, rol. e mancal |
| EMB6146R | 330MM 10 estrias · c/ platô e disco (antes "plato/disco · c/ platô e disco") |
| EMB6236R | 310MM 10 estrias · c/ platô, disco, rol. e mancal |
| EMB6261R | 395MM 10 estrias · c/ platô, disco, rol. e mancal |
| EMB6343R | 362MM 18 estrias · c/ platô, disco, rol. e mancal |
| EMB6453R | 430MM 24 estrias · c/ platô, disco, rol. e mancal |
| EMB6535R | 430MM 18 estrias · c/ platô, disco, rol. e mancal |
| EMB6550R | 395MM 18 estrias · c/ platô, disco, rol. e mancal |
| EMB6585R | 330MM 10 estrias · c/ platô, disco, rol. e mancal |
| EMB6635R | 430MM 18 estrias · c/ platô, disco, rol. e mancal |
| EMB6852R | 362MM 10 estrias · c/ platô, disco, rol. e mancal (antes "plato/disco mancal") |
| EMB827483R | 430MM 24 estrias · c/ platô, disco, rol. e mancal |

Não mudam: EMB3400700648R e EMB3400700649R (a descrição não cita a composição).

## Contagens
| PDF | Páginas antes | Páginas depois | Páginas com texto diferente |
|---|---|---|---|
| A4 | 56 | 56 (múltiplo de 4) | só a p.20 |
| Digital | 312 | **311** | p.2 (sumário), p.87 e p.112; a p.113 (continuação) sai |
| Linha Moto | 17 | 17 | nenhuma (texto e posição iguais) |

- **A4 p.20:** os 15 subtítulos ficam mais curtos e cabe mais uma linha na tabela (EMB6635R entra na página). A chamada passa de "Mais 3 itens desta linha no Catálogo Digital Completo / Aplicações também para Volvo, Volkswagen, Ford e Iveco" para "Mais 2 itens ... / Aplicações também para Volkswagen, Ford e Iveco".
- **Digital p.112:** os 17 itens da família cabem numa página só. A continuação (antiga p.113, com EMB6343R, EMB6635R, EMB6852R e EMB827483R) deixa de existir, e o digital fica com **uma página a menos**. A outra opção (b, abaixo) dá o mesmo: 311.
- **Digital p.113 em diante:** é a antiga p.114 em diante. Conferidas as 199 páginas: texto e posição de cada palavra iguais, só o número da página muda.
- **Digital p.2 (sumário) e p.87 (abertura da Transmissão):** os números das páginas, da Servo e Cilindro de Embreagem em diante, diminuem 1 (ex.: Servo 114 → 113).
- Aviso de uso interno em todas as páginas (56 / 311 / 17). Texto sobreposto: nada novo (só o "17 ITENS" do selo da família, igual ao main). Tamanho: A4 13 MB, Digital 5,7 MB e Moto 0,8 MB.

## Pranchas (150 dpi, antes à esquerda e depois à direita)
- `01_A4_p020_Embreagem.png`
- `02_Digital_p112_Embreagem.png`
- `03_Digital_p113_continuacao_sai.png`
- `04_Digital_p002_sumario.png`
- `05_Digital_p087_Transmissao.png`

## Pergunta ao Alexandre
> **RD-0293: composição do kit nas embreagens pesadas (15 itens; A4 p.20, Digital p.112).** O PDF repetia: "395MM 18 estrias plato/disco/mancal · c/ platô, disco, rol. e mancal". Como fica?
> **a) (recomendado)** "395MM 18 estrias · c/ platô, disco, rol. e mancal": igual à base v27 e ao site, com acento.
> **b)** "395MM 18 estrias plato/disco/mancal": fica a escrita da descrição, sem acento e sem "rol.".
> Nas duas opções o Digital passa de 312 para 311 páginas: a família Embreagem cabe numa página só, e o número das páginas da Servo em diante diminui 1. O A4 continua com 56 e ganha uma linha na p.20. O Linha Moto não muda.
> Recomendação: **1) a**
