---
id: R-20261122-113658-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0027
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T11:36:58+00:00
---
# Autorização de merge da T-0027: #152 (33678a7), #153 (70a3f68) e #154 (67ccc9e); RD-0526 fora

Peço a autorização de merge dos 3 PRs da T-0027 (squash, expectedHeadSha). Eles entram juntos: os 2 pareceres apontam um para o outro e para a entrega.

1) PR #152: entrega (gerador e 3 PDFs com os mesmos nomes; dono catalogo-grafico).
   Head: 33678a7f8dc3f53e02dfacf2bffe3303197f25ae.
   - Testes PASSOU (07:30): gerar_site sem [PARADO]; testar_site OK; 23 testes do gerador; pixel a pixel independente, só as 7 páginas; regerado igual; login 21/21 e os 7 downloads com sha256 igual; 0 "1 itens".
   - UX e marca LIBERADO na entrega final.
   - revisor LIBERADO (07:31); corretor LIBERADO (07:32).
   - CI verde. verificar OK.
2) PR #153: parecer de marca (dono design-de-marca).
   Head: 70a3f68d0e4e2c81e3acf90082069e7b2e76f52c.
   - revisor e corretor LIBERADO (07:32), com a hora certa e o RD-0524 e o RD-0525 corrigidos.
   - CI verde.
3) PR #154: parecer de UX (dono designer-ux).
   Head: 67ccc9e2979033eb3a06761e72b3dc218dc7e4bd.
   - revisor e corretor LIBERADO (07:32), com o RD-0522 e o RD-0523 corrigidos.
   - CI verde.

Pergunta (corretor, RD-0526, baixa): a regra do singular continua copiada em 2 geradores fora dos 3 PDFs (lista_aplicacoes_site.py:126 e kitfiltros/kit.py:235). O texto que sai está certo e nenhuma página muda.
   a) fica fora do #152 e entra junto do RD do Portfólio (2a), na fila do Alexandre, com o plural() num módulo comum ► recomendado (corretor e GP: mexer agora mudaria o diff já aprovado na simulação);
   b) entra agora na T-0027.

Depois do merge: o registro da T-0027 (tarefa e quadro, com o RD do Portfólio e o RD-0526 na fila do Alexandre) e o catálogo de RD da T-0027 (RD-0521 a RD-0526).
