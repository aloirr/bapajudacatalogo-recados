---
id: R-20261123-171436-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0032
responde_a: R-20261123-162032-po
encerra: false
contrato: null
criado_em: 2026-11-23T17:14:36+00:00
---
# T-0032 onda 1: 8 portfólios e 4 treinamentos para o Alexandre (6 perguntas)

A onda 1 da T-0032 está pronta como simulação, liberada pelo designer-ux (que comparou com os originais) e pelo design-de-marca. Nada foi gravado em entregas/.
Anexos em bapajudacatalogo-recados, recados/anexos/T-0032/onda1/ (commit 8884521):
- portfolios/: pdf/ (os 8 PDFs), antes_depois/ (uma imagem por melhoria), antes_depois_ajustes/, INDICE_ONDA1.txt e LEIA-ME.md;
- treinamentos/<deck>/: o .pptx, o PDF de apoio, o mosaico de 8 slides e o comparativo original × novo.

## Portfólios (catalogo-grafico; head 79fb91071697cbe8b14cc08d599d690fdcd3770e)
- Os 8 PDFs, pelo mesmo gerador, com as 11 melhorias altas (8b) e as decisões 10a a 17a:

| Arquivo | Páginas |
|---|---|
| Portfolio_Produtos_BAP_AUTOPARTS.pdf (geral) | 86 |
| Portfolio_Produtos_BAP_AUTOPARTS_Linha_Leve.pdf | 43 |
| Portfolio_Produtos_BAP_AUTOPARTS_Linha_Pesada.pdf | 28 |
| Portfolio_Produtos_BAP_AUTOPARTS_Linha_Moto.pdf | 11 |
| Portfolio_Produtos_BAP_AUTOPARTS_Linha_Lubrificantes.pdf | 10 |
| Portfolio_Produtos_BAP_AUTOPARTS_Linha_Acessorios.pdf | 7 |
| Portfolio_Produtos_BAP_AUTOPARTS_Linha_Baterias.pdf | 6 |
| Portfolio_Produtos_BAP_AUTOPARTS_Linha_Autocenter.pdf | 24 |

- As 11 melhorias:
  1. modelo dos 7 (capa da linha, Quem somos, divisória única e contracapa por linha);
  2. cada linha só com os veículos dela: a regra de veículo pesado ficou num lugar só, o taxo, e a Linha Pesada não perdeu nenhuma aplicação;
  3. ícone de filtro onde não há foto da caixa certa (6b);
  4. fora das aplicações o que não é veículo (o item universal ganha uma frase);
  5. cabeçalho com menos níveis (RD-0535): "LINHA LEVE · 01" e o produto como o maior texto;
  6. corte só em palavra inteira, com "…";
  7. glossário de "linha" e "bom custo-benefício";
  8. aplicações agrupadas por montadora, com a montadora em negrito uma vez;
  9. especificações em 2 colunas (1 coluna quando 2 cortariam a diferença) e a tabela das baterias com o código (14a);
  10. índice com o número da página e link no PDF (241 links no geral);
  11. 2 produtos por página quando cabem. Só 3 páginas juntaram produtos, porque produtos de sistemas diferentes não se juntam.
- Regra nova: o produto sem nenhuma aplicação da linha sai do portfólio daquela linha. Só a Embreagem Remanufaturada saiu da Leve, porque todas as aplicações dela são de caminhão. Lâmpadas e Catraca, que não têm veículo na base, mostram a especificação.
- A foto da vela mostrava o código de outro fabricante (BKR) e virou ícone (MC-0025). Atenção: ela ainda está no Portfólio da T-0029 que acabou de entrar no main; sai quando este geral substituir aquele.
- O A4, o Completo Digital e a Linha Moto saem iguais ao main, pixel a pixel e no texto. Sem preço e sem estoque.

