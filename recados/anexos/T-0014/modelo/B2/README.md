# T-0014 · faixa Placa · Marca · Modelo · Ano · Motor · Versão e cartões da mesma altura (R-20261120-124800) · SIMULAÇÃO

Chromium (Playwright), deviceScaleFactor 2, site local, sem parâmetro. Placa nos prints: **AAA0A00, falsa**, só de teste; a rota do serviço de placas foi interceptada e devolveu um veículo de exemplo (HONDA "CIVIC LXS 1.8", ano_modelo 2008, motor 1.8). Nenhuma consulta real.

## JSON usado
- `json-hoje-*`: o site/data/produtos.json de hoje, sem o campo "ve" (a cascata cai na montagem pela aplicação: SIMULAÇÃO).
- `json-T0017-*`, `linha-5-cartoes-*` e `versao-aberta-*`: uma cópia do site com o JSON de exemplo da T-0017 (scratchpad/t17site/produtos_v17sim.json, fora do repositório), com o "ve". Com o "ve" no JSON, produto sem "ve" fica fora do filtro do veículo e das contagens.

## Prints
- json-hoje-amortecedor-placa-1366 / -390 e json-T0017-amortecedor-placa-1366 / -390: "amortecedor" + placa. Faixa: **Placa** (rótulo em cima, a placa em destaque com o ✕) · Marca · Modelo · Ano · **Motor** · **Versão** (LXS, que veio da placa, pré-escolhida). Saíram "Meu veículo", "Trocar veículo" e o texto "versão LXS". 390: fechada, a placa com o ✕ e, ao lado, "Honda Civic 2008 1.8 LXS" e "Alterar veículo" (abre as 6 caixas; não repete o ✕).
- json-hoje-amortecedor-sem-placa-1366 / -390 e json-T0017-…-sem-placa: o mesmo veículo pelas listas; a caixa da Placa fica com "—"; a Versão sem dado fica desabilitada com "—".
- versao-aberta-1366: a lista Versão (VW › Gol › 2010 → G5), aberta à força no print (lista nativa não sai aberta no Chromium sem janela).
- linha-5-cartoes-mesma-altura-1366: AMT7183, AMT7203, KAP11846D, KAP11846E e AMT7202 (sem foto), todos com 234 px e o "+ Detalhes" na mesma posição.
- cartao-depois-1366 / -390: o cartão (padrão).

## Altura padrão do cartão
| | 1366 px | 390 px |
|---|---|---|
| antes (fc9d4c0): variava com o texto (KAP11846D/E mais baixos) | até 235 px | até 225 px |
| **depois: todos iguais** | **234 px** | **224 px** |
Conferido em 100 cartões de "amortecedor" (1366: uma altura só, 234) e nos 5 do Civic (KAP11846D/E e o sem foto AMT7202): o "+ Detalhes" acaba a 225 px do topo em 1366 e a 215 px em 390, em todos. Título e aplicação com 2 linhas sempre (corte com "…" e o texto completo no title), 1 referência por cartão no computador e 2 no celular.

## Dobra (1º cartão, com a placa)
- 1366×768: y = 355 a 589 (a 1ª fileira inteira acima da dobra).
- 390×844: y = 500 (meta: acima de 620).

## Revisões fechadas neste commit
- corretor-redundancias: RD-0001 (o caminho ve= saiu; link antigo com ve= vira texto da busca em rotaAntiga), RD-0003 (aviso da placa só quando há algo a dizer), RD-0004 (faixa num bloco só, um aria-label "Veículo"), RD-0005 (grupo de filtro sem escolha de verdade some; sem nenhum, sem coluna e sem "Filtrar"), RD-0006 (sem "Trocar veículo"; o ✕ da placa limpa; o celular não repete o ✕), RD-0008 (menu suspenso horizontal: lógica e CSS fora; o botão do grupo só recolhe), RD-0009/0010 (tirarVeiculo e nomeVeiculo), RD-0011 (nProd: "3 produtos" no total e em "Ver 3 produtos"), RD-0012 (titulo usa bonito), RD-0013 (COMBUSTIVEL num lugar só), RD-0014 (fotoZoomHtml, criarDialogo, SEM_FOTO), RD-0015 (CSS repetido e morto), RD-0017 (comentários), e o selo do código que cobria o "Foto em breve" no celular. Mantidos por pedido do Alexandre: RD-0002 e RD-0007.
- revisor-codigo: Citroën com e sem acento dão o mesmo resultado (norm no veículo da rota); sobras do ve= fora; o ano da base (an) vale primeiro no filtro e na lista de anos (casaAno); com "ve" no JSON, produto sem "ve" fica fora do filtro e das contagens (detectado uma vez ao carregar); ✕ da placa 44×42 px; a tela refaz ao girar o tablet (900 px); "+N" sem aria-label num span.

As fotos são ilustrativas. Confira sempre a aplicação antes da compra.
