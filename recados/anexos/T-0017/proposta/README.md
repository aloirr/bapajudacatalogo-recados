# T-0017 · Filtro por veículo: proposta e estimativa (catalogo-dados)

Pedido do Alexandre (R-20261120-121242-alexandre, 12:12): "Incluir o filtro veiculo, com base no catalogo. criar a coluna veiculo no catalogo para ficar mais facil de filtrar: FABRICANTE (MARCA), MODELO e VERSAO (SE TIVER)."

Situação: **só proposta**. Nada foi gravado na base, nenhum commit. Fonte: `dados/BASE_BAP_UNIFICADA_PRODUTOS_BAP.xlsx` do `main` (v16; igual à do clone), lida pelo próprio `ler_base()` do `scripts/gerar_site.py` (NO_CATALOGO_DIGITAL ≠ NÃO e STATUS_CADASTRO ≠ INATIVO) e com a tabela `MONTADORAS` dele.

Arquivos deste diretório:
- `amostra.xlsx`: aba **POR_PRODUTO** (os 4419 produtos: CODIGO_BAP, APLICACAO, FABRICANTE, MODELO, VERSAO, SITUACAO, MOTIVO_DUVIDA; listas com " | ", na mesma ordem), aba **VEICULOS** (uma linha por produto × veículo, já no formato da proposta A) e aba **NUMEROS**.
- `extrair_veiculos.py`: o extrator (refazível: `python3 extrair_veiculos.py /home/user/bapajudacatalogo`).
- `numeros.json`: os números abaixo.
- Nenhum arquivo tem preço, custo, estoque, fornecedor ou DADOS_ADICIONAIS: só código, aplicação e veículo. A `TRAVA` do gerar_site.py foi rodada sobre a saída: limpa.

## 1. Como a extração foi feita

1. A APLICACAO é quebrada em trechos por `;`, quebra de linha, ` + ` e `|` (o `| DETALHE:` é cortado).
2. Em cada trecho: a marca escrita (VW, GM, MB, CITROEN...) vira o fabricante normalizado (tabela `MONTADORAS` mais os apelidos que faltavam nela: VW→VOLKSWAGEN, GM→CHEVROLET, MB/MBB→MERCEDES-BENZ, MAN→VOLKSWAGEN [SUPOSIÇÃO: caminhões MAN no Brasil = VW Caminhões]).
3. Os modelos são achados por um **dicionário de 554 modelos do mercado brasileiro** (carro, utilitário, caminhão, ônibus e moto), com variações de escrita (L 200 = L200, S-10 = S10, F4000 = F-4000, HB 20 = HB20, Doblò = Doblo). O fabricante vem do dicionário (Gol é sempre VW, mesmo quando o texto não diz a marca). Nome curto ou numérico (206, 147, R 440, L 1620, CG, Fan, Tipo, Up) só vale se a marca estiver no trecho ou na coluna montadora do produto (`mo`).
4. VERSAO = palavra de versão logo depois do modelo (LX, LXS, EXS, GLS, LTZ, Adventure, Cross, Sport, Attractive, Highline, Dakar, Full, Mille, Hatch, Sedan, Pick-Up, G5...). **Motor não é versão** (1.6 16V, Fire, EVO, Zetec, 4Cil ficam fora); 4x4 e c/ ABS também ficam fora (são DIFERENCIAL). Caminhão: o número depois do modelo é a versão (Cargo 1722, Constellation 24.250, Axor 2544).
5. Regras de exceção: "Titan 17.310" = caminhão VW; "CG Titan 150" = moto Honda (exceção do legado). "Mille" → Uno, versão Mille. "Novo/New" não vira modelo (New Fiesta → Fiesta) [SUPOSIÇÃO: geração se resolve por ano].
6. SITUACAO por produto:
   - **separado**: tem pelo menos 1 veículo com FABRICANTE + MODELO e nenhum alerta;
   - **duvidoso**: tem alerta (marca citada sem modelo reconhecido; marca do trecho diferente da marca do modelo; só fabricante de motor, câmbio, implemento ou máquina agrícola como Cummins, Eaton, Massey);
   - **sem veículo**: aplicação vazia, universal ou texto sem marca nem modelo.

