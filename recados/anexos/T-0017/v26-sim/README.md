# T-0017 · v26 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: **R-20261121-190649-alexandre**, item 3 (o CV-F35 confirmado no R-20261121-190933-alexandre). Junta o SCE14002 (LS da Mercedes-Benz), a Bongo do CRU100, as linhas normais da VEICULOS (HR, LS, Parati e Santana), o fim 2013 do CV-F35 e os nomes "Mbb", "Vwc" e "NEW Beetle".
- Base de partida: v25 do main 8de7a6d (sha256 `4954ab91…ac93`). A base não foi gravada: a v26 sai depois do "aprovado".

## Arquivos
- `RESUMO.md`: a contagem, o antes e o depois de cada célula, as linhas novas da VEICULOS, o que fica de fora e o que muda no site.
- `SIMULACAO_v26_T-0017.xlsx`, com as abas:
  - LEIA;
  - ANTES_DEPOIS: as 31 células, uma por linha, com a célula inteira (lida pelo `base_v26.py` na gravação);
  - VEICULOS_NOVA: as 4 linhas novas;
  - FORA: o que fica como está, e por quê;
  - SITE: cada chave do `produtos.json` que muda;
  - LOG_CORRECOES_PREVISTO.
- `numeros_v26.json`: as contagens.
- `simular_v26.py`: o script. Ele só lê, usa o `base_comum` e confere a base simulada com a v25 célula a célula. Roda o `scripts/gerar_site.py` numa cópia, em pasta temporária. Uso, na raiz do repositório: `python3 -I dados/simulacoes/T-0017-v26/simular_v26.py dados/BASE_BAP_UNIFICADA_PRODUTOS_BAP.xlsx dados/simulacoes/T-0017-v26`.
