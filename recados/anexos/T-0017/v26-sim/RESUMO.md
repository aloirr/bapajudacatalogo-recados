# T-0017 · v26 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: **R-20261121-190649-alexandre**, item 3. O CV-F35 foi confirmado no **R-20261121-190933-alexandre** ("1 a": 2010–2013).
- Base de partida: v25 do main 8de7a6d (sha256 `4954ab91…ac93`).
- Regra fixa (R-20261120-213300): nada novo marcado como duvidoso, e nenhum produto sai.

## 1. Contagem
| O quê | Quantos |
|---|---|
| Células da PRODUTOS (todas APLICACAO) | 21, em 21 códigos |
| Células da VEICULOS (linhas que já existem) | 10, em 5 linhas de 3 códigos |
| Linhas novas no fim da VEICULOS | 4 (17.292 → 17.296) |
| Códigos mudados | 23 |
| Produtos que saem | 0 (a PRODUTOS continua com 4.695 linhas) |
| Células com "duvidoso" (PRODUTOS + VEICULOS) | 5.122 → 5.120 (a Parati e o Santana do CIL8546 deixam de ser duvidoso; nada novo marcado) |
| LOG_CORRECOES previsto | 29 linhas: 21 APLICACAO, 4 VEICULOS mudados (uma por linha) e 4 VEICULO_NOVO |
| Site (gerar_site numa cópia) | 4.419 produtos nos dois; mudam 22 produtos (21 no "a" e 3 no "ve"); 12.154 → 12.160 veículos no "ve" |

Por item do pedido:
- 1 (SCE14002): 1 célula, junto com o item 6, e 3 linhas novas.
- 2 (CRU100 Bongo): 2 células, a APLICACAO e o ANO_DUVIDA.
- 3 (VEICULOS): 8 células (Parati e Santana) e 4 linhas novas (3 LS e a HR).
- 4 (CV-F35): 1 célula.
- 5 (MF22): nada muda, só foi conferido.
- 6 (nomes): 19 células, mais a do SCE14002. São 9 células com "Mbb", 2 com "Vwc" e 10 com "NEW Beetle".

**Conferência:** a base simulada foi comparada célula a célula com a v25 pelo `base_comum.comparar`.
- Resultado: PRODUTOS 21 mudaram, de 21 esperadas; VEICULOS 10, de 10, mais 4 linhas no fim.
- Diferenças fora do permitido: 0.

## 2. Nomes de montadora (item 6): o que a base mais usa
- **Mercedes-Benz:** na APLICACAO, "MB" aparece 347 vezes; "MERCEDES-BENZ", 255; "MERCEDES BENZ", 89; "Mercedes-Benz", 32. No prefixo "MARCA - ", "MB" aparece 223 vezes e "MERCEDES-BENZ", 20.
  - **Proposta: "Mbb" → "MB".**
- **Volkswagen:** "VW" aparece 896 vezes; "VOLKSWAGEN", 506; "Volkswagen", 15. No prefixo, "VW" aparece 609 vezes e "VOLKSWAGEN", 8.
  - **Proposta: "Vwc" → "VW".**
  - [SUPOSIÇÃO] O "c" de caminhões some; o número do modelo (13180, 16210...) já diz que é caminhão.
- **"NEW Beetle" → "New Beetle"**, como em todas as linhas da VEICULOS e da MODELOS_VEICULO.
- A troca é só da palavra inteira, com a caixa exata ("Mbb", "Vwc", "NEW Beetle"). Nada muda dentro de outra palavra. As outras grafias estão na seção 6.

## 3. Antes e depois (PRODUTOS · APLICACAO)
Nas células longas vai só o trecho que muda. A célula inteira está na aba ANTES_DEPOIS da planilha.

