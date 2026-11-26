---
id: R-20261126-222349-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-26T22:23:49+00:00
---
# T-0040: piloto com WebSearch: 7 de 10 com ano, 5 de 10 confiáveis; WebFetch bloqueado

O piloto foi refeito com WebSearch e WebFetch, sem curl, nos mesmos 10 casos. Nada foi gravado no repositório.

Resultado:
- Com algum ano e fonte: 7 de 10.
- Com o veículo batendo e confiança média ou alta: 5 de 10. Com início e fim: 2 de 10.
  - FCB6343 (F-4000 2.8, 2014+): várias lojas confirmam.
  - FHD6087 (Scania P 250 DC09, 2012+): a linha diz 2011+.
  - FCB6431 (Jumpy 1.6, 2017+): o fim fica vazio, porque as lojas divergem.
  - KF25 (New Fiesta): 2011 a 2019.
  - INT16523 (Volvo FM): 2000 a 2006, pelo catálogo oficial da 3RHO, por versão.
- O ano final é o ponto fraco: as lojas dizem "após 20xx" ou cada uma dá um fim diferente.
- Pneu e câmara de moto: 0 de 2. São vendidos por medida, sem ano.
- Indícios de erro de aplicação na base, que vão para a T-0037:
  - CXD13169: o catálogo Nakata liga a NCD40001 ao Scénic 2000 a 2007, não à Trafic.
  - FSE6056: as fontes dão o OF 809 com motor OM 355/5 de 1978 a 1987, mas a linha diz motor 4.0 e 1996+.

Limitação importante: o WebFetch também foi recusado pela rede da sessão. Todos os anos acima vêm só dos resumos da WebSearch, no modo extended. Nenhuma página foi aberta e conferida. Por isso, nenhum desses anos serve ainda para gravar na base. Na standard, a WebSearch não achou nada.

Tempo e estimativa:
- Cerca de 4 minutos por caso, de 3 a 6.
- Há cerca de 2.132 referências distintas. Uma busca por referência serve várias linhas.
- Total estimado: 150 a 200 horas de agente.
- Rendimento esperado: 50 a 70% das linhas com ano inicial e só 20 a 30% com ano final.

Recomendação:
1. Fazer a Fraga primeiro, pela sessão local do Alexandre, como já decidido. Ela deve cobrir muito mais e já com o código BAP.
2. A internet só para o que a Fraga não achar. Para o ano valer como dado, é preciso abrir a página da fonte. Há dois caminhos:
   - fazer na sessão local do Alexandre, onde os sites abrem;
   - liberar no ambiente da nuvem hosts exatos de fabricantes e de 2 ou 3 lojas grandes (loja.tecfil.com.br, 3rho.com.br, selfcar.com.br e autoz.com.br, por exemplo). Eu faço o pedido de liberação, e o Alexandre aprova num cartão.
3. Revisão humana quando o motor ou a versão não baterem.
