# T-0017 · v27 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: **R-20261121-210229-po** (SCE14002, RD-0284; e, na mesma v27, o SISTEMA dos 194 rolamentos e os textos do TER55227 e do TER5597056) e **R-20261121-200058-alexandre**, item 4 (o SISTEMA dos rolamentos gravado na base, com simulação). O RD-0293 (embreagens pesadas) entrou por decisão do PO, passada pelo gerente.
- Base de partida: v26 do main 3d6a730 (sha256 `3a9f589d…2f2a`). A base e `dados/versoes/` não mudam até o "aprovado".
- Regra fixa (R-20261120-213300): nenhuma marca nova de ano incerto, e nenhum produto sai.

## 1. Contagem (com a recomendação: perguntas 1 b, 2 a, 3 a, 4 a, 6 a)
| O quê | Quantos |
|---|---|
| Células da PRODUTOS | 124, em 124 códigos: 108 SISTEMA (rolamentos), 13 DETALHE_CATALOGO (embreagens) e 3 APLICACAO (SCE14002, TER55227, TER5597056) |
| VEICULOS | nada muda (nenhuma célula, nenhuma linha nova) |
| Células com a marca de revisão | 5.120 → 5.120 |
| LOG_CORRECOES | 124 linhas, uma por célula |
| Site (gerar_site numa cópia) | 4.419 nos dois; mudam 124 produtos: 108 no `si`, 11 no `ss` (sai, porque fica igual ao `si`), 13 no `de` e 3 no `a` |
| "Leve também" | **não muda**, no site (0 produtos) nem no PDF (0 itens, nas 4 combinações das perguntas 1 e 2) |

**Conferência:** a base simulada foi comparada célula a célula com a v26 pelo `base_comum.comparar`: 124 mudaram, de 124 esperadas; diferenças fora do permitido: 0. As abas, as colunas e as 5 primeiras colunas da PRODUTOS (BAP Ajuda e BAP Central) ficam iguais; o formato não muda.

## 2. SISTEMA dos rolamentos
O sistema proposto é o que o site e o PDF **já leem do texto** (o `gerar_site.sistemas_de`: DESCRICAO, DETALHE_CATALOGO e a POSICAO dos DADOS_ADICIONAIS), o mesmo que decide o "Leve também" desde o #97.

| Leitura do texto hoje | Rolamentos |
|---|---|
| só RODAGEM (roda, cubo) ou nada no texto | 62 (não mudam) |
| só câmbio e diferencial | 67 |
| só transmissão (cardã, semi-eixo, embreagem) | 6 |
| só motor (alternador, polia, tensor) | 5 |
| mais de um sistema | 54 |

Quantos mudam em cada resposta (os outros ficam RODAGEM):
| Resposta | Mudam | Para |
|---|---|---|
| **1 b, 2 a (recomendada)** | **108** | **TRANSMISSÃO 88, MOTOR 20** |
| 1 b, 2 b | 84 | TRANSMISSÃO 79, MOTOR 5 |
| 1 a, 2 a | 108 | CÂMBIO E DIFERENCIAL 77, TRANSMISSÃO 11, MOTOR 20 |
| 1 a, 2 b | 78 | CÂMBIO E DIFERENCIAL 67, TRANSMISSÃO 6, MOTOR 5 |

- Na recomendada, os 54 de mais de um sistema: 30 mudam pelo uso citado primeiro (12 de alternador e roda → MOTOR; 3 de alternador e câmbio de moto → MOTOR; 15 de câmbio, diferencial, cardã ou semi-eixo → TRANSMISSÃO) e 24 ficam RODAGEM (o texto cita a roda primeiro).
- **"Leve também" igual:** o site e o PDF continuam lendo o sistema do rolamento pelo texto; o SISTEMA da base só vale quando o texto não diz nada, e esses 62 não mudam. Conferido no `produtos.json` (o `ss`, ou o `si`, de cada produto) e pela leitura do PDF (`G.sistemas_de` com os campos da base).
- **O que muda no site:** o filtro e os números por sistema da página inicial (RODAGEM 460 → 352, TRANSMISSÃO 572 → 660, MOTOR 267 → 287), a trilha da página do produto ("Transmissão › Cubos e Rolamentos") e a busca pela palavra do sistema. A FAMILIA (CUBOS E ROLAMENTOS) e o PRODUTO não mudam.
- **PDFs:** o A4, o Digital e a Linha Moto agrupam pelo PRODUTO (`taxo.py`), por isso as páginas não mudam. O Portfólio (`portfolio.py`) agrupa pelo SISTEMA da base: se for gerado de novo, os rolamentos aparecem em TRANSMISSÃO e em MOTOR (aviso ao catalogo-grafico).
- A aba TAXONOMIA da base continua com "Rolamentos → RODAGEM" (a regra geral); ela não muda nesta v27.

