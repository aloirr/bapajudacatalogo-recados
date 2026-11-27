# T-0045 · Auditoria de UX (só leitura): MENOS É MAIS e botões sempre embaixo e juntos

Agente: designer-ux · 27/11/2026 · main em 68c6dfe · nada gravado em `site/`, `catalogo_grafico/` nem `docs/ux/`.

Pasta dos prints: `/tmp/claude-0/-home-user/903b747d-fcfb-5a75-b107-affc4b1c6eae/scratchpad/t0045-auditoria/`
- `site/`: 1366 × 768, 390 × 844 e 1920 × 1080, deviceScaleFactor 1, servidor local `python3 -m http.server 8000 -d site`. Há um print da tela visível e um da página inteira (`-inteira`). As medidas estão em `site/medidas.json` e `site/medidas_extra.json`.
- `pdf/`: amostra de 44 páginas a 60 dpi e as folhas de contato `folha-*.png`. As medidas estão em `pdf/medidas_pdf.json`.
- `site/20-salvar-pdf-*.pdf/png`: o "Salvar em PDF" (A4) de TER552120, BIE20014 e CXD13074.

Produtos usados: TER552120 (tem aplicação), BIE20014 (12 referências), CXD13074 (aviso "Aplicação em revisão; consulte o vendedor.") e VEL7520 (pedido do gerente, 16 veículos, sem foto).

## Achados

