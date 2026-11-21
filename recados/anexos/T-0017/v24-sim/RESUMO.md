# T-0017 · v24 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: R-20261121-102700-alexandre ("reveja tudo e valide os casos iguais"). Base de partida: v23 (sha256 `05eeb19a…d129`).
- 2ª rodada: corrige o que a revisão e o `testes` apontaram no 128efb3.
  - O trecho que entra em A agora é copiado, literal, da APLICACAO de B.
  - O ano é conferido no trecho isolado de V; faixa com intervalo fica fora.
  - Os casos também vêm da APLICACAO.
  - O ABS (e todo "c/"/"s/") é padronizado antes de comparar.
  - Código com "/" não vira referência.

## Como foi feito
- **Índice:** cada REFERENCIAS_CRUZADAS da PRODUTOS vira pares (MARCA, CÓDIGO), sem espaço, hífen ou ponto e em maiúsculas.
  - A leitura é a do site (`refs_de`): sem o "| ANTERIOR", sem o "BAP BOX", sem as marcas da BAP e sem fornecedor.
  - Também entra a forma sem dois-pontos ("Cofap GP32675 / Nakata HG 33010").
  - Sai o que não é código: "-", "#N/A", "N/A", texto sem dígito e código sem marca.
  - **Código com "/" não vira referência.** Isso vale para a medida de pneu ("RINALDI: HB37 110/70-17"), "FRAS-LE: PD/62-NA", "ARL4152 /1" e "PSC80/2".
    - Na 1ª rodada, a simulação partia o código na barra, e o "HB37 110/70-17" virou a referência falsa "RINALDI 7017".
    - O erro era da simulação, não do `refs_de`: o `refs_de` devolve o "HB37 110/70-17" inteiro.
    - Para o `web-site`: o site mostra esse código como referência do pneu, mas não o parte. Nada a corrigir no `gerar_site.py` por isso.
  - Só a lista com " / " (espaços dos dois lados) ou "," vira códigos separados: "F000KE0P05 / FLR8LDCU+".
- **Trecho de V num produto:** os itens da APLICACAO que começam pelo nome de V (ou por um apelido da MODELOS_VEICULO).
  - Os itens vêm dos blocos separados por ";" e, dentro deles, do "·" e da ",".
  - "Polo Sedan" não conta como "Polo".
  - O trecho só é **isolável** quando:
    - V não aparece em nenhum outro ponto do texto;
    - todos os itens estão em blocos com o mesmo "FAB - ";
    - V tem uma linha só na VEICULOS do produto.
- **Caso:** um par de códigos BAP com a mesma referência e veículos diferentes. Há dois tipos:
  - **na VEICULOS:** V está em B e não está em A;
  - **na APLICACAO:** V está nos dois, mas o trecho de V é diferente.
  - **[SUPOSIÇÃO]** Quando o trecho de V não é isolável em A ou em B, não há como comparar: 308 veículos em comum ficaram sem comparação e não viraram caso.
- **Válido** só quando passa em tudo, nesta ordem (o primeiro que falha é o motivo da aba FORA):
  1. a referência não é genérica;
  2. nenhuma outra referência da mesma marca diverge entre A e B (ex.: Nakata HG33004 x HG33093);
  3. mesma FAMILIA;
  4. mesma peça: o mesmo PRODUTO e as mesmas palavras da DESCRICAO, sem contar embalagem, posição e lado;
  5. a mesma medida, quando as duas citam medida;
  6. pelo menos uma montadora em comum;
  7. a mesma POSICAO e LADO compatível;
  8. nada muda em ABS, Locker, cabine ou "c/"/"s/", nem no DIFERENCIAL ou no ITEM_PARECIDO. Antes de comparar, o texto é padronizado: "com abs", "c/abs" e "c/ abs" são o mesmo, assim como "sem abs", "s/abs" e "s/ abs", e vale para todo "com"/"sem"/"c/"/"s/";
  9. V ainda não está no texto de A;
  10. o trecho de V em B é isolável;
  11. o trecho tem ano;
  12. o ano da VEICULOS de B é o do trecho isolado: o início é o menor ano do trecho e o fim é o maior, ou fica aberto quando o trecho tem "AAAA>";
  13. as faixas do trecho não deixam anos de fora no meio. Exemplo: o Polo do CUB60039 tem "2012–2014 · 2002–2006", que a VEICULOS juntaria em 2002–2014. Fica fora;
  14. a linha de V em B é "separado" e sem ANO_DUVIDA.
