# T-0046 · Lista de trabalho da nova pesquisa de anos

Só leitura, sobre a base **v31** (a base não muda). Refazer: `python3 dados/scripts/lista_T0046.py`.

## Arquivos

- `lista_trabalho_T0046.xlsx`: tem três abas.
  - **LISTA:** 3.069 linhas, 1.154 códigos.
  - **RESUMO:** os totais por origem, por `o_que_falta` e por família, o que mudou da v30 para a v31 e o que ficou fora.
  - **PARA_A_SESSAO_LOCAL:** as instruções da T-0040 e o formato de volta.
- `lista_trabalho_T0046.csv`: as linhas da LISTA, em UTF-8 com BOM e separado por `;`. É este arquivo que vai para a sessão local da Fraga.
- O CSV tem as colunas da lista da T-0040, com duas trocas: o `tipo` virou `o_que_falta` e entrou a coluna `origem`.

## Colunas

- **id_linha:** o número da linha de dados na aba VEICULOS da v31 (a linha do Excel é o id + 1).
  - Os ids da T-0040 eram os da v30. Eles passaram para a v31 pelo alinhamento das duas abas, porque a v31 tirou 2 linhas e pôs 6 no fim.
  - **Vazio** quer dizer veículo do texto da APLICACAO sem linha na VEICULOS. São 10 linhas:
    - FCB6266: Van 310 D e Silverado Conquest;
    - INT16639: Gurgel BR800, Karmann Ghia, Puma, SP2 e TC;
    - INT16652: Puma, SP2 e TC.
  - [SUPOSIÇÃO] Nessas 10 linhas, a montadora e o modelo são os do texto ("VW - …").
- **o_que_falta:** `os dois`, `início`, `fim` ou `conflito`.
  - `conflito` cobre os 92 da v30 e a Ranger do INT16529 (2019–2016).
- **origem:** uma por linha, a primeira em que a linha cai, nesta ordem:
  1. `4 códigos`;
  2. `v30 conflito novo`;
  3. `v30 sem resolução`;
  4. `fora da Fraga`;
  5. `não resolvida`;
  6. `DE_PARA`;
  7. `fora das origens (motivo)`: as linhas sem ano completo que não caem em nenhuma das seis. O motivo vai entre parênteses: `manter_atual da T-0040`, `fora da lista da T-0040` ou `linha nova da v31`.
- A RESUMO mostra o tamanho de cada grupo antes de tirar as linhas repetidas.
- A descrição e as referências vêm do `site/data/produtos.json`. Não há preço, estoque nem dado interno: a planilha passa pelo `sem_interno`, e o CSV pelo `INTERNO`.

## Contas (v30 → v31)

| Grupo | Na tarefa | A pesquisar na v31 |
|---|---|---|
| v30 conflito novo | 86 | 86 (o Taos está na origem `4 códigos`) |
| v30 sem resolução (DIVERGENCIAS) | 6 | 6 |
| não resolvidas | 2.941 | 2.935 (1 saiu e 5 ganharam o ano na v31) |
| fora da Fraga | 483 códigos | 663 linhas de 158 códigos (66 códigos não têm linha na VEICULOS; nos outros 259, as linhas já têm início e fim) |
| DE_PARA | 1.187 pares | 0 (as 4.776 linhas da Fraga já têm início e fim) |
| 4 códigos | 4 | 13 linhas |
| fora das origens | 31 (R-20261127-225955-alexandre) | 31 |

- Havia 33 linhas sem ano completo fora das seis origens (RESUMO, tabela 5). Pela decisão 108 do Alexandre (R-20261127-225955-alexandre), 31 delas entram na origem `fora das origens`:
  - 24 com `manter_atual` na T-0040;
  - 3 que não entraram na lista da T-0040 (JUH70025, Gol 1.6 L e 1.8 L; SFR30017, Gol G5);
  - as 4 linhas novas da v31.
- Ficam fora só os 2 universais (FLU15001 e FLU15002, decisão 5 de 26/11).
- Os 66 códigos fora da Fraga sem nenhuma linha na VEICULOS vão para a T-0052, que é uma lista de aplicação (decisão 109).

## Regras

- Ano só com fonte (URL). Nada é marcado como duvidoso.
- A sessão local entrega o `anos_pesquisa_T0046.csv`, nas colunas do `anos_pesquisa_T0040.csv`, e não grava no repositório.
- Depois vem a simulação para o Alexandre aprovar. Nada vai para a base antes do aprovado.
