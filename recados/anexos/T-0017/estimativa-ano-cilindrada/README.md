# T-0017b · ANO (faixa) e CILINDRADA por veículo: ESTIMATIVA (catalogo-dados)

Pedido do Alexandre (R-20261120-130900-alexandre): "Agora que tem colunas separadas com os veiculos, mude para que nao seja apenas um textão de aplicação na parte do detalhe do produto em anexo, coloque por coluna. MARCA, MODELO, CILINDRADA, VERSAO, ANO (AQUI PODE SER A FAIXA)".

**Só estimativa.** Nada foi gravado na base e não há commit.
- **Fonte:** a v17, com dados iguais ao `main` eedde49. Usei o extrator de `dados/scripts/base_v17.py` com um gancho que guarda onde cada modelo foi achado.
- **Universo:** as **12.251 linhas `separado`** da aba VEICULOS.
- **De onde sai o ano e a cilindrada:** do **mesmo trecho da APLICACAO**, do modelo até o próximo modelo do trecho.
- **Arquivos:**
  - `amostra.xlsx`: aba ESTIMATIVA com as 12.251 linhas (CODIGO_BAP, MARCA, MODELO, CILINDRADA, VERSAO, ANO_INICIO, ANO_FIM, TIPO_DO_ANO, ANO_DE_ONDE, VEZES_NO_TEXTO, TRECHO_DA_APLICACAO) e aba NUMEROS;
  - `estimar_ano_cilindrada.py`: refaz tudo;
  - `numeros.json`.
- **Sem dado interno:** os arquivos não têm preço, estoque nem DADOS_ADICIONAIS. A TRAVA não achou nada.

## Números (12.251 linhas separado)

| O que sai | Linhas | % |
|---|---|---|
| **Com ano** (início e/ou fim) | **10.340** | **84,4%** |
| · ano do próprio trecho do modelo | 8.525 | 69,6% |
| · ano "herdado": o ano vem depois de uma lista de modelos ("Gol / Parati / Saveiro · 1999–2013") | 1.658 | 13,5% |
| · as duas formas (o veículo aparece mais de uma vez) | 157 | 1,3% |
| · faixa completa (ANO_INICIO e ANO_FIM) | 7.060 | 57,6% |
| · só início ("2005>", "em diante", "após 2017", "19/...", ou um ano solto) | 3.249 | 26,5% |
| · só fim ("até 2010", ".../2011") | 31 | 0,3% |
| **Com cilindrada** (1.0, 1.6, 2.0...; moto em cc) | **4.941** | **40,3%** |
| · com mais de uma cilindrada ("1.8/2.0") | 2.172 | 17,7% |
| **Com os dois** | **4.729** | **38,6%** |
| Sem ano | 1.911 | 15,6% |

Cada padrão de ano reconhecido conta uma vez por linha:

| Padrão | Exemplo | Linhas |
|---|---|---|
| AAAA–AAAA | "1999–2013", "2013 até 2018", "2005 · até 2010" | 4.394 |
| AAAA> | "2005>", "2009/...", "2005 em diante" | 2.006 |
| MM/AAAA–MM/AAAA | "01/2007 - 12/2015", "01/199412/2002" | 1.957 |
| ano solto | "(09/2014)" | 1.139 |
| MM/AA MM/AA | "01/10 - 12/16" | 521 |
| AA/AA | "(92/96)" | 263 |
| AA/AA ambíguo | "04/12" (pode ser MM/AA) | 142 |
| após AAAA | — | 108 |
| AA/... | "19/..." | 101 |
| até AAAA | — | 33 |

**Cilindradas mais comuns:** 1.6 (1.662), 2.0 (1.113), 1.0 (1.112), 1.8 (999), 1.4 (847), 1.5 (354), 1.3 (345), 2.5 (282).

A cilindrada aparece em só 40% das linhas porque boa parte dos textos não traz o motor. Exemplos: "Gol / Parati / Saveiro · 1999–2013", "Corsa · 2002–2012".

## 15 exemplos reais (10 comuns e 5 difíceis)

Formato: código | trecho (normalizado) → MARCA · MODELO · CILINDRADA · VERSAO · ANO_INICIO–ANO_FIM

**Comuns:**
1. TAX10653 | "CELER 1.5 L 16V · 2013 ATE 2018" → CHERY · Celer · 1.5 · – · 2013–2018
2. CUB60180 | "STRADA - 01/2007 - 12/2015 - ADVENTURE - 1.3 16V / 1.8 / 1.8 16V ..." → FIAT · Strada · 1.3/1.8 · – · 2007–2015 (o "Adventure" depois da data não vira versão)
3. JUH70267 | "RAV4 01/2000 12/2005 AUTOMATICO COM ABS 4X4 2.0 ..." → TOYOTA · RAV4 · 2.0 · – · 2000–2005
4. EMB6852R | "CONSTELLATION 17.250E / 24.250E · 2006-2012 · CUMMINS INTERACT 6.0 ..." → VOLKSWAGEN · Constellation · 6.0 · 17.250 · 2006–2012
5. KHC125449 | "FLUENCE 01/10 - 12/16 2.0" → RENAULT · Fluence · 2.0 · – · 2010–2016
6. JUH70052 | "ROYALE 1.8/2.0 (92/96)" → FORD · Royale · 1.8/2.0 · – · 1992–1996
7. POL1651 | "BOXER 2.3 16V 2009> MULTIJET" → PEUGEOT · Boxer · 2.3 · – · 2009– (em diante)
8. BOL40006 | "MONZA 2.0 L 8V · 1986 ATE 1996" → CHEVROLET · Monza · 2.0 · – · 1986–1996
9. PAF0042 | "AGILE LTZ FLEX 1.4 2009-12/2009 D" → CHEVROLET · Agile · 1.4 · LTZ · 2009–2009
10. BOL40067 | "BONGO 2.5/2.7" → KIA · Bongo · 2.5/2.7 · – · sem ano (o texto não tem)