| id | onde | regra | o que se vê | medida | print | grav. | correção sugerida · dono |
|---|---|---|---|---|---|---|---|
| UX-T45-01 | Página do produto, 1366 e 390 (VEL7520, TER552120, BIE20014, CXD13074) | botões | O "Voltar" fica no alto, à esquerda, junto do caminho. "Copiar código" e "Salvar em PDF" ficam no topo, ao lado do código. Não há barra no rodapé. | VEL7520 em 1366: Voltar em y 82; Copiar e Salvar em y 140. A página tem 1746 px de altura. Em 390: Voltar em y 80, Copiar em y 224, Salvar em y 276. A página tem 3236 px. | `23-produto-VEL7520-1366-inteira.png`, `23-produto-VEL7520-390.png`, `10-pagina-produto-aplicacao-1366.png` | 🔴 | Uma barra no rodapé do bloco do produto com os 3 juntos: [Copiar código] (principal) [Salvar em PDF] (secundário) e, à direita, [← Voltar aos resultados] (neutro). No celular, a barra fica presa no fim da tela (alcance do polegar). O caminho continua no alto (é link de linha). **Conflito:** o lugar de hoje é a decisão opB2 (R-20261120-141100, botões na linha do código). A regra nova a substitui só com a decisão do PO/Alexandre e com simulação (regra 3). · web-site |
| UX-T45-02 | Janela do produto, 1366 e 390 | botões | É o mesmo caso dentro da janela: "Copiar código" e "Salvar em PDF" no topo, ao lado do código, e o ✕ na barra de cima. | VEL7520 em 1366: Copiar e Salvar em y 93, numa janela de 720 px de altura com rolagem. Em 390: y 153 e y 205, empilhados. | `25-janela-VEL7520-1366.png`, `14-janela-refs-1366.png`, `15-janela-aviso-390.png` | 🔴 | Uma barra fixa no rodapé da janela com os mesmos botões e na mesma ordem do UX-T45-01. O ✕ fica em cima, como controle da janela (padrão de mercado). [SUPOSIÇÃO: registrar o ✕ como exceção em `docs/ux/`, com o ok do PO.] · web-site |
| UX-T45-03 | Todas as telas, 1366 e 1920 | 1 e 2 | São quatro larguras de conteúdo. A busca, o topo e o rodapé usam `--largura` 1880. O início, o produto e o "não encontrado" usam 1200 fixo. A Sobre usa 1160. A janela usa 1120. O conteúdo não se alinha com o logo do topo. | Em 1366, a área útil tem 1334 px na busca, 1168 no início e no produto, 1128 na Sobre e 1120 na janela. As faixas vazias laterais são de 99 px de cada lado no início e no produto e de 119 px na Sobre. Em 1920, o início e o produto ficam com 360 px vazios de cada lado (37,5% da tela) e a Sobre com 380 px. O logo fica em x 36 e o conteúdo começa em x 376. | `01-inicio-1366-inteira.png`, `21-inicio-1920.png`, `23-produto-VEL7520-1920.png`, `24-sobre-1920.png`, `22-busca-1920.png` | 🔴 | Usar um único token de largura (`--largura`) em `.bloco`, `.marca-faixa-in`, `.pagina-produto`, `.sobre`, `.pg` e `.pg-cab-in` (styles.css:108, 223, 526, 617, 746, 753). O texto corrido continua limitado pela largura do parágrafo, não da página. · web-site |
| UX-T45-04 | Página e janela do produto, 1366 | 1 | A Aplicação fica em meia coluna: as linhas da tabela quebram ("E-TORQ SOHC / L4", "Palio / Weekend") e a tabela desce, enquanto ao lado sobra uma área vazia. A coluna da foto fica vazia abaixo da foto. | VEL7520, página: coluna da foto com 200 px (+24 de vão); Aplicação com 466 px de largura e 1179 px de altura; Referências e Ficha com 466 × 668 px. Sobra uma área vazia de 466 × 511 px ao lado da tabela. Abaixo da foto ficam ~1190 px vazios (a foto é sticky). Na janela, a Aplicação tem 422 px. BIE20014 na janela tem o caso inverso: Aplicação com 3 linhas e Referências com 12. | `23-produto-VEL7520-1366-inteira.png`, `14-janela-refs-1366.png` | 🔴 | A Aplicação passa a ocupar a largura toda do conteúdo (944 px na página e 856 na janela), com Referências e Ficha lado a lado embaixo. Outra saída, a partir de 1280 px, são 3 colunas: foto 200, Aplicação 1fr e Referências + Ficha 360. O "Salvar em PDF" já faz assim (UX-T45-11). Precisa de simulação. · web-site |
| UX-T45-05 | Página e janela do produto, 390 | 1 | "Copiar código" e "Salvar em PDF" ficam empilhados na coluna estreita ao lado da foto, e o "Voltar" ocupa uma linha só para ele. | A coluna dos botões tem 215 px. Os 2 botões ocupam 44 + 8 + 44 px de altura, um embaixo do outro, e o código fica em y 140. Cabem lado a lado numa linha de 358 px. | `23-produto-VEL7520-390.png`, `10-pagina-produto-aplicacao-390-inteira.png` | 🟡 | Resolve-se junto com o UX-T45-01: uma barra no rodapé, com os botões lado a lado em 358 px. · web-site |
| UX-T45-06 | Início, 1366 e 390 | botões e 2 | Há dois botões "Buscar", um por campo, que fazem a mesma busca. Eles são maiores que o "Buscar" da tela de busca. | No início: 109 × 64 px em 1366 e 93 × 52 px em 390, nas posições y 384/384 e y 393/505. Na busca: um só "Buscar", com 112 × 44 px. | `01-inicio-1366-inteira.png`, `01-inicio-390-inteira.png`, `02-busca-geral-1366.png` | 🟡 | Um só "Buscar" para os dois campos, como na tela de busca, e altura padrão de 44 px. O desenho do início veio da T-0018, então a mudança vai como simulação. · web-site |
| UX-T45-07 | Busca, início, cartão e janela, 1366 e 390 | 2 e 4 | O mesmo rótulo aparece com caixa diferente em cada tela. Os nomes de produto saem em caixa alta no cartão e na janela, mas não no início. | Início: "Código, descrição ou aplicação". Busca: "CÓDIGO, DESCRIÇÃO OU APLICAÇÃO" (`.campo-rot` com uppercase, styles.css:93). Faixa do veículo: "Marca", "Modelo". Cartão: "PASTILHA DE FREIO", "AMORTECEDOR DE SUSPENSÃO…". Janela: "BIELETA DA BARRA ESTABILIZADORA". Destaques do início: "Amortecedor de Suspensão Dianteiro". | `02-busca-geral-1366.png`, `01-inicio-1366-inteira.png`, `14-janela-refs-1366.png` | 🟡 | Rótulos de campo em caixa normal em todas as telas. O nome do produto passa pelo `bonito()` no cartão, na janela e na página, como já acontece no início. A caixa alta fica só no título pequeno de seção ("APLICAÇÃO"), que é o mesmo nos PDFs. · web-site |
| UX-T45-08 | Página e janela do produto, 1366 e 390 | 2 | O texto do produto é menor que o resto do site e o h1 muda de tamanho de tela para tela. | Produto: texto, tabela e descrição com 12 px; h1 com 21 px (16,8 px em 390). Cartão: 13 px. Corpo do site: 15 px. h1 da busca: 20 px. Início: 42 px. Sobre: 44 px. | medidas em `site/medidas.json` (campo `fontes`) | 🟡 | Adotar a escala padrão da proposta abaixo. **Conflito:** o texto "30% menor" no produto é decisão da T-0014 (`--t: .7`). Muda só com a decisão do PO/Alexandre. · web-site |
| UX-T45-09 | Busca, faixa do veículo, 1366 e 390 | 4 (redundância) e 1 | Sem placa consultada, a faixa mostra "Placa —". Isso repete o campo "Placa do veículo" do quadro logo acima e ocupa espaço. | Em 1366, "Placa —" ocupa a 1ª coluna da faixa, com ~178 px. Em 390, ocupa a 1ª linha da faixa, de 76 px, ao lado do "Escolher veículo". | `04-busca-veiculo-texto-1366.png`, `02-busca-geral-390.png` | 🟡 | Mostrar a "Placa" na faixa só quando há placa consultada. Sem ela, as listas de veículo usam a largura toda. · web-site |
| UX-T45-10 | Estado vazio da busca e "não encontrado", 1366 | 1 e 2 | No vazio, a coluna "Filtros" fica de pé, sem nenhum filtro, ao lado do aviso. Em telas curtas, o rodapé não chega ao fim da tela. | Coluna "Filtros" vazia com 210 × 46 px. O aviso tem 1110 px, quando poderia ter 1334. Abaixo do rodapé sobra uma faixa cinza de 66 px em 1366 × 768 (`09-…`, `12-…`). | `08-vazio-busca-1366.png`, `09-produto-nao-encontrado-1366.png` | 🟡 | Sem filtros, a coluna sai e o aviso usa a largura toda. O rodapé fica preso ao fim da tela quando a página é curta. · web-site |
| UX-T45-11 | "Salvar em PDF" (A4) | 4 (consistência) | A ordem no papel é diferente da tela: o "Leve também" vai para o fim e as Referências e a Ficha sobem para o lado da foto. A Aplicação, porém, ocupa a largura toda, o que está conforme à regra 1. | Margens de 11,1 mm à esquerda e 13,9 a 15,0 mm à direita. Na tela, o "Leve também" vem logo depois do código. No PDF, vem depois da Aplicação. | `20-salvar-pdf-TER552120-1.png` | 🟡 | Uma ordem só na tela e no A4. A sugestão é a tela seguir o A4 na Aplicação com a largura toda (UX-T45-04), com o "Leve também" no mesmo lugar nos dois. · web-site |
| UX-T45-12 | PDF digital (todas as páginas com o link) e Linha Moto | botões e 2 | O "VOLTAR AO SUMÁRIO" fica no alto, à direita, e o link do site fica no rodapé, à esquerda: os links de ação estão em dois lugares. A altura do "Voltar" também muda entre as páginas. | "Voltar ao sumário" em x 165,1 mm, com 36,5 × 8,5 mm. Fica em y 2,9 mm nas páginas de linha (Digital p4, p5; Moto p4) e em y 11,6 mm nas aberturas (Digital p3, p253; Moto p11). O link do site fica em x 9,5 mm e y 284,3 mm. | `pdf/Digital-p004.png`, `pdf/Digital-p003.png`, `pdf/Moto-p004.png` | 🔴 | Uma barra de links no rodapé de cada página, com [Voltar ao sumário] e o site juntos e na mesma altura em todas as páginas. Os links de linha do sumário e das aberturas ficam onde estão (são links de linha). · catalogo-grafico |
| UX-T45-13 | PDF gráfica (A4 impresso), páginas de linha (p5, p8, p14, p22, p31, p39, p46) | 3 | No rodapé há uma "pílula" com "Veja o catálogo digital", desenhada como botão, num material de papel. Ela não tem link. | 0 links por página. A pílula fica na faixa "Mais N itens desta linha", no fim da página. | `pdf/A4_grafica-p005.png` | 🟡 | No papel, trocar o botão por texto com o endereço do catálogo digital [SUPOSIÇÃO: o endereço ou um QR; o QR é elemento novo e passa pelo design-de-marca]. · catalogo-grafico |
| UX-T45-14 | Linha Moto p8 (Filtros Moto, continuação) e o mesmo padrão de tabela no digital | 1 | A Aplicação longa (FLU5240) desce numa coluna fixa, enquanto as colunas "Leve também" e "Equivale a" ficam quase vazias. A página leva 1 item só e sobra a metade de baixo. | A Aplicação vai de 46,5 a 141,8 mm (95 mm, 50% dos 191 mm úteis) e desce até y 125 mm. "Leve também" e "Equivale a" somam 58,7 mm (31%), com 4 linhas curtas e "—". Embaixo ficam 172 mm vazios. | `pdf/Moto-p008.png` | 🔴 | Larguras de coluna pelo conteúdo: quando "Leve também" e "Equivale a" têm pouco texto, a Aplicação ganha a largura delas. Juntar a continuação de 1 item à página anterior. · catalogo-grafico |
| UX-T45-15 | PDF gráfica p39 (Baterias) | 1 e 4 | As colunas "Leve também" e "Equivale a" só têm "—" em todas as linhas. | 50 travessões. As duas colunas vão de 152,7 a 199,8 mm (47 mm, ~25% da largura útil). A mesma página no digital (p187–188) não foi medida. | `pdf/A4_grafica-p039.png` | 🟡 | Coluna toda vazia na página sai e a largura dela vai para "Produto / Especificação". · catalogo-grafico |
| UX-T45-16 | PDF digital p251 (Lubrificantes) e p253 (Químicos); Linha Moto p6 (Filtração) e p9 (Lubrificantes) | 1 | Sistemas com uma só linha recebem uma página inteira de abertura. A lista da abertura ocupa pouco mais da metade da largura e o resto é grafismo. | A lista vai de 9,5 a 115,3 mm (105,8 mm, 55% dos 191 mm úteis). Na Moto, 4 das 17 páginas são aberturas (p3, p6, p9, p11). A p6 abre 1 linha de 3 itens e a p9, 1 linha de 2 itens. | `pdf/Digital-p253.png`, `pdf/folha-Moto-1.png` | 🟡 | Abertura de página inteira só para sistema com 2 linhas ou mais. Com 1 linha, o nome do sistema vai no cabeçalho da página da linha [SUPOSIÇÃO]. Precisa de simulação. · catalogo-grafico |
| UX-T45-17 | Sumário da Moto (p2); PDF gráfica p2 ("Por que BAP?") e p3 ("Como consultar") | 1 (sem excesso; é sobra vertical, não lateral) | A página fica com a metade de baixo ou mais vazia. | Moto p2: 8 links no alto e 200 mm (67% da altura) vazios. Gráfica p2: 131 mm vazios; p3: 130 mm (43%). | `pdf/Moto-p002.png`, `pdf/A4_grafica-p002.png`, `pdf/A4_grafica-p003.png` | 🟡 | Juntar as páginas: na gráfica, "Por que BAP?" e "Como consultar" numa página; na Moto, o sumário com o "como consultar". Precisa de simulação. · catalogo-grafico |
| UX-T45-18 | Lubrificantes, apresentação 16:9, p5 | 2 | A tabela termina antes da margem direita, mas a caixa escura logo abaixo vai até a margem: são duas larguras na mesma página. | A tabela termina em x ~265 mm e a caixa em ~324 mm (margem direita de 14,1 mm). A tabela ocupa ~81% da largura útil. | `pdf/Lubrificantes-p005.png` | 🟡 | Tabela e caixa com a mesma largura útil, como na p4 e na p9. · catalogo-grafico |

