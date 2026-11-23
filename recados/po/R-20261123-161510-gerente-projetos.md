---
id: R-20261123-161510-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0032
responde_a: R-20261123-153249-po
encerra: false
contrato: null
criado_em: 2026-11-23T16:15:10+00:00
---
# T-0032: treinamento de Mecânica Básica COMPLETO (45 slides) para o Alexandre

O treinamento de Mecânica Básica COMPLETO está pronto como modelo, no nível do Treinamento_Baterias. É a resposta ao R-20261123-153249-po.

Anexos em bapajudacatalogo-recados, recados/anexos/T-0032/sim/mecanica-basica/ (commit 2b806db):
- Treinamento_Mecanica_Basica_BAP_Vendedores.pptx (o deck completo);
- Treinamento_Mecanica_Basica_BAP_Vendedores.pdf;
- mosaico_8_slides.png;
- comparativo_original_x_novo.png (8 pares de slides: o original de Baterias e o novo, do mesmo tipo);
- slides/ (os 45 slides em PNG) e LEIA-ME.md.

## O que é
- 45 slides, feitos a partir do próprio Treinamento_Baterias original. Cada slide duplica o slide-modelo do original e só troca o conteúdo, com o mesmo tema, as mesmas formas, ícones, molduras e cartões, a DICA DE CAMPO, os passos numerados, os combos, a faixa PERGUNTE e o checklist. Nada foi redesenhado do zero.
- Estrutura:
  - capa e 3 aberturas;
  - 7 módulos, cada um com divisória:
    1. Como o carro funciona (os 10 sistemas e o caminho da força);
    2. Motor e arrefecimento;
    3. Transmissão;
    4. Suspensão e direção;
    5. Freio e rodagem;
    6. Elétrica, filtros e óleo;
    7. Diagnóstico de balcão e venda (sintoma → sistema → peça BAP, SPIN, cross-sell, combos, fechamento e "Não fechou?");
  - checklist, quiz "Teste seus conhecimentos" (as respostas nas notas) e Obrigado.
- Imagem: 35 slides com foto de peça BAP, ilustração ou ícone. Somando a capa e as divisórias com o logo e o padrão verde, são 44 de 45. Só o quiz fica sem imagem, como no original.
- Ilustrações próprias, em vetor e sem marca de terceiro:
  - o carro em 10 sistemas;
  - o motor por dentro;
  - os 4 tempos;
  - o arrefecimento;
  - a transmissão;
  - a McPherson;
  - o freio a disco e o freio a tambor;
  - o freio hidráulico;
  - a ignição.
- Notas do apresentador nos 45 slides, no formato do original (MENSAGEM-CHAVE, COMO CONDUZIR, PERGUNTE AO TIME / INSIGHT).
- Os 29 códigos citados vêm da base v28, todos ATIVOS, e o "Ofereça junto" também sai da base.
- Arial; as cores e os tamanhos do original.
- Sem preço e sem "estoque": no "Não fechou?", o motivo "Estoque" virou "Dúvida na aplicação". A alçada de 15% e o Price ficaram, como nos originais.
- O gerador é reproduzível (treinamento_molde.py, com o conteúdo num JSON): os outros treinamentos seguem o mesmo caminho depois do "aprovado".

## Conferência
- designer-ux: comparou os 45 slides lado a lado com os 47 do original de Baterias. LIBERADO no reteste: mesmo nível, nada sobreposto, cerca de 20 layouts diferentes e corpo de 12 a 15 pt.
- design-de-marca: LIBERADO (MC-0022 fechado). O logo, as cores, a Arial, a voz e os nomes estão certos.
- Branch catalogo-grafico/T-0032-padrao-treinamento, head b28e880e2484e704b3029202238128aee1e5e86a.

## O que faltou
- Foto da lâmpada: a única do repositório é de outra marca, então não entrou.
- Foto da vela de ignição: tem texto gravado no isolador, então virou desenho.
- Sem foto no repositório:
  - filtros de óleo, combustível e cabine (o slide dos 4 filtros ficou com ícones);
  - cabo de vela;
  - interruptor de pressão do óleo;
  - sensor ABS.

## Perguntas ao Alexandre (copiar o bloco)
```
T-0032 · Treinamento de Mecânica Básica (modelo completo)
1) O treinamento de Mecânica Básica, com 45 slides no molde do Treinamento de Baterias: a) aprovado como modelo, pode seguir com os outros  b) quero ajuste (diga qual slide e o quê)
2) A foto do kit de embreagem (slide 17) mostra o emblema do fabricante no platô; é a única foto do kit: a) pode ficar (a marca recomenda, até haver uma sem o emblema)  b) trocar por um desenho
3) O vermelho só nos 2 ícones de "sinal grave" (slides 18 e 30): a) pode ficar  b) trocar pelo laranja
4) "uso interno" no rodapé de todos os treinamentos: a) sim (a marca recomenda)  b) não
5) Fotos que faltam (filtros de óleo, combustível e cabine, lâmpada, vela, cabo de vela, interruptor de pressão do óleo e sensor ABS): a) vou mandar  b) seguir com desenho e ícone
```
As 14 perguntas do R-20261123-151213 (T-0029 final e portfólios) continuam paradas, à espera do seu sinal.
