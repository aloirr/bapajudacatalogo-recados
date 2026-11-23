# Padrão de treinamento BAP (T-0032): SIMULAÇÃO, a aprovar

Guia tirado dos 3 treinamentos originais (out/2026), em `catalogo_grafico/originais/treinamentos/`:

| Original | Slides | Módulos | Duração (notas) |
|---|---|---|---|
| Baterias | 47 | 7 | cerca de 2h15 |
| Linha Moto | 40 | 5 | não diz |
| Lubrificantes | 43 | 7 | cerca de 1h45 |

- Referência visual: `referencia/tipos_de_slide_originais.png` (os 13 tipos de slide, no de Lubrificantes).
- Amostra no padrão (Mecânica Básica, 8 slides): `../simulacoes/T-0032/`.
- Gerador: `../gerador/treinamento.py` + `../gerador/treinamento_ppt.js` (texto em `../gerador/treinamentos/<nome>.json`).
- Público: vendedor externo BAP. O material fica só no admin (`/admin/pdfs/`). Por isso o conteúdo interno (alçada de desconto, Price) pode ficar.
- Nenhum treinamento final é gerado antes do "aprovado" deste padrão.

## 1. Estrutura

Ordem fixa, igual nos 3 originais:

1. **Capa** (1 slide).
2. **Abertura** (3 slides):
   - O que vamos aprender: frase-objetivo e 3 pilares (ex.: ENTENDER, INDICAR, VENDER);
   - Tópicos: até 8 cartões, um por módulo, e o último "✓ Fechamento";
   - "Ao final deste treinamento, você estará preparado para": 6 verbos (Explicar, Ler, Indicar...).
3. **Módulos 01 a 0N** (5 a 7 módulos). Cada um tem:
   - um slide de **seção**;
   - de 2 a 6 slides de **conteúdo**.
   - O caminho é sempre do técnico para a venda: fundamentos, depois ler o produto ou o código, depois o portfólio BAP, depois o diagnóstico ou a garantia, depois a armazenagem.
4. **Último módulo: Vender**. Segue sempre esta sequência:
   - argumentos e SPIN;
   - cross-sell;
   - "Fechamento em 3 etapas" (Peça, Não fechou, Você resolve);
   - "Não fechou? Os 5 motivos": preço, prazo ou limite, estoque, fornecedor, sem necessidade. A faixa ATENÇÃO traz a alçada de 15% e diz que, acima dela, o Price aprova.
5. **Fechamento**: checklist do vendedor (10 itens) e teste de conhecimentos (6 perguntas).
6. **Obrigado** (no desenho da capa): frase-resumo e site.

**Notas do apresentador:** todo slide tem notas em blocos com título em caixa alta:

- MENSAGEM-CHAVE;
- COMO CONDUZIR;
- PERGUNTE AO TIME ou INSIGHT PARA O CAMPO;
- no quiz, RESPOSTAS;
- na capa, BASE: a versão da base unificada lida na geração. O gerador escreve sozinho (S11).

## 2. Tipos de slide

