# T-0028 · Entrega final: Portfólio e capa da Linha Moto

`catalogo-grafico`, 23/11/2026 08:32 (Manaus). Branch `catalogo-grafico/T-0028-entregas`, head `ac36418`. Decisões 3b, 4a e 5a (R-20261123-122814-po).

## O que foi entregue (`catalogo_grafico/entregas/`, os mesmos nomes)
| Arquivo | Págs. | sha256 |
|---|---|---|
| Portfolio_Produtos_BAP_AUTOPARTS.pdf | 88 (antes, 82) | `600bca9eb94f838cff54f838c9670dcd73edb87907c634b1538d86bd6b671bf7` |
| Catalogo_BAP_2027_Linha_Moto.pdf | 17 | `9b4576f0398dd3bb8cc8f20f29b3e9e6533b625a4a933f416f22df783c809c14` |
| Catalogo_BAP_2027_A4_grafica.pdf (não regravado) | 56 | `f3a4c653fba0b022a5557a634ccfb05d8c6139cf39a136440dba3a62239d2065` |
| Catalogo_BAP_2027_Completo_Digital.pdf (não regravado) | 311 | `6fad79f6130c224d9a0a3649ab0e5ee325862855b3dc83692e9b3e82777e0af1` |

Antes desta entrega, os sha256 eram estes:
- Portfólio: `67c4c1b554790aebbd4b866432ef923c688c25c839fad64a78081936ae8c3f83`;
- Linha Moto: `14aac1c8054d97868b20a9be92ae5de85af8dab64b87c4dda3a3669f76f7e88e`.

## Prova (texto e pixel, PyMuPDF)
| Comparação | Resultado |
|---|---|
| Portfólio entregue × simulação aprovada (variante b, `fe47d1f` + patch), 150 ppi | 88 = 88 págs.; nenhuma página difere |
| Linha Moto entregue × simulação, 150 ppi | 17 = 17; nenhuma página difere |
| Linha Moto entregue × entrega anterior | só a pág. 1 (capa) difere |
| A4 gerado no head × entrega, 100 ppi | 56 = 56; nenhuma página difere. Os bytes mudam (data e ID do PDF), por isso o arquivo não foi regravado |
| Completo Digital gerado no head × entrega, 100 ppi | 311 = 311; nenhuma página difere; não foi regravado |

**Portfólio, conferências de material para cliente:**
- sem palavras internas, de preço ou de estoque (o "preço acessível" do "Quem somos" é o texto institucional já aceito pela marca);
- nenhum "1 itens";
- glifo vazio só na seta "→" da pág. 3 (2 vezes, como na entrega anterior; a troca do caractere fica com a marca);
- metadados "Portfólio de Produtos BAP AUTOPARTS", autor "BAP AUTOPARTS".

**Outros materiais, não regravados:**
- **Lista de aplicações do site:** o gerador dá o mesmo pixel antes e depois da tarefa.
- **Kit Filtros:** muda só o código ("N veículo(s)" pelo `plural()`), com o mesmo texto para qualquer n. Não roda nesta nuvem: os caminhos fixos do `kit.py` e do `parse.py` não existem aqui.

**Testes:** os 3 testes do gerador passaram (23 testes, OK); o `gerar_site.py` rodou sem `[PARADO]`.

## Pranchas (antes à esquerda, depois à direita)
- `moto-p01-capa.png`.
- Portfólio, divisórias e páginas institucionais: `portfolio-quem-somos.png`, `portfolio-sumario-nosso-portfolio.png`, `portfolio-sumario-linha-leve.png`, `portfolio-sumario-linha-pesada.png`, `portfolio-sumario-linha-moto.png`, `portfolio-sumario-universal.png` e `portfolio-contracapa.png`.
- Portfólio, "1 item": `portfolio-1item-lampadas-moto.png` e `portfolio-1item-oleo-hidraulico.png`.
- Portfólio, Rolamentos em Rodagem: `portfolio-rolamentos-leve-rodagem.png`.
- Portfólio, aplicações: `portfolio-aplicacoes-terminais-direcao.png`, `portfolio-aplicacoes-cruzetas.png` e `portfolio-aplicacoes-filtros-de-ar-leve.png`.
- Portfólio, páginas novas (sem "antes"): `portfolio-nova-1item-filtro-ar-moto.png`, `portfolio-nova-pesada-bieletas.png` e `portfolio-nova-universal-rolamentos.png`.

## Fica para a fila
As datas do Portfólio ("Outubro de 2026", "PORTFÓLIO DE PRODUTOS 2026", "Catálogo BAP 2026") continuam como estão (4a).