## 3. Textos (APLICACAO)
| Código | Hoje | Depois |
|---|---|---|
| SCE14002 | Servo Embreagem MB LS 1630 · LS 1929 · LS 1932 · LS 1934 · LS1941 VW 16210 17240 1730 · 111693 | LS 1630 · LS 1929 · LS 1932 · LS 1934 · LS 1941 · VW 16210 17240 1730 · 111693 |
| TER55227 | FORD/VW - 1113 Cargo / … / B1618 / B1621 **·** 01/1970–06/2012 Tractor · Diant. | FORD/VW - 1113 Cargo / … / B1618 / B1621 01/1970–06/2012 **·** Tractor · Diant. |
| TER5597056 | AUDI - Q7 · Diant Esq / Porsche Cayenne · Diant Esq / Volkswagen Amarok · Diant Dir / Volkswagen Touareg Diant Esq / 01/2010–12/2019 | AUDI - Q7 2010–2019 · Diant. Esq. ; PORSCHE - Cayenne 2010–2019 · Diant. Esq. ; VW - Amarok 2010–2019 · Diant. Dir. ; VW - Touareg 2010–2019 · Diant. Esq. |

- **SCE14002:** o texto do R-20261121-210229-po. O "LS1941" ganha o espaço, as linhas LS ficam em ordem e o "Servo Embreagem MB" do começo sai. O nome da peça está na DESCRICAO e no PRODUTO, e a marca está na VEICULOS (MERCEDES-BENZ LS). Fecha o RD-0284.
- **TER55227** (apontado na simulação do B11, `outros-veiculos.csv`): hoje o site lê "01/1970–06/2012 Tractor" como outro veículo, com o "Diant." de detalhe. Na proposta, o ano fica junto da lista de caminhões (como a VEICULOS já tem: Cargo 1970–2012), e "Tractor" e "Diant." viram detalhes dela. Nenhum veículo, ano ou posição entra nem sai.
- **TER5597056** (apontado no LEIA-ME da simulação do B11): hoje o site lê "Diant Esq / Porsche Cayenne" como detalhe do Q7. Na proposta, há um bloco por veículo (" ; "), com a marca no começo, e a posição vai como detalhe ("Diant. Esq.", como no catálogo). Os 4 veículos são os da VEICULOS, que já tem 2010–2019 nos 4. A opção b da pergunta 3 está na aba TER5597056_OPCOES.
- [SUPOSIÇÃO] A leitura do site depois da mudança ("…B1621 01/1970–06/2012: Tractor · Diant." e "Q7 2010–2019: Diant. Esq.") segue a regra do B11 (`docs/DADOS_DO_SITE.md`). O `testes` confere nos prints depois de gravar.

## 3b. Embreagens pesadas, DETALHE_CATALOGO (RD-0293)
- Nas 13 embreagens remanufaturadas abaixo, o DETALHE_CATALOGO diz a composição do kit duas vezes. Fica uma vez, na forma completa; o resto da célula não muda.
  - Exemplo, EMB3400700639R: "395MM 18 estrias plato/disco/mancal · c/ platô, disco, rol. e mancal" → "395MM 18 estrias · c/ platô, disco, rol. e mancal".
  - Os 13: EMB3400700639R, EMB6085R, EMB6126R, EMB6236R, EMB6261R, EMB6343R, EMB6453R, EMB6535R, EMB6550R, EMB6585R, EMB6635R, EMB6852R (que tem "plato/disco mancal") e EMB827483R.
