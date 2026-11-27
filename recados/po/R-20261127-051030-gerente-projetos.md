---
id: R-20261127-051030-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: normal
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T05:10:30+00:00
---
# T-0040: os anos da Fraga não chegam ao site; v29 e site sendo preparados; decisão (a/b/c) para as 6h

O diagnóstico do web-site confirmou o problema: os anos da Fraga não chegam ao site.
- O gerar_site manda para o site só fabricante, modelo e versão de cada veículo. Os anos da VEICULOS não vão.
- O `an` que a T-0033 usa é por produto e sai da DADOS_ADICIONAIS, não da VEICULOS. Só 192 produtos têm `an`, e o BCE3001 e o CXD13062 não estão entre eles.
- No site simulado, a tabela do CXD13062 mostra as versões da Fraga com Ano "—". A busca Gol 2015 não traz o CXD13062, embora a Fraga diga 2008–2018.
- O site se contradiz no BCE3001 simulado:
  - a tabela ainda mostra Ka, Fiesta e Fiorino, porque lê o texto antigo da APLICACAO;
  - o filtro "Meu veículo" (Ford > Ka) já não traz o produto, porque usa só a VEICULOS.

Para fechar a T-0040 até as 6h, está sendo preparado em paralelo, sem nada no main:
1. **catalogo-dados**, branch catalogo-dados/T-0040-v29: a base v29 com a VEICULOS da Fraga, o arquivo em dados/versoes/, o LOG_CORRECOES com a autorização como "pendente" e o aviso à BAP Central sobre a ORIGEM "Fraga T-0040". O texto da APLICACAO NÃO é reescrito, porque é campo digitado.
2. **web-site**, branch web-site/T-0040-fraga:
   - o gerar_site leva ANO_INICIO e ANO_FIM em cada veículo, mais um sinal por produto que diz que os veículos vêm da Fraga. A ORIGEM em si não vai para o site;
   - no app.js, nesses produtos, a tabela, o filtro por veículo e a busca com ano usam só a VEICULOS (Fraga) e não leem mais o texto antigo;
   - nos outros produtos, nada muda;
   - o JSON cresce mais cerca de 8%, além dos +51% da simulação.

Decisão para o Alexandre às 6h, junto com o aprovado:
- (a) Recomendado: nos 3.909 códigos, o site mostra e busca só pela Fraga. O texto antigo da APLICACAO fica na base como está, porque é campo digitado conservado, mas deixa de valer na tela desses códigos. Exemplo: o BCE3001 deixa de aparecer para Ka, Fiesta e Fiorino.
- (b) Também reescrever o texto da APLICACAO dos 3.909 a partir da Fraga. Assim a impressão e a BAP Central ficam iguais à tela, mas o texto digitado se perde.
- (c) Manter a Fraga e o texto somados. Essa não recomendo: a tela e o filtro continuam se contradizendo.

Também para ele ver: a observação da Fraga vai para a Versão, por exemplo "EA111 VHT 1.6 L 8V SOHC L4 · COM FREIO ABS". São 542 versões assim.

Próximos marcos:
- os prints de antes e depois da simulação (testes);
- a v29 no branch;
- o site com os anos;
- as revisões;
- os PRs em rascunho.