| Tipo | Desenho | No gerador (`tipo`) |
|---|---|---|
| Capa | Fundo de padrão verde com ícones de peças, faixa escura de 8,3" à esquerda e logo num quadro branco à direita. Sobretítulo "TREINAMENTO COMERCIAL", título, subtítulo e "Equipe Comercial Externa · Novembro de 2026". | `capa` |
| Abertura: aprender | Frase grande à esquerda, com destaque em verde; 3 cartões de pilar à direita, com ícone. | a fazer |
| Abertura: tópicos | Grade 4 × 2 de cartões: número grande em verde-escuro, ícone no círculo verde, título e descrição. O cartão "✓ Fechamento" tem fundo verde-claro. | `topicos` |
| Abertura: preparado para | Grade 3 × 2: ícone, verbo em verde e complemento. | a fazer |
| Seção do módulo | Mesmo fundo da capa; número "01" grande em verde, título e subtítulo. | `secao` |
| Conteúdo em cartões | Kicker "MÓDULO 0N · TEMA", título e de 3 a 12 cartões, na grade de 4 colunas. Em cada cartão, o nome vem primeiro e o número é apoio, numa linha menor. | `sistemas` (variação, em 4 × 3) |
| Tabela | Cabeçalho verde-escuro, linhas alternando branco e verde-claro, todo o corpo em escuro, 1.ª coluna em negrito. Com mais de 6 linhas, vai em 2 slides (S6). Coluna de produto ("Na BAP") só com o nome do PRODUTO da base, que o gerador confere. | `tabela` |
| Dica de campo | Faixa verde-clara no pé do conteúdo, com lâmpada, "DICA DE CAMPO" em negrito e 1 ou 2 linhas. Uma por slide, no máximo. | `dica` em qualquer conteúdo |
| Atenção | A mesma faixa, em laranja-claro, com o ícone de alerta laranja e a palavra "ATENÇÃO" em laranja-escuro `#8A3F00`. Uso: regra que não pode ser quebrada (norma, alçada, segurança). | `atencao` |
| Cross-sell | Círculo escuro no centro, com a venda-âncora, e 3 cartões de cada lado com o que vai junto. | `hub` |
| Fechamento em 3 etapas | 3 cartões (Peça, Não fechou, Você resolve) e faixa escura com os 5 motivos. | a fazer |
| Não fechou | Tabela com Motivo, Responda com prova e Volte ao pedido, mais a faixa ATENÇÃO da alçada. | `tabela` |
| Checklist | 2 colunas de 5 cartões, cada um com um "✓" no círculo verde. | `checklist` |
| Quiz | 6 faixas, cada uma com o número em escuro num círculo laranja e a pergunta. As respostas ficam só nas notas. | `quiz` |
| Obrigado | Desenho da capa: "TREINAMENTO X BAP", "Obrigado!", frase e site. | `capa` |
| Mitos e verdades | Está no original de Lubrificantes (slide 27). **A desenhar depois:** fica fora do padrão, sem slide, até ter desenho e simulação aprovados. | — |
| Passo a passo numerado | Está no original de Lubrificantes (slide 26). **A desenhar depois:** fica fora do padrão, sem slide, até ter desenho e simulação aprovados. | — |

## 3. Grade, cores e fonte

**Página:** 16:9, 13,333" × 7,5".

**Grade do conteúdo:**

- margem lateral de 0,6" e largura útil de 12,13";
- vão de 0,15" entre cartões;
- 4 colunas de 2,92". A grade de 6 colunas sai do padrão, porque o corpo ficaria abaixo de 12 pt.

**Posições fixas (em polegadas):**

| Elemento | x, y | Tamanho |
|---|---|---|
| Kicker | 0,6; 0,32 | 12 pt negrito, verde-escuro, espaçado |
| Título | 0,6; 0,64 | 30 pt negrito (caixa de 11,2 × 0,75) |
| Logo | 12,2; 0,3 | 0,53 × 0,72 |
| Área útil | y de 1,55 a 5,75 | |
| Faixa de dica ou atenção | y de 5,8 a 6,6 | |
| Rodapé | 0,6; 7,0 | "Treinamento X BAP \| Equipe Comercial Externa", 10 pt cinza |
| Número da página | 12,13; 7,0 | à direita, 10 pt cinza |

**Tamanhos de fonte:**

| Elemento | Tamanho |
|---|---|
| Capa | sobretítulo 16, título 48, subtítulo 20, rodapé 14 |
| Seção | número 96, título 40, subtítulo 20 |
| Cartão | título de 15 a 19; texto de 12 a 14 |
| Rótulo (itens no catálogo, OFEREÇA JUNTO, legenda do hub, rodapé) | 10 ou mais |
| Tabela | de 12 a 13 |
| Dica | 14 |
| Checklist | 16 |
| Quiz | 17 |