- **O que entra em A:**
  - na APLICACAO, no fim: " ; " e o trecho de V **copiado literal** de B, com o "FAB - " do bloco (ex.: "VW - Polo 1.6 L 8V 2012–2014 · Polo 2.0 L 8V 2002–2006"). Os motores e as faixas são os de B, um por um, e nada do texto de A sai;
  - na VEICULOS, a linha de V em B com o CODIGO_BAP de A. Ela bate com o trecho copiado: os anos são os do trecho (iguais à VEICULOS de B), e a CILINDRADA é a do trecho;
  - a linha nova fica "separado", sem MOTIVO e sem ANO_DUVIDA.
- **R19:** na VEICULOS do PAF0338, o R19 tem CILINDRADA "1.6 / 2.2": o 2.2 é o do R21. O trecho copiado é só "RENAULT - R19 1.6 L 8V 1993–2000", e a linha nova do PAF.0338 fica com 1.6. O R21 não entra.

## [SUPOSIÇÃO] Limites e testes a mais
- **Referência genérica:** a que está em 2 ou mais famílias (162) ou em 5 ou mais códigos BAP (3), 165 no total (aba GENERICAS).
  - Ela é o primeiro motivo de 574 veículos fora.
  - **Ela não derruba nenhum válido.** Sem limite nenhum, só com o de famílias ou só com o de 5 códigos, os válidos continuam 21: os 574 caem num teste seguinte.
- **LADO vazio** = os dois lados.
- **Testes além do recado:** os testes 2, 4, 5 e 6 e o "c/ ou s/".
  - Sem eles, entravam casos errados. Exemplos:
    - vela de grau 6 com os carros da de grau 5;
    - palheta de 21" com os da de 22";
    - amortecedor do Mitsubishi ASX com o Uno Sporting.
- **V com mais de uma linha (versões) em B:** não isolável.
- **V que já está em A com outro trecho:** fica fora. Somar trecho a um veículo que já existe em A pede mudar a linha dele na VEICULOS, e esse método não entrou nesta rodada.

## Contagens
| | |
|---|---|
| Referências lidas | 12.044 |
| Referências repetidas (2 ou mais códigos) | 1.256 |
| … delas, genéricas (suspeitas) [SUPOSIÇÃO do limite] | 165 |
| Pares de códigos com referência em comum | 738 |
| **Casos** | **662** (611 com VEICULOS diferente e 51 só pela APLICACAO) |
| Veículos em comum sem trecho isolável, sem comparação [SUPOSIÇÃO] | 308 |
| Veículos testados | 3.315 (3.125 novos em A e 190 com trecho diferente) |
| **Válidos** | **21** veículos em 12 códigos |
| **Fora** | **3.296** (3.294 da auditoria e o Palio do AMT7500 e do AMT7014) |

## Fora, por motivo
| Motivo | Veículos |
|---|---|
| outra referência da mesma marca diverge (item diferente) | 1.736 |
| referência genérica (suspeita) [SUPOSIÇÃO do limite] | 574 |
| veículo já está na APLICACAO de A | 441 |
| produto ou peça diferente (PRODUTO/DESCRICAO) | 417 |
| medida diferente | 49 |
| montadoras sem nada em comum entre A e B (suspeita) | 34 |
| muda c/ ou s/ (c/ parafuso, c/ rolamento, c/ respiro...) | 22 |
| linha de V em B é duvidosa ou tem ANO_DUVIDA | 12 |
| trecho de V em B não isolável | 5 |
| ano de V na VEICULOS de B não bate com o trecho de V em B (CIL8546 Fox e Golf) | 2 |
| só há anúncio da internet como prova (Palio no AMT7500 e no AMT7014) | 2 |
| as faixas do trecho de V em B têm intervalo (CUB60235 Polo) | 1 |
| [SUPOSIÇÃO] V já está em A com outro trecho (sem método) | 1 |

- **ABS:** com o ABS padronizado, nenhum veículo cai em "muda ABS".
  - Os 7 da 1ª rodada tinham o mesmo ABS dos dois lados, só escrito de outro jeito ("sem abs" x "s/ abs", "s/abs" x "s/ abs").
  - Eles continuam fora, pelo motivo certo:
    - CUB60159 x CUB60013: "c/ rolamento";
    - PAF.0094 e PAF.0497: o veículo já está na APLICACAO.
- Os motivos posição, lado, ABS, Locker, cabine, DIFERENCIAL/ITEM_PARECIDO, "V sem ano" e "trechos diferentes entre os B" não aparecem sozinhos: os veículos que cairiam neles já ficaram fora por um teste anterior.

