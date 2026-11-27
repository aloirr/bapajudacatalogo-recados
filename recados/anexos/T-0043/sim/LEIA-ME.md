# T-0043 · simulação: linhas repetidas da tabela de aplicação (RD-0738)

Branch `web-site/T-0043-repetidas`, commit fc44b98 (só simulação; o site no ar não muda).

## O que muda
- Saem 58 linhas repetidas, em 33 produtos: as 16 do RD-0738 (Mazda 626, Grand Caravan, VW EOS, Agrale BX 60, Mercedes 124-Serie, Chery A1, GLE-Class) e mais 28 com o mesmo defeito.
- 203 células de Cilindrada sem repetição: por exemplo, "2.0 / 2.0 16V" vira "2.0 16V". O "40.0" errado do GLE-Class some, e o "3.0" do Clio/R19 também (vinha do nome do motor C3L).
- 52 Versões recuperam o código do motor ("C3L OHV L4", "D2L DOHC L4", "M177DE40L DOHC V8").
- O aviso, o cartão e a seção ficam iguais nos 4.419 produtos. O JSON não muda.

## Prints (antes = site no ar; depois = simulação), recorte das linhas do modelo
CL20 (Mazda 626), CL26 (Grand Caravan), BV12 (GLE-Class), BIE20031 (EOS), ELE1056 e KHC12499 (estes dois não mudam), em 1366 e 390 px.

## Lista completa
`medida-compara.txt`: as 132 tabelas que mudam, linha por linha, com a linha que cobre cada uma que sai.
