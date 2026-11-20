# T-0017 · v19 da base unificada: SIMULAÇÃO (catalogo-dados)

20/11/2026, Manaus. **Nada foi gravado na base**: não há versão nova, commit nem push.
- **Fonte:** `dados/BASE_BAP_UNIFICADA_PRODUTOS_BAP.xlsx` do worktree `wt-v19-sim` (7cca5bb), que é a v18. O sha256 é `2bfac384…9d9b`, igual no começo e no fim.
- **Decisões que valem aqui:**
  - R-20261120-154200-alexandre, item 1;
  - R-20261120-182200-alexandre, "2) a" (a varredura do OFERECA_JUNTO);
  - o "ano solto = a partir de" do R-20261120-132230 (só no JUH70010).

## Arquivos (todos em `scratchpad/v19-sim/`)

| Arquivo | O que tem |
|---|---|
| `saida/SIMULACAO_v19_T-0017.xlsx` | A aba LEIA traz as contagens. Há uma aba por item, com CODIGO_BAP, COLUNA, ANTES, DEPOIS, REGRA, TIPO e PERGUNTA. O ANTES e o DEPOIS são do passo daquela regra. As outras abas: TODAS_AS_CELULAS (v18 → final), 11_PARES_OJ (os 2.933 pares, com a coluna "SEM VEÍCULO EM COMUM"), FICA_DE_FORA e LOG_CORRECOES_PREVISTO (uma linha por código) |
| `saida/numeros.json`, `saida/efeito_site.json`, `saida/mudancas.json`, `saida/oj_pares.json` | Os números e as listas |
| `ferramentas/simular_v19.py` (cópia em `saida/`) | Refaz tudo em cerca de 11 s: `python3 -I simular_v19.py <base.xlsx> <saida> <oj_pares.json>`. Só lê a base |
| `ferramentas/oj.js`, `efeito.js`, `aplic_site.js` | A varredura do OFERECA_JUNTO e a medida do site. Usam o mesmo código de tela do `site/app.js` (linhasAplic, linhasVeiculos e restoAplicacao) |
| `site_antes/`, `site_depois/` | O `produtos.json` gerado pelo `gerar_site.py` do worktree, antes e depois. Os dois rodaram sem `[PARADO]` |

- A cópia da base simulada e a cópia da v18 foram **apagadas** depois de medir, porque trazem os DADOS_ADICIONAIS internos.
- Para recriar as duas, rode o script.
- Na planilha, o preço antigo do histórico aparece como "BAP BOX USD [valor omitido]".

## Contagens

TIPO: AUTOMÁTICO = regra mecânica; CASO = correção proposta célula a célula; DÚVIDA = depende de uma pergunta Pn, e o DEPOIS é a recomendação.

| Item | Células | Produtos | Auto | Caso | Dúvida |
|---|---|---|---|---|---|
| 1 · modelo colado no ano ("1924–1979 até 2026") | 16 | 16 | 16 | | |
| 1 · ano sem veículo (sai) | 18 | 18 | | | 18 (P1) |
| 1 · uma linha por veículo ("X1 2.0 L 16V · 2011 até 2014" → "X1 2.0 L 16V 2011–2014") | 1.660 | 1.660 | 1.660 | | |
| 3 · marca que falta no começo do bloco | 86 | 86 | 45 | | 41 (P2) |
| 4 · casos (AMT7036, FCB6121, BIE20006, CIL8500) | 4 | 4 | | 2 | 2 (P4, P5) |
| 4 · formato do ano (4 dígitos, "–", ">") e a faixa falsa 1960–2026 | 483 | 461 | 448 | | 35 (P3) |
| 4 · caixa do modelo (Asx → ASX) e o "fi" perdido (Za ra → Zafira) | 57 | 57 | | 57 | |
| 5 · referência própria (BAPTA PN 170, BAP PN_2 99) | 269 | 269 | 269 | | |
| 6 · preço no histórico | 7 | 7 | | | 7 (P7) |
| 7 · referências repetidas | 3 | 3 | 2 | 1 | |
| 8 · TINKEN → TIMKEN | **0** | 0 | | | |
| 9 · "Nakata" → "NAKATA" | 161 | 161 | | | 161 (P8) |
| 10 · códigos estranhos | 80 | 80 | 1 | 9 | 70 (P9, P10, P11) |
| 11 · OFERECA_JUNTO sem o mesmo veículo | 224 | 224 | | | 224 (P13) |
| 12 · aplicação dentro da referência (KHC12428D e mais 160 KHC) | 161 | 161 | 159 | | 2 (P15) |
| 13 · datas sem o traço ("01/201112/2021") | 49 | 49 | 49 | | |
| 14 · JUH70010: o "(02/2009)" e o "SKF / PERFEC" (mais 30 JUH) | 32 | 31 | 31 | 1 | |

