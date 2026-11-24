---
id: R-20261124-001634-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: resposta
prioridade: alta
tarefa: null
responde_a: R-20261124-000759-po
encerra: false
contrato: null
criado_em: 2026-11-24T00:16:34+00:00
---
# PR #190: revisor APROVADA, corretor VOLTA PARA AJUSTE (RD-0577 a 0581); #191 pronto

Resultado da rodada única no PR #190 (head 6811f7bc412f7939eb60a390fc0e7d8a339989e9, branch seu). Também peço a autorização do #191.

**Revisor: APROVADA PELA REVISÃO.**
- A trava foi portada sem o FDV.
- 29 comandos do fluxo normal passam: commit, coord.mjs, gerar_site, node --test e `graphify update`.
- Os guardiões que já existiam continuam iguais, e não há segredo.
- guarda-graphify.test.mjs: 14/14. O conjunto do CI deu 176 passando e 6 falhas, todas no coord-recados.test.mjs. Essas 6 falham também no main, por causa do ambiente.
- Observações que não seguram:
  - a :72 da lib nunca é alcançada;
  - `graphify query` sem GRAPHIFY_BACKEND=none também dá a marca;
  - comando com variável, eval ou for passa sem bloqueio, então a trava é de conveniência.

**Corretor: VOLTA PARA AJUSTE** (registro em corretor-redundancias/T-0032-catalogo, 9702f13, docs/qualidade/redundancias/PR-190.md). Os achados que seguram o merge:
- **RD-0577 (média):** a `lerEntrada()` do guarda-graphify.mjs:10-19 copia a `lerEntradaDoHook()` do guarda-bash-lib.mjs:30 e não trata o error do stdin. Trocar por `(await lerEntradaDoHook()) ?? {}`.
- **RD-0578 (baixa):** a sequência commonDirDe → criarRepoDe → lerMarcas → decidir → gravarMarcas → exit 2 se repete no guarda-graphify.mjs:27-42 e no guarda-bash.mjs:74-84. Proposta: `aplicarTrava()` na lib, e `comando`/`evento` sobem para antes da trava.
- **RD-0579 (baixa):** sobras do macuxierp na lib:
  - o return da :72, que nunca roda;
  - as marcas genéricas da :85-88 e da :206-209, que servem para uma marca só;
  - o tipo 'recados' da :46, que dá o mesmo que null;
  - o existsSync da :354, antes do statSync.
- **RD-0580 (média):** a regra aparece em 3 textos que já divergem: o CLAUDE.md:71 e a lib :5-14 e :26-31. O CLAUDE.md não cita o `section` e diz "dados livres", mas a lib conta dados/ como código. Proposta: o CLAUDE.md fica só com a regra e aponta para a lib (o texto pronto está no PR-190.md).
- **RD-0581 (baixa):** a lista de arquivos do guarda-bash está copiada em 3 testes (guarda-agente :153, guarda-recado :183 e guarda-graphify :199). Proposta: um guarda-teste-comum.mjs.

Não seguram: o RD-0582 (a origem do pedido repetida em 4 cabeçalhos, para o próximo PR de governança) e o RD-0583 (o hook-guard e a trava ficam os dois).

**CI do #190:** site, conferir e GitGuardian verdes.

**Você decide**, já que o branch é seu e você pediu uma rodada só:
(a) corrigir o RD-0577 a RD-0581 no branch e voltar ao corretor;
(b) fazer o merge como está e levar os RD para um PR de governança depois do reinício.
Minha recomendação é a (a) só com o RD-0577 e o RD-0580, que são média e mexem no comportamento e na regra escrita, e deixar o resto para depois.

**#191 (registro da pausa, só documentos):** head 6149e9ee0e7332ca03ecaf5f95633fb2a247c3fc, APROVADA PELA REVISÃO.
- O quadro ganha a linha da PAUSA geral e "Main d9330f4 (#189)".
- O diário ganha a sessão de 23/11, com a onda 2 em 7e39340 e os branches do corretor (T-0030-catalogo em 5175b30 e T-0032-catalogo agora em 9702f13).
- CI: conferir e GitGuardian verdes; o site ainda rodava às 20:17.
- Peço a autorização do #191 com esse SHA. Só faço o merge com o site verde.
