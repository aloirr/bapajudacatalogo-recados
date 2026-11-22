# T-0025 · Simulação (só a simulação) · repetições e ajustes de marca

- Feita em 22/11/2026, 05:44 (Manaus), por `catalogo-grafico`.
- Base: main `5c0ddda`. Simulação feita na worktree, sem commit e sem PR. Nada mudou em `catalogo_grafico/entregas/` nem no gerador do main.
- Regra desta rodada (R-20261122-090651-alexandre): a simulação é conservadora. Ela só tira repetição e não muda a marca.
- Diff da simulação: `T-0025_simulacao.diff` (5 arquivos do gerador, +17 −16).
- Como foi gerado: `PYTHONHASHSEED=0`, com os scripts do gerador. Só as páginas afetadas foram geradas. As imagens têm 150 ppi; o zoom do cabeçalho tem 300 ppi.
  - O .pptx foi renderizado no LibreOffice. A Arial aparece como Liberation Sans, que tem as mesmas medidas.
- Conferência do "antes": o "antes" que o gerador do main produz é igual às entregas de hoje. São 0 pixel diferente e o mesmo texto no A4 pág. 2, no PDF de Lubrificantes págs. 2 e 3 e no .pptx slides 2 e 3.

## O que muda em cada item

### 1. RD-0428: a etiqueta "BAP AUTOPARTS" ao lado do logo (Lubrificantes, PDF e .pptx)
- **Arquivos:** `apres_bemol.py` (`S.header`, sai a linha `self.t(72, 34, 'BAP AUTOPARTS', …)`) e `apres_ppt.js` (mestre `BAP_CONTEUDO`, sai o objeto de texto).
- **Páginas:** PDF págs. 2 a 10 e .pptx slides 2 a 10.
- **Resultado:** só some a etiqueta. Nas págs. 3 a 10, a única diferença é a caixa da etiqueta, com 1.193 pixels no PDF e 1.183 no .pptx. A capa (1) e o "Obrigado!" (11) ficaram iguais, com 0 pixel diferente.
- **O logo:** fica no mesmo lugar e no mesmo tamanho. O título "A BAP AUTOPARTS" da pág. 2 também fica.
- **Portfólio:** não muda, porque ele tem o próprio `header` (`portfolio.py:66`).
- **Imagens:** `RD0428_cabecalho_zoom_antes_depois.png`, `RD0428_Lub_PDF_pag03_antes_depois.png` e, avulsas, `Lub_PDF_*_p03.png` e `Lub_PPTX_*_p03.png`.

### 2. RD-0429: A4, pág. 2 ("Por que BAP?")
- **Arquivo:** `print_cat.py`, função `por_que`. **Página:** só a pág. 2 do A4. O A4 continua com 56 páginas, porque a pág. 2 é fixa e não muda a paginação.
- **Marca:** antes ela aparecia 2 vezes, na barra e no sobretítulo. Agora fica só no sobretítulo "BAP AUTOPARTS", e a barra da direita fica vazia, porque à esquerda já está "CATÁLOGO DE PRODUTOS 2027".
- **Garantia:** antes aparecia 3 vezes. Agora fica só no bloco "Garantia Expressa BAP", que já diz "Prazos conforme o certificado da embalagem".
  - Sai o cartão "SAC · garantia direto na fábrica". Os 3 cartões que ficam ocupam a mesma largura total.
  - Sai a linha "Prazos de garantia conforme o certificado da embalagem de cada produto."
- **Subtítulo:** sai "Componentes de qualidade, com segurança e preço acessível.", que repetia o texto do "Quem somos". O sobretítulo e o título se centralizam sozinhos na faixa.
- **Texto do "depois":** é o texto do "antes" sem esses 5 trechos. Nenhuma palavra nova entrou.
- **Imagens:** `RD0429_A4_pag02_antes_depois.png` e, avulsas, `RD0429_A4_antes_pag02.png` e `RD0429_A4_depois_pag02.png`.

### 3. RD-0430: Lubrificantes, pág. 2 (cartão do SAC × caixa de garantia)
- **Arquivos:** `apres_bemol.py` (`build`, pág. 2) e `apres_ppt.js` (slide 2). **Páginas:** PDF pág. 2 e .pptx slide 2.
- **Mudança:** sai o cartão "SAC · garantia direto com a fábrica". Os 3 cartões ocupam a mesma largura total.
- **O que fica:** a caixa "Garantia Expressa BAP", sem mudança.
- **Etiqueta:** nesta mesma página também sai a etiqueta do RD-0428.
- **Imagens:** `RD0428_RD0430_Lub_pag02_antes_depois.png` e, avulsas, `Lub_PDF_*_p02.png` e `Lub_PPTX_*_p02.png`.