### Vistos de passagem (fora das regras da T-0045; vão ao dono do dado)
- BIE20014: a Aplicação mostra "05 /15 ou" em Versão e "—" em Ano no Hyundai Tucson. As Referências repetem BR10053102707 em "TRW/AXIOS" e em "AXIOS". (`14-janela-refs-1366.png`)
- TER552120: a Ficha tem "Lado: Esquerdo e Direito" e também "Posição e lado: DIR. / ESQ.", a mesma informação duas vezes e a segunda em caixa alta. (`10-pagina-produto-aplicacao-1366.png`)
- VEL7520: a linha "Modelos" da Ficha repete a Aplicação, e o rótulo "Especificacoes" está sem acento. (`23-produto-VEL7520-1366-inteira.png`)

## O que já está conforme
- Em 390 px, nenhuma tela rola para o lado: `scrollWidth` deu 390 em todas as 20 telas.
- A busca usa a largura toda: 1334 px em 1366 e 1848 px em 1920. São 4 cartões por linha em 1366 (266 px), 5 em 1920 (286 px) e 2 em 390 (175 px), como decidido na fA2 (R-20261120-141600, no CSS). O primeiro cartão aparece acima da dobra em 390 (y 506).
- Cartão: o "+ Detalhes" é o único botão do cartão, no rodapé, e cai no mesmo y em todos os cartões da linha (y 655 em 1920).
- Painel "Filtrar" (390): um só botão, "Ver 197 produtos", na barra do rodapé, com 366 px de largura.
- "Carregar mais" fica no fim da lista. "Ver o catálogo" é o único botão do bloco da Sobre.
- Margens laterais dos PDFs iguais em todas as páginas medidas:
  - digital e Moto: 9,3–9,5 mm dos dois lados;
  - gráfica: 12,3/12,5 mm, com 3 mm de sangria (≈9,3/9,5 mm do corte);
  - Lubrificantes: 13,4/14,1 mm.