- No site, muda a linha "Detalhe" da ficha técnica desses 13.
- **PDF:** a repetição do A4 (p. 20) e do Digital (p. 112-113) não vem deste campo. Ela é montada pelo gerador: o "plato/disco/mancal" é o fim da DESCRICAO e o "c/ platô, disco, rol. e mancal" é acrescentado pelo `detalhe.essencial`. Essa parte é corrigida pelo `catalogo-grafico`, na mesma rodada de simulação. Lá entra também o EMB1047071R, que repete só no PDF.

## 4. CIL8546 (só conferido; nada muda)
- A v26 está certa: na VEICULOS, a Parati e o Santana estão com 1983–2006, "separado", e os dois aparecem no `ve` do site.
- O "—" na coluna Ano do site vem do site: ele ainda lê o ano do texto da aplicação, e não da VEICULOS. No texto, o ano está num pedaço separado por "|" ("Parati, Quantum, Santana… | 1983 a 2006"), longe do modelo. A correção é do `web-site` (ler o ano da VEICULOS), fora desta v27.

## 5. Fica de fora
- O DESCRICAO do SCE14002 ("MBB", "VWC"): é a 2ª das 5 colunas lidas pelo BAP Ajuda e pela BAP Central, e vem do cadastro.
- A VEICULOS dos VW do TER55227 (12-140, 14-150, 16-170…): o pedido é só o texto.
- O PRODUTO e o SISTEMA do TER55227 ("Terminais de Direção", DIREÇÃO), que é terminal da alavanca do câmbio: trocar de sistema pede decisão própria do Alexandre.

## 6. Perguntas ao Alexandre
1. Nome do sistema dos rolamentos de câmbio e diferencial (77 com a pergunta 2 a; 67 com a 2 b):
   - a) um sistema novo, **CÂMBIO E DIFERENCIAL** (a página inicial do site ganha um 13º sistema);
   - b) **TRANSMISSÃO**, que já existe e já reúne câmbio e embreagem. **Recomendo b**: os 12 sistemas da casa ficam como estão, e o "Leve também" fica igual nas duas.
2. Rolamento com mais de um uso no texto (54; ex.: ROL6202-2RS, "alternador e cubos de roda de motos"):
   - a) o SISTEMA do uso citado primeiro no texto (30 mudam e 24 ficam RODAGEM) — **recomendo a**;
   - b) fica RODAGEM, como hoje (só os 140 de um uso mudam).
3. TER5597056, o ano:
   - a) 2010–2019 em cada um dos 4 veículos, como a VEICULOS já tem — **recomendo a**;
   - b) o ano só no fim, no Touareg ("01/2010–12/2019"), como no texto de hoje.
4. TER5597056, o Amarok está "Diant. Dir." e os outros 3 "Diant. Esq." (o DETALHE diz "Direção esq."):
   - a) fica "Diant. Dir.", como no texto de origem (não há outra fonte) — **recomendo a**;
   - b) passa a "Diant. Esq.", como os outros 3.
5. A v27 como simulada (SCE14002, TER55227 e as respostas de 1 a 4 e 6):
   - a) aprovar e gravar;
   - b) diga o que muda.
6. Embreagens pesadas, a composição do kit repetida no DETALHE_CATALOGO (13 códigos, RD-0293):
   - a) tirar a repetição e ficar só com "c/ platô, disco, rol. e mancal" — **recomendo a**;
   - b) deixar como está.

## Arquivos
- `SIMULACAO_v27_T-0017.xlsx`: LEIA; ANTES_DEPOIS (as 124 células, com a recomendação); ROLAMENTOS (os 108 que mudam em alguma resposta, com o sistema lido e o SISTEMA em cada resposta das perguntas 1 e 2); TER5597056_OPCOES; SITE (cada chave do `produtos.json` que muda); LOG_CORRECOES_PREVISTO.
- `numeros_v27.json`: as contagens.
- `simular_v27.py`: o script. Ele só lê, usa o `base_comum` e o `gerar_site.sistemas_de` (sem cópia) e roda o `scripts/gerar_site.py` numa cópia. Uso, na raiz do repositório: `python3 -I dados/simulacoes/T-0017/v27/simular_v27.py dados/versoes/BASE_BAP_UNIFICADA_PRODUTOS_BAP_v26.xlsx dados/simulacoes/T-0017/v27`.