- **No total, depois de todos os passos:** 2.105 células da APLICACAO, 549 da REFERENCIAS_CRUZADAS e 224 da OFERECA_JUNTO.
  - São 2.878 células de 2.485 produtos.
- **Conferido célula a célula na cópia contra a v18:** só mudaram essas 3 colunas da aba PRODUTOS. Nenhuma outra aba, coluna ou linha mudou.

### Leitura de cada item
1. **As 15 linhas só de ano** estão todas tratadas. Medido no site, havia 46 linhas de 31 produtos com ano sem veículo (1 só de ano, 22 de modelo colado no ano e 23 de ano grudado num veículo que já tinha ano). Depois, são 0.
   - **Caminhões** (FAR6090, FAR6305, FAR6063, FAR6247, FSE6164 e mais FAR6044, FAR6156, FAR6166, FAR6224, FAR6135, FLU6009, FCB6028, FCB6040, ROL33215, PAF0019, PAF.0019): o 1º número é o modelo. "1924–1979 até 2026" vira "1924 (1979–2026)" e "F2000–2001 até 2026" vira "F2000 2001–2026". O modelo só de número leva o ano entre parênteses, para o site não ler o "1938" como ano. Isso resolve também o FCB6144, que fica com "1938 (até 2005)".
   - **CL16, CL19, CL21 e CL22** e mais 14 palhetas (BV, CL, MF), SFR30022 e TAX10543: o modelo se perdeu na importação e já faltava na v8. São 43 pedaços de ano sem veículo, e a proposta é tirá-los (P1).
     - Hoje o site cola esses anos no veículo de antes. No CL16, por exemplo, fica "UX 300h 2025> · 2009–2012".
     - O "· 2025 ;" do MF24 é um desses pedaços.
   - **BOR11081:** fica "2008 (2015>) · 208 (2013>) · Aircross (2010>) · C3 (2013>)". A marca não foi posta: o bloco é um só e não tem outro bloco com marca, por isso fica de fora do item 3.
2. **As 97 linhas ambíguas.** Não achei a lista dos 97. Pela regra do site, o "Outros veículos e detalhes" tem 9.617 linhas de 3.122 produtos e cai para 9.545 de 3.070 com a v19.
   - Os padrões que eu corrijo são o formato do ano e o ano junto do veículo ("Fiesta Rocam 2002 à 2014" → "2002–2014").
   - O resto não se resolve na APLICACAO: é versão que a VEICULOS não tem ("L200 Triton", "Uno Mille Economy") ou carroceria separada por "/" ("Corsa / Pick up", que pode ser Corsa e Corsa Pick-Up ou só a Pick-Up). Isso vai para a parte da VEICULOS, que **não está nesta simulação** (ver "Fica de fora").
3. **Marca que falta:** a marca vem da aba VEICULOS do produto e do dicionário MODELOS_VEICULO. Modelo sem marca entre dois da mesma marca fica com a marca dos vizinhos.
   - 36 produtos (palhetas) têm 196 modelos que não estão no dicionário: BYD Seal e Shark, JAC E-J7, Ferrari, Lamborghini... Esses modelos ficam num bloco sem marca, na mesma ordem (P2).
   - Em 43 produtos, o 1º bloco não é lista de veículos (pneus, ROL universais) e ficou como está.
   - **"Acessórios" repetido:** é a tela, não a base. CATEGORIA = SISTEMA em 175 produtos do site (ACESSÓRIOS 113, QUÍMICOS 38, LUBRIFICANTES 24). A base não muda (P12).
