# T-0017 · aba VEICULOS da v19: SIMULAÇÃO (catalogo-dados)

20/11/2026, 19h05 (Manaus). **Nada foi gravado:** não há versão nova, commit nem push. O `dados/` de nenhum worktree foi tocado.
- **Pedido:** R-20261120-184000-alexandre, item 6 ("6) b": simular hoje). As origens são o R-20261120-132200 (uma linha por VEÍCULO; o ano com dúvida marcado, que aparece mas não filtra) e o R-20261120-132230 (o ano solto vale "a partir de").
- **Partida:** a v19 aprovada, recriada numa cópia com o `simular_v19.py` e as 2 exceções.
  - **P3:** as 35 células com "1960–2026" ficam "1996–2026" (755 ocorrências nessas células). Algumas estavam como "1960 ATÉ 2026" e também foram trocadas.
  - **P9:** o CFR9006 fica como está na v18.
  - Por isso mudam 548 células da REFERENCIAS_CRUZADAS, e não 549. A APLICACAO continua com 2.105 células e a OFERECA_JUNTO com 224.
- **Fonte:** o worktree `wt-veiculos-sim`, no main 05b68cb, só para leitura. A base é a v18, com sha256 `2bfac384…9d9b`, igual no começo e no fim.
- **Cópias apagadas:** apaguei as duas cópias da base, a v19 e a v19 com a VEICULOS, depois de medir, porque trazem os DADOS_ADICIONAIS.

## Arquivos (`scratchpad/veiculos-sim/`)
| Arquivo | O que tem |
|---|---|
| `saida/SIMULACAO_VEICULOS_v19_T-0017.xlsx` | As abas são estas:<br>- LEIA: as contagens;<br>- EFEITO_SITE;<br>- AMOSTRA_50: 50 produtos de 37 marcas, com as 169 linhas antes e depois;<br>- ANTES_E_DEPOIS: as 17.270 linhas;<br>- VEICULOS_DEPOIS: a aba como fica, com 11 colunas;<br>- PAR_SE_PERDE;<br>- V7_ANO_SOLTO_MM;<br>- CASOS_DO_TESTES;<br>- CONJUNTO_V19;<br>- DUVIDAS;<br>- FORMATO_REGRA6;<br>- LOG_CORRECOES_PREVISTO, com 3.815 linhas, uma por código. |
| `saida/numeros_veiculos.json`, `saida/efeito_site_veiculos.json`, `saida/veiculos_base_v19.json` | Os números, o efeito no site e os veículos separados com cilindrada e ano. Este último é o que o site leria |
| `ferramentas/simular_v19_excecoes.py` | A v19 aprovada com a P3 e a P9 |
| `ferramentas/simular_veiculos.py` | A simulação da VEICULOS, que leva cerca de 2 min. Usa o extrator do `base_v17.py` do main, com um gancho de posição |
| `ferramentas/montar_copia.py` | Monta a cópia com a VEICULOS nova e confere célula a célula |
| `ferramentas/medir_veiculos.js`, `aplic_site.js` | O efeito no site. Usa o mesmo código de tela do `site/app.js` |
| `v19/` | A simulação da v19 com as 2 exceções, sem a base |
| `site_v19/`, `site_v19_veic/` | O `produtos.json` do `gerar_site.py`, sem e com a VEICULOS nova. Os dois rodaram sem `[PARADO]` |

Rodar de novo:
```
python3 -I ferramentas/simular_v19_excecoes.py <wt>/dados/BASE…xlsx v19 ../v19-sim/saida/oj_pares.json
python3 -I -B ferramentas/simular_veiculos.py <wt> v19/BASE_v19_SIMULADA.xlsx saida
```

## Como fica a aba VEICULOS
- **A identidade das linhas não muda.** Código, fabricante, modelo, versão e origem ficam como estão.
  - Nenhuma linha entra ou sai: são 17.270 antes e depois, e nenhuma se repete.
  - A aba já tinha uma linha por veículo, ou seja, por código, fabricante, modelo e versão.
  - O que muda é o juntar: um veículo que aparece várias vezes no texto continua numa linha só (V3).
- **Os anos são preenchidos:** ANO_INICIO e ANO_FIM, que estavam vazios.
  - ANO_FIM vazio quer dizer "em diante".
  - ANO_INICIO vazio quer dizer "até".
- **Há 2 colunas novas no fim:**
  - **CILINDRADA**: "1.6", "1.0 / 1.6" ou, em moto, "125cc".
  - **ANO_DUVIDA**: vazia quando o ano é firme; preenchida, traz o motivo. Esse ano aparece, mas não filtra.
