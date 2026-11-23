---
id: R-20261123-140946-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0029
responde_a: R-20261123-135656-po
encerra: false
contrato: null
criado_em: 2026-11-23T14:09:46+00:00
---
# Simulações da T-0029, T-0030 e T-0031 para o Alexandre (9 perguntas)

As 3 simulações da rodada R-20261123-135656-po estão prontas. Nada foi para o main e nada foi gravado na base.
Anexos: bapajudacatalogo-recados, recados/anexos/T-0029/sim/, T-0030/sim/ e T-0031/sim/ (commit bdf59c0), cada um com um LEIA-ME.md.

## T-0029 · Portfólio 2027 e siglas (catalogo-grafico)
- Branch: catalogo-grafico/T-0029-portfolio-2027
- Head: 61ac7ed2b769ab4230a10e81ca21080d6a3a4bb4
- Mudam 26 das 88 páginas, e a contagem continua 88:
  - capa: "PORTFÓLIO DE PRODUTOS 2027" e "Novembro de 2026";
  - p03: "conforme o Catálogo BAP 2027", e a frase sem a seta "→", que a fonte não tem: "Dentro da linha: sistema do veículo, família e produto.";
  - contracapa: 2027;
  - selo "NOVIDADE 2027" em 19 páginas;
  - siglas: "Vw"→"VW" 3 vezes e "Gm"→"GM" 5 vezes (p21, 34, 42 e 67), pela lista de siglas que o gerador já tem;
  - "effitech"→"Effitech" na p81.
- O A4, o Completo Digital e a Linha Moto saem iguais ao main, pixel a pixel e no texto, a 150 ppi.
- Sem preço e sem estoque.
- Pareceres: UX LIBERADO e marca LIBERADO, os dois sem ajuste.
  - UX: branch designer-ux/T-0029-T-0030-simulacao, head b33d54d.
  - Marca: branch design-de-marca/T-0029-T-0030-simulacao, head 07f3b0d.
- Efeito colateral aceito pelo UX: na p67, "GM" é mais largo, então a lista de modelos corta um pouco antes, agora com "…".

## T-0030 · Rótulos da ficha da bateria (web-site; MC-0016)
- Branch: web-site/T-0030-rotulos-bateria
- Head: 3da35c1e8ed67bb5f1d80b203c3101cc9d4b851f
- O que muda: na ficha, "C20(ah)" vira "Ah" e "Cca-18°" vira "CCA".
  - Muda só na tela (site/app.js) e vale também para o "+ Detalhes" e para a ficha impressa.
  - O rótulo vem do nome da chave na base, mas não foi preciso mexer em dados/.
  - A FICHA e a TRAVA ficaram intactas: o gerar_site.py não foi mexido, e o produtos.json não muda.
- Testes:
  - gerar_site: sem [PARADO];
  - testar_site: 0 falhas, com Amperagem 13 opções, CCA 5 faixas e "60ah" 8 itens, iguais aos de antes;
  - prints de 1366 e 390 px, em antes e depois, da 60D-EFB-24 e da 72D-EFB-24.
- Pareceres: UX LIBERADO e marca LIBERADO.
- Para a fila, sem segurar a entrega:
  - "Amperagem" e "Ah" repetem o número na mesma ficha. Em 2 baterias os valores são diferentes: 75AE-LP-18 (Amperagem 40, Ah 75) e 40D-MXWF-15 (Amperagem 45, Ah 40). Vão para o catalogo-dados conferir;
  - "Ca +25c" → "CA (+25 °C)" e "12v" → "12 V".

## T-0031 · Aplicações suspeitas da Linha Pesada (catalogo-dados)
A conferência foi feita na base v27, só lendo. A planilha SIMULACAO_T-0031_aplicacoes_linha_pesada.xlsx tem as abas ANTES_E_DEPOIS, CONFERIDO_SEM_MUDANCA, MESMA_CAUSA_FORA_DO_PEDIDO e EFEITO_NOS_PDFS. Não tem preço nem estoque.
- **"Doblo" nas Bieletas: BIE20042.** A aplicação está certa e a LINHA está errada.
  - As referências cruzadas da própria base são todas de linha leve: Fiat 46836399, Nakata N96003, Cofap BTC03201, TRW JTSB0036 e Axios.
  - A causa: a regra antiga do taxo.py leu o "exc. Cargo" do Doblò como Ford Cargo.
  - Proposta: LINHA PESADA → LEVE. Na aba VEICULOS, a linha "FORD Cargo" passa de `separado` a `duvidoso`. Hoje quem filtra "Ford Cargo" no site vê a bieleta do Doblò.
