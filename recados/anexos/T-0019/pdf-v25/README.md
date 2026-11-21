# T-0019 · PDFs 2027 com a base v25 e a AUTOIMPACT por último (T-0017)

Autorização: R-20261120-235000-alexandre (aprovação antecipada nesta rodada), com o "autorizo" da AUTOIMPACT (R-20261121-113400-alexandre) e a ordem "1 a". Gerado com `PYTHONHASHSEED=0`, um processo por PDF, sobre o main `6819c7b` (base v24 e v25) mais o `9e203da` (TRAVA_PDF com a exceção e a AUTOIMPACT por último). A trava não deu `[PARADO]`. Nenhum layout muda.

- **Antes:** os PDFs do main `6819c7b` em `catalogo_grafico/entregas/`.
- **Depois:** os PDFs novos, já em `catalogo_grafico/entregas/` (A4 e Digital). O Linha Moto não foi trocado: o texto e a posição de cada palavra são iguais; mudam só a data e o ID.

## O que mudou na entrada
- `gerador/digital_data.json` (entrada fixa; ver `catalogo_grafico/LEIA-ME.md`): o AMT7500 já estava no catálogo antigo, então a aplicação vem daqui e não da base. Ganhou o trecho da v25: "FIAT Palio Weekend Adventure · 2000–2007 · Sem ABS".

## Diferenças de texto (PyMuPDF, página a página)
| PDF | Página | O que muda | Por quê |
|---|---|---|---|
| A4 | 5 (destaque AMT7500) | + "FIAT Palio Weekend … (+ outras aplicações)" | v25; o cartão corta como os outros |
| A4 | 13 (Terminal Axial) | "Aplicações também para": Volkswagen, Audi, BMW, Mercedes-Benz, Chevrolet, Peugeot, KIA e Chery (antes Audi, Volkswagen, Peugeot, KIA, Chevrolet, Seat, Citroën e Fiat) | v24 nos itens 116, 130, 141, 144 e 148, fora da página; a frase lista as 8 montadoras mais frequentes |
| A4 | 24 (Cilindro de Roda) | a mesma frase: Volkswagen passa para o 1º lugar | v24 no CIL8546 (3 trechos VW) |
| A4 | 47 (Palhetas) | EQUIVALE A de BS10 a BV15: "—" vira "Autoimpact TS10/TS12/TS14/TR10/TR11/TR12/TR14/TR15" | AUTOIMPACT como concorrência |
| Digital | 4 (destaque AMT7500) | igual ao A4 p.5 | v25 |
| Digital | 17 (AMT7500) | + "· FIAT Palio Weekend Adventure · 2000–2007 · s/ ABS" | v25 |
| Digital | 22 (KAP11120) | LEVE TAMBÉM: "AMT7014 · AMT7033" vira "AMT7500" | o par é recalculado (`oferta.py`): o AMT7500 agora tem Strada e Palio Weekend Adventure dianteiro, como o KAP11120 |
| Digital | 64 (116) | + "VW Logus … · VW Pointer …" | v24 |
| Digital | 65 (130, 141, 144, 148) | + Chery Celer, BMW Serie 1, MB A-Class, GM Classic 1.0 | v24 |
| Digital | 127 (CIL8546) | + Crossfox, Polo e Polo Sedan; LEVE TAMBÉM: "SFR30015 · SFR30025" vira "SFR30015" | v24; com o Polo e o Crossfox a SFR30015 passa à frente e a SFR30025 fica abaixo de 85% da nota |
| Digital | 262 (CUB60235) | + "AUDI S3 1.8 L 20V 2001–2004 · VW NEW Beetle 2.0 L 8V 2000–2003"; LEVE TAMBÉM: "ROL32008" vira "ROL32008 · ROL32009" | v24; o motor e as válvulas novas põem o ROL32009 na faixa do par |
| Digital | 279 a 295 (Palhetas) | as referências AUTOIMPACT entram no fim do EQUIVALE A (ex.: CL14 "Bosch 3397006888 · Tecfil TPB14 · Autoimpact PA14 · Autoimpact PU14") | AUTOIMPACT como concorrência |

Tirando "Autoimpact XXnn" e o "—", o texto das páginas 47 (A4) e 279 a 295 (Digital) é igual ao do main. A v24 nos PAF.0062, PAF.0090, PAF.0338, PAF.0554 e PAF.0635 não aparece: esses itens não estão nos PDFs.

## Conferência
- Páginas: A4 56 (múltiplo de 4), Digital 308 e Moto 17, iguais ao main.
- Tamanho: A4 13,2 MB, Digital 5,9 MB e Moto 0,8 MB.
- Aviso de uso interno em todas as páginas (56 / 308 / 17).
- Texto sobreposto: nada novo (pares de palavras que se cruzam, comparados página a página com o main).
- AUTOIMPACT: 8 no A4 (p.47) e 113 no Digital (p.279 a 295), todas na coluna EQUIVALE A ou nas referências dos destaques, sempre depois das outras marcas; 0 no Moto e 0 fora das referências.
- SUNRISE, fornecedor, estoque, R$, USD, FOB, MOQ, ranking, #N/A, "nan" e duvidoso: 0. Os falsos positivos são os mesmos do main: "preço acessível/competitivo" (texto institucional do A4), "consulte o vendedor BAP" (catálogo interno) e "Custom" (GMC 3500 HD Custom, Digital p.215 e 221).

## Pranchas (150 ppi, antes à esquerda e depois à direita)
`01` a `04`: A4 p.5, 13, 24 e 47 (destaques e tabela com CL14; CL16, CL18, CL19, CL24 e MF24 nos destaques). `05` a `11`: Digital p.4, 17, 22, 64, 65, 127 e 262. `12` a `28`: Digital p.279 (destaques) a 295; tabelas do CL14 (p.281), CL16 (p.282), CL18 (p.283), CL19 (p.284), CL24 (p.288) e MF24 (p.295).
