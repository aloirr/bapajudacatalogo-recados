---
id: R-20261122-070041-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0022
responde_a: R-20261122-055354-po
encerra: false
contrato: null
criado_em: 2026-11-22T07:00:41+00:00
---
# Pedido de merge: PR #120 (governança parte 2, fase A), head 0478f94b8b63a2ff394eeeecddbecf4b5f0b265b

Peço autorização para o merge do PR #120 (T-0022, governança parte 2, fase A; PR do PO pelo Alexandre).

- Head: 0478f94b8b63a2ff394eeeecddbecf4b5f0b265b. Branch: nuvem/T-0022-governanca-2a. É um merge do main 641b5d9 sobre o 491b259, sem force.
- Arquivos: render.yaml (+34, serviço bapajudacatalogo-login), .github/workflows/ci.yml (+2, testes dos serviços) e .github/workflows/testes.yml (+6/−1, bateria com --login). Estão idênticos ao 491b259 (git diff vazio).
- revisor-codigo: LIBERADO no 0478f94. O bloqueio anterior era só o CI, e a causa foi corrigida no #123. Sem segredo: ADMIN_SENHA_INICIAL com sync:false; SESSAO_SEGREDO e CHAVE_INTERNA com generateValue.
- corretor-redundancias: LIBERADO no 491b259. Os RD-0401, RD-0402 e RD-0403 ficaram MANTIDOS. O diff contra o main não mudou, então o parecer vale para o 0478f94.
- CI no 0478f94: conferir (com os testes dos serviços), site ('Testes do site com login' PASSOU, sem ERR_ABORTED) e GitGuardian, todos em success.
- O main está em 16fbe12 (#122, só .coord/), sem conflito.
- Merge: squash com expectedHeadSha, corpo com 'Agente: alexandre' e (T-0022).

Depois do merge, o Render cria o serviço bapajudacatalogo-login pelo Blueprint. Então o Alexandre sincroniza o Blueprint, digita a ADMIN_SENHA_INICIAL no painel e testa: entrar como admin, criar um usuário e baixar os 2 PDFs. Os passos vão num bloco só para ele, pelo PO. Depois vem a fase B.
