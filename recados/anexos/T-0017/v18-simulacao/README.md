# T-0017 · v18 de correção (modelo numérico lido de data ou medida): SIMULAÇÃO

Decisão do Alexandre (R-20261120-131800-alexandre, item 3, "a"): "v18 de correção, já: as ~80 linhas com modelo numérico de data ou medida passam a 'duvidoso'. Simulação primeiro, com a lista de antes e depois. Ela entra antes do merge do site da T-0014."

**Só simulação.** Nada foi gravado na base e não há commit.

O que foi medido e o que muda:
- **Base medida:** a v17 do `main` (c89420c), sha256 `7e200d41…2d16`.
- **Muda:** só a coluna `SITUACAO` (separado → duvidoso) e a `MOTIVO` (vazia → o motivo novo) das linhas listadas da aba VEICULOS.
- **Não muda:** a aba PRODUTOS, as colunas e os anos. Ano e cilindrada ficam para a v19.
- **Digitado:** as linhas `ORIGEM=manual` não são tocadas. Hoje não há nenhuma.

## A regra

Um **modelo numérico** é um MODELO que começa por dígito (Renault 12/19/21, Peugeot 206/2008/3008/5008, Fiat 147/500, Scania 112/113/124, Alfa 145, Agrale 6000, BMW 118i, Chrysler 300C, Porsche 911...).

Ele continua `separado` se **pelo menos uma** das vezes em que aparece na APLICACAO é de modelo. A ocorrência **não é de modelo** quando:
1. vem seguida de "/" e ano: "12/2016", "12/16", "12/..." (é data). Uma lista como "206 / 207" ou "145/146" não é data;
2. vem seguida de "," e número ("19,05 mm"), de "dentes" ou de "mm" (é medida);
3. (modelo de 1 ou 2 dígitos) vem depois de "número/" ou "número-": "04/12", "(08-12)", "01/13 - 12/19" (é o ano de uma data);
4. (modelo que é um ano, como o Peugeot 2008) vem seguida de faixa ou de "em diante" ("2008 até 2013", "2008-2014", "2008>"), ou vem depois de data, "-" ou "até".
   - **Exceção:** "PEUGEOT - 2008 ...", com a marca logo antes, é o modelo.

Procurei em **todos** os fabricantes: são 433 linhas `separado` com modelo numérico. Só Renault 12, 19 e 21 e Peugeot 2008 tinham erro.

Renault 9, 11 e 18 não estão no dicionário. Não geram erro, mas também não são achados.

## Números

| | Antes (v17) | Depois (v18) |
|---|---|---|
| Linhas da VEICULOS | 17.270 | 17.270 |
| separado | 12.251 | **12.150** |
| duvidoso | 5.019 | **5.120** |
| Produtos com `"ve"` no site | 3.619 | 3.618 |

- **Mudam 101 linhas, de 95 produtos.**
  - Por modelo: Renault 12 (67), Peugeot 2008 (21), Renault 21 (7), Renault 19 (6).
  - Por motivo:
    - "/" e ano: 61;
    - ano de data com 2 dígitos: 13;
    - ano depois de data ou "até": 11;
    - faixa de anos: 10;
    - "dentes": 4;
    - "19,05 mm": 2.
- **Ficam 332 linhas numéricas** `separado`, conferidas.
- **Efeito no site:**
  - **1 produto perde o `"ve"` inteiro**: TRI90067. O "12" vinha de "12/1999", e o outro veículo do texto, escrito "TRAFFIC", não está no dicionário.
  - **94 produtos perdem só o veículo errado** e ficam com os outros.

## 10 exemplos

**Mudam (separado → duvidoso):**
1. TER5599492 · RENAULT 12 · "RENAULT - KWID · 01/2017-**12/2020** · DIANT." → é data.
2. SEH80006 · RENAULT 12 · "... 2.5 DIESEL COM ABS (**04/12**) - DIREITO" → é o ano de uma data.
3. CIL8552 · RENAULT 19 · "... TRAS · 3/4" (**19,05 MM**)" → é medida.
4. JUH70156 · RENAULT 21 · "... 1.0 / 1.6 30 DENTES INT. / **21 DENTES** EXT." → é medida. No mesmo produto, o RENAULT 12 vinha de "12/2016" e também muda.
5. ELE1058 · PEUGEOT 2008 · "PEUGEOT - 207 1.6 L 16V · **2008 ATE 2013**" → é ano. O 207 fica.

**Ficam separado:**
6. CXD13173 · RENAULT 12 · "RENAULT 12 ( TODOS )" → é o carro.
7. INT16651 · RENAULT 21 · "R-21 2.0 8V (1992 - 1994)" → é o carro.
8. AMT7492 · PEUGEOT 2008 · "PEUGEOT - 2008 - 05/2015 - 12/2020" → a marca vem logo antes, é o modelo.
9. ABS4512 · PEUGEOT 2008 · "PEUGEOT - 2008, 1.6 4CIL 16V, FLEX" → a vírgula não vem seguida de número colado, é o modelo.
10. PIV5002 · FIAT 147 · "FIAT - 147 / ELBA / FIORINO / OGGI" → é uma lista de modelos, não data.

**Caso de olho:** FAR6135, "PEUGEOT - 2008-2015 ATE 2026 · 208 ...", fica `separado` pela exceção da marca logo antes [SUPOSIÇÃO: é o Peugeot 2008, de 2015 até 2026].

## Arquivos

| Arquivo | O que tem |
|---|---|
| `SIMULACAO_v18_T-0017.xlsx` | Aba `MUDAM` (as 101 linhas, com a linha da VEICULOS, código, fabricante, modelo, versão, SITUACAO antes e depois, MOTIVO novo e o trecho da APLICACAO), aba `FICAM_SEPARADO` (as 332 numéricas que continuam e por quê) e aba `CONTAGENS` (antes e depois, por modelo e por motivo) |
| `simular_v18.py` | Refaz a simulação (só leitura) |
| `numeros.json` | Os números |

Depois do "aprovado":
- o `dados/scripts/base_v18.py` troca só essas 202 células (101 SITUACAO e 101 MOTIVO);
- grava 95 linhas no LOG_CORRECOES, uma por código mudado;
- confere célula a célula com a v17: PRODUTOS igual, e na VEICULOS só as 202 células;
- grava a v18. São cerca de 25 min.

O formato não muda (nenhuma coluna ou aba nova), então não precisa avisar a BAP Central sobre formato.
