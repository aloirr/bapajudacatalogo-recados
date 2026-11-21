# T-0017 · v21 da base unificada: SIMULAÇÃO (catalogo-dados)

21/11/2026, Manaus. **Nada foi gravado na base**: não há versão nova, commit nem push.
- **Fonte:** a v20 do main (e1d9f59), no worktree `wt-v21`. O sha256 é `4372f449…d24b`, igual ao da `versoes/…_v20.xlsx`, no começo e no fim.
- **Pedido:** R-20261120-211200-alexandre ("porque para amanha?"), com os 11 itens passados pelo gerente.
- **Decisões que valem aqui:** a V4a e a V7b da v20 (ano solto = a partir de; ano com mês duvidoso fica marcado), a P1 e a P8 da v19 (o ano sem veículo sai; rótulo da marca em maiúsculas) e o item 4 do R-20261120-185600 (ano de variante vai para simulação).

## Arquivos

| Arquivo | O que tem |
|---|---|
| `SIMULACAO_v21_T-0017.xlsx` | Abas: **LEIA** (contagens), **uma aba por item** (01 a 11, mais 07b e 10b), **TODAS_AS_CELULAS** (v20 → final) e **LOG_CORRECOES_PREVISTO** (945 linhas, uma por código e aba). Colunas: CODIGO_BAP, ABA, COLUNA, ANTES, DEPOIS, REGRA, TIPO, PERGUNTA |
| `scratchpad/v21-sim/ferramentas/` | `carregar.py` (lê a base **sem** os DADOS_ADICIONAIS), `antigas.py` (só APLICACAO e referências da v8, v18 e v19), `variante.cjs` (mede o item 9 com o `site/app.js` do worktree) e `simular_v21.py` (refaz tudo; só lê) |

- Na planilha, o fornecedor sai como "[fornecedor omitido]". Não há preço nem estoque.
- As cópias intermediárias da base foram apagadas depois de medir. Para refazer, rode os 4 scripts na ordem.

TIPO: AUTOMÁTICO = regra mecânica; CASO = correção célula a célula; DÚVIDA = depende da pergunta Pn, e o DEPOIS é a recomendação; INFORMAÇÃO = sem mudança.

## Contagens

| Item | Ocorrências | Células | Auto | Caso | Dúvida |
|---|---|---|---|---|---|
| 1 · faixa fechada com ">", modelo colado no ano, 2 dígitos | 24 | 15 | 3 | 10 | 3 (P1, P2) |
| 2 · " - nan" | 18 | 17 | | | 17 (P3) |
| 3 · MF21 (marcas e Bosch) | 2 | 2 (APLICACAO e referência) | | 2 | (P4) |
| 3 · anos soltos do MF21 e do MF22 | **0** | 0 (já saíram na v19, P1) | | | |
| 4 · sem ano no fim (FAG6317, FAC6108) | 2 | 2 | | | 2 (P5) |
| 4 · "AAAA até" sem o ano final (achado a mais) | 50 | 19 | | | 19 (P6) |
| 5 · linhas ou veículos iguais repetidos | 126 | 18 | 18 | | |
| 6 · ano solto por quebra de linha | 57 | 10 | 10 | | |
| 6 · veículo quebrado no meio ("(510⏎CV)") e aviso de página | 32 + 6 | 15 | 9 | 6 | |
| 7 · duas marcas no mesmo trecho ("Cofap:", "Marca Ref. NAKATA:") | 87 | 87 | | | 87 (P7) |
| 7b · "RT#:" dentro da referência NAKATA (achado a mais) | 246 | 246 | | | 246 (P8) |
| 8 · atributo repetido no mesmo veículo | 16 | 16 | 16 | | |
| 9 · ano de variante (linhas da VEICULOS) | 617 | 617 em 468 produtos | | | 617 (P9) |
| 10 · V7 JUH70010 | 4 | 4 linhas da VEICULOS | | | 4 (P10) |
| 10 · V8 "X1" lido de "M14 x 1,5" | 3 | 3 linhas da VEICULOS | | | 3 (P11) |
| 10 · V8 veículos que faltam na VEICULOS | 50 | 50 linhas novas em 32 produtos | | | 50 (P12) |
| 11 · linhas falsas das Cruzetas | 3 | 3 linhas da PRODUTOS | | | 3 (P13) |

