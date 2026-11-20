# T-0011 · Simulação: busca palavra por palavra e início com 2 abas

Base: main e2ee181 (JSON da v16, 4.419 produtos). "Antes" = app.js do main. "Depois" = app.js do branch web-site/T-0011-busca-palavras.
Prints em 1366×768 e 390×844 (`antes-*.png` e `depois-*.png`). Em todos: scrollWidth ≤ largura, 1 `h1`, console sem erro.

## Prints

| nº | tela | antes | depois |
|---|---|---|---|
| 01 | início | 3 abas (Busca geral, Veículo, Código da peça) | 2 abas (Busca por código, descrição ou aplicação; Busca por placa) |
| 02 | início, aba placa (seta para a direita) | não existe | "Em breve", sem chamar nada, sem os botões |
| 03 | AMORTECEDOR GOL 2007 KYB 441126 | 0 | 1 (AMT7005) |
| 04 | AMORTECEDOR GOL 2015 KYB 441126 | 0 | 1 (AMT7005), aviso "casam com 4 de 5 palavras. Não casou: 2015" |
| 05 | gol amortecedor | 25 (com Golf) | 16 (sem Golf) |
| 06 | MAHLE 33000 (texto literal) | 0 | 2 mais próximos: AMT7179 (GP33000) e FAC6000 (Mahle LA633) |
| 07 | link antigo #/busca?mo=VOLKSWAGEN&modelo=Gol&ano=2018 | 46 | vira q=Volkswagen Gol 2018: 49 |
| 08 | link antigo #/busca?cod=TRW 16900255S | 2 | vira q=TRW 16900255S: 2 (CXD13062, CXD13067) |
| 09 | CL14 | 1 (CL14) | 1 (CL14 em 1º) |

## Exemplos do Alexandre

Não há na base um produto com Mahle e 33000 juntos (Mahle só no FAC6000, filtro de cabine; 33000 só no AMT7179, COFAP GP33000, Fiorino).
Equivalente real: **AMT7005**, amortecedor dianteiro, "VW - Gol / Saveiro · 01/1980–12/2009", referência **KYB 441126**.

| busca | resultado |
|---|---|
| AMORTECEDOR GOL 2007 KYB 441126 | 1: AMT7005 (casa as 5) |
| gol 2007 amortecedor 441126 kyb | igual |
| amortecedor gol 2007 kyb 441126 | igual |
| AMORTECEDOR GOL 2015 KYB 441126 | 1 mais próximo: AMT7005 (4 de 5; falta 2015) |
| KYB 441126 | AMT7005 (marca do produto é BAP; KYB é a concorrente) |
| texto literal com MAHLE 33000 (as 4 formas) | 8 / 8 / 8 / 7 mais próximos, nunca vazio |
| MAHLE 33000 | 2 mais próximos (AMT7179 e FAC6000) |

Testes: `testes_resultado.txt` (43 de 43 passaram; script `testes_t0011.js`).

## Comparação com o main (comparacao.txt, script comparar.js)

436 buscas: 130 na busca geral, 30 da aba Código e 276 da aba Veículo (os 138 modelos da T-0008, sem ano e com 2018). Os links das abas antigas passam pelo redirecionamento.

- No total: 107 iguais, 118 só com a ordem nova e 211 com a lista mudada. A ordem muda porque agora o código exato vem 1º e depois o campo em que a palavra casou: descrição antes da aplicação.
- Aba Veículo sem ano (138 casos): 26 iguais, 76 só com a ordem nova e 36 que ganham itens (635 no total, nenhum sai). Ganham os produtos que trazem o modelo na descrição ou na referência (BDA50001 "BOMBA DE AGUA ... FIAT"). "Ka+" e "a b c d e f g h" davam 0 e agora mostram os mais próximos.
- Aba Veículo com 2018 (138 casos): 5 iguais, 9 só com a ordem nova e 124 que mudam, com 190 saídas e 715 entradas. O motivo é a leitura nova do ano:
  - entram as faixas que o main não lia, como "06/2008–12/2020" (AMT7002 e AMT7004 no Gol 2018), "2018 2021", "05-10" e "07/17";
  - saem as que o main não lia e deixava passar "sem ano", como "Parati ../08" (CXD13057), "Chevette 73/93" e "Ducato 01/97 - 12/09".
  - VOLKSWAGEN + Gol + 2018: 46 → 49 (entram AMT7002, AMT7004, FAC6241 e JUH70134; sai o CXD13057). Nenhum Golf.
