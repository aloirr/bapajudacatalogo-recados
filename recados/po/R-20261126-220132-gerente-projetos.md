---
id: R-20261126-220132-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0039
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-26T22:01:32+00:00
---
# T-0039: autorização de merge #222, #223, #224 e #226

Peço a autorização de merge da T-0039. Todos os merges são squash com expectedHeadSha, nesta ordem:

1. #222 web-site · head 931a7e900ea30783b85cf675e9f2bc3484c5967d · site/app.js. É a mudança da busca: palavra inteira no nome de modelo e moto primeiro. O merge publica no Render o main inteiro, já com a T-0033 (7dd0d1b).
2. #223 design-de-marca · head b86ca75a26381508bcea1307c7c7a55ebcd2e72a · docs/marca/pareceres/T-0039.md
3. #224 designer-ux · head 7a46e716a3fd72fdfd44333062bbe24749992c64 · docs/ux/pareceres/T-0039.md
4. #226 corretor-redundancias · head e30aa45db25d14607c596fae0f281b50d8b037e6 · docs/qualidade/redundancias/T-0039.md e CATALOGO.md

Os 4 estão com o CI verde: site, conferir e GitGuardian.

Revisões:
- testes: PASSOU na rodada final no 931a7e9, com o testar_site completo e a curta da T-0033 (19 de 19).
- revisor-codigo: APROVADO PELA REVISÃO nos 4.
- corretor-redundancias: LIBERADO (RD-0666 a RD-0669 corrigidos).
- designer-ux e design-de-marca: LIBERADO.

O que muda para o vendedor:
- "filtro titan" mostra o FAR6365 (Honda CG) em 1º e os 7 do caminhão VW Titan logo abaixo.
- "titan" mostra os 7 produtos de moto primeiro.
- Nenhuma busca perdeu ou ganhou produto: comparei 3.624 termos.

Os prints antes e depois estão no branch testes/T-0039-titan, em testes/prints/T-0039/. Falta o OK do Alexandre à simulação. Se você já tem o OK, os 4 podem entrar.

Depois do #222, vem o #225 (testes da T-0033 e da T-0039, no lugar do #218). Hoje o CI "site" dele falha, como esperado, porque o teste novo cobra a ordem nova. Depois do merge do #222, o testes atualiza o branch com o main e eu peço o #225 com o SHA novo. Por último entra o registro único da T-0033 e da T-0039.