- Nas páginas de linha dos PDFs, o conteúdo cobre de 91% a 95% da largura. "Destaques da linha" tem 5 cartões por linha, de margem a margem, em todos os PDFs.
- Os links do sumário dos PDFs digitais são links de linha: 56 no digital e 8 na Moto.
- O "Salvar em PDF" sai em uma folha A4 com a Aplicação na largura toda.
- Não vi preço nem estoque em nenhum print ou página.

## Não medido
- Botão e menu da conta, Entrar, Trocar senha, Admin e Estoque: dependem do serviço de login (`/api/eu` dá 404 no `http.server`).
- Busca pela placa: depende da API de placas.
- A mesma checagem do UX-T45-15 nas páginas de Baterias do PDF digital (p187–188).
- PDFs fora da lista (Portfólio, Kit Filtros, Treinamentos).
- O movimento (durações), que não aparece em print parado.

## Proposta de tamanhos padrão (só proposta; nada gravado em `docs/ux/`)
Parte do que já existe nos tokens do `:root` (`site/styles.css`), nos pareceres de `docs/ux/` e no `docs/marca/manual.md`.

**Site**
- **Largura:** um só token, `--largura: 1880px`, para o topo, a busca, o início, o produto, a Sobre, os estados e o rodapé.
  - Margem lateral de 16 px, como hoje na busca (fica 36 px em 1920).
  - O texto corrido mantém a largura máxima de parágrafo que já existe (520–760 px).
