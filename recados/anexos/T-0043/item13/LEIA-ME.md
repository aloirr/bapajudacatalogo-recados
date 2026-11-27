# T-0043 · item 13 (Idea 1.8) e conferência do item 12 · SIMULAÇÃO

Branch `web-site/T-0043-repetidas`:
- fc44b98: linhas repetidas (aprovado no item 11). Já tira as 14 linhas das velas do item 12, sem código novo.
- 8b24fb5: SIMULAÇÃO do item 13 (site/app.js, função `arrumar`; docs/DADOS_DO_SITE.md).

Todos os prints e as comparações usam os dados da v31 (simulação f6e8957).
- antes: main c909a2f
- depois: 8b24fb5

## Causa do "Idea 1.8 · 2004–2020"
A linha do texto "Idea 1.8 L 16V 2010–2015" entra na tabela com o ano certo. No fim, a regra da T-0040, "toda linha que não é da VEICULOS mostra o ano do produto (an)", troca esse ano pelo do produto inteiro, 2004–2020.

## Correção simulada
O ano do produto continua valendo para a linha sem ano e para a linha com o ano fora dele. A linha cujo ano veio do texto e cabe inteiro dentro do ano do produto fica com o ano do texto.
- VEL7520: Idea 1.8 16V, 2010–2015.

## O que muda no catálogo inteiro
- 27 produtos: a lista e os detalhes estão em compara-item13.txt.
- 142 linhas trocam o ano do produto pelo ano do texto. Exemplos:
  - VEL7574, Fox 1.0: de 1995–2024 para 2005–2015;
  - ROL4533, Courier: de 1987–2014 para 1997–2013;
  - L803775, Volvo VM 6.5: de 1980–2024 para 2003–2005.
- 8 linhas entram e 1 sai.

## Busca com ano
- Fiat Idea 2018: de 25 para 24 produtos (sai o VEL7520).
- Fox 2020: de 66 para 65.
- Marea 2012: de 9 para 8.

## Prints, em 1366 e 390
- VEL7520: a página inteira e a tabela;
- VEL7503, VEL7561 e VEL7574: a tabela (item 12);
- ROL4533 e L803775: a tabela (item 13).
