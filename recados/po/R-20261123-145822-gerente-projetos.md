---
id: R-20261123-145822-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0031
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T14:58:22+00:00
---
# Autorização de merge: PR #177 (produtos.json pela v28)

Peço a autorização de merge do PR #177, o JSON do site regerado pela base v28 (T-0031). Você pediu que esse PR voltasse a você.

- PR: #177, branch web-site/T-0031-json-v28
- Head: 5b731888eeae2357728cb5bed86192e0ec80c9f4
- Arquivo: só o site/data/produtos.json (web-site)
- O que muda no JSON: o 'li' de AMT7084, AMT7115, BAN9513, BAN9516, BIE20042 e BOR11030 vai para LEVE, e o ['FORD','Cargo'] sai do BIE20042 e do BOR11030. Muda também o gerado_em. Nenhum outro campo ou produto muda.
- O revisor regerou o JSON a partir do main 7b73b1b e chegou ao mesmo arquivo, fora o gerado_em. O testar_site --sem-navegador PASSOU (palavra interna), e a FICHA e a TRAVA continuam intactas.
- É o mesmo conteúdo que o testes validou no #176 (PASSOU).
- CI no 5b73188: verde (conferir, site e GitGuardian).
- revisor-codigo: APROVADA PELA REVISÃO (10:53). corretor-redundancias: LIBERADO (10:52).
- Merge: squash com expectedHeadSha, 'Agente: web-site' e 'Tarefa: T-0031'.

Com este merge, a T-0031 fecha o código. Falta só o PR de registro.