## 2. Estimativa (catálogo digital: 4419 produtos)

| Indicador | Produtos | % |
|---|---|---|
| Com pelo menos 1 veículo FABRICANTE + MODELO | **4057** | 91.8% |
| separado (sem alerta, pronto para gravar) | **3620** | 81.9% |
| duvidoso (precisa de olho humano; a maioria já tem veículos bons) | **590** | 13.4% |
| sem veículo | **209** | 4.7% |

- Sem veículo (209): aplicação vazia 106; universal ou genérico (óleo, químico, "caminhões", "motos", agrícola) 78; texto sem marca nem modelo do dicionário 25.
- Motivos de dúvida (um produto pode ter mais de um): marca sem modelo reconhecido 445 (ex.: "MB - 1620, 1720", "VW - ônibus"); marca do trecho diferente da do modelo 217 (gêmeos Ducato/Boxer/Jumper, falsos positivos); só fabricante de motor/câmbio/agrícola 89.
- Linhas produto × veículo: **17149** (média de 3.9 por produto).
- Distintos: **39 fabricantes**, **832 modelos** (fabricante + modelo; inclui séries de caminhão como "MB L 1620" e "SCANIA R 112"), **475 versões** (fabricante + modelo + versão; inclui números de caminhão).
- Por LINHA:

| LINHA | separado | duvidoso | sem veículo |
|---|---|---|---|
| LEVE | 3385 | 324 | 86 |
| PESADA | 190 | 182 | 47 |
| LEVE E PESADA | 36 | 64 | 0 |
| UNIVERSAL | 2 | 0 | 74 |
| MOTO | 7 | 20 | 2 |

A linha LEVE sai quase toda automática (89% separado). A PESADA é onde está a maior parte da dúvida (182 de 419): número de caminhão sem nome de modelo, motor Cummins/MWM, eixos Meritor.

### Top 20 fabricantes (produtos)

| # | Fabricante | Produtos |
|---|---|---|
| 1 | FORD | 720 |
| 2 | CHEVROLET | 718 |
| 3 | VOLKSWAGEN | 625 |
| 4 | FIAT | 624 |
| 5 | RENAULT | 351 |
| 6 | HONDA | 319 |
| 7 | TOYOTA | 270 |
| 8 | HYUNDAI | 249 |
| 9 | CITROËN | 230 |
| 10 | PEUGEOT | 218 |
| 11 | MERCEDES-BENZ | 218 |
| 12 | AUDI | 180 |
| 13 | NISSAN | 174 |
| 14 | KIA | 159 |
| 15 | MITSUBISHI | 157 |
| 16 | VOLVO | 134 |
| 17 | JEEP | 93 |
| 18 | SCANIA | 85 |
| 19 | IVECO | 71 |
| 20 | BMW | 58 |

### Top 30 modelos (produtos)

| # | Modelo | Produtos |
|---|---|---|
| 1 | FIAT Palio | 227 |
| 2 | VOLKSWAGEN Gol | 219 |
| 3 | FIAT Uno | 181 |
| 4 | FIAT Strada | 179 |
| 5 | FORD Fiesta | 162 |
| 6 | VOLKSWAGEN Saveiro | 159 |
| 7 | FIAT Siena | 153 |
| 8 | FIAT Fiorino | 152 |
| 9 | VOLKSWAGEN Polo | 150 |
| 10 | CHEVROLET Corsa | 135 |
| 11 | FORD Ka | 134 |
| 12 | CHEVROLET S10 | 132 |
| 13 | VOLKSWAGEN Parati | 123 |
| 14 | VOLKSWAGEN Golf | 123 |
| 15 | VOLKSWAGEN Fox | 122 |
| 16 | VOLKSWAGEN Voyage | 122 |
| 17 | CHEVROLET Prisma | 120 |
| 18 | HONDA Civic | 116 |
| 19 | FORD Cargo | 115 |
| 20 | TOYOTA Hilux | 111 |
| 21 | FORD EcoSport | 109 |
| 22 | RENAULT Sandero | 109 |
| 23 | CHEVROLET Onix | 108 |
| 24 | FORD Ranger | 108 |
| 25 | CHEVROLET Montana | 105 |
| 26 | FIAT Doblo | 105 |
| 27 | RENAULT Logan | 101 |
| 28 | FIAT Palio Weekend | 100 |
| 29 | FIAT Idea | 100 |
| 30 | AUDI A3 | 100 |

