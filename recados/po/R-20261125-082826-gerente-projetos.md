---
id: R-20261125-082826-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0033
responde_a: R-20261125-060140-po
encerra: false
contrato: null
criado_em: 2026-11-25T08:28:26+00:00
---
# T-0033: simulação pronta (busca com ano + fim do 'Outros veículos e detalhes'), BCE3001 antes e depois, 4 perguntas

## Contexto
Simulação, sem merge. Prints antes e depois, em 1366 e 390:
https://github.com/aloirr/bapajudacatalogo/tree/testes/T-0033-busca-ano/testes/prints/T-0033
(branch testes/T-0033-busca-ano 6317471; tela web-site/T-0033-busca-ano e60061a)
- janela-BCE3001: antes com o bloco, depois sem.
- busca-polo-2026 e busca-BCE3001-polo-2026: a BCE3001 sai do Polo 2026.
- janela-JUH70013 e janela-ROL0015E: detalhes ('s/ ABS', 'Roda Dir/Esq') na coluna Versão.
- busca-TER5593103-onix-2021: peça com ano 2020–2023 continua aparecendo.

a) Busca por veículo COM ano: a peça só entra se o ano dela bater com o daquele modelo. '1996+' vale para 2026. Aplicação sem ano não entra.

## O que preciso / o que mudou
Busca

## Pronto quando
Antes | Depois |  | Polo 2026 | 56 | 24 |  | Gol 2010 | 103 | 45 |  | Strada 2020 | 100 | 63 |  | Onix 2018 | 74 | 44 |  | Ka 2015 | 79 | 49 |  | Escort 2000 | 37 | 21 | Nenhuma peça entra que antes não entrava. Uma conferência automática garante que nenhuma peça cujo texto dá o ano certo some (0 perdas).
A busca SEM ano não mudou (Polo: 121 = 121), nem a busca por código ou referência.

b) O bloco 'OUTROS VEÍCULOS E DETALHES' acabou nos 3.089 produtos que o tinham. O que só estava nele virou linha da tabela de aplicação (12.158 → 17.611 linhas). Detalhes como 's/ ABS' e 'Dianteiro' vão para a coluna Versão. A ficha impressa continua com o texto completo. A base NÃO mudou: o site lê o texto da APLICACAO.

BCE3001 depois:
- Ford: Escort em 4 linhas (a última 'Sedan 1997+'), Verona, Royale, Ka, Fiesta, Courier 1993+ e Versailes;
- Fiat: Fiorino MPI 1995–2004, Palio 1996+, Strada 1999+ e outros;
- VW: Polo sem ano, e assim fora do Polo 2026;
- Chevrolet: Corsa Sedan, Corsa Pick-Up 1996+ e Kadet 1996+.

Conferências:
- testes: PASSOU, 49 itens, 4 rodadas.
- No caminho apareceram e foram corrigidos dois problemas:
  - marcas inventadas ('General Motors', 'Fiat / Alfa Romeo', 'Motos'); agora só montadoras conhecidas;
  - peças que somiam da busca.
- designer-ux e design-de-marca: LIBERADO COM AJUSTES; os ajustes foram feitos.

Perguntas ao Alexandre (recomendação marcada):
1) Em 'Ka, Fiesta, Courier 1993+', o '1993+' vale para os três ou só para o Courier? Hoje vale só para o Courier, e Ka e Fiesta ficam sem ano (saem da busca com ano). a) só o Courier (recomendado, porque é o mais seguro para o cliente); b) os três.
2) A tela lê o texto livre da aplicação, e ainda há ~1.500 linhas com leitura imperfeita (ex.: 'Audi A1, Versão: Dolphin Plus 2025>' e vários caminhões Cargo colados na Versão). a) aprovar agora assim e abrir uma tarefa para o catalogo-dados passar os veículos do texto para a aba VEICULOS (v29, com simulação da base) (recomendado); b) só aprovar depois de arrumar a base.
3) A busca DIGITADA ('polo 2026' no campo de busca) ainda traz a BCE3001; a regra nova vale para a busca por veículo. a) deixar a busca digitada como está (recomendado); b) aplicar a regra também nela.
4) A busca por veículo SEM ano continua como hoje, mostrando tudo do modelo. a) sim (recomendado); b) outra regra.

[SUPOSIÇÕES] na simulação:
- 'após / a partir de / desde 2003' vale como '2003+';
- a busca com ano aceita o ano que o texto dá direto ao modelo, além da tabela.

Para a fila (catalogo-dados):
- grafias 'Versailes' e 'Kadet' (o certo é Versailles e Kadett);
- lâmpadas com 'Polo' no veículo por causa de '1 Polo' (polo elétrico).

Com o aprovado, sigo para revisor, corretor e PRs.