- **Colunas:**
  - lista: 2 (≤640), 4 (641–1679) e 5 (≥1680), como hoje;
  - sistemas do início: 6 por linha em 1366, como hoje;
  - filtros: 210 px;
  - produto: foto com 200 px, Aplicação na largura toda do conteúdo e Referências + Ficha em 2 colunas iguais embaixo (ou 3 colunas a partir de 1280 px);
  - janela: a mesma grade, com largura de min(área útil − 48 px, 1334 px) [SUPOSIÇÃO].
- **Tipografia:** uma escala só, em tokens:
  - 12 px: rótulo e título pequeno de seção;
  - 13 px: cartão, tabela e filtro;
  - 15 px: texto;
  - 17 px: subtítulo;
  - 20 px: h1 das telas de trabalho (busca e produto);
  - 24 px: h2 de seção;
  - 42–44 px: h1 de vitrine (início e Sobre).
  - Rótulo em caixa normal. A caixa alta com espaçamento fica só no título pequeno de seção.
  - Depende de decidir o "30% menor" da T-0014.
- **Botões:**
  - altura de 44 px em todos;
  - 36 px só no "+ Detalhes" do cartão, com área de toque de 44 px, como hoje;
  - raio de 8 px, `--raio` 12 nos cartões;
  - uma barra por bloco, no rodapé, com vão de 10 px. A ordem é principal → secundário → neutro à direita (Voltar), e destrutivo à direita (Desativar, no Admin) [SUPOSIÇÃO];
  - no celular, a barra fica presa no fim da tela;
  - fora da barra: só a busca, os filtros, os links de linha e o ✕ da janela.

**PDF**
- **A4:**
  - margem lateral de 9,5 mm (área útil de 191 mm), com +3 mm de sangria na gráfica;
  - cabeçalho até ~12 mm e rodapé a partir de 284 mm, como hoje.
- **Tabela de linha:**
  - posições de hoje: Código em 11,6 mm, Aplicação em 46,5, Leve também em 141,8 e Equivale a em 164,0;
  - uma coluna toda "—" sai e a largura dela vai à Aplicação;
  - uma continuação de 1 item junta-se à página anterior.
- **Links do PDF digital:** uma barra no rodapé com [Voltar ao sumário] e o site juntos, na mesma altura em todas as páginas.
- **Apresentação 16:9:** margem de 14 mm dos dois lados. Tabela e caixa com a mesma largura útil.
- **Aberturas de sistema:** só com 2 linhas ou mais [SUPOSIÇÃO].

As correções de layout acima (UX-T45-01 a 04, 06, 14, 16 e 17) vão primeiro como simulação ao Alexandre, pelo PO (regra 3). Os conflitos com as decisões opB2 (R-20261120-141100) e T-0014 (`--t: .7`) ficam para o PO decidir.