### Versões mais comuns

| Versão | Produtos |
|---|---|
| FIAT Uno Mille | 32 |
| FIAT Strada Adventure | 17 |
| CHEVROLET Corsa Pick-Up | 17 |
| FIAT Palio Adventure | 15 |
| MITSUBISHI Pajero Sport | 14 |
| FORD Cargo 2422 | 14 |
| MITSUBISHI Pajero Dakar | 14 |
| MITSUBISHI Pajero Full | 12 |
| FORD Cargo 1317 | 11 |
| VOLKSWAGEN Gol G5 | 11 |
| FIAT Doblo Adventure | 10 |
| FORD Cargo 815 | 10 |
| FORD Cargo 1622 | 10 |
| CHEVROLET Corsa Sedan | 9 |
| FORD Cargo 2428 | 9 |

## 3. Exemplos reais (32: 20 comuns e 12 difíceis)

### Comuns

| Código | APLICACAO | Veículos extraídos (FABRICANTE MODELO VERSAO) | Situação |
|---|---|---|---|
| BAN9525 | FIAT - Grand Siena / Mobi / Palio / Uno · 01/2010–12/2018 · Novo c/ barra estab. / Bucha / Coxim / Sem Pivô | FIAT Grand Siena; FIAT Mobi; FIAT Palio; FIAT Uno | separado |
| INT16532 | GM - Montana 1.2 turbo, Onix 1.0 3 cilindros, 1.0 turbo (após 2020), Tracker 1.0 turbo, 1.2 turbo (após 2021) | CHEVROLET Montana; CHEVROLET Onix; CHEVROLET Tracker | separado |
| AMT7167 | VW - Polo / Virtus · 09/2017–12/2020 | VOLKSWAGEN Polo; VOLKSWAGEN Virtus | separado |
| BIE20129 | CAMARO 11 / ... (LD) | CHEVROLET Camaro | separado |
| JUH70179 | FORD - Fiesta New Aut. 1.0 / 1.5 / 1.6 01/201112/2021 Roda 21 dentes int. / 25 dentes ext. | FORD Fiesta | separado |
| PAF0811 | NISSAN - Frontier 2.5 2008> · Navara 2005> · Pathfinder 2005> · XTerra 2005> · diant. | NISSAN Frontier; NISSAN Pathfinder; NISSAN X-Terra | separado |
| TER5593038 | GM Cruze 01/11 12/15 Dir/ Esq | CHEVROLET Cruze | separado |
| ABS4537 | FORD - Ranger, 2.2 4Cil 16v, Diesel, 2013> · Ranger, 2.5 4Cil 16v, Flex, 2013> · Ranger, 3.2 5Cil 20v, Diesel, 2013> | FORD Ranger | separado |
| CXD13117 | i30 (07/2012) | HYUNDAI i30 | separado |
| KAP11899 | C3 2013 / ... | CITROËN C3 | separado |
| PIV5029 | CITROËN - Fiat/Peugeot: Boxer / Ducato / Jumper · 01/1998–12/2017 · Ø do início do cone com 17 mm · Diant. · Dir / Esq | PEUGEOT Boxer; FIAT Ducato; CITROËN Jumper | separado |
| BAN9506 | VW - Gol / Parati / Saveiro / Voyage · 01/1993–12/2008 Com Buchas / Sem Pivô | VOLKSWAGEN Gol; VOLKSWAGEN Parati; VOLKSWAGEN Saveiro; VOLKSWAGEN Voyage | separado |
| AMT7481 | HONDA - CR-V - 07/2011 - 12/2016 - Dianteiro - Dir | HONDA CR-V | separado |
| JUH70161 | FORD EcoSport 01/2003 12/2013 Automático 4X2 2.0 23 dentes int. / 25 dentes ext. Roda Dir / Esq | FORD EcoSport | separado |
| CUB60216 | HONDA - Civic · c/ ABS · 01/2017–12/2020 · 5 Furos | HONDA Civic | separado |
| PIV5022 | VW- Brasilia / Fusca / Karmann Ghia / SP-2 / TL / Variant - 01/1970 - 12/1996 - TC - Superior - Dir / Esq | VOLKSWAGEN Brasilia; VOLKSWAGEN Fusca; VOLKSWAGEN TL; VOLKSWAGEN Variant | separado |
| JUH70190 | DODGE / FIAT Freemont / Journey Automático 2.4 / 2.7 V6 01/08 12/16 Travamento no eixo anel interno Dianteiro 32 dentes int. / 32 dentes ext. Roda | FIAT Freemont; DODGE Journey | separado |
| KAC11420 | Gol (exc. G5) 1999–2013 · Parati 1999–2013 · Saveiro 1999–2009 | VOLKSWAGEN Gol; VOLKSWAGEN Parati; VOLKSWAGEN Saveiro | separado |
| POL1654 | KA 1.5 12V DRAGON 3CIL 18/20 ¦ ECOSPORT 1.5 12V DRAGON 3CIL 17/20 | FORD Ka; FORD EcoSport | separado |
| FAR6335 | FORD EXPLORER 5.0 L - 1998 ATÉ 2000 / FORD RANGER 2.3 L - 2001 ATÉ 2012 / FORD RANGER 2.5 L - 1997 ATÉ 2001 / FORD RANGER 4.0 L - 2001 ATÉ 2003 | FORD Explorer; FORD Ranger | separado |