| Código | Linha | Antes | Depois | Item |
|---|---|---|---|---|
| SCE14002 | 1317 | Servo Embreagem Mbb LS 1630 1929 · 1932 · 1934 LS1941 Vwc 16210 17240 1730 · 111693 | Servo Embreagem **MB** LS 1630 **· LS** 1929 **· LS** 1932 **· LS** 1934 **·** LS1941 **VW** 16210 17240 1730 · 111693 | 1 e 6 |
| CRU100 | 2447 | Hyundai HR 2.5 4x2 (04/2007–12/2017), Kia Motors Bongo 2500 (07/2017) | Hyundai HR 2.5 4x2 (04/2007–12/2017), Kia Motors Bongo 2500 (07/2017**>**) | 2 |
| TER555249 | 292 | MB - Accelo 1016C Mbb 816 Accelo Esq 01/2002–12/2015 | MB - Accelo 1016C **MB** 816 Accelo Esq 01/2002–12/2015 | 6 |
| ROL33019 | 499 | …eixo tubular Mbb) | …eixo tubular **MB**) | 6 |
| ROL6204-2RS | 578 | …(caminhões Mbb, Scania, Volvo)… | …(caminhões **MB**, Scania, Volvo)… | 6 |
| ROL6204-2Z | 580 | …(caminhões Mbb, Scania, Volvo)… | …(caminhões **MB**, Scania, Volvo)… | 6 |
| BOL40041 | 1265 | MB - Mbb/Diesel | MB - **MB**/Diesel | 6 |
| SCE14008 | 1318 | Servo Embreagem Mbb Actros 2546 2646 2655 4844 2013> Axor= 9701500080 | Servo Embreagem **MB** Actros … | 6 |
| SCE14000 | 1319 | Servo Embreagem Mbb O500R O500RS O500RSD 1938S 1944S 2638S AT · 111696 | Servo Embreagem **MB** O500R … | 6 |
| SCE14007 | 1327 | Cilindro Auxiliar Embreagem Vwc 13180 15180 17260 24250 26260 · 119452 ; VW - Constellation… | Cilindro Auxiliar Embreagem **VW** 13180 … | 6 |
| LAM2007 | 4610 | …Curta para Sinaleira Mbb 1113 1313 | …Curta para Sinaleira **MB** 1113 1313 | 6 |
| BDA50028 | 1190 | …; VW - NEW Beetle 2.0 L 8V 1999–2010… | …; VW - **New Beetle** 2.0 L 8V 1999–2010… | 6 |
| CL21 | 1343 | …Golf 2.8 L 24V 2002–2003 · NEW Beetle 2.0 L 8V 2000–2010… | …· **New Beetle** 2.0 L 8V 2000–2010… | 6 |
| KG22 | 1397 | …; VW - NEW Beetle 1.4 L 16V 2013–2017 | …; VW - **New Beetle** 1.4 L 16V 2013–2017 | 6 |
| JUH70232 | 3249 | …· NEW Beetle 2.0 L 8V 2000–2003… | …· **New Beetle** 2.0 L 8V 2000–2003… | 6 |
| CUB60039 | 3344 | …; VW - NEW Beetle 2.0 L 8V 2000–2003… | …; VW - **New Beetle** 2.0 L 8V 2000–2003… | 6 |
| CUB60235 | 3538 | …; VW - NEW Beetle 2.0 L 8V 2000–2003 | …; VW - **New Beetle** 2.0 L 8V 2000–2003 | 6 |
| CV-V28 | 3686 | …· NEW Beetle 2.0 L 8V 1999–2010… | …· **New Beetle** 2.0 L 8V 1999–2010… | 6 |
| POL1625 | 3714 | …· NEW Beetle 2.0 L 8V 1999–2010 | …· **New Beetle** 2.0 L 8V 1999–2010 | 6 |
| PAF0362 | 3897 | …· NEW Beetle 2.0 L 8V 1999–2005… | …· **New Beetle** 2.0 L 8V 1999–2005… | 6 |
| VEL7544 | 4041 | …; VW - NEW Beetle 2.0 L 8V 1999–2010… | …; VW - **New Beetle** 2.0 L 8V 1999–2010… | 6 |

- **SCE14002:** os números 1929, 1932 e 1934 ganham o "LS" e passam a ser modelos. Na base, nenhum desses números vira ano: as linhas LS da VEICULOS ficam sem ano.
  - O site já descarta ano de 4 dígitos antes de 1950, então a busca não muda.
  - O "LS1941" fica junto, como no exemplo do gerente e no texto de hoje.
- **CRU100:** "a partir de 07/2017" no formato da casa ("em diante" com ">"), como o "02/2009>" e o "2013>" da base.

