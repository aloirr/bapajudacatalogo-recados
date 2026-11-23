---
id: R-20261123-151213-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0032
responde_a: R-20261123-141744-po
encerra: false
contrato: null
criado_em: 2026-11-23T15:12:13+00:00
---
# T-0029 final e T-0032 Passo 1 para o Alexandre (15 perguntas)

Seguem num recado só a T-0029 final e o Passo 1 da T-0032, como você pediu. Nada foi gravado em entregas/ e nenhum treinamento foi gerado.
Anexos em bapajudacatalogo-recados, commit ae720a1:
- recados/anexos/T-0029/final-sim/ (rodada2/ e rodada3/, cada uma com LEIA-ME.md; o PDF completo está em rodada3/);
- recados/anexos/T-0032/sim/treinamento/;
- recados/anexos/T-0032/sim/portfolios/.

## T-0029 · Portfólio final (catalogo-grafico)
- Branch catalogo-grafico/T-0029-portfolio-2027, head 6d8f14300b37b790ece8176fc87e6191ce35d3ca, já com o main (base v28).
- 87 páginas: a p46, Bieletas da Pesada, saiu pela v28. Em relação à simulação aprovada (61ac7ed):
  - selo de volta a "NOVIDADE 2026" (9a);
  - "ProActive" e "Shiftease" nas p74, p78 e p79 (10a), e "Effitech";
  - contagens da v28 na capa e nas divisórias: Leve 4.050 itens; Pesada 24 produtos e 508 itens;
  - 16a, a Linha Pesada só com veículos pesados.
    - Para isso, o gerador ganhou uma regra melhor de veículo pesado (taxo.HEAVY):
      - voltam à Pesada máquinas agrícolas e de obra, motores diesel pesados e caminhões Fiat, VW, GM, MB e Ford;
      - saem Focus, V40, 300C, Ducato Cargo, Expert Cargo, Topic e Daily.
    - A regra só afeta o Portfólio: o site e a base não usam o taxo.
  - Os modelos nunca saem cortados no meio da palavra, e todo corte leva "…". Isso muda 18 páginas, também na Leve, na Moto e na Universal.
  - "Ford F-12000, F14000" (p56) e "F12000, F14000, F16000" (p59): o "2000" deixou de ser lido como ano.
- A4 (56 págs.), Completo Digital (311) e Linha Moto (17): iguais ao main, pixel a pixel e no texto.
- Sem preço e sem estoque.
- UX LIBERADO e marca LIBERADO, os dois na rodada 3. O MC-0017 fecha com a entrega.
- Com o "aprovado": o catalogo-grafico grava o PDF em entregas/ (mesmo nome), com a prova pixel a pixel contra esta simulação, e depois vem o fluxo de testes, revisão e PR.

## T-0032 · Passo 1
### (i) Padrão de treinamento (catalogo-grafico)
- Branch catalogo-grafico/T-0032-padrao-treinamento, head 0371d28e86ede0291ad834eeeb2f45efde450ef1.
- O guia PADRAO_TREINAMENTO.md foi tirado dos 3 .pptx. Ele define:
  - a estrutura: capa; 3 aberturas; de 5 a 7 módulos, do técnico à venda; o módulo "Vender" com SPIN, cross-sell, fechamento e "Não fechou"; checklist; quiz; Obrigado;
  - as notas do apresentador em todo slide;
  - 16:9, Arial, cores dos originais e corpo de 12 pt ou mais.
- 8 slides de exemplo de Mecânica Básica, gerados pelo script, com códigos e OFEREÇA JUNTO tirados da base (o script para se algum código não existir).
- Sugestões S1 a S12, explicadas no guia:
  - S1: Arial;
  - S2: tirar a coluna "Estoque" e o "estoque nas 7 filiais", porque o número envelhece;
  - S3: números pela base;
  - S4: 3 aberturas em todos;
  - S5: notas padrão;
  - S6: corpo com 12 pt ou mais;
  - S7: datas das normas API;
  - S8: um treinamento remete ao outro;
  - S9: PDF de apoio;
  - S10: o verde;
  - S11: a versão da base nas notas;
  - S12: "uso interno" no rodapé.
- A proposta de módulos dos 11 novos e dos 3 atualizados está na seção 5 do guia.
- UX LIBERADO e marca LIBERADO (MC-0018, MC-0019 e MC-0020 fechados).

