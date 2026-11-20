# T-0017 · Filtro por veículo (FABRICANTE, MODELO, VERSAO): SIMULAÇÃO da v17

Simulação de 20/11/2026 (Manaus), feita pelo `catalogo-dados`. **A base não foi gravada.** `dados/versoes/` também não mudou. A base continua sendo a v16 (sha256 `69b9cd98…c4dd`, igual a `dados/versoes/BASE_BAP_UNIFICADA_PRODUTOS_BAP_v16.xlsx`).

- **Pedido** (R-20261120-121242-alexandre): "Incluir o filtro veiculo, com base no catalogo. criar a coluna veiculo no catalogo para ficar mais facil de filtrar: FABRICANTE (MARCA), MODELO e VERSAO (SE TIVER)."
- **Decisões** (R-20261120-122800-alexandre, "1) a 2) me de 5 exemplos do porque ele é duvidoso 3) Sim 4) sim 5) ok 6) sim", e R-20261120-122930-alexandre, "2) colocar do jeito que ta. vamos revisar depois"):
  - **Forma:** aba `VEICULOS` + aba `MODELOS_VEICULO`. A aba `PRODUTOS` não muda.
  - **Duvidosos:** entram na `VEICULOS` como estão, com `SITUACAO=duvidoso` e o motivo na coluna `MOTIVO`.
    - Ficam fora do filtro "Meu veículo" até a revisão: o `gerar_site.py` só leva ao `ve` as linhas `separado`.
    - A busca geral continua achando esses produtos pela APLICACAO.
  - **Carroceria** (Hatch, Sedan, Pick-Up, SW) entra como VERSAO. Furgão, Wagon e Cabine Dupla/Simples entram também [SUPOSIÇÃO: também são carroceria].
  - **Número de caminhão** entra como VERSAO: Cargo **1722**, Constellation **24.250**, Axor **2035**.
    - Série com letra também: MB `L` **1620**, Scania `R` **440**. A letra é o MODELO [SUPOSIÇÃO].
  - **Ano:** fica para a etapa 2. `ANO_INICIO` e `ANO_FIM` ficam vazios.
  - **BAP Central:** o `po` avisa. São duas abas novas no fim; a `PRODUTOS` e as 5 primeiras colunas não mudam.

## Arquivos

| Arquivo | O que tem |
|---|---|
| `SIMULACAO_T-0017.xlsx` | O que a v17 vai ganhar, mais a revisão e o resumo (abas abaixo) |
| `../../scripts/base_v17.py` | `--simular` refaz esta planilha e a conferência, sem gravar. Sem opção, grava a v17 a partir desta planilha (só depois do "aprovado") |

Abas da `SIMULACAO_T-0017.xlsx`:

| Aba | Vai para a base? | O que tem |
|---|---|---|
| `VEICULOS` | **sim**, igual | CODIGO_BAP, FABRICANTE, MODELO, VERSAO, ANO_INICIO, ANO_FIM, ORIGEM (`automático`), SITUACAO (`separado`/`duvidoso`), MOTIVO (só nos duvidosos) |
| `MODELOS_VEICULO` | **sim**, igual | O dicionário: FABRICANTE, MODELO, APELIDOS (como aparece no texto), LINHA (LEVE/PESADA/MOTO), PRECISA_MARCA |
| `DUVIDOSOS` | não | Só a **lista de revisão**: uma linha por produto duvidoso, com a aplicação, o que foi achado, o tipo da dúvida e o porquê. As linhas desses produtos já estão na `VEICULOS` |
| `RESUMO` | não | Contagens (geral, por fabricante, por modelo, por versão) e os que não separam |
| `LOG_CORRECOES_PREVISTO` | sim, no fim do `LOG_CORRECOES` | Uma linha por código que ganha linhas na `VEICULOS` (TIPO `VEICULO_NOVO`, T-0017, 20/11/2026) |

Os arquivos não têm preço, custo, estoque, fornecedor nem DADOS_ADICIONAIS. Têm só código, aplicação e veículo, e passam pela `TRAVA` do `gerar_site.py`.

## Números (com carroceria e número de caminhão como versão)

| Indicador | Valor |
|---|---|
| Produtos do catálogo digital | 4.419 |
| Com pelo menos 1 veículo FABRICANTE + MODELO | 4.057 (91,8%) |
| **separado** (vai ao filtro do site) | **3.619** (81,9%) |
| **duvidoso** (na VEICULOS, fora do filtro até a revisão) | **591** (13,4%) |
| sem veículo (não entra na VEICULOS) | 209 (4,7%) |

**Linhas da VEICULOS:** 17.270 no total, de 4.210 produtos.
- `separado`: 12.251 linhas. Destas, 1.427 têm VERSAO.
- `duvidoso`: 5.019 linhas:
  - 4.499 com fabricante e modelo;
  - 485 só com a marca;
  - 35 sem veículo achado, só com o código e o MOTIVO.

**Distintos nos separados:** 39 fabricantes, 511 modelos e 586 versões. O dicionário tem 553 modelos.
- A série de caminhão contada uma vez ("MB L", com o número na versão) baixou os modelos de 832 para 511.
- O número de caminhão como versão subiu as versões de 475 para 586.

**Top 10 modelos (produtos separados):** FIAT Palio 206, VW Gol 185, FIAT Strada 164, FIAT Uno 164, FORD Fiesta 148, FIAT Siena 140, FIAT Fiorino 134, VW Saveiro 133, CHEVROLET Corsa 128, FORD Ka 124.

**Versões mais comuns:** Uno Mille 30, Corsa Pick-Up 21, Strada Adventure 17, Gol G5 12, Palio Adventure 12, Corsa Wagon 12, Pajero Dakar 12, Corsa Sedan 11.

