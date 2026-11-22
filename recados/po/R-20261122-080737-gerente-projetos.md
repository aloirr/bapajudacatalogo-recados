---
id: R-20261122-080737-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: normal
tarefa: T-0023
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T08:07:37+00:00
---
# T-0023: 1 decisão (RD-0428, etiqueta ao lado do logo) e o estado do #128, #129 e #130

Estado da T-0023:
- O PR #128 (gerador e entregas, head 574dd24) tem LIBERADO do designer-ux, do design-de-marca (MC-0010 fechado) e do revisor (com o CI 'site' verde no 574dd24).
  - O CI do 1380e9f falhou porque os pareceres de outros donos entraram por cherry-pick. Eles saíram do #128 e foram para PRs dos donos: #129 (UX) e #130 (marca), ambos em revisão. O merge desses dois vem junto com o do #128.
  - O corretor pediu 3 ajustes de doc e de código morto (RD-0425 a RD-0427) e um comentário (RD-0433). O catalogo-grafico está aplicando; nada muda nas entregas.
  - Falta o parecer do testes.

Decisão sua, ou do Alexandre:
1) RD-0428 (corretor, média): com o logo escuro (MC-0010), o 'bap' do cabeçalho de Lubrificantes passou a aparecer. Ao lado dele fica a etiqueta 'BAP AUTOPARTS', e na pág. 2 a marca aparece 3 vezes em uns 180 pt. No .pptx isso já era assim. A proposta é tirar a etiqueta do cabeçalho no PDF e no .pptx, o que pede simulação.
   a) Tirar da T-0023 e abrir uma tarefa própria, com simulação. O #128 segue como foi aprovado: páginas iguais, fora a grafia e o MC-0010. (RECOMENDADO)
   b) Fazer agora na T-0023: simulação ao Alexandre e nova geração. Atrasa o #128.

Achados anteriores à tarefa, para uma tarefa futura (não seguram):
- RD-0429: na pág. 2 do A4, a marca aparece 2 vezes, a garantia 3 vezes e o subtítulo repete o texto ao lado.
- RD-0430: em Lubrificantes, o cartão do SAC repete a caixa de garantia.
- RD-0431: a apresentação existe em 2 cópias inteiras (apres_bemol.py e apres_ppt.js).
- RD-0432: há cópias antigas do gerador (simulacao_detalhe/ e kit_v1_32pag.py).
- MC-0011: o .pptx sai em Arial e o PDF em Poppins.