## Válidos (21 veículos, 12 códigos): o trecho que entra, copiado de B
| Código A | Trecho copiado de B | Anos na VEICULOS | Referência que prova | B |
|---|---|---|---|---|
| 116 | VW - Logus 1.6 L 8V 1993–1996 · Logus 1.8 L 8V 1992–1996 · Logus 2.0 L 8V 1992–1996 | 1992–1996 | AMPRI 66007, NAKATA N92006, TRW JARB0067, VIEMAR 680007 | TAX10007 |
| 116 | VW - Pointer 1.8 L 8V 1993–1996 · Pointer 2.0 L 8V 1993–1996 | 1993–1996 | idem | TAX10007 |
| 130 | CHERY - Celer 1.5 L 16V 2013–2018 | 2013–2018 | AMPRI 62653, NAKATA N93087, VIEMAR 680653 | TAX10653 |
| 141 | BMW - Serie 1 2.0 L 16V 2004–2013 · Serie 1 3.0 L 24V 2005–2010 | 2004–2013 | AMPRI 60298, TRW JARB0046, VIEMAR 680298 | TAX10298 |
| 144 | MB - A-Class 1.9 L 8V 2000–2005 · A-Class 2.0 L 16V 2004–2011 | 2000–2011 | AMPRI 60101, NAKATA N99020, TRW JARB0131, VIEMAR 680101 | TAX10101 |
| 148 | GM - Classic 1.0 L 8V 2003–2016 | 2003–2016 | AMPRI 62169, NAKATA N93003, TRW JARB0032, VIEMAR 680169 | TAX10169 |
| CIL8546 | VW - Crossfox 1.6 L 8V 2005–2014 | 2005–2014 | KATHO K1002 | CIL8511 |
| CIL8546 | VW - Polo 1.0 L 16V 2002–2005 · Polo 1.6 L 8V 2002–2014 · Polo 2.0 L 8V 2002–2012 | 2002–2014 | KATHO K1002 | CIL8511 |
| CIL8546 | VW - Polo Sedan 1.6 L 8V 2002–2014 · Polo Sedan 2.0 L 8V 2002–2014 | 2002–2014 | KATHO K1002 | CIL8511 |
| CUB60235 | AUDI - S3 1.8 L 20V 2001–2004 | 2001–2004 | FREMAX FWB0622 | CUB60039 |
| CUB60235 | VW - NEW Beetle 2.0 L 8V 2000–2003 | 2000–2003 | FREMAX FWB0622 | CUB60039 |
| PAF.0062 | FORD - F-250 4.2 L 12V 1998–2003 · F-250 4.2 L 18V 1998–2006 | 1998–2006 | SYL 1222 | PAF0062 |
| PAF.0062 | FORD - F-350 3.9 L 8V 1998–2005 | 1998–2005 | SYL 1222 | PAF0062 |
| PAF.0090 | FIAT - Mobi 1.0 L 8V 2016–2023 | 2016–2023 | SYL 2184 | PAF0090 |
| PAF.0338 | RENAULT - R19 1.6 L 8V 1993–2000 | 1993–2000 (CILINDRADA 1.6) | SYL 1357 | PAF0338 |
| PAF.0338 | RENAULT - Sandero 1.0 L 16V 2007–2014 · Sandero 1.6 L 16V 2007–2014 · Sandero 1.6 L 8V 2007–2014 | 2007–2014 | SYL 1357 | PAF0338 |
| PAF.0338 | RENAULT - Symbol 1.6 L 16V 2009–2013 · Symbol 1.6 L 8V 2009–2013 | 2009–2013 | SYL 1357 | PAF0338 |
| PAF.0338 | RENAULT - Twingo 1.0 L 16V 2001–2002 · Twingo 1.0 L 8V 1999–2001 · Twingo 1.1 L 8V 1998–2000 · Twingo 1.2 L 8V 1993–1997 | 1993–2002 | SYL 1357 | PAF0338 |
| PAF.0554 | HONDA - CR-V 2.4 L 16V 2003–2006 | 2003–2006 | SYL 1258 | PAF0554 |
| PAF.0554 | SUZUKI - SX4 2.0 L 16V 2009–2015 | 2009–2015 | SYL 1258 | PAF0554 |
| PAF.0635 | HYUNDAI - Azera 3.3 L 24V 2008–2012 | 2008–2012 | SYL 2274 | PAF0635 |

