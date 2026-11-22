---
id: R-20261122-112046-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: alta
tarefa: T-0027
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T11:20:46+00:00
---
# T-0027: simulação do "1 item" para decidir (2 perguntas, recomendação 1a 2a)

Simulação: bapajudacatalogo-recados, recados/anexos/T-0027/sim/ (commit bc5058f): LEIA.md, diff-gerador.patch e os PNGs antes e depois das 7 páginas.
- Gerador: commit local 2164a2d (catalogo-grafico/T-0027-entregas). Entra o plural() num lugar só (digital2.py), usado nos 7 pontos dos 3 PDFs, e sai o cover_page, que é código morto.
- Prova pixel a pixel: mudam 7 de 384 páginas (Moto 2, 3 e 5; Completo 2, 300 e 302; A4 50). Em cada uma muda só uma palavra (itens → item, ITENS → ITEM).
- UX LIBERADO (designer-ux/T-0027-simulacao, 6714fa3): só a palavra muda, o alinhamento à direita fica igual, nada se sobrepõe.
- Marca LIBERADO (design-de-marca/T-0027-simulacao, eca705a): voz e grafia coerentes; marca, texto institucional e metadados iguais.

Perguntas:
1) O painel do cabeçalho com 1 item (A4 pág. 50, Completo pág. 302, Moto pág. 5):
   a) "1 / ITEM" ► recomendado (UX e marca);
   b) manter "1 / ITENS".
2) O Portfólio, material para cliente, também tem "1 itens" (págs. 69 e 76; portfolio.py:154, :180 e :257):
   a) fica fora da T-0027, num RD novo para a fila do Alexandre, com simulação própria ► recomendado (UX e marca; critério conservador). Pela nota do UX, a correção deve usar o mesmo plural(), num módulo que os dois geradores importem;
   b) entra na T-0027, com nova simulação do Portfólio.

Nota do UX, que não segura: a página da Lâmpadas Moto tem 1 cartão e cerca de 2/3 em branco. É layout e fica para o Alexandre, se ele quiser.

Com a decisão, sigo para a entrega: PDFs com os mesmos nomes, testes, revisor, corretor e o pedido de merge.
