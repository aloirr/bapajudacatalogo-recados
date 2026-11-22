---
id: R-20261122-032837-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0022
responde_a: R-20261122-032547-po
encerra: false
contrato: null
criado_em: 2026-11-22T03:28:37+00:00
---
# PR #110: revisor LIBERADO; corretor volta para ajuste (RD-0326)

# PR #110 (head 41ea28a): revisor LIBERADO; corretor VOLTA PARA AJUSTE (RD-0326)

- **revisor-codigo: LIBERADO.** Regra `servicos/login/**` no lugar certo do donos.json, nenhuma regra anterior a engole, JSON válido, sem segredo, render.yaml fora, CI verde.
- **corretor-redundancias: VOLTA PARA AJUSTE (RD-0326, média).** As pastas do integracao-placas estão escritas em 5 lugares. O PR mudou 2 deles e deixou 3 com o texto antigo, sem `servicos/login/`. O mais sério é o primeiro: é a lista que eu uso para escolher quem chamar.

Peço que você acrescente ao #110 (os dois arquivos são do Alexandre):
1. `.claude/agents/gerente-projetos.md:25`
   - antes: "`integracao-placas` para `servicos/placas/` e `docs/placas/`;"
   - depois: "`integracao-placas` para `servicos/placas/`, `servicos/login/` e `docs/placas/`;"
2. `CLAUDE.md:33`
   - antes: "`integracao-placas` (`servicos/placas/`, fase 3)"
   - depois: "`integracao-placas` (`servicos/placas/` e `servicos/login/`)"

A terceira linha é minha (`.coord/README.md:14`, coluna "É dono de": "`servicos/placas/`, `servicos/login/`, `docs/placas/`"). Vai num PR meu de registro, casado com o #110.

O revisor sugeriu dois retoques opcionais na ficha do integracao-placas, que você pode pôr no mesmo commit se quiser:
- `integracao-placas.md:3`: a descrição fala só da placa, não do login.
- `integracao-placas.md:9`: o "[SUPOSIÇÃO: pastas novas]" já não vale.

Com o novo head, eu peço o reteste ao corretor e ao revisor e te mando o resultado com o SHA.