- **De onde vêm o ano e a cilindrada:** do trecho da APLICACAO da v19 em que o modelo aparece, do modelo até o próximo modelo.
  - Os modelos numéricos que a v18 marcou como erro (o Renault 12 lido de "12/2016", por exemplo) não cortam o trecho.
- **Conferido na cópia:** só mudam as células da VEICULOS:
  - 13.851 de ANO_INICIO;
  - 10.027 de ANO_FIM;
  - 6.997 de CILINDRADA;
  - 2.236 de ANO_DUVIDA;
  - 2 de SITUACAO e 2 de MOTIVO, da V5.
  - As outras abas ficam iguais.

## Contagens
| | Separado (vai ao site) | Duvidoso com modelo | Todas com modelo |
|---|---|---|---|
| Linhas | **12.148** | 4.602 | 16.750 |
| Produtos | **3.616** | 535 | 4.057 |
| Com cilindrada / sem | **4.926 / 7.222** | 2.071 / 2.531 | 6.997 / 9.753 |
| · com mais de uma ("1.0 / 1.6") | 2.169 | 753 | 2.922 |
| Com ano / sem | **10.265 / 1.883** | 3.667 / 935 | 13.932 / 2.818 |
| · faixa completa | 7.172 | 2.774 | 9.946 |
| · só início (em diante) | 3.026 | 879 | 3.905 |
| · só fim (até) | 67 | 14 | 81 |
| Ano firme (filtra) | 8.223 | 3.473 | 11.696 |
| **Ano duvidoso marcado** | **2.042** | 194 | 2.236 |
| · herdado de lista | 1.623 | 168 | 1.791 |
| · AA/AA ambíguo ("04/12") | 137 | 4 | 141 |
| · ano solto "(MM/AAAA)" (V7) | 320 | 22 | 342 |
| Com cilindrada e ano | 4.717 | 2.019 | 6.736 |
| Veículo repetido no texto | 2.306 | 1.230 | 3.536 |
| · **par cilindrada-ano que se perde** | **2.056** | 1.108 | 3.164 |

- **Linhas sem nada a preencher:**
  - 520 linhas sem modelo, que só têm a marca;
  - as 101 linhas que a v18 tirou do filtro (o Renault 12 lido de data).
- **De onde veio o ano nas linhas separado:**

  | Formato no texto | Linhas |
  |---|---|
  | AAAA–AAAA | 4.552 |
  | MM/AAAA–MM/AAAA | 2.331 |
  | AAAA> | 2.062 |
  | ano solto AAAA | 428 |
  | ano solto MM/AAAA | 362 |
  | MM/AA MM/AA | 201 |
  | AA/AA ambíguo | 137 |
  | AA/AA | 125 |
  | "após AAAA" | 108 |
  | "AAAA AAAA" | 108 |
  | AA/... | 101 |
  | "até AAAA" | 67 |

- **A estimativa das 17h era de 2.313 pares perdidos;** agora são 2.056. A diferença vem da v18 (101 linhas fora do filtro) e do texto da v19.

## Efeito no site
Rodei o `gerar_site.py` do main numa cópia, fora do `dados/`, e medi com o código de tela do `app.js`.
- **O site de hoje não quebra com a base nova.** O `produtos.json` sai igual, menos o FLU15001 e o FLU15002, que perdem o "ve" (V5).
  - Hoje o `gerar_site.py` lê só FABRICANTE, MODELO, VERSAO e SITUACAO. As colunas novas e os anos ficam de fora até o PR do web-site.
- **Tabela da aplicação**, com 12.150 linhas hoje:
  - **4.926 linhas ganham a cilindrada pela base** e **10.265 ganham o ano pela base**, e não mais pelo texto. 4.717 ganham os dois.
  - **3.110 linhas** deixam de mostrar "—" em pelo menos uma coluna.
  - **Cilindrada:**
    - igual ao texto em 2.510;
    - mais completa em 2.040, porque a base junta todas e a tela de hoje mostra só a 1ª;
    - nova em 364;
    - perdida em 43, porque o "1.5" do texto era rosca ou tonelada;
    - diferente em 12, também tonelada ("Jumper 1.8 Ton").
  - **Ano:**
    - igual em 6.300;
    - novo em 2.967, nos casos em que a tela mostra "—" quando há duas faixas;
    - diferente em 998, quase todas porque a base junta a faixa mais larga das vezes em que o veículo aparece;
    - perdido em 398, quando o ano estava em outro bloco, depois do ";", e a base não herda entre blocos.
  - 2.042 linhas mostrariam ano duvidoso.