### Difíceis

| Código | APLICACAO | Veículos extraídos | Situação | O que ensina |
|---|---|---|---|---|
| ROL33214 | VW/FORD/MB/VOLVO - VW Constellation 17.250, 24.250, Titan 17.310 ; FORD - Cargo 1722, 2422, 2428 ; MB - 1620, 1720 ; VOLVO - VM 260 · 1995–2024 · Cummins Isc / Isb, OM-366, Mwm 7.2L · Diferencial Meritor RS-19-145, MS-19-145 · ... | VOLKSWAGEN Constellation 17.250; VOLKSWAGEN Constellation 24.250; VOLKSWAGEN Titan 17.310; FORD Cargo 1722; FORD Cargo 2422; FORD Cargo 2428; VOLVO VM; MERCEDES-BENZ | duvidoso | números de caminhão viram VERSAO (Constellation 17.250, Titan 17.310 = VW, não Honda); "MB - 1620, 1720" sem prefixo fica só a marca |
| CFR9010 | FORD - C-1215 / F-12000 / ônibus ; MB - L1620 ; VW - ônibus · Caminhões trucados ; FORD - Cargo 5.9 L 12V · 1992 até 2002 · Cargo 6.6 L 12V · 1986 até 1992 | FORD C-1215; FORD F-12000; MERCEDES-BENZ L 1620; FORD Cargo; VOLKSWAGEN | duvidoso | "L1620" vira MB L 1620; "VW - ônibus" é genérico e fica só a marca |
| TER556548 | SCANIA - F112 / K112 / R112 / R142 / S112 / T112 / T142 / TL112 - 01/1981 - 12/1998 - E / H / M Dianteiro | SCANIA F 112; SCANIA K 112; SCANIA R 112; SCANIA R 142; SCANIA S 112; SCANIA T 112; SCANIA T 142; SCANIA TL 112 | separado | Scania: série + letra (R 112, T 142); duas siglas distintas por modelo |
| ROL102949/102910 | FORD/GM/DODGE/TROLLER - Ford F-1000, Ranger ; GM - D20, C20, Bonanza, Veraneio, Silverado, S10, Blazer ; TROLLER - T4 ; DODGE - Dakota · 1992–2012 · 2.5, 2.8, 3.0, 4.0, 4.1, 4.3 V6, Maxion / Mwm / Power Stroke / Vortec · Difere... | FORD F-1000; FORD Ranger; CHEVROLET D20; CHEVROLET C20; CHEVROLET Bonanza; CHEVROLET Veraneio; CHEVROLET Silverado; CHEVROLET S10; CHEVROLET Blazer; TROLLER T4; DODGE Dakota | separado | 4 marcas numa linha separadas por ";" |
| ROL0015E | FIAT / ALFA ROMEO - Uno, Mille, Fiorino, Prêmio, Elba, Palio, Siena, Strada, Doblò (s/ ABS), Alfa Romeo 145/146 - 1984 a 2014 - 1.0, 1.3, 1.4, 1.5, 1.6 8V (Fiasa / Fire) - Roda Dianteira (Direita / Esquerda) ¦ DETALHE: Rolament... | FIAT Uno; FIAT Uno Mille; FIAT Fiorino; FIAT Premio; FIAT Elba; FIAT Palio; FIAT Siena; FIAT Strada; FIAT Doblo; ALFA ROMEO 145; ALFA ROMEO 146 | separado | "Mille" vira Uno Mille; Alfa Romeo 145/146 com número |
| CFR9017 | MB - Axor 1933 / Axor 2035S / Axor 2040S / Axor 2044S / Axor 2533S / Axor 2640S / Axor 2644S | MERCEDES-BENZ Axor 1933; MERCEDES-BENZ Axor; MERCEDES-BENZ Axor 2040; MERCEDES-BENZ Axor 2044; MERCEDES-BENZ Axor 2533; MERCEDES-BENZ Axor 2640; MERCEDES-BENZ Axor 2644 | separado | "Axor 2035S": 2035 parece ano e é descartado (limite da regra automática) |
| VEL7525 | HONDA - Suzuki / Dafra (Motocicletas) · Honda Cbx 250 Twister, XR 250 Tornado, Cbx 200 Strada, XR 200R, NX 200, NX 350 Sahara, Xlx 350R, VT 600 Shadow ; SUZUKI - Intruder 250 · 1987–2016 · 200cc, 250cc, 350cc, 600cc 4 Tempos DO... | HONDA CBX; HONDA Twister; HONDA XR; HONDA NX; SUZUKI Intruder; HONDA CG; FORD Cargo; HONDA Titan; KASINSKI; YAMAHA | duvidoso | motos: "Cbx 200 Strada" não é Fiat Strada (corrigido); restam falsos (Cargo) → duvidoso |
| AMT7036 | GM - Corsa Hatch / Sedan (Enc. Mod. Antigo) · 04/2002–07/2012 / Meriva · 08/2002–07/2012 | CHEVROLET Corsa Hatch/Sedan; CHEVROLET Meriva | separado | carroceria como versão: "Corsa Hatch / Sedan" → Hatch/Sedan |
| PIV5024 | MITSUBISHI - L 200 / Pajero · Dakar / Full / Triton · 01/2001–12/2021 · Diant. Superior · Dir. / Esq. | MITSUBISHI L200; MITSUBISHI Pajero; MITSUBISHI Triton | separado | "Pajero · Dakar / Full": versão depois de "·" não é pega (fica sem versão) |
| ROL6002-2RS | UNIVERSAL / MOTOS HONDA, YAMAHA / ELETROVENTILADORES - Motos Honda CG Titan 150/160, NXR Bros, Biz 125 (comando / bomba de óleo / caixa); Eletroventiladores de radiador automotivo - Todos os anos - Motos 125cc a 300cc, motores ... | HONDA CG Titan 150; HONDA CG Titan 160; HONDA NXR Bros; HONDA Biz | separado | universal com motos citadas: CG Titan 150/160 (cilindrada como versão) |
| CXD13099 | VW 16.170 91 / 00 - CARGO 1621 99 / 02 - 1622 91 / 02 - 1630 93/02 - | FORD Cargo 1621 | separado | "VW 16.170" sem nome de modelo: some sem aviso (marcado separado por ter o Cargo) |
| TER55128 | Nielson Onibus + VW Brasilia Diant. 01/197312/1980 + VW Fusca Diant. 01/197312/1996 + VW Kombi Diant. 12/1979 + VW Kombi Carat Diant. 01/199712/2003 ; VW - Variant 1.6 L 8V · 1973 até 1980 | VOLKSWAGEN Brasilia; VOLKSWAGEN Fusca; VOLKSWAGEN Kombi; VOLKSWAGEN Kombi Carat; VOLKSWAGEN Variant | separado | "Nielson Onibus +" (encarroçadora) ignorado; VW em cada trecho |

