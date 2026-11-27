# T-0045 · SIMULAÇÃO do site: UX-T45-01 a 05 e a letra do produto na escala única

Branch `web-site/T-0045-sim-site`: commits 1023320 e ec9c7fb (só site/app.js e site/styles.css). O JSON e os dados não mudam. Decisões do Alexandre: R-20261127-192108-alexandre, itens 14 a 16.

Revisões:
- designer-ux: 🟢 no ec9c7fb.
- design-de-marca: LIBERADO no ec9c7fb. Os achados MC-0053 e MC-0054 foram fechados.
- testar_site: PASSOU.

## O que muda
1. **Botões (UX-T45-01, 02 e 05).**
   - A página do produto tem uma barra só, embaixo e com os botões juntos: [Copiar código] [Salvar em PDF] [← Voltar].
   - A barra fica presa no fim da tela em todas as larguras. No fim da página, ela encosta no fim do bloco.
   - No celular, os botões ficam lado a lado, e o Voltar só com a seta (44 × 44).
   - Na janela do produto, a barra fica no rodapé e o ✕ de fechar fica em cima.
   - Isso substitui a decisão de 20/11 (opB2), que punha os botões ao lado do código.
2. **Largura única (UX-T45-03).**
   - Todas as telas usam a mesma largura: 1334 px úteis em 1366 e 1848 em 1920, com o conteúdo alinhado ao logo.
   - Antes, o início e o produto tinham 1168 px, com 99 px vazios de cada lado em 1366 e 376 px em 1920.
3. **Aplicação na largura toda (UX-T45-04).**
   - A Aplicação ocupa a largura toda: no VEL7520 em 1366, passa de 466 para 1110 px.
   - Referências e Ficha ficam lado a lado, embaixo dela.
4. **Letra (item 15).**
   - O produto usa só 12, 13, 15, 17 e 20 px. Sai a letra 30% menor da T-0014.
   - O código tem 20 px e a descrição, 15 px.

## O que fica igual
- O "Salvar em PDF" sai sem botões. O TER552120 continua em 1 folha e o VEL7520 em 2, como já era no main.
- No celular (390 px), nada rola para o lado.

## Observação para o PR (não segura)
Em telas acima de 1912 px, a barra presa deixa 20 px cinza de cada lado. No PR, ela passa a ir de ponta a ponta.

## Prints
`antes-` = main, `depois-` = simulação, em 1366, 390 e 1920:
- início, busca, Sobre, não encontrado, vazio;
- produto VEL7520 e BIE20014: a página inteira, a tela visível (`-tela`) e a página rolada 900 px (`-rolado900`);
- janela do TER552120;
- PDF do VEL7520.