- **Filtro "Meu veículo"** (marca, modelo e ano, de 1980 a 2026; são 526.635 combinações de produto, modelo e ano):
  - **Hoje** o ano vem do texto inteiro do produto. Um ano de outro veículo do mesmo produto também vale.
  - **Com a base**, o ano é o do próprio veículo, e o duvidoso e o sem ano não filtram.
  - Casam hoje 217.851; com a base, 237.402.
  - **Saem 53.241.** Em todas, a faixa do veículo não cobre o ano: o ano era de outro veículo ou de outro motor. É o ganho de precisão.
  - **Entram 72.792:**
    - 49.455 pelo ano duvidoso, que não filtra;
    - 18.505 de veículo sem ano na base;
    - 4.832 pela faixa firme.
  - O ano muda em 2.003 produtos.
  - **Exemplos (produtos hoje → com a base):**

    | Busca | Produtos | Entram | Saem |
    |---|---|---|---|
    | Gol 2015 | 97 → 117 | 36 | 16 |
    | Palio 2010 | 153 → 141 | 19 | 31 |
    | Civic 2008 | 33 → 46 | 17 | 4 |
    | Ka 2016 | 79 → 68 | 3 | 14 |
    | Onix 2018 | 74 → 74 | 4 | 4 |

  - **Lista "Motor":**
    - hoje 7.246 pares de produto e modelo têm motor, tirado do texto inteiro; pela base, 4.656;
    - em 2.673 a lista fica menor, só com as cilindradas daquele veículo;
    - em 2.609 o veículo não diz o motor e passa a servir para qualquer um.
  - O "Leve também" usa o mesmo teste de ano e muda junto.
- **O `gerar_site.py` precisa ler as colunas novas?** Sim. Isso fica para um PR do web-site, depois da gravação. A minha proposta, que a decisão é dele:
  - o `veiculos_de` leva CILINDRADA, ANO_INICIO, ANO_FIM e ANO_DUVIDA para o "ve", com a ordem por veículo;
  - o `linhasVeiculos` usa a base primeiro;
  - o `casaVeiculo` e o `anoServe` testam o ano por veículo, e o duvidoso não filtra;
  - o `motoresDe` usa só o veículo;
  - a TRAVA continua valendo.

## Perguntas ao Alexandre (o DEPOIS da planilha é a recomendação)
- **V1 · Como marcar o ano duvidoso?**
  - a) uma coluna ANO_DUVIDA com o motivo [**recomendo**];
  - b) ANO_SITUACAO e ANO_MOTIVO;
  - c) usar SITUACAO e MOTIVO, o que tiraria o veículo inteiro do filtro.
- **V2 · CILINDRADA:**
  - a) só a cilindrada, "1.6" ou "1.0 / 1.6" [**recomendo**: o filtro Motor compara só ela];
  - b) com a válvula, "1.6 16V", como a tabela mostra hoje.
- **V3 · Juntar o mesmo veículo** (2.056 pares perdidos, aba PAR_SE_PERDE). Ex.: "Versa 1.0 2016>" e "Versa 1.6 2012>" viram "Versa · 1.0 / 1.6 · 2012–".
  - a) cilindradas juntas e a faixa mais larga [**recomendo**; o texto continua na tela];
  - b) igual à a, e o ano fica duvidoso quando o par se perde;
  - c) só a 1ª vez que o veículo aparece.
- **V4 · Ano solto sem mês** ("Strada 2021", 420 linhas separado):
  - a) a partir de [**recomendo**, como a decisão do "(09/2014)"];
  - b) só aquele ano;
  - c) duvidoso.
- **V5 · FLU15001 e FLU15002 (fluido DOT 3 e DOT 4):** o "Mercedes-Benz ML" saiu do "500 ml". São os 2 únicos produtos UNIVERSAL com veículo separado.
  - a) SITUACAO passa a duvidoso, com o motivo [**recomendo**]. O produto sai do "ve", volta ao "Leve também" de todo carro (item sem "ve" fica) e fica fora do "Meu veículo", como o resto dos universais. Na v20, o extrator deixa de ler "ml" como o ML.
  - b) deixar como está;
  - c) apagar a linha (não recomendo: a regra 4 não deixa apagar).