## 4. Antes e depois (VEICULOS, linhas que já existem)
| Código | Linha | Veículo | Coluna | Antes | Depois | Item |
|---|---|---|---|---|---|---|
| CRU100 | 8257 | KIA Bongo | ANO_DUVIDA | ano solto '07/2017': pode ser 'a partir de' ou AA/AAAA (faixa) | (vazio) | 2 |
| CIL8546 | 6282 | VOLKSWAGEN Parati | ANO_INICIO | (vazio) | 1983 | 3 |
| CIL8546 | 6282 | VOLKSWAGEN Parati | ANO_FIM | (vazio) | 2006 | 3 |
| CIL8546 | 6282 | VOLKSWAGEN Parati | SITUACAO | duvidoso | separado | 3 |
| CIL8546 | 6282 | VOLKSWAGEN Parati | MOTIVO | cita FORD, SEAT, VOLKSWAGEN sem dizer o modelo (ou só com número): "VW / FORD / SEAT" | (vazio) | 3 |
| CIL8546 | 6284 | VOLKSWAGEN Santana | ANO_INICIO | (vazio) | 1983 | 3 |
| CIL8546 | 6284 | VOLKSWAGEN Santana | ANO_FIM | (vazio) | 2006 | 3 |
| CIL8546 | 6284 | VOLKSWAGEN Santana | SITUACAO | duvidoso | separado | 3 |
| CIL8546 | 6284 | VOLKSWAGEN Santana | MOTIVO | (o mesmo da Parati) | (vazio) | 3 |
| CV-F35 | 12536 | FORD Fiesta | ANO_FIM | (vazio) | 2013 | 4 |

- **CRU100 Bongo:** o ANO_INICIO 2017 e o ANO_FIM vazio já estão certos. Só sai a dúvida, que o Alexandre resolveu.
- **CIL8546:** a Parati e o Santana **já têm linha** na VEICULOS, mas como duvidoso, e por isso não aparecem no site.
  - [SUPOSIÇÃO] "Entram como normais" quer dizer trocar essas duas linhas, e não pôr outra igual. Uma linha nova deixaria o mesmo veículo duas vezes, uma delas duvidosa.
  - O ano vem do texto: "Parati, Quantum, Santana, Saveiro / … | 1983 a 2006".
- **CV-F35:** o fim 04/2013 **está no texto**: "Fiesta 1.6 16v / Sigma 05/2010–04/2013 LT".
  - A linha do Fiesta fica 2010–2013. O ANO_INICIO 2010 já estava lá.
  - A APLICACAO não muda, nem o trecho "Fiesta 1.6 16v Ti-Vct/ Sigma 04/2013", conforme a leitura do PO.

## 5. Linhas novas da VEICULOS (no fim da aba)
| CODIGO_BAP | FABRICANTE | MODELO | VERSAO | ANO_INICIO | ANO_FIM | ORIGEM | SITUACAO | MOTIVO | CILINDRADA | ANO_DUVIDA |
|---|---|---|---|---|---|---|---|---|---|---|
| SCE14002 | MERCEDES-BENZ | LS | 1929 | (vazio) | (vazio) | automático | separado | (vazio) | (vazio) | (vazio) |
| SCE14002 | MERCEDES-BENZ | LS | 1932 | (vazio) | (vazio) | automático | separado | (vazio) | (vazio) | (vazio) |
| SCE14002 | MERCEDES-BENZ | LS | 1934 | (vazio) | (vazio) | automático | separado | (vazio) | (vazio) | (vazio) |
| CRU100 | HYUNDAI | HR | (vazio) | 2007 | 2017 | automático | separado | (vazio) | 2.5 | (vazio) |

- **LS:** seguem as linhas LS 1630 e LS 1941 do mesmo código: MODELO "LS" e VERSAO com o número.
  - O texto não tem ano, então o ano fica vazio. "Com o ano do texto" aqui é sem ano.
- **HR:** ano e cilindrada do texto "Hyundai HR 2.5 4x2 (04/2007–12/2017)". Segue as outras linhas HYUNDAI HR da aba: CILINDRADA "2.5" e VERSAO vazia.
  - [SUPOSIÇÃO] O "4x2" fica só no texto: nenhuma linha da aba guarda tração na VERSAO.
- [SUPOSIÇÃO] ORIGEM "automático", como as 17.292 linhas da aba e a linha da v25. A decisão do Alexandre fica no LOG_CORRECOES.