### 4. Título dos metadados da Linha Moto
- **Arquivos:** `digital2.py` ganha `DOC_META`, no mesmo modelo do `DOC_TITULO`; o padrão continua "Catálogo BAP 2027 — Completo (uso interno)". `catalogo_moto.py` troca para o título da Linha Moto.
- **Páginas:** nenhuma. A mudança é só nos metadados do PDF.
- **Antes:** `Catálogo BAP 2027 — Completo (uso interno)`. **Depois (proposto):** `Catálogo BAP 2027 — Linha Moto`.
- **Conferência:** a Linha Moto foi gerada inteira de novo. Tem 17 páginas, como a entrega, e o texto é igual nas 17. O autor continua "BAP AUTOPARTS".
- **O Completo Digital:** mantém o título de hoje, porque o valor padrão é o mesmo.

### 5. MC-0011 e MC-0012: só mostrar, não aplicar nada
- **MC-0011 (.pptx em Arial, PDF em Poppins):** veja `MC0011_pptx_fonte_arial_poppins.png`, com os slides 3 e 8 em Arial (hoje), em Poppins com a fonte instalada e em Poppins sem a fonte.
  - **O que mudaria:** no `apres_ppt.js:5`, `headFontFace` e `bodyFontFace` passariam a `'Poppins'`.
  - **Risco 1, fonte ausente:** quem abre o .pptx sem a Poppins vê outra fonte, escolhida pelo programa. Aqui saiu Inter; no Windows sem Poppins, [SUPOSIÇÃO] deve sair Calibri ou Arial. Ou seja, o arquivo não fica igual em toda máquina, e essa é a razão provável de hoje ser Arial.
  - **Risco 2, sem fonte embutida:** o `pptxgenjs` não embute fonte. Embutir só no PowerPoint do Windows, à mão ("Salvar com fontes inseridas").
  - **Risco 3, quebras de linha:** a Poppins é mais larga que a Arial, e as quebras mudam. No slide 8, "Fluido de freio DOT 4" deixa o "4" sozinho na linha de baixo, contra a regra B8.
- **MC-0012 (assinatura do logo ilegível; tamanho mínimo):** veja `MC0012_cabecalho_logo_30_48_72pt.png`, o cabeçalho da pág. 3 a 300 ppi com o logo em 30 pt (hoje), 48 pt e 72 pt, na mesma posição.
  - **Tamanho da assinatura:** [SUPOSIÇÃO] a medida em pt vem da proporção do parecer: cerca de 2,5 pt quando o logo tem 30 pt.
  - **O que mudaria:** a assinatura só fica legível perto de 72 pt, ou seja, com o logo 2,4 vezes maior.
  - **Risco:** já com 48 pt o logo encosta no sobretítulo, e com 72 pt cobre o sobretítulo e o título. Para isso funcionar, seria preciso descer o sobretítulo e o título nas 9 páginas e nos 9 slides, o que aperta o conteúdo. Isso é mudança de layout e de marca, não só tirar repetição.
  - **O site:** o topo do site (46 px) tem o mesmo problema, mas é do `web-site`.
  - **A saída de marca:** é uma versão oficial do logo sem a assinatura, para usos pequenos, e só o Alexandre pode fornecer. O parecer pede não cortar o PNG.

### 6. RD-0431 e RD-0432: código, nenhuma página muda

**RD-0431: a apresentação de Lubrificantes em 2 cópias (`apres_bemol.py` para o PDF e `apres_ppt.js` para o .pptx).**
- **Fica o `apres_bemol.py`, que não pode sair.** O `portfolio.py:10-11` importa dele `S`, `W`, `H`, `C`, `LOGO`, `LOGO_G` e `pdfmetrics`. Ele também gera o PDF em Poppins.
- **O `apres_ppt.js` continua sendo o gerador do .pptx.** O .pptx é uma entrega, e só ele sai editável.
- **O que se repete hoje:** são cerca de 130 trechos iguais nos dois arquivos (contei as strings de 12 caracteres ou mais), entre títulos, parágrafos, tabelas e códigos. O desenho é diferente de propósito: o .pptx tem círculos numerados e outros corpos de letra.
- **Proposta:** sai a cópia do conteúdo. Textos e tabelas passam para um arquivo só, `apres_conteudo.json`, lido pelos dois geradores. Nenhum arquivo sai.
  - Conferência: o PDF e o .pptx saem iguais aos de hoje, pixel a pixel.
- **Outras saídas, que não recomendo:**
  - Gerar o PDF a partir do .pptx: o PDF iria para Arial (MC-0011), e o `apres_bemol.py` continuaria existindo por causa do Portfólio.
  - Deixar de entregar o .pptx: sairiam o `apres_ppt.js` e o `apply_theme.js`. Nada no main os importa ou chama, fora o `require` de um no outro; só o `LEIA-ME.md` e o `LEIA_GERADOR.md` os citam.

