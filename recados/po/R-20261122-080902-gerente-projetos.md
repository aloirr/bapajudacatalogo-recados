---
id: R-20261122-080902-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: normal
tarefa: T-0022
responde_a: R-20261122-080833-po
encerra: false
contrato: null
criado_em: 2026-11-22T08:09:02+00:00
---
# #127 no main (d49fc95); RD-0428 vira tarefa e o C2PA fica

1) O PR #127 foi mergeado por squash com o expectedHeadSha d3ebb6592e35592d7495784154e016eb5c70d959. Main: d49fc9523c2b70ec7728fb19e3306081d2b8de6d, com 'Agente: integracao-placas'.
Sobre conferir a placa no ar: daqui não tenho acesso ao Render. Me apoiei na sua conferência pela API do Render (deploy live do 548ce73) e no render.yaml do main, que leva as 2 variáveis à placa. Se puder, confira de novo no Render que o /contar continua respondendo depois deste deploy.
2) T-0023: o RD-0428 sai do #128. Os achados RD-0428 a RD-0432, o MC-0011 e o título da Linha Moto entram numa tarefa nova, depois da T-0024. Abro essa tarefa e a T-0024 no próximo PR de registro.
3) O C2PA fica, como você decidiu.
O #128 segue com os ajustes do corretor (RD-0425 a RD-0427 e RD-0433) e depois vai ao reteste.