- **No total:** 105 células da APLICACAO e 334 da REFERENCIAS_CRUZADAS (PRODUTOS); 627 células e 50 linhas novas na VEICULOS; 3 linhas que saem da PRODUTOS.
- **Só mudam** APLICACAO e REFERENCIAS_CRUZADAS na PRODUTOS, e ANO_DUVIDA, SITUACAO e MOTIVO na VEICULOS. As outras colunas e abas não mudam.
- **Efeito no site (item 7), medido com o `refs_de` do worktree:** os trechos com 2 marcas caem de 333 para 0.

### O que sai de texto digitado (dito aqui, um por um)
- **Item 2:** o " - nan" (18).
- **Item 4:** o " - DE" do FAG6317 e o "em Diante" do FAC6108. O "até" dos 50 vira ">".
- **Item 5:** 126 repetições, **só as idênticas**: a 1ª vez fica. O FSE6167 tem a lista inteira duas vezes (92 linhas).
- **Item 6:** "Contnua..." (FSE6215) e "..continuação" (5 BAN), que são o aviso de página do PDF de origem.
- **Item 8:** 16 atributos repetidos em seguida.
- **Item 11:** as 3 linhas falsas. O LOG guarda o conteúdo inteiro de cada uma.

### Leitura de cada item
1. **Faixa fechada com ">" e anos colados.** Procurei 4 formas: "AAAA–AAAA>", 8 dígitos colados, ">-" e "M/AA>".
   - **Peugeot 2008** (BV11, BV12, MF16): o modelo colou no ano desde a v8 ("2008–20142019" é o 2008 de 2014 a 2019). Fica "2008 (2014–2019) · 2008 (2025>)", com o modelo só de número e o ano entre parênteses, como o "1924 (1979–2026)" da v19. É o caso do BV12 e do MF16 "2008–2025>".
   - **Modelo de caminhão:**
     - PAF0116 e PAF.0116: "Axor 1933–2005>" vira "Axor 1933 (2005>)";
     - CRUSPL250: "19382000>" vira "1938 (2000>)";
     - POL1648 e POL1705: "19381999–2006" vira "1938 (1999–2006)";
     - POL1705: "194403/2005" vira "1944 (03/2005)".
   - **INT16506:** "(20092013)" vira "(2009–2013)", e "(20132019)" vira "(2013–2019)".
   - **KAC11931:** fica "NISSAN - Kicks 2016> · March 2011> · Versa 2011>".
   - **PAF0635 e PAF.0635:** o HYUNDAI Coupe "3/02>" vira "03/2002>" (3 vezes em cada).
   - **Não muda:** o FLU6441 "MERCEDES-BENZ 1938 - 1998>" já está certo (o 1938 é o modelo).
2. **" - nan":** são 18 em 17 interruptores (INT). A marca fica e o "nan" sai: "AGRALE - nan ; CBT - Tratores" vira "AGRALE ; CBT - Tratores".
3. **MF21:**
   - As marcas foram trocadas na v19, pelo dicionário. Fortwo vira SMART, GR Supra vira TOYOTA e Boxter vai para PORSCHE. CLS e GLB voltam para o bloco MB.
   - "BOSCH: 397016728" vira "BOSCH: 3397016728", como no MF22.
   - **Os anos soltos do MF21 ("· 2011> ·") e do MF22 ("· 2019> · 2011> ·") já não existem na v20.** Saíram na v19 (P1 aprovada). O PDF que os mostrava era da v18.
   - A VEICULOS do MF21 não tem o Fortwo nem o GR Supra: entram no P12.
