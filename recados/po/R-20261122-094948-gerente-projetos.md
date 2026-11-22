---
id: R-20261122-094948-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: alta
tarefa: T-0025
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T09:49:48+00:00
---
# T-0025: simulação pronta, 10 perguntas (recomendação marcada)

Simulação: bapajudacatalogo-recados, recados/anexos/T-0025/sim/ (5402d30), com o LEIA.md e os PNGs de antes e depois. Nada mudou em entregas/, no gerador do main nem em dados/. O 'antes' gerado pelo main é igual às entregas, sem nenhum pixel diferente.
Pareceres: designer-ux LIBERADO (05:47, db6ad07) e design-de-marca LIBERADO (05:48, 4ee5577), os dois sem achado que segure.

1) RD-0428, etiqueta 'BAP AUTOPARTS' ao lado do logo no cabeçalho de Lubrificantes (PDF e .pptx, págs. 2 a 10):
   a) tirar;
   ► b) manter. O UX e o catalogo-grafico preferiam a); a marca prefere b), e eu sigo a marca pela regra conservadora:
     - nas págs. 3 a 10, a etiqueta é o único nome completo legível;
     - o Portfólio usa o mesmo cabeçalho;
     - tirar só de Lubrificantes separa as duas apresentações.
   A decisão vai ao Alexandre junto com o MC-0012 (MC-0014, baixo, aberto).
2) RD-0429, barra da pág. 2 do A4: ► a) lado direito vazio; b) 'CATÁLOGO 2027' (repete o título da esquerda).
3) RD-0429, resto da pág. 2 do A4 (saem o subtítulo, o cartão do SAC e a linha 'Prazos de garantia…'; o SAC segue no bloco da garantia): ► a) sim; b) não.
4) RD-0430, Lubrificantes pág. 2: ► a) sai o cartão do SAC e ficam 3 cartões mais a caixa 'Garantia Expressa BAP'; b) fica o SAC e sai a caixa.
5) Título dos metadados da Linha Moto: a) 'Catálogo BAP 2027 — Linha Moto'; ► b) 'Catálogo BAP 2027 — Linha Moto (uso interno)'. Sai só o 'Completo', que está errado; os 3 pareceres concordam.
6) MC-0011 (.pptx em Poppins): a) agora; ► b) deixar para o Alexandre (muda a fonte para quem não tem a Poppins e quebra o 'DOT 4' no slide 8).
7) MC-0012 (tamanho do logo e assinatura): a) agora; ► b) deixar para o Alexandre (refaz o cabeçalho das 9 páginas e dos 9 slides; o topo do site entra na mesma decisão).
8) RD-0431 (conteúdo da apresentação em 2 cópias): ► a) um arquivo só (apres_conteudo.json), lido pelos 2 geradores, com as páginas iguais pixel a pixel e a prova na entrega; b) fica como está; c) deixar de entregar o .pptx.
9) RD-0432: apagar simulacao_detalhe/ e kitfiltros/kit_v1_32pag.py (nada os importa): ► a) sim; b) não.
10) gerador/portfolio_v1_por_sistema.py (cópia antiga, sem uso, com uma 3ª cópia do texto da garantia): ► a) incluir na T-0025, com RD novo; b) outra tarefa.

Resumo da recomendação: 1b, 2a, 3a, 4a, 5b, 6b, 7b, 8a, 9a, 10a.
Fora da tarefa, só para registro: o Completo Digital tem 311 páginas (o padrão é cerca de 200); a pág. 2 do A4 segue com 1/3 vazio embaixo (sugestão de tarefa futura, com simulação).

Em paralelo: PR #140 (catálogo de RD da T-0024, 583d846) com revisor LIBERADO; peço a autorização quando o CI fechar.
