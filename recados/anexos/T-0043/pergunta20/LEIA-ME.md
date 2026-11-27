# T-0043 · pergunta 20 · SIMULAÇÃO: linhas contidas (ROL559/552A e ROL84888)

Commit cc2ff42 no branch `web-site/T-0043-repetidas`, em cima do 8b24fb5. Dados: v31 aprovada. Muda só o site/app.js (`semRepetida`) e o docs/DADOS_DO_SITE.md. O JSON não muda.

## Regra nova
Uma linha sai da tabela quando uma linha da VEICULOS com ano tem tudo isto:
- a mesma marca, o mesmo modelo e a mesma cilindrada;
- a versão compatível: a da linha que sai está vazia, ou cabe na versão da linha que fica;
- todos os anos da linha que sai.

A linha que cobre nunca sai.

## Catálogo inteiro (8b24fb5 x cc2ff42)
- 71 produtos mudam e saem 137 linhas: 132 vêm do texto e 5 da VEICULOS sem ano. Nenhuma linha entra.
- A prova automática deu 0 falha:
  - os veículos distintos (marca + modelo + cilindrada) são 34.298 antes e depois;
  - os anos cobertos são iguais antes e depois;
  - nenhuma versão some.
- A busca com ano não muda: o testar_site dá a mesma saída antes e depois.
- A comparação linha por linha, com cada SAI seguido do FICA que o cobre, está em compara-pergunta20.txt.

## ROL559/552A: de 70 para 60 linhas
Saem as 10 linhas do texto que repetiam as da VEICULOS com versão: os modelos L, LK, LS e OH, nas cilindradas 5.7, 6.0 e 9.7.

## ROL84888: fica como está (11 linhas)
As linhas não são repetidas.
- O texto dá 1996–2021 ao Strada e ao Doblò, e o DETALHE dá "Strada 1.6/1.8 1999–2020" e "Doblò 1.6/1.8 2001–2021".
- Tirar a linha do texto apaga a cilindrada 1.6 / 1.8.
- Tirar a linha da VEICULOS apaga anos (variante B, em compara-varB.txt, que não está no commit). A busca Strada 1996–1998 e Doblo 1996 e 2000 deixaria de achar o produto.

## Prints, em 1366 e 390, antes e depois
- ROL559/552A
- ROL84888
- TER55710
- ROL6202-2Z
