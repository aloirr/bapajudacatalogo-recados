---
id: R-20261127-061835-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: normal
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T06:18:35+00:00
---
# T-0040: PAUSA cumprida; ponto de retomada às 03:30

PAUSA cumprida: todos os agentes pararam, e o trabalho ficou salvo com commit e push.

Onde parou cada branch:
- #228, base v29: catalogo-dados/T-0040-v29, commit 24fd327. Revisor APROVADO e corretor LIBERADO, com a condição de conferir o head que o aprovar_v29.sh vai gerar.
- #229, site: web-site/T-0040-fraga, commit e054a2c. Os números e os prints de antes e depois sobre a v29 24fd327 já estão prontos. Faltam:
  - rodar de novo o testar_site;
  - corrigir a tabela, onde o "2016" do texto está entrando nas linhas Fox da Fraga ("2008, 2016");
  - a RD-0678, que é não repetir a linha sem versão na tabela.
- testes: testes/T-0040, commit 5fee056. Com a v29 24fd327, o gerar_site sai sem [PARADO] (4,5 MB) e o testar_site no site novo passa. Faltam o testar_site no main, a conferência da T-0033 e os prints finais.

Achados para resolver na retomada (web-site, e dado com o catalogo-dados):
- busca digitada sem produtos que a tabela mostra (POL1618 com Gol 2001+, TER5596023 com Strada 2008–2020);
- KAP11315 falha na conferência da T-0033;
- KTM não aparece na lista Marca;
- o BCE3001 não leva os 3 Escort da Fraga, porque a linha atual os absorveu;
- JUH70025 e SFR30017 ficam fora de "gol 2010".

Retomo às 03:30 de Manaus, a partir daqui.
