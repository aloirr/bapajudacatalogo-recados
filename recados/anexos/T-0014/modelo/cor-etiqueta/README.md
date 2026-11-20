# Etiquetas da busca: 3 opções de cor (simulação, T-0014)

Pedido (R-20261120-131100-alexandre): "Aprovado as telas, com exceção deste texto. me sugira uma cor diferente. ela não está profissional. está amadora"

- **Onde:** `.etq` em `site/styles.css` (linhas 136 a 139 do branch T-0014). Vale para o "Busca: “…”" e para **todas as etiquetas de filtro marcado** ("Sistema: Suspensão"...), porque usam o mesmo estilo. A placa (`.mv-placa-grande`, fundo branco e borda --escuro) tem estilo próprio e não muda.
- **Hoje:** fundo --verde-claro #EAF6E5, texto --verde-txt #2E6B1F (5,8:1). O fundo quase some no fundo da página (--verde-claro × --fundo = 1,02:1): por isso fica com cara de "lavado".
- **Montagem:** cópia do site do branch (`git archive HEAD site`), Playwright 1366 × 900 e 390 × 844, deviceScaleFactor 2. Busca "amortecedor" + Sistema: Suspensão + placa de teste AAA0A00 (serviço interceptado, resposta falsa Honda Civic 2008 1.8 LXS; o serviço real não foi chamado). CSS de cada opção injetado com `page.addStyleTag`; nada no repositório mudou.
- **Só tokens do :root; nenhum hex novo e nenhum token novo.**

## Opção A: neutra (RECOMENDADA)
```css
.etq { background: var(--branco); color: var(--escuro); box-shadow: inset 0 0 0 1px var(--borda-campo); font-weight: 500; }
.etq button { color: var(--texto-2); }
.etq button:hover { background: var(--fundo); color: var(--escuro); }
```
Contraste: texto --escuro × --branco **18,3:1**; ✕ --texto-2 × --branco **6,3:1**. Borda --borda-campo (a mesma dos campos e listas) para a etiqueta não sumir no --fundo (--linha daria só 1,15:1 com o fundo).

## Opção B: escura
```css
.etq { background: var(--escuro); color: var(--branco); font-weight: 500; }
.etq button { color: var(--branco); }
.etq button:hover { background: color-mix(in srgb, var(--branco) 18%, transparent); }
```
Contraste: --branco × --escuro **18,3:1** (texto e ✕).

## Opção C: contorno verde
```css
.etq { background: transparent; color: var(--verde-txt); box-shadow: inset 0 0 0 1.5px var(--verde-txt); }
.etq button { color: var(--verde-txt); }
.etq button:hover { background: color-mix(in srgb, var(--verde-txt) 12%, transparent); }
```
Contraste: --verde-txt × --fundo **5,9:1**. Com --verde-esc daria só 3,7:1 no --fundo (4,1:1 no branco) e **não passa** em 4,5:1; por isso o C usa --verde-txt.

## Recomendação: A
- A etiqueta é informação ("o que está filtrado"), não é ação nem marca. Neutra, ela fica com o mesmo acabamento dos cartões e campos (branco, borda fina): cara de sistema profissional, como os grandes e-commerces.
- O verde fica para o que o cliente deve tocar (Buscar, + Detalhes) e para a marca; não se gasta verde num rótulo.
- B pesa: o preto fica igual aos selos dos códigos (AMT7183) e puxa o olho para o lugar errado.
- C parece botão: o contorno verde é o mesmo desenho do "+ Detalhes" e do "Filtrar" (no celular, ficam lado a lado).

## Prints (1366 = recorte da faixa do veículo, etiquetas e cartões; 390 = topo do celular)
- `0_atual_1366.png`, `0_atual_390.png` (hoje, para comparar)
- `opcao_A_1366.png`, `opcao_A_390.png`
- `opcao_B_1366.png`, `opcao_B_390.png`
- `opcao_C_1366.png`, `opcao_C_390.png`

Conferido nos dois tamanhos: etiquetas "Busca: “amortecedor”" e "Sistema: Suspensão", placa AAA0A00 na faixa, sem rolagem para o lado em 390 px.

Observação fora do pedido: o cabeçalho do grupo marcado na coluna de filtros (`.filtro-bt.ativo`, "Sistema (1)") também usa --verde-claro. Não é etiqueta e entrou nas telas aprovadas; fica como está, a não ser que o Alexandre queira a mesma linha.
