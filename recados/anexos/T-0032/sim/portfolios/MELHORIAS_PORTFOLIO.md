# T-0032 · Lista de melhorias do Portfólio geral (consolidada, para o Alexandre aprovar)

| Campo | Valor |
|---|---|
| Tarefa | T-0032, passo 1 (iii), decisão 7a: "Revisão completa do Portfólio geral (catalogo-grafico, designer-ux e design-de-marca), com a lista de melhorias para o Alexandre aprovar" (R-20261123-141744-po) |
| Fontes | Pareceres da amostra (Autocenter e Baterias): `docs/ux/pareceres/T-0032-portfolios-amostra.md` (95f2ab4) e `docs/marca/pareceres/T-0032-portfolios-amostra.md` (7a3b2cb) · `designer-ux`: `docs/ux/pareceres/T-0032-melhorias-portfolio.md` (12 itens, branch `designer-ux/T-0032-melhorias`, 5d6bbb8) · `design-de-marca`: `docs/marca/pareceres/T-0032-melhorias-portfolio.md` (12 itens, branch `design-de-marca/T-0032-melhorias`, 5249098) · `catalogo-grafico`: 2 itens novos e 2 complementos |
| Data | 23/11/2026 (Manaus) |
| Base | v28, Portfólio geral do branch da T-0029 (87 páginas) |

As 24 propostas dos 2 pareceres, mais as do `catalogo-grafico`, viraram **23 itens**. Juntei os pedidos iguais:

- UX 8 e marca 11 e 12 viraram o item 1;
- UX 4 e marca 6 viraram o item 8.

A coluna "Origem" diz de onde veio cada item. Nada muda no Portfólio geral sem o "aprovado".

- **Ordem:** primeiro a prioridade (alta, média, baixa). Na mesma prioridade, o que destrava os 7 portfólios e o menor esforço vêm antes.
- **Estado:** "na simulação" quer dizer que o item já está aplicado nos 2 PDFs de simulação (Linha Autocenter e Linha Baterias), e só neles. O Portfólio geral continua igual ao da T-0029.
- **Quem faz:**
  - CG = `catalogo-grafico`;
  - CD = `catalogo-dados` (correção na base, com versão nova e LOG_CORRECOES);
  - DM = `design-de-marca` (manual);
  - AG = decisão ou material do Alexandre.

**Correção à marca (item 11, tabela dos títulos):** a composição do Autocenter **já foi definida** pela decisão 3a, e a [SUPOSIÇÃO] do parecer cai. O Autocenter tem só a Linha Leve:

- Filtração (ar, óleo, combustível e cabine);
- Palhetas;
- Suspensão (amortecedores, kit batente, bieletas, buchas, bandejas e pivôs);
- Freio (pastilhas, sapatas, cilindro de roda e sensor ABS);
- Lubrificantes e Baterias.

Por isso, a frase de apoio da capa passa a ser: "Os itens de troca rápida do autocenter: filtros, palhetas, suspensão, freio, lubrificantes e baterias." São 14 palavras, e "troca rápida" é a expressão do Alexandre.

## Lista