- **"Ford Focus" e "Volvo V40" nos Filtros de Cabine: FAC6260.** Segundo a fonte (tabela de filtros 2026, Tecfil ACP213), está certo.
  - A LINHA é LEVE E PESADA porque o mesmo filtro serve também o VW Delivery.
  - Quem mostra o Focus e o V40 na Linha Pesada é o Portfólio (p62), que lista todos os veículos dos itens LEVE E PESADA. A base não muda.
  - Não deu para conferir no catálogo Tecfil, porque não há internet aqui. O FAC6227 (Tecfil ACP206) também diz Focus 2.0 2014–2015.
- **Fora do pedido, mesma causa (aba separada, só com aprovação):**
  - BOR11030: LINHA PESADA → LEVE, e "FORD Cargo" vai para `duvidoso`;
  - AMT7084, AMT7115, BAN9513 e BAN9516: LEVE E PESADA → LEVE.
- **Efeito nos PDFs:** só no Portfólio.
  - Com o BIE20042, a p46 (Pesada, Bieletas) some, porque fica com menos de 3 itens. O Portfólio passa a 87 páginas.
  - Com os 5 da mesma causa, a p45 (Pesada, Amortecedores) cai para 3 itens.
  - O catalogo-grafico regera junto com a T-0029. Com a aprovação, a entrega final da T-0029 sai com 87 páginas e não com 88, com as páginas novas mostradas antes.
- O catálogo de 2027 (A4, Digital e Moto) e o Kit Filtros não mudam.
- O site muda quando o web-site regerar o JSON.
- Com o "aprovado", a base ganha a versão v28, a linha no LOG_CORRECOES e os campos digitados conservados. O formato da base não muda.

## Perguntas ao Alexandre (copiar o bloco)
```
T-0029 · Portfólio 2027 e siglas
1) Mês da capa: a) "Novembro de 2026", o mês da entrega (a marca recomenda: o 2027 é o ano do material, como no Catálogo BAP 2027)  b) "Janeiro de 2027"
2) Selo de novidade: a) voltar a "NOVIDADE 2026", o ano de lançamento, igual ao "LANÇAMENTO 2026" do A4 e do Digital (a marca recomenda)  b) "NOVIDADE 2027" só no Portfólio, como na simulação  c) 2027 em todos os materiais (o A4 e o Digital mudam junto, com simulação própria)
3) Nomes das linhas "proactive" e "shiftease" (7 vezes cada no Portfólio): a) corrigir já para "ProActive" e "Shiftease", só no Portfólio, mostrando as páginas antes da entrega (a marca recomenda)  b) deixar para depois
4) Simulação da T-0029: a) aprovado, com as respostas 1 a 3  b) quero ajuste (diga qual)

T-0030 · Rótulos da ficha da bateria
5) "Ah" e "CCA" na ficha: a) aprovado  b) quero ajuste (diga qual)

T-0031 · Aplicações da Linha Pesada
6) BIE20042 (bieleta do Doblò) passa a LEVE, e sai do filtro "Ford Cargo" do site: a) aprovado  b) não
7) Os 5 itens da mesma causa (BOR11030, AMT7084, AMT7115, BAN9513 e BAN9516) passam a LEVE: a) aprovado  b) não
8) FAC6260 (Focus e V40 no filtro de cabine que também serve o VW Delivery): a) mantém como está  b) conferir no catálogo Tecfil antes de decidir
9) No Portfólio, a Linha Pesada mostra só os veículos pesados dos itens "LEVE E PESADA" (tira o Focus e o V40 da p62): a) sim, com simulação  b) não, fica como está
```
