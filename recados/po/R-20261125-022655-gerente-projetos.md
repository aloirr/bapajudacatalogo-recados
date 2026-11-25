---
id: R-20261125-022655-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0035
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-25T02:26:55+00:00
---
# T-0035: autorização de merge dos PRs #202, #203 e #204 (filtros da aba Estoque), nesta ordem

Merge NESTA ORDEM:
1) #202 servidor (integracao-placas): head e106f45ad9026eed2a9cd08015d8b8b9df2f6bc9. Rebaseado sobre o main d0fadae, que já tem a T-0036.
2) #203 tela (web-site): head 2a9c84bedd6ae940c52a55d6eb0cb8824c374df9.
3) #204 testes (testes): head e476fe885dfc04e960c19de13a497a4b64c94a8d.

Conferências:
- Simulação aprovada pelo Alexandre (1a, 2a, 3a). Sigla DOT acrescentada: era a única que aparecia na planilha.
- testes PASSOU: e2e dos filtros e da T-0034, suíte 66/66, testar_site com e sem login, gerar_site.py sem [PARADO]. O catálogo e o botão da conta ficaram idênticos.
- designer-ux e design-de-marca: LIBERADO COM AJUSTES (feitos).
- revisor-codigo: APROVADA nos 3, incluindo o delta final.
  - Ele achou 1 efeito no catálogo: a regra nova da seta também animava a setinha dos grupos de filtro.
  - Corrigido em 2a9c84b (a regra passou a valer só para svg.seta).
  - O testes conferiu: a setinha do catálogo ficou igual à do main.
- corretor-redundancias: LIBERADO (RD-0612 a RD-0623; branch corretor-redundancias/T-0035-filtros c2b6101, que já inclui os da T-0036).
- CI verde nos 3: conferir, site e GitGuardian.

Para a fila: 'FREIO A AR' aparece 'Freio A Ar'. Pôr o 'A' como conectivo mudaria 'Classe A' no catálogo; fica para decidir.

Depois dos merges: PR de registro das T-0035 e T-0036 (pareceres de UX e marca da T-0035, redundâncias das duas, tarefas, quadro e ROADMAP).
