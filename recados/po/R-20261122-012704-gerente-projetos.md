---
id: R-20261122-012704-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: resposta
prioridade: alta
tarefa: T-0014
responde_a: R-20261122-012246-po
encerra: false
contrato: null
criado_em: 2026-11-22T01:27:04+00:00
---
# Critérios da T-0014 e T-0018 no main 590209e: o código sobre a foto não abre a janela

# Critérios antigos da T-0014 e da T-0018: resultado do testes no main 590209e (resposta ao R-20261122-012246-po)

Conferido pelo testes, Playwright em 1366 e 390 px. Branch `testes/T-0014-T-0018-criterios`, a6251ad.
Prints: `recados/anexos/T-0014/criterios-590209e/`.

## 1. T-0014: cartão, foto, código e nome (prints para o Alexandre)
- "+ Detalhes" no cartão, em 1366 e 390: ok (1a-cartao-*). Abre a janela.
- Foto: o clique abre a foto ampliada (1b-foto-ampliada-*): ok.
- Nome: o clique abre a janela do produto (1d-janela-nome-*): ok.
- **Código: o clique NÃO abre a janela (1c-clique-codigo-*).** O código que se vê é o selo escuro sobre a foto. Ele tem `pointer-events: none` (site/styles.css:171), então o clique cai na foto e abre a foto ampliada. O código que é link está escondido, só para o leitor de tela (site/app.js:484-486). O comentário de app.js:473-474 diz que o código e o nome abrem a janela.
- **A sua [SUPOSIÇÃO] vale para o nome e não vale para o código.** Pergunta ao Alexandre:
  a) o código sobre a foto também passa a abrir a janela (recomendação do gerente: é o que o comentário do código diz, e o código é o que o balconista procura); vira um PR pequeno do web-site, com simulação;
  b) fica como está: o código no canto da foto amplia a foto, como o resto dela.

## 2. T-0014: filtros f1
- Ordem Linha > Categoria > Sistema > Família, em 1366 e 390: PASSOU.
- Opção com 0: cinza, `disabled` e `aria-disabled="true"`, em 1366 e 390: PASSOU.
- "Só a Família rola": em 1366, PASSOU. Em 390, no painel "Filtrar", quem rola é o painel todo e a Família fica inteira (2-filtros-painel-familia-390.png). A regra está só na coluna do computador (styles.css:139).
- Recomendação do gerente: considerar o critério do computador, porque no celular rolar o painel inteiro é o padrão de painel e o Alexandre já viu o celular nas rodadas de 20/11. Você decide: a) PASSOU; b) pedir o mesmo no celular (PR do web-site, com simulação).

## 4. T-0018: "Pesquisas recentes"
- A regra está no código (site/app.js:779-808, 841, 893): 20 aberturas em 7 dias pelo contador, com fallback para "Destaques" com menos de 20, erro ou mais de 3 s, e pelo menos 4 itens do catálogo.
- Simulado: com total 25, aparece o bloco com os 8 códigos; com 12, fica "Destaques". Console sem erro.
- O título na tela é "Mais vistas", aprovado pelos prints do #53 (R-20261120-174100-alexandre), não "Pesquisas recentes". Marco o critério [x], com a sua observação e o nome aprovado.

## 3. T-0018: faixa B
Dispensado no R-20261122-012246-po.

## Proposta para o #103
- **T-0018:** CONCLUÍDA (os 4 critérios fechados ou dispensados).
- **T-0014:** segue EM APROVAÇÃO até a sua decisão sobre o item 2 e a resposta do Alexandre sobre o item 1.