**Por que é duvidoso** (um produto pode ter mais de um motivo):

| Tipo da dúvida | Produtos |
|---|---|
| a marca aparece sem modelo | 445 |
| a marca do trecho é diferente da marca do modelo | 146 |
| só fabricante de motor, câmbio ou máquina agrícola | 89 |

**Sem veículo, por motivo:**

| Motivo | Produtos |
|---|---|
| aplicação vazia | 106 |
| universal ou genérico (óleo, químico, "caminhões", agrícola) | 78 |
| texto sem marca nem modelo conhecido | 25 |

## Os 5 exemplos de duvidoso (para o Alexandre)

| Código | Aplicação (só o texto da aplicação) | O que o extrator achou | Por que ficou duvidoso |
|---|---|---|---|
| CFR9024 | "Volkswagen / Ford — caminhões e ônibus com freio a ar" | VOLKSWAGEN e FORD, sem modelo | Fala só a marca e "caminhões e ônibus", sem dizer qual caminhão. |
| SCE14001 | "Servo Embreagem Volvo N10 NL10 N12 NL12 B7 B10 B12 Volvo VM FH12 FH16 · 111700 ; VOLVO - B 10 M 9.6 L 12V · 1998 até 2003 · ... B 58 ..." (lista longa de caminhões e ônibus Volvo) | VOLVO N10, NL10, N12, NL12, B12, VM, FH12, FH16, B10M, B58 e um **HONDA City** | Os Volvo estão certos, mas o extrator achou um "City" no meio do texto e leu como o carro da Honda: só uma pessoa confirma. |
| PAF0796 | "FORD - Focus (Todos modelos) 2008> ; PEUGEOT - 508 1.6 Thp 16V 2011> ; VOLVO - C30 2.0 2007> · S40 T-5 2.5 2004> · V40 2.0 2012> · V50 2.4 2004> · V50 T-5 2.5 2004> · tras." | FORD Focus; VOLVO C30, S40, V40; **JAC T5**; PEUGEOT sem modelo | O Peugeot "508" não está no dicionário, então ficou só a marca. O "T-5" do Volvo (versão do motor) foi lido como o carro JAC T5. Também faltou o Volvo V50. |
| VEL7525 | "HONDA - Suzuki / Dafra (Motocicletas) · Honda Cbx 250 Twister, XR 250 Tornado, Cbx 200 Strada, ... ; HONDA - ... CG 125 Cargo ... CG 125 Titan ..." (vela de moto, muitas motos) | Honda CBX, Twister, XR, NX, CG, Titan; Suzuki Intruder; **FORD Cargo**; KASINSKI e YAMAHA sem modelo | "CG 125 Cargo" é moto Honda, mas "Cargo" foi lido como o caminhão Ford. As motos Kasinski Magik e Yamaha FZR não estão no dicionário e ficaram só com a marca. |
| ROL33214 | "VW/FORD/MB/VOLVO - VW Constellation 17.250, 24.250, Titan 17.310 ; FORD - Cargo 1722, 2422, 2428 ; MB - 1620, 1720 ; VOLVO - VM 260 · 1995–2024 · ..." | VW Constellation 17.250 e 24.250; VW Titan 17.310; FORD Cargo 1722, 2422 e 2428; VOLVO VM; MERCEDES-BENZ sem modelo | Está quase tudo certo. O "MB - 1620, 1720" só tem o número, sem o nome do modelo (L, LS, Atego?), e o extrator não arrisca. |

Resumo para o Alexandre: o duvidoso quase sempre já tem os veículos certos. Ele só tem **um pedaço** que a máquina não garante:
- só a marca, sem modelo;
- uma palavra que também é nome de carro (City, Cargo, T5);
- modelo que ainda não está no dicionário (Peugeot 508, motos Kasinski).

Corrigir é trocar a linha na `VEICULOS` (com `ORIGEM=manual`) ou acrescentar o modelo no `MODELOS_VEICULO`.

## Conferência da aba PRODUTOS (célula a célula)

O `--simular` monta a v17 num diretório temporário a partir da base de hoje, aplicando o que está nesta planilha. Depois compara com a v16, valor e formatação, em todas as abas que já existem. Resultado:

- **PRODUTOS: 84.582 células conferidas, 0 diferentes.** Linhas, colunas, larguras, alturas, filtro e painel congelado também iguais. As 5 primeiras colunas não mudam.
- As outras 10 abas antigas ficam iguais, fora o permitido:
  - `LOG_CORRECOES`: +4.210 linhas no fim;
  - `LEIA-ME`: +5 linhas no topo, com o título e o resumo da v17.
- Duas abas novas no fim, `VEICULOS` e `MODELOS_VEICULO`, iguais às desta planilha.
- Diferenças fora do permitido: **0**.

## Para gravar a v17 (depois do "aprovado")

1. `python3 dados/scripts/base_v17.py`. O script para sem gravar se:
   - a base não for mais a v16;
   - a v17 já existir;
   - um código da `VEICULOS` não estiver na `PRODUTOS`;
   - o LOG não tiver uma linha por código;
   - a comparação com a v16 achar qualquer diferença fora do permitido.
2. Ele grava a base e `dados/versoes/BASE_BAP_UNIFICADA_PRODUTOS_BAP_v17.xlsx` e imprime os sha256.
3. Depois:
   - o `web-site` lê a aba `VEICULOS` no `gerar_site.py` e leva ao campo `"ve"` só as linhas `SITUACAO=separado`, sem mudar a FICHA nem a TRAVA;
   - o `testes` confere;
   - o `po` avisa a BAP Central.
4. Se o "aprovado" vier em outro dia: troque `DATA` no script e rode `--simular` de novo, para o LOG levar a data certa.
