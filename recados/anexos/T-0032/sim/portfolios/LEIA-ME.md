# T-0032 · Simulação dos portfólios por linha (Passo 1, iii)

Só simulação: nada vai para `entregas/`. Gerado em 23/11/2026 com a base v28, `PYTHONHASHSEED=0`, pelo `gerador/portfolio.py` com o filtro novo (`--linha=`).

| Arquivo | O que é |
|---|---|
| `Portfolio_Produtos_BAP_AUTOPARTS_Linha_Autocenter.pdf` | 24 páginas: capa, Quem somos, divisória com página, 19 produtos, a tabela das baterias e a contracapa |
| `Portfolio_Produtos_BAP_AUTOPARTS_Linha_Baterias.pdf` | 6 páginas: capa, Quem somos, Baterias da Linha Leve, a tabela das 38, Baterias da Linha Pesada e a contracapa (sem divisória: só 2 produtos) |
| `png_autocenter/`, `png_baterias/` | Todas as páginas dos 2 PDFs, em PNG a 100 ppi (só na cópia de trabalho, fora do Git) |
| `antes_depois/autocenter_pNN_antes_x_depois_heavy.png` | Autocenter antes (em cima) e depois (embaixo) do merge da T-0029 (6d8f143): p06 e p07 sem caminhão e sem máquina (`taxo.HEAVY` novo); p08 e p10 com o corte de modelo da T-0029 ("…" em fim de palavra) |
| `antes_depois/` (os outros 2) | A mesma página do Portfólio geral (em cima) e do Autocenter (embaixo): Filtros de Combustível (geral p39 × Autocenter p06, só veículo leve) e Baterias (geral p32 × Autocenter p22, que aponta para a tabela da p23) |
| `INDICE_PORTFOLIOS.md` | As páginas, os grupos, as famílias e os produtos dos 7 portfólios. Os 5 sem PDF são Leve, Pesada, Moto, Lubrificantes e Acessórios |
| `MELHORIAS_PORTFOLIO.md` | A lista consolidada de melhorias do Portfólio geral (UX + marca + catálogo), para o Alexandre aprovar |

## O que foi aplicado só nos 2 da simulação

Nada disso muda o Portfólio geral, que saiu igual ao da T-0029 pixel a pixel, a 150 ppi.

- **Blocos opcionais:** a capa da linha, sem a pág. 3. A divisória é única, com a página de cada produto. Na Baterias não há divisória. A contracapa tem o fim de frase da linha.
- **Capa:** é a mesma do geral, com "Linha X", a frase de apoio, a contagem ("19 produtos · 1.893 itens"; na Baterias, "Linha Leve e Linha Pesada · 47 itens") e as fotos da linha. O total sai só na capa: a divisória fica sem contagem.
- **Especificações:** vão em 2 colunas, e o corte é em fim de palavra, com "…". Os óleos saem sem "Litro óleo" e "Óleo lubrificante", com viscosidade, API e litro num padrão só. As baterias seguem o padrão "45 Ah LP · 18 meses".
- **Tabela das baterias:** com mais de 12, uma página de tabela, "Baterias da Linha Leve · 38 itens". A página do produto não repete a lista: aponta para a página da tabela. O KTB1500 (kit de terminais) fica na tabela, porque o PRODUTO dele na base é "Baterias".
- **Descrição das baterias:** segue a linha (Leve × Pesada).
- **Autocenter:** só aplicação de veículo leve: sai o que o `taxo.HEAVY` (o novo, da T-0029) reconhece como pesado.

## Como gerar de novo

Dentro de `catalogo_grafico/gerador/`:

    PYTHONHASHSEED=0 python portfolio.py <saida.pdf> <base.xlsx> --linha=autocenter
    PYTHONHASHSEED=0 python portfolio.py <saida.pdf> <base.xlsx> --linha=baterias
    PYTHONHASHSEED=0 python portfolio.py x <base.xlsx> --indice