**Difíceis:**

11. TER5593038 | "CRUZE 01/11 12/15 DIR/ ESQ" → CHEVROLET · Cruze · – · – · 2011–2015
    - Ano de 2 dígitos, MM/AA MM/AA. Lido certo.
12. TAX10196 | "C4 PALLAS 04/12" → CITROËN · C4 Pallas · – · – · 2004–2012 (?)
    - **Ambíguo:** pode ser "abril de 2012 em diante". São 142 casos assim. Proposta: deixar o ano vazio e marcar duvidoso.
13. POL1626 | "TRACKER 1.0 12V 19/... TURBO ¦ TRACKER 1.2 12V 19/... TURBO" → CHEVROLET · Tracker · 1.0/1.2 · – · 2019– (em diante)
    - "AA/..." quer dizer em diante. O veículo aparece 2 vezes no texto.
14. FCB6055 | "HILUX DX CABINE DUPLA 4X2 MEC. 2.5 16V TURBO · 2005 ATE · ¦ HILUX DX ... · 2005 · ATE 2010 ¦ HILUX ..." → TOYOTA · Hilux · 2.5/3.0 · DX Cabine Dupla · 2005–2011
    - **"até" sem ano** num pedaço e várias ocorrências juntadas: a faixa vira o mínimo e o máximo de todas.
15. JUH70270 | "LIVINA / ..." (o ano está depois do próximo modelo) → NISSAN · Livina · – · – · 2008–2014, **herdado**
    - Lista de modelos com um ano só no fim. Quase sempre vale para todos, mas nem sempre.

## Riscos

1. **Ano herdado (1.658 linhas, 13,5%).** Em "Fiesta / EcoSport 2003–2012", o ano pode ser só do último modelo. Proposta: coluna ANO_DE_ONDE (próprio/herdado) ou levar o herdado como duvidoso.
2. **Veículo repetido no texto (2.313 linhas).** É o mesmo modelo com motor ou ano diferente: "Versa 1.0 2016>" e "Versa 1.6 2012>". Numa linha só, a faixa fica de 2012 em diante e a cilindrada fica 1.0/1.6, e o par cilindrada-ano se perde.
   - O mais fiel é **uma linha por ocorrência** (veículo + cilindrada + faixa).
   - A separado passaria de 12.251 para cerca de **16.585 linhas** (+35%).
3. **Ano de 2 dígitos ambíguo (142 linhas):** "04/12", "12/18" (AA/AA ou MM/AA?).
4. **Ano solto (1.139 linhas):** "(09/2014)". Li como início [SUPOSIÇÃO: é o ano a partir do qual serve], mas pode ser só aquele ano.
5. **Cilindrada:**
   - em caminhão é a do motor citado (Cummins 6.0), que pode ser só uma das opções;
   - moto: 125cc, 150cc;
   - não confundir com medida: tirei "mm", "kg", "bar" e "V".
6. **ERRO QUE ACHEI NA v17 (urgente, já está no `main`):** modelo numérico lido de data ou de medida. Na aba VEICULOS, como `separado`:
   - "RENAULT 12": 68 linhas, cerca de 60 erradas. Saem de "12/2016", "12/2022", que são datas.
   - "RENAULT 21": 6 de 8 erradas ("21 dentes").
   - "RENAULT 19": 2 de 7 erradas ("19,05 mm").
   - "PEUGEOT 2008": cerca de 14 de 34 erradas (é o ano 2008).
   - **Total: cerca de 80 linhas erradas.** Se o `web-site` levar o `ve` com elas, o filtro mostra "Renault 12" em produto que não é do Renault 12.
   - Correção proposta: modelo numérico não vale quando vem seguido de "/", ",", "dentes", "mm" ou data, nem quando é um ano (2008).
   - Essas linhas passam a duvidoso. Pode entrar como v18 junto com o ano e a cilindrada, ou antes, numa v18 só de correção, se o site já for publicar o filtro.

## Como ficaria a v18 (formato muda de novo, aviso à BAP Central)

**Mudanças na base:**
- Coluna nova **CILINDRADA** na VEICULOS. Proponho pôr **no fim**, depois de MOTIVO, para não mudar a posição das colunas que já existem [SUPOSIÇÃO: o site mostra na ordem pedida, MARCA, MODELO, CILINDRADA, VERSAO, ANO, seja qual for a ordem da base].
- Opcional: coluna **ANO_DE_ONDE** (próprio/herdado).
- **ANO_INICIO e ANO_FIM preenchidos.** ANO_FIM vazio quer dizer "em diante".
- As linhas `ORIGEM=manual` nunca são tocadas.

**Decisões para o Alexandre:**
- uma linha por ocorrência (recomendo) ou uma por veículo;
- os herdados e os AA/AA ambíguos: preencher ou levar como duvidoso;
- se o ano solto quer dizer "a partir de".

**Tempo (meu trabalho):**
- Simulação: cerca de **1h15**. É o extrator definitivo de ano e cilindrada dentro do `base_v18.py`, a correção dos modelos numéricos e a planilha antes e depois por linha da VEICULOS, com README.
- Gravação depois do "aprovado": cerca de **15 min**. Mesma conferência da v17: PRODUTOS igual célula a célula, só a VEICULOS, o LOG e o LEIA-ME mudam.
- **Total: 1h30**, mais o `web-site` (mostrar as colunas no detalhe) e o `testes`.