**RD-0432: cópias históricas do gerador.**
- **Saem:** `gerador/simulacao_detalhe/` (`detalhe.py`, `moto.py` e `print_cat.py`, uma cópia antiga) e `gerador/kitfiltros/kit_v1_32pag.py` (o Kit Filtros de 32 páginas, de 22/10).
- **Ficam:** `gerador/print_cat.py`, `detalhe.py`, `moto.py` e `kitfiltros/kit.py` (com o `parse.py`).
- **Nada no main importa ou chama o que sai.** O `git grep` acha esses nomes só em `.coord/tarefas/`, `docs/marca/pareceres/`, `docs/qualidade/` e `docs/legado/` (que é congelado).
  - Não acha nenhum `import`, `sys.path` ou comando no código, em `scripts/`, em `testes/` ou no CI.
  - O CI só faz `compileall`, que continua passando sem eles.
  - Nenhuma cópia é pacote, porque não há `__init__.py`.
- **Custo de manter:** a T-0023 teve de corrigir a grafia também no `simulacao_detalhe/print_cat.py`.
- **Histórico:** fica no Git.

## Perguntas ao PO (recomendação marcada com ►)

1. **RD-0428:** tirar a etiqueta "BAP AUTOPARTS" do cabeçalho de Lubrificantes, no PDF e no .pptx (págs. e slides 2 a 10)?
   - ► a) Sim, como na simulação.
   - b) Não, fica como está.
2. **RD-0429, barra da pág. 2 do A4:**
   - ► a) Lado direito vazio, como na simulação. Nada se repete.
   - b) "CATÁLOGO 2027", como nas págs. 3, 4 e nas de anotações. Segue o padrão dessas páginas, mas repete o "CATÁLOGO DE PRODUTOS 2027" que já está à esquerda.
3. **RD-0429, o resto da pág. 2 do A4:** tirar o subtítulo, o cartão do SAC e a linha "Prazos de garantia…", como na simulação?
   - ► a) Sim.
   - b) Não.
4. **RD-0430, Lubrificantes pág. 2:**
   - ► a) Sai o cartão do SAC e ficam 3 cartões mais a caixa "Garantia Expressa BAP", como na simulação.
   - b) Fica o cartão do SAC e sai a caixa. Nesse caso se perdem o nome "Garantia Expressa BAP" e o "conforme o certificado da embalagem".
5. **Título dos metadados da Linha Moto:**
   - a) `Catálogo BAP 2027 — Linha Moto`, como pedido e como está na simulação.
   - ► b) `Catálogo BAP 2027 — Linha Moto (uso interno)`. A Linha Moto é material interno: a capa diz "LINHA MOTO · USO INTERNO" e todas as páginas têm o aviso. Os títulos do A4 e do Completo Digital mantêm "(uso interno)". Pela regra conservadora, só sairia o "Completo", que está errado.
6. **MC-0011 (.pptx em Poppins):**
   - a) Fazer agora.
   - ► b) Deixar para o Alexandre, pelo manual "a aprovar". A troca não é só tirar repetição: muda a fonte para quem abre sem a Poppins e quebra o "DOT 4" no slide 8.
7. **MC-0012 (tamanho do logo e assinatura):**
   - a) Fazer agora.
   - ► b) Deixar para o Alexandre. Um logo legível exige refazer o cabeçalho das 9 páginas e dos 9 slides, e a saída de marca (logo sem a assinatura, em vetor) só ele pode fornecer.
8. **RD-0431:**
   - ► a) O conteúdo vai para um arquivo só (`apres_conteudo.json`), lido pelos 2 geradores. As páginas ficam iguais, pixel a pixel.
   - b) Fica como está e o RD é fechado como "aceito".
   - c) Deixar de entregar o .pptx.
9. **RD-0432:** apagar `simulacao_detalhe/` e `kitfiltros/kit_v1_32pag.py`?
   - ► a) Sim.
   - b) Não.
10. **`gerador/portfolio_v1_por_sistema.py`:** é a mesma situação do RD-0432, uma versão antiga do Portfólio, de 23/10, e nada a importa ou chama. Mas não está no RD-0432. Incluir na T-0025, com um RD novo do `corretor-redundancias`?
    - ► a) Sim.
    - b) Não, fica para outra tarefa.

## Fora desta tarefa, só para registro
- **Tamanho do Completo Digital:** tem 311 páginas, acima do limite de cerca de 200 do padrão do catálogo. Não foi mexido.
- **Material para cliente:** o texto extraído do PDF e do .pptx de Lubrificantes ("depois") não tem "ranking", "vendedor", "MOQ", "FOB", "fornecedor", "uso interno" nem "estoque".
  - "preço" aparece 1 vez, em "preço acessível", e "cliente" 1 vez, em "perfil de cliente". As duas ocorrências já estavam no "antes", e nenhuma é valor ou nome de cliente.