4. **Casos:**
   - AMT7036: "Corsa Hatch / Sedan (…) 04/2002–07/2012 · Meriva 08/2002–07/2012".
   - FCB6121: "Asia Motors", "Daihatsu" e "Mazda" viram começo de bloco.
   - BIE20006: desembaralhado (P4).
   - CIL8500: "Brava 2000–2003 · Doblô 2002>" (P5).
   - KAP11302: "Astra 01/1995–12/2012 , Monza 01/1982–12/1989, 01/1990–12/1996".
   - **INT16533 fica de fora:** as colunas estão misturadas e só a fonte resolve.
5. **Referência própria:** saem BAPTA PN (170) e BAP PN_2 (99), todas com o próprio código. O site já tirava essas referências.
   - Conferi o que é o BAPTA: o código é sempre o próprio código BAP. Aparece também no cabeçalho do "CADASTRO MASTER TERMINAL AXIAL (FORNECEDOR AMPRI)".
   - [SUPOSIÇÃO] É o código BAP na planilha do fornecedor, e não o código do fornecedor.
   - Os "BAP: PAF.nnnn" (103) **ficam**, pela decisão da T-0010 (P6).
6. **USD:** são 105 células, e nenhuma vai para o site.
   - 7 estão na REFERENCIAS_CRUZADAS, todas no histórico "| ANTERIOR" dos ROL30205, 30208, 6006-2RS, 6007-2RS, 6008-2RS, 6009-2RS e 6302-2RS, com "BAP BOX USD …" (P7).
   - 98 estão nos DADOS_ADICIONAIS, que são dado interno por desenho (a FICHA não leva). Ficam fora da v19.
   - Não sobra preço em outra coluna.
7. **Repetidas:**
   - BDA50024: o bloco vinha duas vezes. Fica uma vez, com as duas URBA (UB0639 e UB0638, que são diferentes).
   - KAP11245 e KAP11930: sai a 2ª SAMPEL.
   - No site, as 3 repetidas viram 0.
8. **TINKEN:** já não há nenhum "TINKEN" no trecho vivo, e o site mostra 0. Os 71 que sobram estão só no histórico "| ANTERIOR", e o histórico não se reescreve. Os 62 rótulos medidos antes eram do site sem o corte do RD-0199.
9. **Nakata:** os rótulos da base são NAKATA (1.351), NAKATA PN (965) e Nakata (161). A proposta é "NAKATA" (P8). No site, fica NAKATA 2.252 e Nakata 0.
10. **Códigos estranhos:**
    - CFR9006 (P9).
    - JUH70105: o "#N/A" sai.
    - SEH80042, 43, 48 e 49 e mais SEH80044, 45, 46, 56 e 57: "Nakata / Spicer" sem código sai, e "Axios LT…", "Ima AL-…" e "OEM …" viram "MARCA: código".
    - "Pruduct PN SUNRISE" nos 8 ROD (P10).
    - "NT", "NÃO TEM", "S/REF", "S/N" e "S/ refº original" saem de 61 células (P11).
    - **Os "1" e "10" ficam como estão:** são 2 das 154 linhas só de número do Terminal Axial, fora do site desde a v15 (T-0007), e a T-0007 decidiu manter o texto.
11. **OFERECA_JUNTO:** 2.933 pares no site.
    - 100 pares (de 79 produtos) não têm nenhuma marca e modelo em comum.
    - 173 pares (de 147 produtos) têm o modelo em comum, mas a cilindrada ou o ano não batem. É o caso do KHC12428D: o JUH70010 é Fiesta 1.0 e EcoSport 1.0/1.6 de 2009, e o KHC é EcoSport 2.0 e Fiesta 1.6 16V de 2012–2017.
    - **No total, 273 pares de 224 produtos.**
    - Os outros pares: 1.987 compatíveis, 156 universais, 443 sem veículo separado para comparar e 74 com o item fora do site.
    - **Proposta (P13):** trocar por um item do mesmo PRODUTO (ou da mesma FAMILIA) com o mesmo veículo, ou tirar quando não há um.
      - 126 produtos só com troca, 43 com troca e item tirado, 55 só com item tirado.
      - Em 15 produtos o campo fica vazio.
      - No KHC12428D: o JUH70010 vira JUH70153 (Fiesta 1.6 2012–2018) e o JUH70179 sai. Uma junta do Civic 1.8 2007–2012 (JUH70184) pode entrar como complemento: está na P13.
