---
id: R-20261122-070143-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: normal
tarefa: T-0022
responde_a: R-20261122-070059-po
encerra: true
contrato: null
criado_em: 2026-11-22T07:01:43+00:00
---
# #120 no main (582c38b): fase A da governança parte 2

PR #120 mergeado por squash com expectedHeadSha 0478f94b8b63a2ff394eeeecddbecf4b5f0b265b. Main: 582c38bb1090efe250674800adb0aeb3e314c1ac, com 'Agente: alexandre' e a autorização R-20261122-070059-po.

Agora é com você e o Alexandre:
1) Ele sincroniza o Blueprint no painel do Render. Aparece o serviço novo, bapajudacatalogo-login (Starter, com disco de 1 GB).
2) Digita a ADMIN_SENHA_INICIAL no painel. Sem ela, o serviço responde 503 e o /saude, 200.
3) Testa no ar: entrar como admin, trocar a senha obrigatória, criar um usuário e baixar os 2 PDFs.
O site atual e a placa não mudam nesta fase.

Depois do teste dele, vem a fase B: o endereço antigo redireciona; a placa ganha CATALOGO_URL, CHAVE_INTERNA e ORIGEM_PERMITIDA, mais o teste 'serviço fechado com a chave certa'; o CLAUDE.md; e o previews.generation, se o revisor confirmar.
Em paralelo, peço ao corretor o PR do catálogo de RD (RD-0401 a RD-0411) e faço o registro da T-0022 e da T-0023 no quadro.
