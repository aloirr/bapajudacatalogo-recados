---
id: R-20261122-010822-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0014
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T01:08:22+00:00
---
# Pedido de autorização de merge: PR #101 no commit d7fdc203757e0d5b8d571fcb04dbde2557a3f8ba (aperto dos testes, T-0014 e T-0018)

# PR #101: aperto dos testes do site (T-0014 e T-0018)

- **PR:** #101, do testes. Branch testes/T-0014-T-0018-aperto.
- **Head:** d7fdc203757e0d5b8d571fcb04dbde2557a3f8ba, sobre o main 3d6a730. mergeable_state: clean.
- **Arquivos (12):** scripts/testar_site.mjs e testes/prints/T-0014-T-0018/ (10 prints e o resumo.txt). Nenhum arquivo de governança; site, JSON e gerador iguais.
- **CI:** conferir, site e GitGuardian em success no d7fdc20.
- **testes:** a bateria passou no main com 0 falha. Prova: com o comportamento antigo, falha (14 falhas); com role=tab, falha (1 falha).
- **revisor-codigo:** LIBERADO no d7aa3ac e no d7fdc20.
- **corretor-redundancias:** RD-0294 a RD-0297 CORRIGIDOS no d7fdc20; LIBERADO. O parecer está em corretor-redundancias/T-0014-aperto, ce11ba8, e entra no PR de registro.
- [SUPOSIÇÃO] Dois apertos foram decisão do testes, e o revisor aceitou: o rótulo Placa em 390 px (p1, #57) e df/ip fora do JSON (#50).
- Não muda tela nem PDF, por isso não há simulação ao Alexandre. É o aperto previsto na T-0014 e na T-0018.

Peço a autorização do merge do PR #101 no commit d7fdc203757e0d5b8d571fcb04dbde2557a3f8ba. Squash, com Agente: testes.
