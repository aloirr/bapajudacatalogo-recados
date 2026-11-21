# T-0017 · v24 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: **R-20261121-102700-alexandre** ("reveja tudo e valide os casos iguais"). Auditoria das referências cruzadas repetidas, com a regra de prova do recado, e revisão do AMT7500 e do AMT7014.
- Base de partida: v23 do main 3748c34 (sha256 `05eeb19a…d129`). A base não foi gravada e não há v24 em `dados/versoes/`.
- Regra fixa (R-20261120-213300): nada novo marcado nem escrito como duvidoso. Nenhum produto sai.
- 2ª rodada, depois da revisão do 128efb3:
  - o trecho que entra em A é copiado, literal, da APLICACAO de B;
  - os casos também vêm da APLICACAO;
  - o ABS é padronizado;
  - código com "/" não vira referência.

## Arquivos
- `RESUMO.md`: as contagens, os casos válidos, os motivos de quem ficou fora e a conclusão do AMT7500 e do AMT7014.
- `SIMULACAO_v24_T-0017.xlsx`, com as abas:
  - LEIA;
  - VALIDOS: um veículo por linha, com o trecho copiado de B, o antes e o depois da APLICACAO e a linha nova da VEICULOS;
  - FORA: o motivo de cada veículo;
  - GENERICAS: as referências tratadas como suspeitas;
  - AMT7500_AMT7014.
- `numeros_v24.json`: as contagens.
- `simular_v24.py`: o script. Ele só lê a base e usa o `base_comum` e o `refs_de` do `gerar_site.py`, a mesma leitura do site. Uso: `python3 -I simular_v24.py <base.xlsx> <pasta_saida>`.