Leitura dos difíceis: a extração automática erra pouco no carro de passeio e erra mais em caminhão (números que parecem ano, número sem nome de modelo) e moto (nomes curtos). Por isso a proposta guarda a ORIGEM de cada linha e deixa o "duvidoso" marcado para revisão, em vez de esconder.

## 4. Como guardar na base

### A) Aba nova `VEICULOS` (uma linha por produto × veículo)

Colunas: `CODIGO_BAP, FABRICANTE, MODELO, VERSAO, ANO_INICIO, ANO_FIM, ORIGEM (automático/manual), SITUACAO (separado/duvidoso)`.

- Prós: um veículo por linha (dá para filtrar no Excel e no site sem quebrar texto); cabe ano por veículo; a coluna ORIGEM protege o digitado (o script só refaz as linhas "automático"; as "manual" nunca são tocadas; regra 3 do catálogo); a aba PRODUTOS não muda; corrigir um veículo é trocar uma linha.
- Contras: ~17 mil linhas; quem lê a base precisa juntar duas abas pelo código; precisa conferir que todo CODIGO_BAP da aba existe na PRODUTOS.
- 5 primeiras colunas da PRODUTOS: **não mudam**. Nenhuma coluna da PRODUTOS muda.
- BAP Central: é **aba nova** = mudança de formato pela regra → **avisar** (não quebra a leitura dela, mas ela pode querer usar o filtro).

