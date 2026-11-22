---
id: R-20261122-081642-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0023
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T08:16:42+00:00
---
# Pedido de merge: #130 (c09f6e7), #129 (363281d) e #128 (4a86467), T-0023

Peço autorização para os 3 merges da T-0023, nesta ordem: #130, #129, #128. Os dois primeiros vêm um logo depois do outro, porque os pareceres citam um ao outro.

1) PR #130: pareceres de marca. Head c09f6e75f64f0ed6f6095db321fa6a5a31424fcb, branch design-de-marca/T-0023-parecer.
- Arquivos: docs/marca/pareceres/T-0023-simulacao.md e T-0023-entregas.md (dono: design-de-marca).
- LIBERADO e MC-0010 fechado. MC-0011 (o .pptx em Arial) e MC-0012 (a assinatura do logo ilegível no cabeçalho) são achados baixos, anteriores à tarefa, e não seguram.
- revisor-codigo e corretor-redundancias: LIBERADO no c09f6e7 (RD-0437 a RD-0441 CORRIGIDOS).
- CI no c09f6e7: conferir, site e GitGuardian em success.
- Merge: squash com 'Agente: design-de-marca'.

2) PR #129: pareceres de UX. Head 363281d9790f44fa01e8fd993d47096b785e3c5c, branch designer-ux/T-0023-parecer.
- Arquivos: docs/ux/pareceres/T-0023-simulacao.md e T-0023-entregas.md (dono: designer-ux).
- revisor-codigo e corretor-redundancias: LIBERADO no 363281d (RD-0434 a RD-0436 CORRIGIDOS).
- CI no 363281d: conferir, site e GitGuardian em success.
- Merge: squash com 'Agente: designer-ux'.

3) PR #128: gerador e entregas. Head 4a86467d923de4b27f9e1fbf1dd40a118d45e35d, branch catalogo-grafico/T-0023-grafia. Só arquivos de catalogo_grafico/ (16).
- O que muda:
  - a grafia 'BAP AUTOPARTS' nas 3 formas;
  - o MC-0010 (logo escuro no cabeçalho de Lubrificantes);
  - as fotos de Lubrificantes vindas de pptimg/;
  - o apply_theme.js novo;
  - os 2 LEIA corrigidos;
  - a nova geração do A4, do Digital, da Linha Moto e do PDF e do .pptx de Lubrificantes;
  - no Kit Filtros, só o Author.
- testes: PASSOU nos 6 itens. Páginas iguais; 0 'auto parts'; só a grafia muda; nenhum dado interno novo; os arquivos abrem; gerar_site sem [PARADO].
- designer-ux e design-de-marca: LIBERADO nas entregas finais.
- revisor-codigo: LIBERADO no 574dd24 e no delta até o 4a86467.
- corretor-redundancias: LIBERADO no 4a86467. RD-0425 a RD-0427 e RD-0433 CORRIGIDOS. RD-0428 a RD-0432 ficam ABERTOS sem segurar, pela sua decisão R-20261122-080833.
- O C2PA das PNG do .pptx fica, pela sua decisão.
- CI no 4a86467: conferir, site e GitGuardian em success.
- Merge: squash com 'Agente: catalogo-grafico'.

Depois dos 3 merges, faço o PR de registro da T-0022 e da T-0023. Ele leva o MC-0010, as fotos de pptimg/ e o C2PA no Registro da T-0023, a T-0024 nova e a tarefa da etiqueta e dos achados anteriores. Em seguida vem o catálogo de RD-0415 a RD-0441.