- **V6 · TER5599096 e TER5599097** ("HONDA - New Civic 06/2011"):
  - a) ANO_INICIO 2006 e ANO_FIM 2011 na VEICULOS [**recomendo**: é par do TAX10288, Civic 2006–2011]. A APLICACAO vira "HONDA - New Civic 2006–2011 · Dir/Esq" na **v20**, porque a v19 já está aprovada.
  - b) a regra do ano solto, 2011 em diante;
  - c) duvidoso.
- **V7 · Ano solto com mês "(MM/AAAA)"** (336 linhas separado). **Há prova de que às vezes é AA/AAAA:** em 17 casos o par do "Leve também" tem a faixa 20AA–AAAA. Exemplos: Stilo (02/2009) com o par 2002–2009, Civic (01/2006) com 2001–2006, Fit 03/2008 com 2003–2008 e Agile 09/2014 com 2009–2014. Nos itens com par, 19 batem com a faixa (contando os 2 TER) e 25 com "a partir de".
  - a) manter "a partir de" e corrigir só os 17;
  - b) corrigir os 17 pela faixa do par e marcar os outros 320 como duvidosos, que aparecem e não filtram [**recomendo**];
  - c) "a partir de" em todos.
  - Atenção: o JUH70010 da v19 já ficou "02/2009>" no texto. Se for "2002–2009", isso vai para a v20.
- **V8 · Veículos que o texto da v19 mudaria** (44 produtos: 55 a mais e 5 a menos):
  - a) não mexer agora e revisar numa v20 [**recomendo**: entre eles voltam o Renault 12 e o Peugeot 2008 lidos de data];
  - b) acrescentar como duvidoso.
- **V9 · Preencher também as 4.602 linhas duvidoso com modelo?**
  - a) sim [**recomendo**: ajuda a revisão e a BAP Central; o site não as lê];
  - b) só as separado.

## Regra 6: formato e aviso à BAP Central
**Muda o formato da aba VEICULOS:**
- 2 colunas novas no fim, a 10 (CILINDRADA) e a 11 (ANO_DUVIDA);
- ANO_INICIO e ANO_FIM passam a vir preenchidos.

**O que não muda:**
- as 9 colunas de antes, com a mesma ordem e o mesmo nome;
- as 17.270 linhas;
- a aba PRODUTOS, com as 5 primeiras colunas iguais;
- a MODELOS_VEICULO e as outras abas.

O LOG_CORRECOES e o LEIA-ME ganham linhas.

**Texto do aviso** (o `gerente-projetos` passa ao `po` antes da gravação):
> BAP Central: na v19 a aba VEICULOS da base unificada muda de formato. Ganha 2 colunas no fim, depois de MOTIVO: CILINDRADA (texto: '1.6', '1.0 / 1.6', '125cc') e ANO_DUVIDA (texto: vazio = ano firme; preenchido = o motivo da dúvida). ANO_INICIO e ANO_FIM, que eram vazios, passam a vir preenchidos (número de 4 dígitos; ANO_FIM vazio = em diante; ANO_INICIO vazio = até). As 9 colunas de antes ficam na mesma ordem e com o mesmo nome; continua uma linha por produto x veículo (mesmo número de linhas). A aba PRODUTOS não muda de formato (as 5 primeiras colunas ficam iguais); mudam só textos da APLICACAO, da REFERENCIAS_CRUZADAS e da OFERECA_JUNTO, como já avisado. Quem lê a VEICULOS pela posição da coluna não precisa mudar nada; quem lê pelo nome pode passar a usar as colunas novas.

## Fica de fora (e por quê)
- **O "L200 Triton", o "Corsa / Pick up" e o "Uno Mille Economy":** são versão ou carroceria que a VEICULOS não separa. Isso muda o conjunto de veículos, e não as colunas. Vai junto da V8, numa v20.
- **"BMW X1" lido de "M14 X 1,5":** 6 linhas em 6 produtos, 3 delas separado. É erro do extrator e fica para a v20.

## Na gravação (depois do "aprovado")
- **Ordem:** a v19 aprovada da outra sessão, na branch `catalogo-dados/T-0017-v19`, entra primeiro. Esta parte é uma v20 ou entra na mesma v19, se ainda der tempo; a escolha é do gerente.
- **Script:** `dados/scripts/base_vNN.py` grava só as células da VEICULOS listadas, com a mesma conferência célula a célula.
  - Não toca nas linhas digitadas: hoje não há linha `ORIGEM=manual`.
- **LOG_CORRECOES:** 3.815 linhas, uma por código.
- **Antes de gravar:** o aviso à BAP Central.
- **Depois:**
  - o `web-site` roda o `gerar_site.py`; o PR dele usa as colunas;
  - o `testes` confere.
