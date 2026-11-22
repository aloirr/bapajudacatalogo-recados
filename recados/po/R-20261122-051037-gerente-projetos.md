---
id: R-20261122-051037-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0022
responde_a: R-20261122-050959-po
encerra: false
contrato: null
criado_em: 2026-11-22T05:10:37+00:00
---
# #118 no main (008b9d7); pedido de autorização: PR #114 no 8e529f5 e depois PR #117 no eec6010

#118 no main: squash com expectedHeadSha 125272d → 008b9d73cd7ccb043156b4552f0649a14dc03895, 'Agente: integracao-placas'.

Ordem: primeiro o #114, depois o #117. Os dois foram conferidos sem conflito com o main 008b9d7 (git merge-tree).

1) PR #114 (telas do login, 'Agente: web-site'), head 8e529f5b0cdf74541db2be44a698d29afb43aff8, 14 arquivos só em site/. CI no head: conferir, site e GitGuardian em success. Revisões no 8e529f5: revisor-codigo LIBERADO; designer-ux LIBERADO (no 87ec078, e o 8e529f5 só muda impressão e tira código sem uso); design-de-marca LIBERADO; corretor-redundancias LIBERADO (RD-0352 a RD-0363 corrigidos). Bateria ponta a ponta PASSOU com o serviço do #118. FICHA, TRAVA e produtos.json iguais ao main. No site estático de hoje nada quebra: sem o serviço, o botão do canto não aparece. Merge: squash com expectedHeadSha 8e529f5…, 'T-0022: telas do login (entrar, trocar senha, botão do canto, Criar usuários e Catálogos em PDF) (T-0022)', 'Agente: web-site'.

2) PR #117 (bateria com login, 'Agente: testes'), head eec601035f18055e16294886874147f3004d9b63, 2 arquivos (testes/login.mjs e scripts/testar_site.mjs). CI no head: conferir, site e GitGuardian em success. Revisões no eec6010: revisor-codigo LIBERADO e corretor-redundancias LIBERADO (RD-0364 a RD-0374 corrigidos). O modo sem --login, que é o do CI, fica igual ao do main linha por linha. Merge: squash com expectedHeadSha eec6010…, 'T-0022: bateria de testes do site com login (--login e --comparar) (T-0022)', 'Agente: testes'.

Depois dos dois, mando o bloco da governança parte 2 (render.yaml e os 2 passos de CI).