12. **KHC12428D e mais 160 KHC:** o "APLICAÇÃO REVISADA (Conforme catálogo NAKATA).: …" sai da referência, porque a APLICACAO já tem o mesmo texto.
    - Em 2 produtos, a APLICACAO não cita todos os modelos (P15).
13. **Datas sem o traço:** 49 células.
14. **JUH70010:** fica "Fiesta 1.0 02/2009> / … / Focus 1.6 06/2009>".
    - "SKF / PERFEC PN: VKJA…" vira "SKF: VKJA…" no JUH70010 e em mais 30 JUH (o VKJA é da SKF).
    - Os outros 96 produtos com ano solto "(MM/AAAA)" (192 vezes) não mudam aqui.

## Efeito no site (gerar_site.py do worktree, cópia fora do dados/)

| | Antes (v18) | Depois (v19 simulada) |
|---|---|---|
| Produtos | 4.419 | 4.419 |
| Produtos com "ve" | 3.618 | 3.618 |
| Linhas da aplicação com ano sem veículo | 46 (31 produtos) | **0** |
| "Outros veículos e detalhes" | 9.617 linhas, 3.122 produtos | 9.545 linhas, 3.070 produtos |
| Referências | 12.321 (4.252 produtos) | 12.203 (4.244 produtos) |
| Rótulo sem marca | 218 | 167 |
| Repetidas | 3 | 0 |

- **Mudam no site:**
  - a aplicação de 2.071 produtos;
  - as referências de 273 produtos: saem 316 e entram 201, que são as mesmas reescritas ("SKF: VKJA…", "AXIOS: LT…");
  - o "Leve também" de 224 produtos.
- **Ficam sem referência os 8 ROD** (o SUNRISE era a única).
- A TRAVA não parou nenhuma vez.

## Perguntas ao Alexandre (cada uma com a recomendação)
- **P1 · Ano sem veículo (43 pedaços, 18 produtos):**
  - a) tirar [recomendo: o modelo se perdeu desde a v8, e hoje o ano aparece no veículo errado];
  - b) deixar;
  - c) pedir a fonte (catalogofraga).
- **P2 · Modelo sem marca no dicionário (36 produtos, 196 modelos):**
  - a) deixar num bloco sem marca, na ordem [recomendo];
  - b) eu completo o dicionário (BYD, JAC, Ferrari...) numa v20.
- **P3 · "1960–2026" (35 células):** é o "todos os anos" disfarçado.
  - a) tirar e deixar o veículo sem ano [recomendo];
  - b) deixar.
- **P4 · BIE20006:**
  - a) a proposta da planilha, em que sai o "–2007>" sem veículo e o "/20" [recomendo];
  - b) pedir a fonte.
- **P5 · CIL8500:**
  - a) "Brava 2000–2003 · Doblô 2002>", os anos na ordem dos veículos [recomendo];
  - b) deixar como dúvida.
- **P6 · "BAP: PAF.nnnn" (103):**
  - a) fica na base, porque o site já não mostra e é a decisão da T-0010 [recomendo];
  - b) tirar.
- **P7 · "BAP BOX USD" no histórico (7):**
  - a) tirar só o preço, e o resto do histórico fica [recomendo];
  - b) deixar, porque a base é interna.
- **P8 · Caixa da marca:**
  - a) "NAKATA" na base [recomendo; é como estão quase todos os rótulos, e o jeito de mostrar fica com o site];
  - b) "Nakata";
  - c) deixar misturado.
- **P9 · CFR9006:**
  - a) "SCHULZ: 816.5028-0", com o 815 no histórico [recomendo; a família toda é 816.50xx e a correção já estava no texto];
  - b) deixar o 815.