### B) 3 colunas no fim da PRODUTOS (`VEICULO_FABRICANTE`, `VEICULO_MODELO`, `VEICULO_VERSAO`, listas com " | ")

- Prós: tudo numa aba só, fácil de ver ao lado da aplicação.
- Contras: três listas paralelas que precisam ficar alinhadas posição a posição (um " | " a mais desalinha o resto); versão vazia vira " |  | "; célula com até 60 veículos; sem lugar para ano nem para ORIGEM, então não dá para separar o automático do digitado; filtrar no Excel exige "contém".
- 5 primeiras colunas: **não mudam** (as colunas entram depois de OFERECA_JUNTO).
- BAP Central: **coluna nova** = mudança de formato → **avisar**.

### C) (recomendada) A + aba `MODELOS_VEICULO` (dicionário controlado)

A aba `VEICULOS` da forma A, mais uma aba pequena `MODELOS_VEICULO` com `FABRICANTE, MODELO, APELIDOS (como aparece no texto: "L 200", "S-10", "F4000"), LINHA (LEVE/PESADA/MOTO), PRECISA_MARCA (SIM/NÃO)`. É o dicionário que hoje está dentro do script (554 modelos) passando a ser dado, revisável pelo Alexandre.

- Prós: tudo da A; modelo novo ou apelido novo se resolve na planilha, sem mexer em código; garante grafia única (o filtro do site não mostra "Doblò" e "Doblo" separados); a lista do filtro (fabricante → modelo) sai pronta dessa aba.
- Contras: duas abas novas para manter; mais um passo de revisão na primeira carga.
- 5 primeiras colunas: **não mudam**. BAP Central: **avisar** (2 abas novas).