- Busca geral (130 casos): 49 iguais, 33 só com a ordem nova e 48 que mudam. Saem:
  - os casos de "pedaço de palavra": Golf no "gol" (AMT7096 e AMT7357), "Fora de Estrada" no "strada" e "Gold Wing" no "gol";
  - "ka" (2.602 → 139), "up" (507 → 124), "l 200" (2.112 → 94) e "t cross" (307 → 32).
- Busca geral, o que entra:
  - os mais próximos, quando ninguém casa com tudo ("kit embreagem gol": 0 → 45);
  - conectivo ignorado ("amortecedor para gol": 10 → 16; "terminal de direcao": 255 → 398);
  - ano por faixa ("amortecedor 2007": 47 → 252).
- Aba Código (30 casos): 27 iguais e 3 que mudam: "TRW" sozinho traz as 509 com referência TRW (a marca casa com a concorrente), o EAN 7908680411297 traz o AMT7179, e "441126" traz também o POL1642 (pedaço de referência).

## Tempo

4.419 produtos. A função buscar foi medida no Chromium (Playwright), 5 vezes por busca: mediana entre 1,6 e 25 ms e maior tempo 38,7 ms, sempre abaixo de 50 ms.

| busca | mediana | maior |
|---|---|---|
| AMORTECEDOR GOL 2007 KYB 441126 | 17 ms | 27 ms |
| kit embreagem gol 1.6 2010 luk | 23 ms | 26 ms |
| a b c d e f g h i j | 25 ms | 26 ms |
| gol 2007 amortecedor 33000 mahle (390 px) | 18 ms | 38,7 ms |
| Volkswagen Gol 2018 | 8 ms | 8 ms |
| TRW 16900255S | 2 ms | 2 ms |

No Node, nas 436 buscas da comparação, a média é 5,9 ms e o maior tempo 26 ms.

## Sem os campos separados da aba Veículo: o que podia piorar e como ficou

1. **Montadora como filtro.** Agora a montadora é uma palavra, que casa com a montadora do produto (mo) ou com a aplicação. Entraram apelidos: VW = Volkswagen, GM e Chevy = Chevrolet, MB e Mercedes = Mercedes-Benz. Assim, "vw gol" acha o Gol de montadora VOLKSWAGEN.
2. **Ano "sem ano na aplicação, mostra".** Na aba Veículo, o produto sem ano na aplicação aparecia. Na busca nova, o ano só casa com produto sem ano quando outra palavra digitada casou com a aplicação dele (o modelo). Esse produto vai para o fim da lista, com nota 5. O ano sozinho ("2007") não traz quem não tem ano.
3. **Modelo com hífen.** O hífen entre letras vale como espaço, como na T-0008: "Space-Fox" = "Space Fox" e "T-Cross" = "T Cross". Com número, fica junto: "33-000" = "33000", "F-1000".
4. **Palavra do modelo em outro campo.** "Gol" casa também com a descrição e com a referência, como no BDA50001 ("... FIAT" na descrição). Para não virar pedaço de palavra, o começo de palavra (HOMOC → HOMOCINÉTICA) não vale para nome de veículo: palavra que está em pelo menos 5 vezes mais aplicações que descrições, como POLO, CORSA e GOL. Assim, POLO não vira POLOS.
5. **Sistema.** Saiu do formulário e continua nos filtros do resultado. O link antigo com si= mantém o sistema.
6. **Links antigos.** #/busca?mo=&modelo=&ano= e #/busca?cod= viram #/busca?q=... com location.replace, e o botão Voltar não repete o redirecionamento.

Não achei caso que ficou pior sem um ganho de precisão junto: comparei com o main e saem só Golf, "Fora de Estrada" e as faixas de ano que o main não lia.

## O que o testes precisa ajustar no scripts/testar_site.mjs (parte do navegador)

O `--sem-navegador` PASSOU. A parte do navegador para em `.abas button[data-aba="codigo"]`, porque a aba não existe mais. Trocas:

- o formulário da aba Código ("cxd-13062" + Enter) vira o campo q;
- o formulário da aba Veículo (select mo, modelo e ano) sai; fica a rota antiga, que redireciona;
- o teste de teclado "Enter na aba Veículo abre os campos" vira "seta para a direita abre a aba placa";
- as rotas #/busca?cod= e #/busca?mo=&modelo=&ano= continuam e podem ser testadas como redirecionamento;
- VOLKSWAGEN + Gol + 2018 passa de 46 para 49.
