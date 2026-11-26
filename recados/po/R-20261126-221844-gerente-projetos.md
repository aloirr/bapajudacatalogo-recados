---
id: R-20261126-221844-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-26T22:18:44+00:00
---
# T-0040: lista de trabalho em CSV pronta (7.214 linhas, 2.145 códigos)

A lista de trabalho em CSV está no branch, pronta para a sessão local consultar a Fraga.

Onde está:
- branch catalogo-dados/T-0040-lista, commit 2e8275debb00d48da76035f63ecc529fa0566c5e;
- arquivo dados/T-0040/lista_trabalho.csv: UTF-8, separador ";", colunas id_linha;codigo_bap;descricao;montadora;modelo;versao;motor;ano_atual;tipo;referencias_cruzadas;
- script para refazer: dados/scripts/lista_T0040.py. A base não foi tocada: o sha256 é conferido antes e depois.

Sobre o id_linha: é o número da linha de dados na aba VEICULOS (a linha do Excel é o id + 1). Pula números, de propósito, para que a resposta da Fraga volte direto para a linha certa da base.

Contagem:

| tipo | linha | linhas | códigos |
|---|---|---|---|
| sem_ano | LEVE | 1.957 | 689 |
| sem_ano | PESADA | 808 | 218 |
| sem_ano | LEVE E PESADA | 457 | 74 |
| sem_ano | MOTO | 116 | 24 |
| sem_ano | UNIVERSAL | 2 | 2 |
| **sem_ano** | **total** | **3.340** | **1.007** |
| so_inicial | LEVE | 3.465 | 1.181 |
| so_inicial | PESADA | 230 | 85 |
| so_inicial | LEVE E PESADA | 174 | 32 |
| so_inicial | MOTO | 5 | 3 |
| **so_inicial** | **total** | **3.874** | **1.301** |

- No total são 7.214 linhas e 2.145 códigos.
- 2.130 desses códigos têm referência cruzada.
- O sem_ano bate com o número de antes: 3.340 linhas e 1.007 códigos.

Sem preço e sem estoque: a descrição e as referências vêm do produtos.json do site, que já passou pela FICHA e pela TRAVA. O texto da APLICACAO ficou de fora, porque um deles tem preço. O script para com [PARADO] se aparecer palavra interna, e não apareceu.

Decisões para o Alexandre:
1. Entram 2.330 linhas "duvidosas", em que o veículo pode estar errado e que por isso não vão ao site: 1.453 sem ano e 877 só com o ano inicial. Pesquisar todas, ou só as já separadas (1.887 + 2.997)?
2. 81 linhas têm só o ano final ("até 2008") e ficaram fora da lista. Entram na meta de 100%?
3. 341 linhas têm um ano solto ("08/2022"). Vale como "em diante" ou como só aquele ano?
4. Veículo ainda em produção: o ano final fica 2026, marcado "(em produção)"?
5. Os 2 produtos UNIVERSAL sem ano precisam de ano?

Próximo passo do lado da nuvem: o piloto de 10 códigos por referência cruzada na internet, para medir a taxa de acerto e o tempo.
