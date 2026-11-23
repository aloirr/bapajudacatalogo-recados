---
id: R-20261123-113921-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: alta
tarefa: T-0028
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T11:39:21+00:00
---
# T-0028 (Portfólio e capa da Linha Moto): simulação para o Alexandre, 2 perguntas (recomendação 1b 2a)

T-0028, pedidos 9a e 11a do R-20261123-112006-alexandre. Dono catalogo-grafico.
- Simulação nos recados: recados/anexos/T-0028/sim/ (commit 59bdf6f): LEIA.md, diff-gerador.patch, diff-variante-b.patch e os PNGs.
- No Portfólio: 'antes' é a entrega de outubro (82 págs.); 'depois-a' é a v27 como está (94 págs.); 'depois-b' tem os Rolamentos em Rodagem (88 págs.).
- Gerador: branch catalogo-grafico/T-0028-entregas, head 223ce6b.

O que muda:
- O singular fica num módulo comum (plural.py). O '1 itens' do Portfólio vira '1 item' (RD-0527). As cópias da regra nos outros geradores saem (RD-0526).
- A capa da Linha Moto passa a dizer '7 linhas · 75 itens para motocicletas' (MC-0015). É a única página da Linha Moto que muda.
- A4 e Completo Digital não mudam (provado pixel a pixel e no texto, também pelo designer-ux).
- O Portfólio é regerado pela base v27: os números e as aplicações sobem (a pág. 2 passa de '+2.700' para '+4.500 itens no catálogo'), com páginas novas.
- Testes: 23 do gerador OK; gerar_site sem [PARADO]; sem preço e sem estoque.

Pareceres:
- Marca LIBERADO (design-de-marca/T-0028-simulacao, 250314e).
- UX 🟡, ajuste em andamento (designer-ux/T-0028-simulacao, e4d78e5): na v27, algumas aplicações saem coladas, sem separação ('…2014–2015HONDA CG 12…'), em 3 páginas de cada variante. O catalogo-grafico está corrigindo. Isso não muda as perguntas.

Perguntas ao Alexandre (o po leva no formato do R-20261123-111806, com o bloco para copiar):
1) Como agrupar os Rolamentos no Portfólio? A v27 dividiu os Rolamentos em 3 sistemas (Transmissão, Motor e Rodagem).
   a) v27 como está: 94 páginas; 'Cubos e Rolamentos' aparece até 3 vezes na mesma linha, e a lista da divisória da Linha Leve encosta no número da página.
   b) Rolamentos em Rodagem, como no Catálogo BAP (A4 e Digital), e o resto pela v27: 88 páginas ► recomendado (catalogo-grafico, UX e marca).
   c) voltar à base de outubro (v11): números antigos.
2) Datas do Portfólio: a capa diz 'Outubro de 2026' e 'PORTFÓLIO DE PRODUTOS 2026', e a pág. 3 diz 'conforme o Catálogo BAP 2026', enquanto os catálogos já são 2027.
   a) ficam nesta tarefa; a troca (ano da capa e da contracapa, data, pág. 3 e o selo 'NOVIDADE 2026') vai para a fila, com simulação própria ► recomendado.
   b) trocar agora, com nova simulação.
   Além disso, o 'aprovado' da simulação, com a resposta da 1.

Vai para a fila, sem pergunta agora:
- MC-0017 (marca, baixa, já existia em outubro): siglas de montadora em caixa errada nas aplicações do Portfólio ('Vw/Audi', 'Ford/Gm'), e 'effitech' em vez de 'Effitech'.
- A seta 'sistema → família → produto' da pág. 3 não aparece, porque a fonte não tem o caractere. Já era assim em outubro. Se o caractere for simples, o catalogo-grafico corrige no mesmo ajuste.
- Dados da base (catalogo-dados): 'Doblo' nas Bieletas da Linha Pesada; 'Ford Focus' e 'Volvo V40' nos Filtros de Cabine da Pesada.
- As divisórias da Moto e do Universal têm muito espaço vazio, como já tinham em outubro.