| # | O que muda | Origem | Quem faz | Esforço | Prioridade | Precisa de simulação? |
|---|---|---|---|---|---|---|
| 1 | **Modelo dos 7 portfólios por linha.** Blocos opcionais: capa da linha → Quem somos → divisória única com a página de cada produto → produtos → contracapa. A pág. 3 (os 4 cartões de linha) fica só no geral. A capa é a mesma do geral: mesmo verde, logo e faixa "PORTFÓLIO DE PRODUTOS 2027", com o nome da linha, a frase de apoio (até 15 palavras), "N linhas de produtos · N itens", o mês da edição e as fotos da própria linha. Título do PDF: "Portfólio de Produtos BAP AUTOPARTS · Linha X". Nenhuma cor nova e nunca "uso interno". O Quem somos é o mesmo nos 8. Na contracapa, o fim da frase muda com o cliente: "…para o seu autocenter" e "…para a sua loja, oficina ou frota" (Pesada) | UX 8 · Marca 11 e 12 | CG | Médio | Alta | Sim. **Na simulação** (Autocenter e Baterias) |
| 2 | **Aplicações só da linha.** Cada linha mostra só veículos dela: hoje a Leve mostra caminhão e máquina (Volvo VM, MB 709, MB 2219, pulverizador Jacto, Dynapac CC21) e a Moto mostra Scania e Bandeirante. *Complemento do CG:* a regra `taxo.HEAVY` não pega "Fiat 130", "Fiat 190", "Fiat Allis FG 70" nem "VW 7100", que ficaram nos Filtros de Combustível do Autocenter (p06), nem "Dynapac CC21", "Muller 26" e "Putsmeister BSA1003", nos Filtros de Óleo (p07); a lista de modelos pesados precisou crescer: o `taxo.HEAVY` novo da T-0029 (máquinas, motores diesel pesados, caminhões pelo número) já pega todos | Marca 4 · UX (amostra) · CG | CG (saída); CD (origem) | Médio | Alta | Sim. **Na simulação** só no Autocenter: sai o que o `taxo.HEAVY` reconhece como pesado (p06 e p07 sem caminhão e sem máquina). No geral, a Leve e a Moto ainda mostram |
| 3 | **Foto certa nos filtros.** As páginas de Filtros de Cabine, de Combustível, de Óleo e Outros Filtros usam a foto da caixa "Filtro de Ar": são 8 páginas do geral (3 na Leve, 4 na Pesada e 1 na Moto) e 3 no Autocenter. Cada família de filtro deve ter a foto da sua caixa | CG (novo) | AG (fotos); CG | Baixo, se houver a foto | Alta | Sim |
| 4 | **Aplicação que não é veículo.** "UNIVERSAL / MOTO / LINHA LEVE", "Uso sem câmara", marcas de terceiros (Bosch, Valeo, Delco Remy), código de vela de outra marca e o "- DE" saem do bloco. Item universal ganha uma frase ("Uso universal: motos, linha leve e indústria") | Marca 5 | CG (saída); CD (origem) | Médio | Alta | Sim |
| 5 | **Cabeçalho da página de produto com menos níveis.** O sobretítulo fica só com a linha e o número ("Linha Leve · 01"), o título é o sistema, menor que o nome do produto, e o produto passa a ser o maior texto da página. Isso resolve o sistema repetido (RD-0535) | UX 1 | CG | Baixo | Alta | Sim |
| 6 | **Corte das aplicações.** Corta só em fim de palavra e sempre com "…" (hoje sai "…diesel, Com", "Sie", "VW Fus"), ou a linha quebra em 2, com recuo. A regra é a mesma em todas as páginas | UX 3 | CG | Baixo | Alta | Sim |
| 7 | **Glossário de nomes.** "Linha + nome" para o segmento ou o portfólio (Linha Leve, Linha Baterias); "linhas de produtos" para a contagem; a p02 passa a dizer "3 linhas de veículo: leve, pesada e moto". ProActive, Shiftease e Effitech são "nomes de produto BAP", com a grafia fixa, também no A4, no Digital e na base. Nos portfólios por linha, o total vai uma vez, na capa: "N produtos · N itens" ("produtos" conta as páginas de produto e "itens" conta os códigos); na Linha Baterias, "Linha Leve e Linha Pesada · 47 itens" (MC-0021). A divisória fica sem contagem | Marca 3 · UX e marca (amostra) | DM (manual); CG (PDFs); CD (DESCRICAO) | Baixo | Alta | Sim (p02) |
| 8 | **Aplicações agrupadas por montadora, com uma grafia só.** O nome da montadora aparece uma vez, em negrito, e os modelos vêm depois: no máximo 2 linhas por montadora, em ordem alfabética, sem "GM/GM" e sem "VW" e "Volkswagen" juntos. A montadora tem a inicial maiúscula e as siglas ficam em maiúsculas (VW, GM, MB, MAN, BMW, KTM, GMC, CBT). Quando falta a montadora, ela entra antes do modelo ("Fiat Uno"). Na Moto, sai o "0.1 L" | UX 4 · Marca 6 | CG; CD (origem) | Médio | Alta | Sim |
| 9 | **Especificações em 2 colunas e tabela da Bateria.** A partir de 7 linhas, a lista vai para 2 colunas (hoje a p32 mostra 9 das 38 baterias). No portfólio de Baterias, entra uma página de tabela, com uma linha por bateria: código, capacidade, garantia e observação. Com a tabela, a página do produto não repete a lista: só aponta para a página da tabela. O título da tabela diz a linha ("Baterias da Linha Leve · 38 itens") | UX 7 | CG | Médio | Alta | Sim. **Na simulação** (as 2 colunas nos 2 PDFs; a tabela na Baterias e no Autocenter) |
| 10 | **Índice com página e link.** A divisória de cada linha e os cartões da p3 trazem o número da página de cada produto. No PDF, o link é clicável: da divisória para o produto e do rodapé para a divisória | UX 2 | CG | Médio | Alta | Sim. **Na simulação**, a página na divisória única (sem link) |
| 11 | **Página adaptável.** Com até 4 aplicações ou especificações, cabem 2 produtos da mesma família ou do mesmo sistema por página, cada um em meia página; com mais de 12, até 8 linhas por coluna. Isso evita a meia página vazia, que é a maioria na Pesada, na Moto e na Baterias | UX 5 | CG | Alto | Alta | Sim |
| 12 | **Descrição do produto conforme a linha.** "Baterias para automóveis, picapes e utilitários" na Leve, "Baterias para caminhões, ônibus e máquinas" na Pesada e "Filtros de combustível para motores a diesel" na Pesada | Marca 9 | CG | Baixo | Média | Sim. **Na simulação** (Baterias Leve e Pesada) |
| 13 | **Especificações com um padrão de escrita.** Unidade com espaço ("20 L", "45 Ah", "50 mm"), viscosidade em maiúsculas ("0W20"), siglas em maiúsculas (API SN, JASO MA, ATF Dexron III, MXFF), a capacidade da bateria uma vez só e "jogo com 2 peças". *Complemento do CG:* nos óleos, tirar "Litro" e "Óleo lubrificante" do começo, porque em 2 colunas o texto corta ("Litro óleo ProActive 100 semissintético 1"). O corte que sobrar é em fim de palavra, com "…", e o volume do fim fica ("Shiftease 110 80W90 API GL5… 20 L") | Marca 7 · UX (amostra) · CG | CG (saída); CD (base) | Médio | Média | Sim. **Na simulação**: baterias ("45 Ah LP · 18 meses") e óleos ("ProActive 300 0W20 API SN sintético", "0W20 sintético API SN · 200 L") |
| 14 | **Voz da capa do geral.** O subtítulo deixa de explicar como ler e passa a ser: "Componentes de qualidade para as linhas leve, pesada e moto: peças, baterias, filtros, lubrificantes e acessórios." | Marca 1 | CG | Baixo | Média | Sim |
| 15 | **Contato da contracapa.** Pôr "BAP AUTOPARTS · Componentes de qualidade" junto do logo e escolher o contato: a) o do Alexandre, como hoje; b) um canal comercial da empresa; c) o vendedor de cada linha. **Recomendação da marca: b, se o canal comercial existir; senão, a** | Marca 2 | AG (decide); CG | Baixo | Média | Sim |
| 16 | **Legibilidade.** O sobretítulo passa para o verde escuro dos rótulos (#1F7A32, contraste de 5,4:1). As aplicações ficam com 10,5 pt ou mais e o sobretítulo com 9 pt ou mais. O mesmo mínimo de 10,5 pt vale para a tabela das baterias (hoje 9,5 pt, cerca de 8,3 pt impresso) e para a lista da divisória (hoje 8,8 pt). Conferir numa impressão de teste em A4 paisagem | UX 12 · UX (amostra) | CG | Baixo | Média | Sim (e prova impressa) |
| 17 | **"N itens" junto do nome.** Sai de baixo da foto e vai para a linha de apoio, abaixo da descrição | UX 11 | CG | Baixo | Média | Sim |
| 18 | **Foto que falta.** Fica um estado só: o logo pequeno, em cinza claro, com "Foto em breve" (hoje é o logo grande, nas p31, p36, p53, p57, p60 e p83) | UX 10 | CG | Baixo | Média | Sim |
| 19 | **Divisória com poucos produtos.** Com até 10 produtos, entra um mosaico de miniaturas (foto, nome e página) ou a lista em fonte maior, centralizada (Moto, Universal) | UX 6 | CG | Médio | Média | Sim. **Na simulação**, só o mais barato: a divisória usa só as colunas de que precisa, e a Baterias (2 produtos) fica sem divisória |
| 20 | **Enquadramento da foto.** O produto ocupa cerca de 80% da maior dimensão da caixa, centralizado, com a mesma margem em todas as páginas | UX 9 | CG | Médio | Média | Sim |
| 21 | **"Preço acessível" no Quem somos.** A frase "com segurança e preço acessível" é a única ocorrência da palavra "preço" num material de cliente; a regra é "sem preço". Proposta: "com segurança e bom custo-benefício" (**recomendação da marca**) [SUPOSIÇÃO: a regra fala de valor, não da palavra; a decisão é do Alexandre] | CG (novo) · marca (amostra) | AG (decide); CG | Baixo | Média | Não (só texto) |
| 22 | **Selo de novidade com uma palavra só.** "NOVIDADE 2026" na página de produto, "NOVIDADE" no sumário e no Digital (hoje "NOVO") e, na próxima edição do A4, "NOVIDADE 2026" também. Opções: a) "NOVIDADE" em tudo; b) "LANÇAMENTO" em tudo; c) fica como está. **Recomendação da marca: a**, "NOVIDADE" em tudo | Marca 10 | AG (decide); CG | Baixo | Baixa | Sim |
| 23 | **Nomes de produto na ortografia oficial.** "Palhetas Limpa-Para-Brisa", "Semieixo Homocinético" e "Bomba d'Água". A troca é na coluna PRODUTO da base, e a busca do site tem de continuar achando "parabrisa" e "semi eixo" | Marca 8 | CD (base); CG e `web-site` conferem | Baixo | Baixa | Sim (base) |

## Ordem sugerida de execução

1. Itens que destravam os 7 portfólios: 1, 2, 9, 10 e 12. Eles já estão na simulação dos 2 e precisam do "aprovado" para ir aos outros 5 e, se for o caso, ao geral.
2. Itens rápidos e de efeito alto: 3, 5, 6, 7, 16, 17 e 18.
3. Itens de conteúdo, na saída e na base: 4, 8 e 13.
4. Acabamento: 11, 19, 20, 14, 15, 21, 22 e 23.
