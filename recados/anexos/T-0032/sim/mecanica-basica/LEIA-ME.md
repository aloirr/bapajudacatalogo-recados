# T-0032 · Treinamento de Mecânica Básica BAP: modelo completo (SIMULAÇÃO)

Pedido do Alexandre (23/11/2026, R-20261123-153249-po): "CRIE UM MODELO ASSIM. QUERO VER UM MODELO COMPLETO. PODE SER O DE MECANICA BASICA".

Ainda é simulação: nada foi para `entregas/` e não há PR.

## Rodada 2: ajustes dos pareceres de UX e de marca (MC-0022)

| Slide | O que mudou |
|---|---|
| 1 | "Novembro de 2026". |
| 7 | Os mesmos 10 sistemas do slide 6, com o mesmo nome e na mesma ordem, em grade 2 × 5. O painel escuro diz "12 sistemas no catálogo: os 10 do carro, mais Acessórios e Químicos". |
| 26 | Legenda numerada sob cada desenho: "1 Disco · 2 Pastilha · 3 Pinça · 4 Pistão · 5 Fluido" e "1 Tambor · 2 Sapata · 3 Lona · 4 Cilindro · 5 Mola". |
| 32 | A pergunta combina com a foto: "Quem recarrega a bateria com o motor ligado? O alternador". O motor de partida está na definição e nas notas. |
| 39 | "Kit Batente de Amortecedor", o PRODUTO da base. |
| 40 | Nos combos, os nomes do PRODUTO da base: "Kit Batente de Amortecedor"; "Sapata de Freio + Cilindro de Roda + Fluido de Freio"; "Kit de Distribuição + Bomba D'Água". |
| Tema (todos) | O amarelo `#F2C14E` saiu: o accent5 virou a borda `#D9E6DA` e o accent6 o laranja-escuro `#8A3F00`. O vermelho `#D64545` ficou gravado direto só nos 2 ícones de sinal grave (slides 18 e 30), que não mudaram de cor. No guia, ele está registrado como "só em ícone", a aprovar pelo Alexandre junto com o padrão. |

**Foto da embreagem (slide 17): ficou como estava.** Não há outra foto BAP do kit no repositório: `site/img` não tem foto de código EMB, e a única é a capa do catálogo (`dimg/cover_15`). Vira pergunta ao Alexandre: "pode ficar?".

## Arquivos

| Arquivo | O que é |
|---|---|
| `Treinamento_Mecanica_Basica_BAP_Vendedores.pptx` | O deck completo: 45 slides, notas em todos. |
| `Treinamento_Mecanica_Basica_BAP_Vendedores.pdf` | O mesmo deck em PDF (LibreOffice). |
| `slides/slide_01.png` … `slide_45.png` | Cada slide a 100 ppi. |
| `mosaico_8_slides.png` | 8 slides representativos: 1, 3, 6, 10, 22, 26, 39 e 40. |
| `comparativo_original_x_novo.png` | 8 pares lado a lado: o slide do original de Baterias e o slide novo feito a partir dele. |

## Como foi feito

- **Molde:** o próprio `Treinamento_Baterias_BAP_Vendedores.pptx`. Para cada slide novo, o gerador duplica o slide do original do mesmo tipo (o XML e as relações de imagem) e troca só o conteúdo: textos, notas, ícones e a imagem.
  - Ficam iguais ao original: o tema, os layouts, a capa dividida, as divisórias, os cartões, os círculos, a faixa DICA DE CAMPO, a faixa PERGUNTE, as etiquetas dos combos, a tabela do "Não fechou?", o checklist e o quiz.
- **Ícones:** os brancos dos 3 originais, escolhidos pelo nome (ex.: `FaWrench`, `FaOilCan`).
- **Fotos:** das peças BAP do site (`site/img/<CÓDIGO>.jpg`, código conferido na base) e as capas do catálogo (`gerador/dimg/`).
- **Esquemas em corte:** desenhados em vetor pelo `treinamento_desenhos.py`: o carro em 10 sistemas, o motor por dentro, os 4 tempos, o arrefecimento, a transmissão, a McPherson, o freio a disco, o freio a tambor, o freio hidráulico e a ignição.
- **Fonte:** Arial em tudo, no tema e nos textos. O LibreOffice deste ambiente não tem Arial e usa a Liberation Sans, que tem as mesmas medidas.
- **Cores:** as do original. Duas exceções, já fechadas pela marca:
  - texto verde sobre fundo claro sai em `#2F7D36`;
  - texto laranja sobre fundo claro (ATENÇÃO, "= o que isso significa", o "+") sai em `#8A3F00`.
- **Base:** v28, só leitura. São 29 códigos citados, todos ATIVOS, com o "Ofereça junto" vindo da própria base. Os nomes da coluna "Peça BAP" são PRODUTOS da base.
- **Conteúdo interno:** sem preço e sem "estoque". A alçada de 15% e o Price ficam, como nos originais.

## Estrutura (45 slides)

1. Capa.
2. a 4. Aberturas: o que vamos aprender, tópicos e "Ao final… você estará preparado para".
5. a 8. **Módulo 01 · Como o carro funciona:** os 10 sistemas, a função de cada um e o caminho da força.
9. a 14. **Módulo 02 · Motor e arrefecimento:** o motor por dentro, 4 tempos e sincronismo, kit de distribuição, o circuito de arrefecimento e o superaquecimento.
15. a 19. **Módulo 03 · Transmissão:** do motor à roda, embreagem, sinais da homocinética, e semieixo, trizeta e cruzeta.
20. a 24. **Módulo 04 · Suspensão e direção:** a McPherson por dentro, o teste do amortecedor, barulhos e a direção.
25. a 30. **Módulo 05 · Freio e rodagem:** disco × tambor, o freio hidráulico, o fluido, pastilha, sapata e cilindro, e cubo e rolamento.
31. a 35. **Módulo 06 · Elétrica, filtros e óleo:** partida e carga, ignição, os 4 filtros e lubrificação.
36. a 42. **Módulo 07 · Diagnóstico de balcão e venda:** sintoma → sistema → peça BAP, SPIN, cross-sell, combos, fechamento em 3 etapas e "Não fechou?".
43. Checklist.
44. Teste seus conhecimentos (as respostas estão nas notas).
45. Obrigado.

## Conferências feitas

- 45 páginas no PDF.
- Nenhum bloco de texto sobreposto ou fora da página (PyMuPDF).
- 45 de 45 slides com notas.
- Nenhuma ocorrência de "estoque", "R$" ou "Calibri".
- Duas gerações seguidas dão um .pptx idêntico byte a byte (o zip é gravado com data fixa).

## Imagens que faltaram

- **Lâmpada:** a única foto (`dimg/cover_32`, `capa_3`) é de outra marca; o número 64193 está gravado no vidro. Não entrou.
- **Vela de ignição:** a foto (`dimg/cover_29`, `capa_6`) tem texto gravado no isolador, que pode ser marca de terceiro. No lugar dela entrou o desenho vetorial da ignição.
- **Sem foto no repositório:** filtro de óleo, de combustível e de cabine (só existe a caixa do filtro de ar), cabo de vela, interruptor de pressão do óleo e sensor ABS. O slide dos 4 filtros ficou só com ícones.
- **Disco de freio:** não é linha BAP, então só aparece no desenho.

## Como gerar de novo

```
cd catalogo_grafico/gerador
PYTHONHASHSEED=0 python treinamento_molde.py mecanica_basica --sim PASTA
```

O conteúdo está em `gerador/treinamentos/mecanica_basica.json`. Os outros treinamentos seguem o mesmo caminho: um JSON por treinamento.
