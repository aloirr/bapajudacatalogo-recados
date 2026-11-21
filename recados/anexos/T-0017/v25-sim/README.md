# T-0017 · v25 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: **R-20261121-112900-alexandre**, item 4: "coloque o palio no amt7500 assim como na internet. Olhe os catalagos unificados antigos para validar".
- Base de partida: v24 (sha256 `a77de850…04d2`), da branch catalogo-dados/T-0017-v24. A base não foi gravada e não há v25 em `dados/versoes/`.
- Regra fixa (R-20261120-213300): nada novo marcado nem escrito como duvidoso. Nenhum produto sai.

## Arquivos
- `RESUMO.md`: o resultado da busca nos catálogos antigos, o antes e o depois, a linha nova da VEICULOS e a fonte.
- `SIMULACAO_v25_T-0017.xlsx`, com as abas:
  - LEIA;
  - ANTES_DEPOIS: a célula APLICACAO do AMT7500;
  - VEICULOS_NOVA;
  - BUSCA: cada registro dos catálogos antigos com o AMT7500 ou uma referência dele.
- `numeros_v25.json`: as contagens, por arquivo procurado.
- `simular_v25.py`: o script. Ele só lê e usa o `base_comum`. Uso, na raiz do repositório: `python3 -I dados/simulacoes/T-0017-v25/simular_v25.py dados/BASE_BAP_UNIFICADA_PRODUTOS_BAP.xlsx dados/simulacoes/T-0017-v25`.
