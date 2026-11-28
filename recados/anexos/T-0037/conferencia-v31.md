# T-0037 · conferência na v31 (catalogo-dados, só leitura)

Feita em 27/11/2026, ~19:45 (Manaus), sobre dados/versoes/BASE_BAP_UNIFICADA_PRODUTOS_BAP_v31.xlsx. Os scripts ficaram só no scratchpad do gerente. Este arquivo registra o resultado, como o catalogo-dados relatou ao gerente-projetos.

| # | Item | Situação | Evidência resumida |
|---|---|---|---|
| 1 | Veículos só no texto da APLICACAO | ABERTO | 287 dos 4.570 produtos com APLICACAO têm algum modelo ausente da VEICULOS, com 818 ocorrências. São 243 sem nenhuma linha na VEICULOS, todos com NO_CATALOGO_DIGITAL = NÃO (148 com código numérico e 95 PAF.*), e 44 parciais, dos quais 34 estão no site. Por outro corte, 27 produtos do site têm APLICACAO e nenhuma linha na VEICULOS. Há também 2.144 linhas automáticas com ANO_DUVIDA, das quais 1.734 são "herdado" e o site tira o ano delas. A contagem é heurística, com falso positivo e falso negativo. |
| 2 | "Versailes" e "Kadet" | PARCIAL | Na VEICULOS não sobra nenhum. Na APLICACAO sobram 3: BCE3001 (2) e BOL40031 (1). |
| 3 | "Polo" nas lâmpadas | ABERTO | O LAM2004 saiu na v31. Sobram LAM2005, LAM2006, LAM2007, LAM2012 e LAM2013. |
| 4 | CIL8528 | ABERTO | L200 de 2007 a 2020, sem o "exc. 2020 c/ disco". |
| 5 | ROL0015E | ABERTO | A cilindrada aparece só no Alfa 146. |
| 6 | CXD13090 | PARCIAL | O V50 e o C70 já estão como modelo. O Focus 1.6 aparece, mas o texto o exclui. |
| 7 | PIV5002 | ABERTO | As versões do Uno estão fora da tabela. |
| 8 | Modelo excluído no próprio `ve` | ABERTO | São 24 produtos e 27 linhas. Ex.: o AMT7050 ainda tem o HB20X. |
| 9 | Caixa alta | ABERTO | CXD13090 e POL1678. |
| 10 | TAX10305 | PARCIAL | O 307 2002–2010 entrou pela Fraga. Falta o 2001/2011 do texto. |
| 11 | LAM2020 | ABERTO | O JAC T5 continua na linha MOTO. |
| 12 | "NISSANFRONTIER" colado | ABERTO | No FCB6266. |
| 13 | Rolamentos "Motos Honda" | ABERTO | 39 ROL na LEVE ou na LEVE E PESADA (70 produtos, contando todos com "moto"). |

Total: 0 resolvidos, 3 parciais (2, 6 e 10) e 10 abertos.

Para onde vai cada item, pelas decisões 23 a 25 do R-20261127-200014-alexandre:
- a lista A é formada pelos itens 2 a 12 (11 itens);
- o item 1 vai para a T-0048;
- o item 13 vai código a código, pela decisão 24.