## 6. O que fica de fora, e por quê (aba FORA)
- **DESCRICAO** ("MBB" e "VWC" no SCE14002, SCE14008, SCE14000 e SCE14007): fica.
  - É a 2ª das 5 colunas lidas pelo BAP Ajuda e pela BAP Central, e vem do cadastro.
  - O pedido é a escrita no catálogo.
- **DADOS_ADICIONAIS** ("MBB" e "New Beetle"): é a cópia da fonte e fica.
- **Outras grafias na APLICACAO**, que não são as do pedido. Ficam, com uma **pergunta ao Alexandre** se ele quiser na mesma v26:
  - "MBB" em maiúsculas, 5 células: TER555082, TER555218, ROL32011, ROL6204-2RS-C3 e ROL683/672.
    - O ROL6204-2RS-C3 é irmão do ROL6204-2RS e do ROL6204-2Z, que passam a "MB". Sem isso, os três ficam diferentes.
  - "New beetle", com b minúsculo, no ELE1049.
  - "New Beatle", escrito errado, no CL21. O "NEW Beetle" da mesma célula muda.
  - "Vw" no CXD13055, no 116 e no TAX10007 (Vw Touareg, Vw Apollo).
  - "NEW BEETLE" no FAC6249, FAC6301, FAR6210, 42 e CUB60042: o bloco inteiro está em maiúsculas.
- **TER555249 e BOL40041:** muda só a palavra, como pede a regra 4. Ficam "MB - Accelo 1016C MB 816 …" e "MB - MB/Diesel".
  - A marca repetida já estava lá, escrita "Mbb". Tirar a repetição seria outra mudança.
- **SCE14002:** os VW do texto (16210, 17240 e 1730) não entram na VEICULOS, porque o pedido é só os LS.
- **CIL8546:** Quantum, Saveiro, Royale, Versailles, Cordoba e Ibiza continuam duvidoso. O pedido não reabre a P12.
- **CRU100:** "Kia Motors" fica como está, porque não foi pedido.
- **MF22:** a "AUTOIMPACT: MA21" fica. Conferido na REFERENCIAS_CRUZADAS.
- **Outras abas** (LOG_CORRECOES, INCLUIDOS_V7, ROLAMENTOS_INTEGRADOS, VELAS_INTEGRADAS, INTEGRADOS_V6 e o MOTIVO da VEICULOS): são histórico e citação do texto antigo. Ficam.
- **Fora da base:** o `catalogo_grafico/gerador/digital_data.json` ainda tem o texto antigo do SCE14002 ("1929–19321934").
  - Os PDFs leem 19AA e 20AA como ano (`datas.py`).
  - Aviso ao `catalogo-grafico`, que é o dono do arquivo.

## 7. No site (gerar_site.py rodado numa cópia, com a v25 e com a v26 simulada)
- Sem `[PARADO]`: 4.419 produtos nos dois, a TRAVA passa e nenhum produto entra ou sai.
- **"ve" (filtro "Meu veículo"):**
  - SCE14002 ganha MERCEDES-BENZ LS 1929, LS 1932 e LS 1934;
  - CRU100 ganha HYUNDAI HR;
  - CIL8546 ganha VOLKSWAGEN Parati e Santana.
  - O total passa de 12.154 para 12.160 veículos.
- **"a" (aplicação):** mudam os 21 códigos da seção 3.
- **Não muda:**
  - o ano do CV-F35 e o da Bongo na VEICULOS, porque os anos da VEICULOS não vão para o site;
  - as referências, a ficha, a TRAVA e a FICHA.

## 8. Formato
- Não há coluna nova nem aba nova, e as 5 primeiras colunas da PRODUTOS ficam iguais. A VEICULOS ganha 4 linhas no fim.
- Previsto no LOG_CORRECOES: 29 linhas (aba LOG_CORRECOES_PREVISTO). O LEIA-ME ganha o bloco da v26 no topo.
- Na gravação, depois do "aprovado": `dados/scripts/base_v26.py` lê a ANTES_DEPOIS e a VEICULOS_NOVA desta planilha e grava pelo `base_comum.rodar`, com `novas_no_fim={"VEICULOS": 4}`.
