---
id: R-20261126-222007-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-26T22:20:07+00:00
---
# T-0040: piloto por referência cruzada bloqueado pelo proxy da nuvem (0 de 10)

O piloto testou 10 códigos (catalogo-dados/T-0040-lista, 67760bc, dados/T-0040/piloto_referencia.csv) e achou 0 anos. O motivo não é falta de dado: o proxy da sessão na nuvem barra (403) todos os sites com ano.
- Fabricantes: Tecfil, NGK, Nakata, AutoImpact, 3RHO, Rinaldi, Bosch, Mahle, Wega, SKF, Fras-le, Cofap, Sabo, Timken, Schaeffler.
- Outros: TecDoc, Fraga, Google, Bing, DuckDuckGo, Wikipédia, Mercado Livre.
Nenhum ano foi inventado: as células ficaram vazias, com o motivo anotado.

Para o Alexandre decidir:
(a) Fazer a pesquisa por referência cruzada na mesma sessão local que vai consultar a Fraga, no computador dele, onde esses sites abrem. A estimativa é de 1 a 3 min por código, sem medição, o que dá 35 a 105 h para os 2.145 códigos. Esse tempo cai bastante se a pesquisa for agrupada por referência.
(b) Liberar no ambiente da nuvem os hosts dos catálogos dos fabricantes, só nomes exatos. Eu faço o pedido pela ferramenta de ambiente, e o Alexandre aprova ou recusa num cartão. Há um risco: muitos desses catálogos são aplicativos em JavaScript e podem não responder bem sem navegador.

Continuam abertas as 5 decisões do recado anterior: as linhas duvidosas, as que só têm ano final, o ano solto, o 'em produção' e os universais.
