---
id: R-20261123-144943-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0031
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T14:49:43+00:00
---
# Autorização de merge: PRs #175 e #176 (T-0031, base v28)

Peço a autorização de merge dos 2 PRs da T-0031, aprovados no 13a, 14a e 15a do R-20261123-141744-po.

1) PR #175, branch catalogo-dados/T-0031-v28
- Head: ccbcbc50ac6e1e93d595de780130c8845cdfd115 (2 commits)
- Arquivos, todos em dados/ (catalogo-dados):
  - a base;
  - dados/versoes/…_v28.xlsx (sha256 e3480dfd…d225, idêntico à base);
  - dados/scripts/base_v28.py e base_comum.py (2 funções novas; as versões v22 a v27 sem mudança);
  - dados/simulacoes/T-0031/
- O que muda na base:
  - 6 células LINHA na PRODUTOS;
  - 4 na VEICULOS (2 'FORD Cargo' → duvidoso, com MOTIVO);
  - 8 linhas no LOG_CORRECOES;
  - o bloco da v28 no LEIA-ME;
  - as outras abas sem diferença, o formato igual e nenhum campo digitado mexido.
- CI no ccbcbc5: verde (conferir, site e GitGuardian)
- revisor-codigo: APROVADA PELA REVISÃO (reteste às 10:46)
- corretor-redundancias: LIBERADO (reteste às 10:46). RD-0544 e RD-0545 CORRIGIDOS; RD-0546 (baixa, 2 linhas de docstring) fica ABERTO para o próximo PR do catalogo-dados.
- testes: PASSOU
- Merge: squash com expectedHeadSha, 'Agente: catalogo-dados' e 'Tarefa: T-0031'

2) PR #176, branch testes/T-0031-v28
- Head: e4507b463f2c5dea7309cfb969c5421a0a87017d
- Arquivos: testes/prints/T-0031/ (testes)
- CI no e4507b4: verde
- revisor: APROVADA PELA REVISÃO; corretor: LIBERADO
- Merge: squash com expectedHeadSha, 'Agente: testes' e 'Tarefa: T-0031'

Dois pontos para você saber:
- O catalogo-dados lembra que a regra R-20261120-213300 ('nada novo como duvidoso', da T-0017) cede aqui à aprovação explícita do Alexandre (13a e 14a): entram 2 'duvidoso' novos na VEICULOS.
- Depois do merge, o web-site regera o produtos.json num PR próprio, e o site deixa de mostrar o BIE20042 e o BOR11030 em 'Ford Cargo'.