**Recomendação: C.** Na v17 gravar só as linhas **separado** como `ORIGEM=automático` (3620 produtos) e os veículos bons dos **duvidosos** com `SITUACAO=duvidoso`, para revisão; anos (`ANO_INICIO/ANO_FIM`) ficam vazios na v17 e entram numa segunda etapa [SUPOSIÇÃO: 3387 produtos têm ano de 4 dígitos no texto, mas há muito ano de 2 dígitos ("01/07 12/19", "18/20") e o ano é por veículo; prefiro não chutar agora].

## 5. Como o gerar_site.py levaria isso ao produtos.json (dono: web-site)

- `ler_base()` lê também a aba `VEICULOS` (se existir; sem ela nada muda), agrupa por CODIGO_BAP e põe no produto o campo novo **`"ve": [[fabricante, modelo, versao], ...]`** (versão omitida quando vazia: `["FIAT","Uno"]`), só com linhas que têm FABRICANTE + MODELO. O campo `mo` continua igual.
- **FICHA não muda**: ela filtra os DADOS_ADICIONAIS; o `ve` vem de colunas próprias que só têm marca, modelo e versão.
- **TRAVA não muda**: ela continua varrendo o JSON inteiro, `ve` incluído. Nada a afrouxar.
- Tamanho: o `produtos.json` atual tem 2.78 MB. O `ve` acrescenta ~**379 KB** (+14%) com o nome do fabricante repetido, ou ~**251 KB** (+9%) com o fabricante como índice de uma lista no topo do JSON. Com gzip do Render, bem menos [SUPOSIÇÃO: texto repetitivo comprime ~5×].
- O filtro na tela (lista fabricante → modelo → versão) é do `web-site`/`designer-ux`; fora do meu escopo.

## 6. Decisões que o Alexandre precisa dar

1. Forma de guardar: A, B ou C (recomendo C).
2. Duvidosos: gravar marcados para revisão (recomendado) ou revisar os 590 antes de gravar.
3. Carroceria como versão (Hatch, Sedan, Pick-Up, SW): sim ou não. "Palio Weekend", "Grand Siena", "Corsa Classic", "Marea Weekend" ficam como **modelo próprio** [SUPOSIÇÃO].
4. Número de caminhão como versão (Cargo **1722**, Constellation **24.250**): sim ou não.
5. Anos por veículo: agora (mais demora e mais dúvida) ou na etapa 2.

## 7. Previsão para gravar a v17 (depois do "aprovado")

1. `dados/simulacoes/T-0017/`: planilha antes e depois (aba nova, então "antes" vazio; mais as linhas por produto) para o "aprovado". Esta amostra já é quase isso.
2. `dados/scripts/base_v17.py`: copia a v16 para `dados/versoes/BASE_..._v17.xlsx`, cria as abas novas, grava 1 linha no `LOG_CORRECOES` por código que ganhou veículos (TIPO=VEICULO_NOVO, T-0017, 20/11/2026), confere que a PRODUTOS ficou idêntica à v16 célula a célula.
3. Recado ao `gerente-projetos` para o `po` avisar a BAP Central (abas novas); pedir ao `web-site` o campo `ve` e ao `testes` a conferência.
- Tempo: ~1h30 de trabalho meu depois das decisões (30 min simulação, 40 min script v17 e conferência, 20 min LOG e recados). A revisão manual dos duvidosos, se o Alexandre quiser antes, é à parte (~590 produtos).
