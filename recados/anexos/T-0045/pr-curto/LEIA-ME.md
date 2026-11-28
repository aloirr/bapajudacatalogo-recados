# T-0045 · SIMULAÇÃO do PR curto: espaço do topo (RD-0767), A4 (RD-0769) e toque na trilha

Branch `web-site/T-0045-rd0767`, head 9b334f2, sobre o main faadcc7 (#247). Revisão: designer-ux 🟢 no 9b334f2.

## O que muda na tela do produto
1. **Sem o espaço vazio do lugar antigo dos botões (RD-0767).** A faixa do topo, com a trilha "Início › sistema › família", passa de 44 px para 19,5 px, a altura da própria trilha. Entre a barra de botões e o rodapé, o espaço vai de 96 para 56 px no computador e de 80 para 40 px no celular. A página fica 64 px mais curta.
2. **Toque de 44 px na trilha.** Os links "Início", sistema e família aceitam toque numa área de 44 px, sem aumentar a faixa. A área termina no topo do bloco do produto e não cobre a foto.
3. **A4 sem mudança (RD-0769).** Duas regras de impressão foram limpas, e o A4 do VEL7520, do CXD13055 e do CIL8548 saiu igual ao do main (texto, pixels a 150 dpi e desenhos).
4. **Rolagem para o lado:** continua sem nenhuma, em 1366, 390 e 1920.

## Arquivos
- `<largura>-<produto>-<topo|meio|fim|janela>.png`: o antes (main) e o depois lado a lado, em 1366, 390 e 1920, no VEL7520, no BIE20014 e na janela do TER552120. O rótulo diz 0ff5d0e; o 9b334f2 sai igual nos pixels, porque a área de toque não aparece.
- `medidas-antes.json` e `medidas-depois.json`: as alturas e os espaços medidos.
- `toque-trilha.json`: as medidas da área de toque.

O testar_site passou no 9b334f2, com 0 falhas.
