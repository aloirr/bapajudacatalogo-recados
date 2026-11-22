---
id: R-20261122-040724-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0019
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T04:07:24+00:00
---
# Pedido de autorização de merge: PR #112 no eb65ede; aviso do GitGuardian no #113

# Pedido de autorização de merge: PR #112 no commit eb65ede423bba6d89cb13563948cf2a4b0382cbb (e um aviso sobre o #113)

## PR #112 (catálogo de redundâncias, 'Agente: corretor-redundancias')
- **Head:** eb65ede423bba6d89cb13563948cf2a4b0382cbb, sobre o main c9975a5. O main agora está em f9fcc35, com os PRs #110 e #111, que só mexem em `.coord/`, `.claude/` e `CLAUDE.md`. Não há conflito.
- **Arquivos:** só em `docs/qualidade/redundancias/`:
  - `CATALOGO.md`, com uma linha para cada achado de RD-0284 a RD-0349, sem número repetido nem buraco (o RD-0307 está marcado como pulado);
  - `T-0014.md`, `T-0019.md` e `T-0022.md`.
- **CI no head:** conferir, site e GitGuardian em success.
- **Revisões:**
  - revisor-codigo: LIBERADO no eb65ede (reteste), com as situações conferidas contra os merges #99, #101, #103, #104, #106, #107, #108 e #109;
  - o autor é o corretor-redundancias.
- **Depois do merge:** o RD-0326 e o RD-0331 a RD-0333 já podem passar a CORRIGIDO (#110 e #111 estão no main). Isso entra no próximo PR de pareceres.
- **Merge:** squash com expectedHeadSha eb65ede…, título "Redundâncias: pareceres da T-0014, T-0019 e T-0022 e catálogo de RD-0284 a RD-0349 (T-0019)" e o trailer 'Agente: corretor-redundancias'.

## Aviso: PR #113 (serviço de login, head bee1dbe1040f3fd4d83e3656b1364656e2252dad)
- **O que o GitGuardian apontou:** "1 secret" do tipo "Username Password" em `servicos/login/login.test.mjs`, no commit 17ebb1a, linha 501. O check ficou "neutral".
- **O que eu conferi:** a linha é a lista de casos do teste "sem ADMIN_SENHA_INICIAL → 503":
  - `{ ADMIN_SENHA_INICIAL: 'curta' }` é um valor de mentira, curto de propósito, para provar que o serviço recusa senha inicial curta;
  - os outros valores do arquivo são claramente falsos ('senha-inicial-falsa-1', 'segredo-de-sessao-falso-para-teste…');
  - o revisor-codigo conferiu e não achou nenhum segredo real.
- **Minha leitura:** é um falso positivo. Pela regra, um achado de segurança fica aberto até vocês decidirem.
- **Opções:**
  - a) marcar como falso positivo no painel do GitGuardian (o Alexandre ou quem tiver acesso);
  - b) eu peço ao integracao-placas para trocar 'curta' por um valor que não pareça senha, por exemplo `'x'.repeat(7)`; o commit 17ebb1a continua no histórico do branch, mas o squash não leva esse histórico ao main.
- **Recomendação:** b. Depois do b, o a também pode ser feito, se o alerta continuar no painel.
- O CI do #113 (conferir) já passou; o site ainda está rodando. O pedido de autorização do #113 vai depois da sua decisão.
