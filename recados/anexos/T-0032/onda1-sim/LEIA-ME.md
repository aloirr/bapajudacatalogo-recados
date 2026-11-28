# T-0032 · SIMULAÇÃO da onda 1 e "Não fechou?" com 6 motivos

Branch `catalogo-grafico/T-0032-onda2b`, head 917a2ec. Revisões: designer-ux 🟢 e design-de-marca LIBERADO.

## 1. Aprovado, vai no PR: "Não fechou? Os 6 motivos" (R-20261127-224247-alexandre, item 5)
Vale para o slide 37 dos 5 decks da onda 2 e para o slide 42 da Mecânica Básica.
- A tabela tem 6 linhas, na ordem e com os nomes da faixa: Prazo ou limite, Preço, Disponibilidade, Aplicação, Fornecedor, Sem necessidade.
- A linha nova de Disponibilidade diz "Ofereça o equivalente pela referência ou pelo código. Anote a demanda." / "Se eu te passar o equivalente, fechamos?".
- Prints: `Arrefecimento_s37`, `Direcao_s37`, `Freio_s37`, `Suspensao_s37`, `Transmissao_s37` e `Mecanica_Basica_s42`, cada um com `_antes` e `_depois`.

## 2. Simulação para aprovar: a lista nova na onda 1 (Baterias, Linha Moto e Lubrificantes)
Os números são os dos slides do deck gerado.
- **Fechamento em 3 etapas** (Baterias 43, Linha Moto 37 e Lubrificantes 43):
  - a faixa diz "prazo ou limite · preço · disponibilidade · aplicação · fornecedor · sem necessidade";
  - o cartão 2 diz "Escute até o fim: o motivo é um dos 6 da faixa abaixo.";
  - a palavra "estoque" sai.
- **Não fechou? Os 6 motivos** (Baterias 44, Linha Moto 38 e Lubrificantes 44): a mesma tabela de 6 linhas.
  - **Disponibilidade:** fica o texto próprio de cada deck.
    - Baterias: "Ofereça a equivalente: mesma caixa, polaridade e tecnologia (SLI pode subir para EFB; AGM só por AGM). Anote a demanda."
    - Linha Moto: "Pneu: mesma medida, carga e velocidade iguais ou maiores. Vela e rolamento: pela referência ou pelo código. Anote a demanda."
    - Lubrificantes: "Ofereça a mesma viscosidade com norma igual ou mais recente, nunca anterior. Anote a demanda." A volta ao pedido é "Se eu te passar o equivalente, que atende o manual, fechamos?".
  - **Aplicação:** é TEXTO NOVO, porque a onda 1 não tinha essa linha. A volta ao pedido é sempre "Se eu te mostrar que serve, fechamos?".
    - Baterias: "Mostre no Catálogo BAP a aplicação, a caixa, a polaridade e as referências cruzadas."
    - Linha Moto: "Mostre no Catálogo BAP a aplicação, a medida do pneu e as referências cruzadas."
    - Lubrificantes: "Mostre no Catálogo BAP a aplicação do veículo e a viscosidade indicada."
- **Guia do molde** (PADRAO_TREINAMENTO.md): passa a descrever a lista nova e a tabela de 6 linhas.
- Prints: `Baterias_s43` e `s44`, `Linha_Moto_s37` e `s38`, `Lubrificantes_s43` e `s44`. O "antes" é o main. Os PDFs dos 3 decks estão nesta pasta.

## Fica como está, para o Alexandre decidir depois
- **Fornecedor:** Linha Moto e Lubrificantes começam com "Não brigue com ele."; a onda 2 e Baterias, com "Não peça para trocar tudo.".
- **Faixa ATENÇÃO:** em todos os decks, ela repete a regra de "prazo e limite" que a tabela já traz.
