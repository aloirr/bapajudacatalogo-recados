---
id: R-20261122-004118-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0019
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T00:41:18+00:00
---
# B8 no A4: código longo quebra no meio; proposta para simular ao Alexandre antes do merge do #99

# B8 no A4: código longo quebra no meio (proposta para simulação ao Alexandre)

## O que achei no PR #99 (head f52e409, mesmo texto do 854236c)
Com a marca e o código juntos (B8), um código longo da referência cruzada não cabe na coluna e quebra no meio. Quatro páginas do A4:
- p.21: "Kongsberg 100050486 / 9AMK" (EMB1047071R);
- p.29: na aplicação do cartão, "Zetec Roca / m/Supercharger" (a palavra quebra no meio; na proposta fica "Rocam/Supercharger"). O "Fo / cus" continua, porque o texto da base não tem espaço depois da vírgula (fica para a limpeza de dados);
- p.40: na tabela, a linha corta um pouco antes ("T5 1.5 …"); na proposta cabe "T5 1.5 L" (mudança pequena, só para conferência);
- p.44: "FAG KLM102949LM10291 / 0" e "FAG KLM104949LM10491 / 1" (sobra um dígito sozinho na última linha, o contrário do que o B8 prometeu).

## Proposta (simulada, ainda não gravada no PR)
Quando a marca e o código não cabem juntos na linha, a marca fica numa linha e o código inteiro na de baixo. O código nunca quebra no meio. A coluna da referência ganha uns milímetros da coluna da aplicação, nas mesmas páginas, sem mudar o total de páginas do A4.

Pranchas antes e depois (A4 p.21, 29, 40 e 44): `recados/anexos/T-0019/cortes-b8/` no repositório de recados.

## Pergunta ao Alexandre (regra 3, simulação)
1. Código da referência sem quebrar no meio (marca em cima e código inteiro embaixo, quando não cabe):
   a) aprovar e entrar no próprio #99, antes do merge (**recomendação do gerente**: é o mesmo item B8 e evita uma rodada a mais de PDFs);
   b) fazer o merge do #99 como está e corrigir num PR seguinte;
   c) deixar como está.

## Situação do #99
- Head f52e409, com o main 3d6a730 (#100, pares_de) já dentro (merge a3fc4c2). CI verde (conferir, site, GitGuardian).
- Estou refazendo testes, revisor-codigo e corretor-redundancias no f52e409. designer-ux e design-de-marca entram depois da resposta acima, sobre as páginas finais.
- Peço a autorização de merge só depois disso, com número e SHA.