4. **Sem ano no fim:**
   - FAG6317 e FAC6108 já vieram assim da v8: o ano se perdeu na origem.
   - **Achado a mais:** 50 "AAAA até" sem o ano final, em 19 filtros ("Ducato Maxicargo … 2018 até"). O site não os lê como faixa (PR #54).
5. **Linhas repetidas:**
   - FSE6167 (92 repetidas), FUR6445 (6), FAR6531, FCB6328, FCB6451, FAC6349, FCB6273, PAF0104, PAF.0104, PAF0498S, PAF.0498S, ABS4511, ABS4523, ABS4638, BV10, FLU6009, FSE6164 e POL1693.
   - O veículo só conta como repetido quando está inteiro (tem nome e ano, e o pedaço de antes fecha com ano). "Fox · (Teves) 2010> · Gol · (Teves) 2010>" fica como está.
   - **Atenção:** no PAF0104 e no PAF0498S, a repetição é o número do modelo que se perdeu ("LO-2002>", "Boxer Série 2005>"). O texto que fica é o mesmo, sem a cópia.
6. **Ano solto por quebra de linha:** são os 57, em 10 filtros pesados (DAF, Scania, VW Golf). O ano volta para o veículo: "P-7 -⏎2021–2024" vira "P-7 - 2021–2024".
   - **A mais:** 32 quebras no meio do veículo ("(510⏎CV) - 2015–2018", "METÁLICA⏎4X2 12.0…") e 6 avisos de página.
   - O item 5 roda depois deste: sem a junção, as linhas "CV) - 2015–2018" pareceriam repetidas.
7. **Duas marcas no mesmo trecho:** são 87 (81 "Cofap:" e 6 "Marca Ref. NAKATA:"). Hoje o site mostra "NAKATA: NKJ479, Cofap: KJD01207" como um código só da NAKATA.
   - **A mais:** 246 TER têm "NAKATA PN: N1011, RT#: RTL84684". O "#" faz o mesmo efeito.
8. **Atributo repetido:** são 16 (o gerente contou ~11): 15 AMT ("exc. Classic · exc. Classic", "Diesel · Diesel", "4x4 · 4x4", "2.0 · 2.0") e o TRI90024 ("Aut. · Aut."). Já vinham assim na v8.
9. **Ano de variante:** medi com o `app.js` do worktree.
   - De 12.148 linhas da tabela, 5.267 vão pelo caminho de 1 faixa, e 2.457 delas não têm a entrada pura.
   - Dessas, **617 linhas (468 produtos, os "~480")** têm uma variante entre o modelo e o ano: "Ecosport **4x2** 2003–2012", "Triton **4x4 3.2/3.5**", "Fiesta **Rocam**", "Corsa **/ Pick up**".
   - As outras 1.840 são detalhe depois do ano ("Diant.", "D/T") ou texto que o site não separa, e ficam de fora.
   - **Não mudam nem o texto nem o ano.** Só se marca na VEICULOS (ANO_DUVIDA) que a faixa é da variante. Como mostrar isso fica para o web-site.
10. **V7 e V8:**
    - **JUH70010:** os pares do "Leve também" (KHC12869 e KHC12909) **não** têm 2002–2009 (têm 1999–2006, 2000–2013, 2003–2007...). Pela V7b, não há prova para trocar, e o ano fica marcado como duvidoso.
    - **V8, "X1" lido de rosca:** são 3 linhas ainda "separado" (TER558662 "M30 x 1,5", TER5599615 e TER5599616 "M14 x 1,5"). As outras 3 já estavam duvidoso.
    - **V8, Renault 12/19/21 lidos de data:** as 80 linhas já estão duvidoso desde a v18. As 3 "separado" restantes são de verdade ("Renault 12 ( Todos )", "R-21 2.0 8V").
    - **V8, linhas que faltam:** das 55 da lista da v20, 7 não entram (Renault de data, "aro 19/21" das câmaras). Entram 48 e mais o Fortwo e o GR Supra do MF21. O "HONDA NX" vira LEXUS NX.
11. **Linhas falsas:** "Veículo", "HYUNDAI" e "KIA MOTORS" são **3 linhas da aba PRODUTOS**, com código = aplicação = o texto do cabeçalho de um bloco da planilha de origem.
    - Não têm referência nem veículo, e estão com NO_CATALOGO_DIGITAL = NÃO.
    - Não estão no site, mas o PDF Digital as imprime (pág. 107).

## Perguntas ao Alexandre (o DEPOIS da planilha é a recomendação)
- **P1 · ELE1076 e ELE1079, "HRV 1.8 16V 2015–20162017":**
  - a) "2015–2017" [**recomendo**];
  - b) "2015–2016 · 2017".
- **P2 · SCE14002, "LS 1630 1929–19321934 LS1941":**
  - a) são modelos MB, "LS 1630 1929 · 1932 · 1934 LS1941" [**recomendo**: não há ano nesse texto];
  - b) deixar.
- **P3 · " - nan" (18):**
  - a) a marca fica e o "nan" sai [**recomendo**];
  - b) sai o bloco inteiro ("AGRALE - nan").
- **P4 · MF21, "Cooper S ; 2 Lugares 2012>":**
  - a) "Cooper S 2 Lugares 2012>" [**recomendo**];
  - b) "Cooper S · 2 Lugares 2012>", com o 1º sem ano.
