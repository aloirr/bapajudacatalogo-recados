---
id: R-20261125-154416-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0033
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-25T15:44:16+00:00
---
# T-0033: autorização de merge do #217 (busca com ano), prints e pendências

Peço a autorização de merge do PR #217 (web-site), head 22bc12908314d124305573aaa62db4703cee5749, squash com expectedHeadSha. O CI está verde (site, conferir e GitGuardian).

Arquivos: site/app.js, site/styles.css e docs/DADOS_DO_SITE.md. O produtos.json não muda e FICHA e TRAVA continuam intactas.

O PR #218 (testes, head 716e2d1) vem depois. Hoje o CI "site" dele falha, como esperado: o testar_site novo cobra o aviso de tipo, que só existe no site do #217. Depois do merge do #217, o testes atualiza o branch com o main, o CI fica verde e eu peço a autorização do #218 com o SHA novo.

Revisões:
- testes: PASSOU.
  - Rodada oficial no 28b3b3a. Acréscimos sem justificativa: 0 de 1.976. Perdas com justificativa: 0 de 112.165.
  - Rodada curta no 22bc129.
  - Restrição visível e inteira em 334 de 334 produtos, em 1366 e 390.
  - O aviso passa. As contagens ficam iguais: polo 2026 = 27, gol 2010 = 71, strada 2020 = 70, polo = 156, filtro 2010 = 241, BCE3001 = 1. Pela faixa: Polo 2026 = 24, Gol 2010 = 55, Strada 2020 = 64.
- revisor-codigo: APROVADO PELA REVISÃO em 22bc129 e 716e2d1. O achado das restrições escondidas foi resolvido.
- corretor-redundancias: LIBERADO (branch 33176d3, renumerado a partir do RD-0645). Fila: RD-0655.
- designer-ux e design-de-marca: LIBERADO na tela final. U5 a U7, MC-0046 e MC-0047 feitos.

O que mudou depois da simulação aprovada (o designer-ux diz que não precisa de nova simulação):
- A restrição do texto fica inteira na Versão da tabela. Exemplo: CXD13090 "Focus 2.0 · Não aplica no Focus 1.6 - Motor Sigma".
- Quando o modelo excluído está na lista de veículos, a linha mostra "Não serve". Exemplo: AMT7050, linha HB20X.
- 9 produtos têm a linha "Restrição(ões) da aplicação:" abaixo da tabela. Exemplo: POL1678.
- O aviso da opção (a): "Nenhuma bomba de combustível para Polo 2026. Veja outras peças do Polo."

O designer-ux recomenda mostrar ao Alexandre, só para informar, os prints de AMT7050, POL1678 e CXD13090. Eles estão no branch testes/T-0033-busca-ano, em testes/prints/T-0033/ (depois-1366-produto-*.png, depois-390-produto-*.png e depois-*-aviso-bomba-combustivel-polo-2026.png).

Pendências aceitas pelo gerente e pelo revisor, para a T-0037 ou a base:
- CIL8528: "L200 | exc. Mod. 2020 c/ Disco | 2020". O ano vem de dentro da exceção, e a restrição aparece na mesma linha. No main a peça já aparecia em "l200 2020". Na base: todos os anos, menos 2020 com disco.
- ROL0015E: as cilindradas aparecem só no Alfa 145/146. A correção é a cilindrada por veículo na base.
- CXD13090: Volvo S40 com a Versão "V50 / C 70".
- PIV5002: versões do Uno omitidas na tabela. O risco é de omissão, não de peça errada.
- Caixa alta que vem da base: "SISTEMA ELETRO HIDRAULICO" e "PICASSO" (U8).
- A modelo excluído na lista de veículos (16 produtos, por exemplo AMT7050 com HB20X): talvez a base precise de correção (catalogo-dados).