## Treinamentos (catalogo-grafico; head 5f9a45aec78d28f063596b4a10a57634d9ae4e41)
| Arquivo (.pptx e .pdf) | Slides | O que mudou |
|---|---|---|
| Treinamento_Mecanica_Basica_BAP_Vendedores | 45 | o aprovado, com "uso interno" e #59BA61 |
| Treinamento_Baterias_BAP_Vendedores | 47 | tabela do portfólio pela base; o CCA da 60D-LP-18 é 485 A (o original dizia 430 A); "estoque" → "falta do modelo"; o YouTube trocado por um ícone |
| Treinamento_Linha_Moto_BAP_Vendedores | 41 | sem a coluna Estoque e sem as "4.261 unidades"; o slide "preparado para" entrou; notas em todos |
| Treinamento_Lubrificantes_BAP_Vendedores | 47 | o módulo Químicos entrou (4 slides); pela base, a ProActive 200 é API SN (não SM), o Shiftease 120 é sintético (não mineral) e o fluido de radiador vai até 20 L |

- Em todos: Arial, "uso interno" no rodapé, o verde #59BA61, notas em todos os slides e códigos conferidos contra a base v28 (o gerador para se algum não existir ou não estiver ATIVO). Sem preço e sem estoque. A alçada e o Price ficam.
- Nenhuma imagem sem uso dentro do .pptx (o logo do YouTube saiu também do pacote).
- Os dados dos originais que não têm fonte na base foram mantidos e estão listados no LEIA-ME de treinamentos/. Exemplos: emplacamentos, registro ANP, tempo de recarga.

## Lista final de nomes (para o seu PR do render.yaml)
- Portfólios: os 8 nomes da tabela acima. O geral mantém o nome de hoje.
- Treinamentos: os 4 nomes acima, cada um em .pptx e .pdf (8 arquivos), sem o "_27-10" do original da Moto.
- Página de Materiais do admin: o integracao-placas põe os 8 portfólios no grupo 'materiais' e os 8 arquivos de treinamento no grupo 'treinamentos', depois do "aprovado".

## Depois do "aprovado"
O catalogo-grafico grava em entregas/, com a prova pixel a pixel contra esta simulação. Depois vêm os testes, a revisão e o corretor, um PR do catalogo-grafico (portfólios e treinamentos juntos), o PR do integracao-placas (admin) e o seu do render.yaml.

## Para a fila (sem segurar)
- catalogo-dados:
  - a LINHA da Embreagem Remanufaturada;
  - "Cherry" → "Chery";
  - lâmpadas e catraca sem aplicação por veículo;
  - "Oximico", "anti ferrugem" e o formato das especificações das cintas e da catraca;
  - "(03.08)" e "Ano:" na Bomba d'Água;
  - "Citroën Fiat/Peugeot".
- catalogo-grafico:
  - "MWM" no A4 e no Digital (hoje "Mwm"), com simulação;
  - foto de pneu e de óleo 4T na capa da Moto quando houver;
  - "1L" → "1 L";
  - o "7 linhas" da capa do catálogo Moto × "7 produtos" (decisão 11a);
  - as 12 melhorias médias e baixas.

## Perguntas ao Alexandre (copiar o bloco)
```
T-0032 · Onda 1
1) Os 8 portfólios (geral com 86 págs. e os 7 por linha), com as 11 melhorias: a) aprovado, pode gravar as entregas  b) quero ajuste (diga qual PDF e página)
2) Os 4 treinamentos (Mecânica Básica, Baterias, Linha Moto e Lubrificantes): a) aprovados, pode gravar  b) quero ajuste (diga qual deck e slide)
3) Vermelho e amarelo dos originais de Baterias: na escala de leitura da tensão (slide 23) e na faixa "garantia improcedente" (slide 29), além dos 2 ícones já aprovados: a) pode ficar  b) trocar pelo laranja
4) "BATER LIFE" aparece no testador (slide 24) e no certificado de garantia (slide 29) de Baterias: a) pode ficar (a marca recomenda; é material interno)  b) tirar
5) Categoria nova de óleo diesel no Lubrificantes (o original dizia "CL-4, licenças em 01/01/2027"; não deu para confirmar o nome aqui): a) escrever "nova categoria API para diesel, prevista para 2027", sem o nome, até confirmar (recomendo)  b) "PC-12"  c) manter "CL-4" como no original
6) Produto sem nenhuma aplicação na linha sai do portfólio daquela linha (só a Embreagem Remanufaturada saiu da Leve): a) de acordo  b) manter, com a frase "aplicação em caminhões"
```
