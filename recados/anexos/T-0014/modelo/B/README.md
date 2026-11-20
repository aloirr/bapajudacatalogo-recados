# T-0014 · modelo B como padrão, filtros à esquerda, cartão compacto (R-20261120-123630 e 123800) · SIMULAÇÃO

Chromium (Playwright), deviceScaleFactor 2, site local, **sem parâmetro** (o B virou o padrão; ?m= saiu). Placa nos prints: **AAA0A00, falsa**, só de teste; a rota do serviço de placas foi interceptada e devolveu um veículo de exemplo (HONDA "CIVIC LXS 1.8", ano_modelo 2008, motor 1.8). Nenhuma consulta real.

**SIMULAÇÃO dos dados do "Meu veículo":** as listas Marca › Modelo › Ano › Motor/Versão são montadas em JavaScript a partir do produtos.json de hoje (marca do campo mo; modelo = a palavra depois da marca na aplicação; ano = as faixas da aplicação; motor = os "1.8" da aplicação), com a contagem dentro do resultado da busca e dos filtros atuais. Tem ruído conhecido. O dado de verdade virá do campo "ve" da T-0017. O produtos.json não mudou.

## JSON usado
- Todos os prints, menos os dois "json-T0017-*": o site/data/produtos.json de hoje (sem o campo "ve"): a cascata cai na montagem pela aplicação (SIMULAÇÃO).
- json-T0017-amortecedor-placa-1366 / -390: uma cópia do site com o JSON de exemplo da T-0017 (scratchpad/t17site/produtos_v17sim.json, fora do repositório), com o campo "ve" ([fabricante, modelo, versão?]). Aí a cascata usa o "ve": Honda › City, Civic, CR-V, Fit, HR-V, WR-V (sem ruído); VW › Gol › 2010 › Motor/Versão "G5". O ano continua vindo da aplicação.

## Prints
- amortecedor-placa-1366 / -390: "amortecedor" + placa AAA0A00. Faixa do "Meu veículo" abaixo da busca com a **placa em destaque** (com o ✕ que tira o veículo), as 4 listas preenchidas (Honda › Civic › 2008 › 1.8) e "Trocar veículo". A chave liga/desliga e o "Departamentos" saíram. 390: a faixa compacta numa linha ("Honda Civic 2008 1.8" + "Alterar veículo", que abre as 4 listas) e a placa em destaque.
- amortecedor-sem-placa-1366 / -390: o mesmo veículo escolhido pelas listas, sem placa: só o rótulo "Meu veículo".
- coluna-filtros-esquerda-marcado-1366: Sistema, Família, Linha e Categoria numa coluna fina (190 px) à **esquerda** dos cartões, de cima a baixo, com Linha: Leve marcado; **5 cartões por linha** em 1366 (216 px cada).
- filtrar-aberto-390: no celular, o botão "Filtrar (n)" abre o painel por cima (fundo escurecido, foco preso).
- cartao-antes-448257e-1366 / -390 e cartao-depois-1366 / -390: o cartão antes (448257e, ?m=B) e depois.

## Altura do cartão (busca "amortecedor", 1ª linha)
| | 1366 px | 390 px |
|---|---|---|
| antes (448257e, simulação ?m=B) | 274 px | 264 px |
| antes (448257e, padrão sem parâmetro) | 285 px | 276 px |
| **depois (padrão)** | **235 px** | **225 px** |

Como: sem vão entre título, aplicação, "Ref. Cruzada:" e "+ Detalhes" (cada cartão com a sua altura, sem esticar até o maior da linha); no computador as referências numa linha só (as que couberem, até 2, e o "+N"); "+ Detalhes" com 34 px visíveis e 44 px de toque; o link do nome com 44 px de toque sem vão. Texto mínimo 12 px. O código BAP fica sobre a foto, no canto inferior direito, também no celular.

## Dobra (1º cartão)
- 1366×768: 1º cartão de y=407 a y=642, a 1ª fileira inteira acima da dobra (antes começava em y=530).
- 390×844: 1º cartão em y=607 com a placa e y=557 sem veículo (meta: acima de 620; antes y=825).

As fotos são ilustrativas. Confira sempre a aplicação antes da compra.
