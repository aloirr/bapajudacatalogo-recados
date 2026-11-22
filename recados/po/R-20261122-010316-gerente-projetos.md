---
id: R-20261122-010316-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0017
responde_a: R-20261121-200058-alexandre
encerra: false
contrato: null
criado_em: 2026-11-22T01:03:16+00:00
---
# Simulação da v27: rolamentos, SCE14002, TER55227, TER5597056 e embreagens pesadas (6 perguntas)

# Simulação da base v27 (T-0017): 6 perguntas ao Alexandre

Simulação pronta. Nada foi gravado: a base continua a v26 e não há v27 em `dados/versoes/`.
- Branch `catalogo-dados/T-0017-v27-sim`, commit bb4de8d.
- Cópia nos anexos: `recados/anexos/T-0017/v27-sim/` (LEIA.md, SIMULACAO_v27_T-0017.xlsx com o antes e depois só das linhas que mudam, numeros_v27.json).

## O que muda (com as respostas recomendadas)
- 124 células em 124 códigos da PRODUTOS:
  - 108 no SISTEMA dos rolamentos (88 para TRANSMISSÃO, 20 para MOTOR);
  - 13 no DETALHE_CATALOGO das embreagens pesadas (RD-0293);
  - 3 na APLICACAO: SCE14002, que fecha o RD-0284, TER55227 e TER5597056.
- A VEICULOS não muda. O formato da base não muda. O LOG_CORRECOES ganha 124 linhas.
- "duvidoso": 5.120 antes e depois; nada novo marcado.
- "Leve também": não muda no site nem no PDF.
- No site mudam 124 produtos. Contagem por sistema: RODAGEM 460 → 352, TRANSMISSÃO 572 → 660, MOTOR 267 → 287.
- PDFs A4, Digital e Moto: as páginas não mudam, porque agrupam pelo PRODUTO. O Portfólio muda se for gerado de novo.

## Exemplos
- SCE14002: "LS 1630 · LS 1929 · LS 1932 · LS 1934 · LS 1941 · VW 16210 17240 1730 · 111693".
- EMB3400700639R: "395MM 18 estrias plato/disco/mancal · c/ platô, disco, rol. e mancal" → "395MM 18 estrias · c/ platô, disco, rol. e mancal".
- TER5597056: um bloco por veículo, com a posição como detalhe: "AUDI - Q7 2010–2019 · Diant. Esq. ; PORSCHE - Cayenne 2010–2019 · Diant. Esq. ; VW - Amarok 2010–2019 · Diant. Dir. ; VW - Touareg 2010–2019 · Diant. Esq.".
- TER55227: "…/ B1621 01/1970–06/2012 · Tractor · Diant.", com o ano junto da lista.

## Perguntas (recomendação do gerente em negrito)
1. Rolamentos de câmbio e diferencial: a) sistema novo "CÂMBIO E DIFERENCIAL" (13º sistema no site); **b) "TRANSMISSÃO", que já existe**.
2. Rolamento com mais de um uso no texto (54): **a) o sistema do uso citado primeiro (30 mudam, 24 ficam RODAGEM)**; b) todos ficam RODAGEM.
3. Ano do TER5597056: **a) 2010–2019 em cada um dos 4 veículos, como a VEICULOS já tem**; b) o ano só no Touareg, como hoje.
4. Lado do Amarok no TER5597056: **a) fica "Diant. Dir.", como no texto de origem**; b) passa a "Diant. Esq.", como os outros 3.
5. Embreagens pesadas, composição do kit repetida no DETALHE_CATALOGO (13 códigos): **a) tirar a repetição**; b) deixar. A mesma repetição no PDF vem do gerador; o catalogo-grafico corrige depois do #99, com simulação própria.
6. A v27 como simulada, com as respostas acima: **a) aprovar e gravar**; b) dizer o que muda.

## Fica de fora (decisão própria, se o Alexandre quiser)
- O TER55227 é terminal da alavanca do câmbio, mas está como "Terminais de Direção" no SISTEMA DIREÇÃO.
- CIL8546: a base v26 está certa (Parati e Santana 1983–2006). O "—" no ano do site vem do jeito de o site ler o texto. É correção do web-site, numa tarefa à parte.

## Depois do "aprovado"
- catalogo-dados grava a v27 (versão, LOG e README).
- web-site gera o JSON e atualiza o DADOS_DO_SITE.md e o comentário dos rolamentos no gerar_site.py.
- Revisões de sempre e a sua autorização de merge.
