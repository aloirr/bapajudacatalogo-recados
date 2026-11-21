# T-0017 · v23 da base unificada: simulação e gravação

Pedido: **R-20261120-235000-alexandre**, item 1.3. Nesta rodada houve **aprovação antecipada**: a simulação segue a recomendação do dono e do gerente, sem esperar o "aprovado" de cada ponto.
- Os limites: nada novo duvidoso, nenhum produto sai, nenhuma coluna muda de formato, nada de preço, estoque ou fornecedor.

Gravada pelo `dados/scripts/base_v23.py` sobre a v22 (sha256 `0c403c37…54ba`). A v23 tem sha256 `05eeb19a…d129`.

## Arquivos
- `RESUMO.md`: o antes e o depois de cada célula, com a recomendação e o motivo, e o que ficou de fora.
- `SIMULACAO_v23_T-0017.xlsx`: as abas LEIA, ANTES_DEPOIS (lida pelo script) e FORA.
- `numeros_v23.json`: as contagens.
- `simular_v23.py`: o script, que só lê a base.

## Conferência
- `base_v23.py --conferir`: 1 célula mudou na PRODUTOS e 3 na VEICULOS, como esperado. O LOG_CORRECOES ganhou 4 linhas (uma por célula) e o LEIA-ME, o bloco da v23 no topo (6 linhas). Mesmas abas e colunas da v22; nenhuma diferença fora do permitido.
- `scripts/gerar_site.py`: 4419 produtos, como na v22. No `produtos.json`, só muda a chave `a` do CRU100 (o JSON vai em PR do `web-site`).