- **Os 8 casos da revisão:**
  - 7 entram com os motores e as faixas de B, um por um: CIL8546 Polo, PAF.0338 R19 e Twingo, 116 Logus, 141 Serie 1, 144 A-Class e PAF.0062 F-250.
  - O **CUB60235 Polo fica fora**: as faixas de B (2012–2014 e 2002–2006) deixam 2007 a 2011 de fora no meio, e a VEICULOS juntaria em 2002–2014.
- **Faixas que se emendam:** a VEICULOS guarda uma linha por veículo, com o menor e o maior ano do trecho. Isso vale só quando as faixas se emendam sem buraco (ex.: Twingo 1993–1997 e 1998–2000), e esses anos são os da VEICULOS de B.
- **Frasle dos PAF:** a Frasle ("PD/62-NA") tem "/" e não conta mais. A prova dos PAF é a SYL, igual em A e em B.
- A aba VALIDOS mostra o texto inteiro antes e depois. O DEPOIS da última linha de cada código é o texto final.

## O que muda no site e o que não muda
- **Muda:** só 2 produtos do site, o CIL8546 (3 veículos) e o CUB60235 (2), com 5 veículos:
  - o texto da aplicação (campo "a") ganha os trechos copiados;
  - o filtro "Meu veículo" (campo "ve") ganha fabricante e modelo de cada veículo novo. Os anos da VEICULOS não vão para o site.
- **Não muda:**
  - os outros 10 códigos (116, 130, 141, 144, 148 e os PAF com ponto). Estão com NO_CATALOGO_DIGITAL = NÃO, que o site não mostra; são o cadastro antigo do mesmo item do B;
  - nenhum outro campo do site: referências, ficha, foto, OFEREÇA JUNTO;
  - a TRAVA e a FICHA;
  - o número de produtos.

## Anotação (sem mexer na base): "FORNECEDOR AMPRI" na REFERENCIAS_CRUZADAS
- Na v23, 152 códigos numéricos (de 1 a 164) têm na REFERENCIAS_CRUZADAS o texto "CADASTRO MASTER TERMINAL AXIAL (FORNECEDOR AMPRI) …". Entre eles estão o 1, o 102, o 116 e o 123.
- Todos estão com NO_CATALOGO_DIGITAL = NÃO, e o site não os mostra.
- O 116 está entre os válidos. A v24 só muda a APLICACAO dele; a REFERENCIAS_CRUZADAS fica como está.
- O nome do fornecedor é dado interno: vale uma decisão do Alexandre antes de algum desses códigos ir para o site.
- [SUPOSIÇÃO] O `FORNECEDORES` do `gerar_site.py` só tem AUTOIMPACT e SUNRISE; quem decide se a AMPRI entra é o Alexandre, e quem muda é o `web-site`.

## AMT7500 e AMT7014: conclusão
- Os dois dividem a **Cofap GP30120** e a **Monroe 94176** e têm os mesmos veículos (Strada), com o mesmo trecho na APLICACAO ("Strada 01/2001–12/2020"). Por isso não formam caso.
  - Mesmo que formassem, ficariam fora: a Nakata diverge (HG33004 x HG33093), e o ABS os separa (DIFERENCIAL s/ ABS x c/ ABS, ITEM_PARECIDO um do outro).
- Nenhum produto BAP com referência do AMT7500 ou do AMT7014 tem o Palio.
  - O AMT7506 (Cofap GP32675, Nakata HG33010 e HG41365) e o AMT7510 (Cofap GL12497, Nakata HG31139) têm o Palio Weekend Adventure Locker.
  - Não dividem referência com os dois e são Locker.
- A ligação da Cofap GP30120 ao "Palio Weekend Adventure 2000/2007" só existe em anúncio. Fica fora: "só há anúncio da internet como prova".
- **Conclusão: o Palio NÃO entra no AMT7500 nem no AMT7014. Os dois ficam como estão na v23.**
- O script confere isso na base (assert).

## Formato e gravação (depois do "aprovado")
- As abas e as colunas não mudam. Só mudam:
  - 12 células APLICACAO na PRODUTOS;
  - 21 linhas novas no fim da VEICULOS.
- Previsto no LOG_CORRECOES: 42 linhas, uma por veículo na APLICACAO e uma por linha nova da VEICULOS.
- O LEIA-ME ganha o bloco da v24 no topo.
- [SUPOSIÇÃO] A linha nova na VEICULOS é a decisão que ficou pendente na P12 da v21, que este pedido traz.
  - O `comparar()` do `base_comum` ainda não conhece linha nova no fim da VEICULOS: o `base_v24.py` vai precisar disso.