- **P10 · "Pruduct PN SUNRISE" (8 ROD):**
  - a) tirar [recomendo; SUNRISE parece a fábrica das rodas, e fornecedor não aparece];
  - b) virar "SUNRISE: código", se for marca de mercado.
- **P11 · "NT", "NÃO TEM", "S/REF" (61):**
  - a) tirar [recomendo];
  - b) deixar.
- **P12 · "Acessórios" repetido:**
  - a) a tela mostra uma etiqueta só quando CATEGORIA = SISTEMA (web-site), e a base não muda [recomendo];
  - b) trocar o SISTEMA de 175 produtos (decisão de taxonomia).
- **P13 · OFERECA_JUNTO (224 produtos):**
  - a) trocar quando há um item compatível e tirar quando não há [recomendo];
  - b) só tirar;
  - c) trocar e também complementar (ex.: a junta do Civic JUH70184 no KHC12428D).
  - Das 169 trocas, 119 (em 119 produtos) não têm a cilindrada e o ano para conferir; recomendo que o vendedor revise essas.
- **P15 · Aplicação na referência sem o modelo na APLICACAO (2):**
  - a) tirar da referência e acrescentar o que falta na APLICACAO [recomendo];
  - b) só tirar.
- **Extra · AUTOIMPACT** (palhetas, 99 "Linha AUTOIMPACT" nos DADOS_ADICIONAIS e a referência "AUTOIMPACT PN" no site): parece o fornecedor das palhetas. Se for, precisa sair do site pela regra 1. É uma pergunta nova; não mexi.

## Fica de fora (e por quê)
- **A parte da VEICULOS da v19 não está nesta simulação:** a coluna CILINDRADA, o ANO_INICIO e o ANO_FIM preenchidos, uma linha por veículo e o ano duvidoso marcado (R-132200 e R-132230).
  - A especificação da T-0017 ainda a lista para a v19, e é ela que resolve o "L200 Triton" e o "Corsa / Pick up".
  - Proponho uma simulação à parte (v19b ou v20), em cerca de 1h15.
- INT16533 (só pela fonte).
- O ano solto "(MM/AAAA)" fora do JUH70010: são 192 vezes.
- 71 "TINKEN" no histórico.
- 98 células com USD nos DADOS_ADICIONAIS.
- Os 154 Terminais Axiais só de número.
- Achados para depois: "JARBOOOS", "JARBOOSO" e "JARBOOSS" (TRW JARB000x, com letra O no lugar do zero), as cores "ROSA", "VERDE" e "AZUL" e o "1L" nas referências dos RAD250xx, os "CROSS FARJ" com quebra de linha nos SCE140xx e o "Expedibor W-…" sem dois-pontos nos BOR.

## Formato (regra 6)
**O formato não muda:** as abas e as colunas são as mesmas, e as 5 primeiras colunas da PRODUTOS ficam como estão.
- Muda o conteúdo da APLICACAO, da REFERENCIAS_CRUZADAS e da OFERECA_JUNTO.
- O texto da aplicação fica com um veículo por pedaço ("Modelo AAAA–AAAA") e a marca no começo de cada bloco.
- A BAP Central lê esses campos como texto. Não precisa de aviso de formato, mas vale um aviso de conteúdo.
- Se a parte da VEICULOS entrar, aí muda o formato (coluna CILINDRADA nova) e o aviso é obrigatório.

## Na gravação (depois do "aprovado")
- Antes de gravar, copio a base para `dados/versoes/BASE_BAP_UNIFICADA_PRODUTOS_BAP_v19.xlsx`.
  - O script vai em `dados/scripts/base_v19.py`, com a função comum dos base_vNN (RD-0041).
- O LOG_CORRECOES ganha uma linha por código, cerca de 2.485, com o item, a T-0017 e a data. A aba LOG_CORRECOES_PREVISTO mostra como fica.
- O que foi digitado fica:
  - só as células da lista mudam;
  - o histórico "| ANTERIOR" não se reescreve (fora o preço, se a P7 for "a");
  - a conferência é célula a célula contra a v18, como nesta simulação.
- Depois:
  - atualizo o LEIA-ME;
  - o web-site roda o `scripts/gerar_site.py`;
  - o testes confere.
