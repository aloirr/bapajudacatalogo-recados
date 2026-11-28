# T-0047 · v32 · SIMULAÇÃO curta do P7 (BIE20062)

Branch `catalogo-dados/T-0047-v32`, commit 850aee6. A base real continua sendo a v31. Os pontos P1 a P6 já foram aprovados (R-20261127-224247-alexandre).

## P7, o BIE20062 com o mesmo "Tucson 05 /15"
- **APLICACAO:** "Tucson 05 /15 (diant. Direita ou Esquerda)" passa a "Tucson 2005–2015 (diant. Direita ou Esquerda)". O resto do texto, com o Sportage, não muda.
- **VEICULOS, linha 21800:** a linha já tem 2005–2015 desde a v20. Sai só o ANO_DUVIDA ("AA/AA ambíguo").
- **Fonte:** o "AA /AA" das bieletas é ano a ano, como em XSARA 98 /03, 206 99 /12 e SPRINTER 97 /12, igual ao P1.
- **Na tela:** sai a linha "Hyundai Tucson — 05 /15 ou —". Não entra linha nova, porque o Tucson 2005–2015 já está coberto pelo Tucson 2.0 2004–2019 da Fraga. A busca continua achando a peça.

## Fica de fora (aba SEM_FONTE), para uma tarefa nova
Há um conflito de posição:
- o texto diz "diant.";
- o DETALHE diz "Tras. esq.";
- a POSICAO diz "DIANTEIRO E TRASEIRO";
- a Fraga só traz o Tucson traseiro.

Nenhuma célula de posição muda.

## Prints
`BIE20062_<antes|depois>_<1366|390>.png`