### (ii) Lista de melhorias do Portfólio geral
- catalogo_grafico/simulacoes/T-0032/MELHORIAS_PORTFOLIO.md, no anexo portfolios/: 23 itens, juntando o catalogo-grafico, o UX e a marca. Cada item tem o dono, o esforço, a prioridade e se precisa de simulação.
- Os de prioridade alta:
  1. modelo dos 7 portfólios;
  2. cada linha só com os veículos dela;
  3. foto certa nas caixas de filtro;
  4. tirar das aplicações o que não é veículo;
  5. cabeçalho com menos níveis;
  6. corte só com "…";
  7. glossário de "linha";
  8. aplicações agrupadas por montadora;
  9. especificações em 2 colunas;
  10. índice com página e link;
  11. página adaptável.

### (iii) Portfólios de amostra (catalogo-grafico)
- Branch catalogo-grafico/T-0032-portfolios, head a90cd1091394f2b62417a50948cc93014168ec65. Ele contém a T-0029 e gera pelo mesmo portfolio.py, com o filtro --linha. O Portfólio geral sai igual, pixel a pixel.
- Linha Autocenter: 24 páginas, 19 produtos e 1.893 itens. Só Linha Leve, com Filtração, Palhetas, Suspensão, Freio, Lubrificantes e Baterias (3a). Caminhões e máquinas saem pela regra nova.
- Linha Baterias: 6 páginas, 47 itens (Linha Leve e Linha Pesada), com a tabela "Baterias da Linha Leve · 38 itens".
- Índice dos outros 5:
  - Linha Leve: 44 páginas;
  - Linha Pesada: 28;
  - Linha Moto: 11;
  - Linha Lubrificantes: 12;
  - Linha Acessórios: 7.
- UX e marca: os ajustes que pediram foram aplicados (MC-0021 e os 4 do UX).

## Para a fila (sem segurar nada)
- catalogo-dados:
  - o HC26 (Etios) marcado só PESADA;
  - "PUTSMEISTER", "Iveco S-WAY", "Mwm" e "API sljaso MA" (p74), que vêm da base;
  - as Amperagens 75AE-LP-18 e 40D-MXWF-15, que não batem com o Ah;
  - "Ca +25c" e "12v";
  - os 2 textos de MOTIVO para a mesma causa na VEICULOS;
  - o RD-0546 (2 linhas de docstring);
  - o PAF1582, que ainda é "LEVE E PESADA" por causa da "Expert Cargo".

## Perguntas ao Alexandre (copiar o bloco)
```
T-0029 · Portfólio final
1) O Portfólio de 87 páginas: selo NOVIDADE 2026, ProActive/Shiftease, Linha Pesada só com veículos pesados (regra nova: voltam máquinas e caminhões; saem Focus, V40, 300C, vans) e modelos cortados sempre com "…": a) aprovado, pode gravar a entrega  b) quero ajuste (diga qual)

T-0032 · Padrão de treinamento
2) O padrão e os 8 slides de exemplo de Mecânica Básica: a) aprovado, com as sugestões S1 a S9 e S11  b) quero ajuste (diga qual)
3) S10, o verde dos treinamentos: a) manter o #59BA61, o verde do logo (a marca recomenda)  b) passar ao #62BB47 do site
4) S12, "uso interno" no rodapé dos treinamentos: a) sim (a marca recomenda)  b) não

T-0032 · Portfólios
5) A lista de 23 melhorias do Portfólio geral: a) aprovar todas para o Passo 2  b) só as de prioridade alta (1 a 11)  c) quero escolher (diga quais)
6) Autocenter e Baterias como modelo dos 7 portfólios: a) aprovado  b) quero ajuste (diga qual)
7) Nome: a) "Linha Baterias" (a marca recomenda)  b) "Linha Bateria"
8) Autocenter: a) o Óleo Hidráulico entra e os químicos (aditivo de radiador e fluido DOT) não, como na simulação  b) os dois entram  c) nenhum dos dois entra
9) Linha Lubrificantes inclui os químicos e a Água Desmineralizada: a) sim, como na simulação  b) não
10) Linha Acessórios, palhetas da Leve e da Pesada: a) 2 páginas, como na simulação  b) 1 página
11) A tabela das baterias mostra o código BAP (é a única página do Portfólio com código): a) sim  b) não
12) "preço acessível" no "Quem somos": a) trocar por "bom custo-benefício" (a marca recomenda)  b) manter
13) Contato da contracapa dos 8 portfólios: a) o seu, como hoje  b) um canal comercial da empresa (diga qual)  c) o vendedor de cada linha
14) Contagem na capa: a) "19 produtos · 1.893 itens" (como na simulação)  b) "19 linhas de produtos"
15) Fotos das caixas de filtro de óleo, combustível e cabine (hoje a caixa do filtro de ar aparece em 8 páginas): a) existem, vou mandar  b) não existem, fica sem foto de caixa
```