**Cores** (tema dos originais; no gerador, tema "BAP Treinamento"):

| Papel | Hex |
|---|---|
| Escuro (títulos, faixa da capa, centro do hub) | `#1E2B22` |
| Verde, o do logo (fundo, círculo de ícone, faixa; texto e número só sobre o escuro, como na capa) | `#59BA61` |
| Verde-escuro (todo texto e número verde sobre fundo claro: kicker, número, cabeçalho de tabela, rótulos; 5,1:1 no branco) | `#2F7D36` |
| Verde-claro (faixa de dica, linhas alternadas) | `#EEF7EF` |
| Borda de cartão | `#D9E6DA` |
| Cinza (texto de apoio, rodapé) | `#6B7570` |
| Laranja (ícone de alerta, círculo do quiz com o número em escuro) | `#F28C28` |
| Laranja-escuro (a palavra "ATENÇÃO"; é o `otext` do catálogo digital) | `#8A3F00` |

**Tema do .pptx:** só cores desta tabela. O vermelho `#D64545` e o amarelo `#F2C14E` do tema dos originais saíram: nenhum slide os usa. No tema, o accent5 é a borda e o accent6 é o laranja-escuro.

**Contraste:** o `#59BA61` no branco dá 2,4:1. Por isso nunca é cor de texto sobre fundo claro. O cinza `#6B7570` fica para texto de apoio sobre o branco, nunca no corpo de tabela.

**Fonte:** **Arial** em tudo (decisão 7 a, `docs/marca/manual.md`). Os originais estão em Calibri.

**Ícones:** brancos, dentro de um círculo verde. São os mesmos dos originais, em `gerador/treinamento_img/icones/`.

## 4. O que melhorar em relação aos originais (sugestões para aprovar)

| # | Sugestão | Por quê |
|---|---|---|
| S1 | Trocar Calibri por Arial nos 3 (já decidido) e **revisar a quebra de linha**. | A Arial é mais larga: títulos de cartão que cabiam numa linha em Calibri passam para duas. O gerador já reserva 2 linhas. |
| S2 | **Tirar a coluna "Estoque" e os números de estoque** da Linha Moto (6 tabelas, mais as "4.261 unidades" da lâmpada) e a frase "toda a linha ativa tem estoque nas 7 filiais" de Lubrificantes. | É foto de 13/10 que envelhece. O estoque não entra no Git, então o gerador não teria como atualizar. No lugar, vale "consulte o estoque antes de ofertar". |
| S3 | **Códigos e números pela base unificada**, gerados por script: quantidade de itens, códigos BAP e OFEREÇA JUNTO. | Hoje estão digitados à mão. Com o script, a base mudou e o slide muda junto. Código fora da base ou não ATIVO trava a geração. |
| S4 | **Todos com as 3 aberturas.** | A Linha Moto não tem o "Ao final… você estará preparado para". |
| S5 | **Notas sempre no mesmo formato** (MENSAGEM-CHAVE, COMO CONDUZIR, PERGUNTE AO TIME ou INSIGHT, e RESPOSTAS no quiz) **e com a duração na capa.** | As notas da capa da Linha Moto são um parágrafo solto e não dizem a duração. |
| S6 | **Corpo com 12 pt ou mais; rótulo** (itens no catálogo, OFEREÇA JUNTO, legenda do hub, rodapé) **com 10 pt ou mais.** Tabela com mais de 6 linhas vai em 2 slides, com o mesmo título, "(1 de 2)" e o cabeçalho repetido. O gerador já faz a divisão. | Há tabelas com 7 a 11 linhas (ProActive, ficha técnica) que ficam pequenas no projetor. |
| S7 | **Conferir as datas de norma antes de gerar.** | "API SQ desde 31/03/2025" e "CL-4 (PC-12), licenças a partir de 01/01/2027" precisam ser checadas com a fonte da API. [SUPOSIÇÃO: podem ter mudado.] |
| S8 | **Remissão entre treinamentos.** | Elétrica remete a Baterias; Freio e Arrefecimento remetem a Lubrificantes (fluido e aditivo); Rodagem remete à Linha Moto (pneus e câmaras). Evita repetir conteúdo. |
| S9 | **PDF de apoio saindo do mesmo .pptx** (LibreOffice), para o `/admin/pdfs/`. | As notas de Lubrificantes prometem o "Material de Apoio em PDF". |
| S10 | **Verde do padrão.** A recomendação da marca é **manter o `#59BA61`**, que é o verde do logo (medido nos 4 arquivos de logo), com o `#2F7D36` para o texto. A outra opção é o `#62BB47` do catálogo. A escolha final é do Alexandre. | Pela decisão de 20/11, o verde oficial é o do logo. Com qualquer dos dois, o texto verde sobre fundo claro usa o `#2F7D36`. |
| S11 | **Versão da base nas notas da capa** (bloco BASE, com a versão da base do dia, escrita pelo gerador) ou no rodapé do Obrigado. Não vai na capa. | Mostra de que base vieram os códigos. O vendedor não precisa dela para agir. |
| S12 | **"uso interno" no rodapé** de todos os treinamentos: "Treinamento X BAP \| Equipe Comercial Externa · uso interno". | Sugestão da marca. Mesmo só no admin, o slide pode ser mostrado ao cliente. A capa da Linha Moto já faz assim. |

