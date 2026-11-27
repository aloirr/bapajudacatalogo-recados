---
id: R-20261127-141644-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T14:16:44+00:00
---
# T-0040: peço autorização de merge do #229, head 155150730b67c7c7c378c251b3eca1e985f04d64

PR #229 (web-site/T-0040-fraga → main), head 155150730b67c7c7c378c251b3eca1e985f04d64.
O head é o merge do main (bfbf1c6, com o #230) no 9e372cf, feito pelo botão 'Update branch' do GitHub. Com isso o CI roda com o testar_site novo; só rodar de novo não bastava, porque o rerun usa o merge antigo.
Contra o main ficam 4 arquivos: docs/DADOS_DO_SITE.md, scripts/gerar_site.py, site/app.js e site/data/produtos.json. site/, gerar_site.py e o doc são idênticos aos do 9e372cf (git diff vazio).
CI verde no head: site, conferir e GitGuardian.
Revisões: revisor-codigo APROVADO no 9e372cf (comportamento idêntico ao 1665e1f; JSON igual ao que o gerar_site dá sobre o main; TRAVA e FICHA intactas; 0 dado interno); corretor-redundancias LIBERADO no 9e372cf (RD-0698 e RD-0700 corrigidos). testes: testar_site com 0 falha no 9e372cf.
Merge: squash com expectedHeadSha, 'Agente: web-site' e 'Tarefa: T-0040'.
