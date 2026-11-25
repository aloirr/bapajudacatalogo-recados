---
id: R-20261125-020052-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0036
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-25T02:00:52+00:00
---
# T-0036: autorização de merge do PR #201 (recarga diária às 06:00), head 31ceb02feeaf895a745f9fb0688dd97e78ef3f04

PR #201 (integracao-placas), head 31ceb02feeaf895a745f9fb0688dd97e78ef3f04. Muda só servicos/login/.

Revisões:
- revisor-codigo: APROVADA (6e4a1ed e o delta até 31ceb02).
- corretor-redundancias: LIBERADO (5f1b289).
- testes: PASSOU (suíte, e2e T-0034, testar_site, gerar_site.py e teste de fumaça). A suíte deu 65/65 no head final.

CI: GitGuardian verde; 'conferir' e 'site' ainda rodavam quando mandei. Confira antes de autorizar.

[SUPOSIÇÕES] no corpo do PR, para o Alexandre:
- hora 06:00 de Manaus;
- nova tentativa a cada 1 h se a partida falhar;
- se a recarga das 06:00 falhar com base no ar, a posição pode ficar com até ~48 h;
- pico de memória medido: 257 MB, dentro dos 512 MB.

Ordem: este entra ANTES da T-0035. Depois, o integracao-placas rebaseia a T-0035 e resolve o conflito simples no LEIA.md, mantendo os dois lados.

T-0035: aprovada pelo Alexandre. O web-site está acrescentando as siglas reais (3a). Depois vêm revisor e corretor, e te peço a autorização dos PRs dela.
