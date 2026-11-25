---
id: R-20261125-144635-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0038
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-25T14:46:35+00:00
---
# T-0038: autorização de merge #209, #210, #211 e #212 (Onboarding do Vendedor), nesta ordem

Peço a autorização de merge da T-0038 (Onboarding do Vendedor). Faço os 4 merges nesta ordem, squash com expectedHeadSha:

1. #209 catalogo-grafico · head 821c5ca23dcf2f495f7ab35b1b24c0780cc0df3c · PDF e PPTX (24 slides), JSON, treinamento_molde.py, LEIA-ME, LEIA_GERADOR, PADRAO_TREINAMENTO
2. #210 integracao-placas · head e53ad3c1456b8492f944f7d4232734e7051c93c5 · server.mjs, login.test.mjs, LEIA.md
3. #211 web-site · head c4a8e45d8e78742248c2f41f74f41013cf6155f4 · site/admin/pdfs/pdfs.js
4. #212 testes · head 7bcd94c52c75a3d713fd039263d3e95093279688 · testes/prints/T-0038 (4 prints)

O CI está verde nos 4: site, conferir e GitGuardian.

Revisões:
- testes, rodada 4: PASSOU. PDF e PPTX com 24 páginas e 24 slides. Em todo o XML, 0 "estoque", 0 "R$", 0 "Ofereça junto" e 0 nome de pessoa. Os 10 passos estão iguais à fonte. Os 4 treinamentos da T-0032 continuam idênticos byte a byte. A trava nova para quando falta a chave nota_base.
- revisor-codigo: APROVADO PELA REVISÃO em 821c5ca. A TRAVA PROIBIDO está intacta. e53ad3c e c4a8e45 também estão aprovados.
- corretor-redundancias: LIBERADO em 821c5ca (branch do corretor em 584247b). RD-0624 a RD-0629 e RD-0632 a RD-0638 estão corrigidos e RD-0643 e RD-0644 também. RD-0639 fica MANTIDO.

O que mudou depois da simulação aprovada:
- "até lá, com o supervisor" saiu. Era um procedimento fora da fonte. O texto agora diz só "botão ainda não publicado".
- O Dia Foco aparece como proposta do analista, e a duração de 1h30 saiu.
- As notas do slide 1 deixaram de ter "Códigos e 'Ofereça junto' conferidos". O gerador ganhou a chave "nota_base" e uma trava [PARADO] para essa linha num deck sem código.
- Na tarefa, onde estava "Poppins", entra Arial, a fonte que o PPTX usa.

Pendências para você levar:
- RD-0630 (baixa) e RD-0631 (alta) continuam ABERTOS, fora desta entrega.
- As imagens da simulação aprovada só ficam no commit 06b8c62 do branch catalogo-grafico/T-0038-onboarding. Proponho manter esse branch depois do squash, ou criar uma tag.

Depois do merge vêm o deploy no Render e o PR de registro: tarefa, quadro, ROADMAP, pareceres de UX e de marca, e relatório do corretor com a numeração RD conferida com a da T-0033.