- **P5 · FAG6317 ("17-220 8.3 L 12V - DE") e FAC6108 ("Eclipse Cross 1.5 L 16V · em Diante"):**
  - a) tirar o "- DE" e o "em Diante", e o veículo fica sem ano [**recomendo**: o ano não existe desde a v8];
  - b) FAC6108 com "2018>" [SUPOSIÇÃO: o ano de lançamento no Brasil];
  - c) deixar.
- **P6 · "AAAA até" sem o ano final (50 em 19 filtros):**
  - a) "AAAA>", em diante [**recomendo**, como a V4a];
  - b) só o ano "AAAA";
  - c) deixar.
  - Atenção: o FCB6190 tem "de 1960 até" (Komatsu) e fica "1960>".
- **P7 · "Cofap:" e "Marca Ref. NAKATA:" (87):**
  - a) "COFAP:" e "NAKATA:" [**recomendo**, como a P8 da v19];
  - b) trocar a "," por ";".
- **P8 · "RT#:" (246 TER):**
  - a) "RT:" [**recomendo**: o PDF já mostra "RT"];
  - b) deixar, e o site continua mostrando o RT como código da NAKATA.
- **P9 · Ano de variante (617 linhas da VEICULOS, 468 produtos):**
  - a) marcar o ANO_DUVIDA com a variante ("a faixa 2003–2012 é da variante 'EcoSport 4x2'…"). A tela fica para o web-site, que pode mostrar o "—" ou "2003–2012 (4x2)" [**recomendo**: não muda texto nem ano];
  - b) pôr a variante na VERSAO (mexe no filtro "Meu veículo");
  - c) deixar.
- **P10 · JUH70010 "02/2009>":**
  - a) marcar o ANO_DUVIDA nas 4 linhas e manter o texto [**recomendo**: o par não prova 2002–2009];
  - b) "2002–2009" no texto e na VEICULOS;
  - c) deixar.
- **P11 · "X1" lido de rosca (3 linhas):**
  - a) passam a duvidoso, com o motivo [**recomendo**, como a V5a];
  - b) deixar.
- **P12 · As 50 linhas que faltam na VEICULOS (32 produtos):**
  - a) entram como duvidoso, com o motivo "conferir", e não aparecem no site [**recomendo**];
  - b) entram como separado, sem ano, e passam a filtrar;
  - c) não entram.
- **P13 · As 3 linhas falsas das Cruzetas:**
  - a) saem da aba PRODUTOS, e o LOG guarda o conteúdo inteiro [**recomendo**: não são produto];
  - b) ficam, e o catalogo-grafico passa a pular as linhas com NO_CATALOGO_DIGITAL = NÃO.

Os itens sem pergunta (o resto do 1, o 3, o 5, o 6 e o 8) entram com o "aprovado".

## Formato e aviso à BAP Central
- **Não muda o formato:** não há coluna nova nem aba nova, e as 5 primeiras colunas da PRODUTOS ficam iguais.
- **Muda o número de linhas:** com a P13a, a PRODUTOS perde 3 linhas ("Veículo", "HYUNDAI", "KIA MOTORS"); com a P12, a VEICULOS ganha até 50.
- O `gerente-projetos` avisa o `po` antes da gravação.

## Fica de fora (e por quê)
- **Ano com 2 dígitos sem ">"** (973 vezes em 407 produtos, quase todos caixa de direção: "Marajó 73/93", "Punto 07/17"):
  - não dá para saber se é MM/AA ou AA/AA;
  - o site já lê as duas formas.
- **Outras marcas trocadas pela v19, como no MF21:** BV11 "PEUGEOT - Classe 2008–2015" e BV12 "HONDA - NX 200t… UX 300h", que é Lexus. Vão para uma v22 com simulação. O MF22 continua sem marca (P2 da v19).
- **CRUSPL250:** o resto do texto, com os separadores "+" e o "Cursos" em vez de "Cursor", precisa da fonte.

## Na gravação (depois do "aprovado")
- `dados/scripts/base_v21.py`, com o `base_comum.rodar()`: aplica as respostas e compara a v20 com a v21 célula a célula.
- A v21 sai em `dados/versoes/`, com as linhas no LOG_CORRECOES (945 previstas: 105 APLICACAO, 334 referências, 468 ANO_DUVIDA, 32 VEICULO_NOVO, 3 duvidoso e 3 linhas removidas) e o bloco no LEIA-ME.
- Depois, o `web-site` roda o `gerar_site.py` e o `testes` confere.