## 5. Estrutura proposta dos treinamentos

Todos seguem a estrutura da seção 1. Abaixo vão só os módulos de conteúdo. O último módulo é sempre **Vender**, seguido do checklist, do quiz e do Obrigado. A lista de "Na base" é dos produtos que o slide de portfólio vai puxar.

### 11 novos

| Treinamento | Módulos | Na base (produtos) |
|---|---|---|
| **Mecânica Básica** | 01 O carro em sistemas · 02 Motor e arrefecimento · 03 Suspensão, direção e rodagem · 04 Freio e transmissão · 05 Elétrica e filtração · 06 Sinais de desgaste · 07 Cross-sell e fechamento | os 12 sistemas |
| **Suspensão** | 01 Para que serve e tipos (McPherson, eixo de torção, feixe) · 02 Amortecedor e kit (batente, coxim, troca em par) · 03 Bandeja, pivô, bieleta, bucha e suporte tensor · 04 Ler o código e a posição BAP · 05 Diagnóstico e garantia · 06 Vender (com direção e alinhamento) | amortecedor, kit batente, bandeja, bieleta, pivô, suporte tensor, bucha |
| **Direção** | 01 Mecânica, hidráulica e elétrica · 02 Caixa de direção · 03 Terminal e axial · 04 Aplicação e código · 05 Folga, ruído, vazamento e alinhamento · 06 Vender | caixa de direção, terminal, axial |
| **Transmissão** | 01 Embreagem, câmbio, diferencial e semieixo · 02 Junta homocinética e kit reparo (coifa e graxa) · 03 Trizeta, semieixo e cruzeta · 04 Embreagem remanufaturada, servo e cilindro · 05 Rolamentos e diagnóstico · 06 Vender (óleo de câmbio: remete a Lubrificantes) | junta, kit reparo, trizeta, semieixo, cruzeta, embreagem, servo, rolamentos |
| **Freio** | 01 Disco, tambor, hidráulica e ABS · 02 Pastilha (indicador, assentamento) · 03 Sapata, cilindro de roda e catraca · 04 Linha pesada: cuíca e catraca · 05 Sensor ABS · 06 Fluido e segurança (remete a Lubrificantes) · 07 Vender | pastilha, sapata, cilindro de roda, sensor ABS, cuíca, catraca |
| **Arrefecimento** | 01 Como o motor controla a temperatura · 02 Bomba d'água (junto com o kit de correia) · 03 Eletroventilador · 04 Aditivo e diluição (remete a Lubrificantes) · 05 Superaquecimento: diagnóstico · 06 Vender | bomba d'água, eletroventilador |
| **Motor** | 01 Motor de 4 tempos · 02 Distribuição: kit de correia, polias e tensionadores · 03 Lubrificação: bomba de óleo e interruptor de pressão · 04 Bomba de combustível · 05 Ruído de correia e luz do óleo · 06 Vender (kit + bomba d'água) | kit de distribuição, polias, bomba de óleo, interruptor, bomba de combustível, rolamentos |
| **Elétrica** | 01 Circuito 12 V e 24 V · 02 Ignição: vela e cabo (código, grau térmico, folga) · 03 Lâmpadas (tipos e potência) · 04 Interruptores e sensores · 05 Bateria em 1 slide (remete a Baterias) · 06 Vender | vela, cabo de vela, lâmpada, interruptor e sensor, bateria |
| **Filtração** | 01 Os 4 filtros do carro · 02 Óleo · 03 Ar do motor · 04 Cabine · 05 Combustível (flex e diesel) · 06 Linha pesada e Kit Filtros · 07 Vender (troca de óleo) | filtros |
| **Rodagem** | 01 Roda, cubo e rolamento · 02 Cubo de roda (com e sem ABS) · 03 Rolamento (código, 2RS e 2Z) · 04 Rodas de aço e de alumínio · 05 Pneu e câmara de moto (remete à Linha Moto) · 06 Vender | cubo, rolamentos, rodas, pneus e câmaras moto |
| **Acessórios** | 01 Palheta (medida por lado, encaixe, Multi Fit) · 02 Cinta e catraca (capacidade e uso) · 03 Vender (troca rápida e exposição) | palhetas, cintas e catracas |

### 3 atualizados

Em todos: estrutura mantida, Arial, números e códigos pela base atual, notas no formato S5 e correções de texto.

| Treinamento | O que muda |
|---|---|
| **Baterias** (7 módulos) | Linhas e códigos pela base: 25 ativos (EFB, TF, LP, MXW, MXP...). Conferir a garantia por linha com a descrição da base. Remeter a Elétrica no cross-sell de velas. |
| **Linha Moto** (5 módulos) | Tirar a coluna "Estoque" e os números de estoque (S2). Pneus e câmaras pela base: 12 pneus e 9 câmaras ativos. Incluir o "preparado para" (S4). |
| **Lubrificantes** (7 módulos + Químicos) | Tirar a frase das 7 filiais (S2). Conferir as datas API (S7). ProActive, Shiftease e Effitech pela base: 24 itens, 18 ativos. Incluir o **módulo Químicos**: fluido de freio, aditivos, desengripante e silicone; 38 itens na base. |

## 6. Como gerar (depois do aprovado)

```
cd catalogo_grafico/gerador
python treinamento.py mecanica_basica --png ../simulacoes/T-0032
```

- Precisa do Node com `pptxgenjs` e do LibreOffice (`soffice`), este só para os PNGs.
- A saída vai para `gerador/saidas/` e, depois do aprovado, para `entregas/`.
- Tipos ainda **a fazer** no gerador: aprender, preparado para e fechamento em 3 etapas. Neles, o texto verde sobre branco (os pilares do "aprender" e os verbos do "preparado para") vai em `#2F7D36`, e não no verde dos originais.
- Eles seguem o desenho dos originais (`referencia/tipos_de_slide_originais.png`) e entram antes de gerar os treinamentos completos.
- Mitos e verdades e passo a passo numerado ficam fora do padrão até ter desenho (seção 2).
- Grafia: os nomes de linha vão como "ProActive", "Shiftease" e "Effitech"; caixa alta só onde todo o texto é caixa alta (kicker). O nome do produto sai do Catálogo BAP (PRODUTO da base), não é digitado.
