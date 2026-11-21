# T-0017 · v22 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: R-20261120-221700-alexandre ("1) a"). Base de partida: v21 do main 39477d6 (sha256 `2f1e442f…7e4e`).
Regra fixa (R-20261120-213300): nada novo marcado nem escrito como duvidoso; o fim só entra quando o texto da APLICACAO prova a faixa.

## O que foi procurado
- A faixa com seta entre dois anos, no catálogo inteiro (aba PRODUTOS; a PRODUTOS_MOTO não tem nenhuma).
- **54 códigos** têm a faixa com seta:
  - "AAAA->AAAA": 45 vezes, em 10 códigos (todos ELE);
  - "AAAA>AAAA": 147 vezes, em 43 códigos;
  - "AAAA> AAAA": 2 vezes, em 2 códigos;
  - "AAAA - > AAAA", "AAAA–>AAAA" e "AAAA→AAAA": nenhuma.

## Contagens
- **23 células ANO_FIM em 9 códigos entram com o "aprovado"**: ELE1060, ELE1066, ELE1068, ELE1070, ELE1071, ELE1077, ELE1080, ELE1084 e ELE1086.
  - Inclui os 5 do ELE1084 (Apollo 1990–1992, Parati 1989–1995, Quantum 1985–1991, Saveiro 1989–1997 e Voyage 1989–1995), como o Gol da P14.
- **4 células dependem da P1** (ELE1092) e **3 da P2** (ELE1068 Uno).
- **9 linhas ficam como estão** (aba FICAM), porque o mesmo veículo tem outro trecho aberto no texto.
  - Exemplo: "Fiorino 1992>" ao lado de "Fiorino 750 kg 2008>2010".
- **9 códigos sem linha na VEICULOS** (38, 41, 47, 53, 54, 57, 60, 70 e 71): nada muda.
- Todas as "AAAA>AAAA" sem hífen caem em linha que já tem o fim certo, que fica (FICAM) ou que não tem VEICULOS.
- Quando o veículo tem várias faixas, todas fechadas, o ANO_FIM é o maior fim. Exemplo: Corsa B hatch, estate e van dão 1993–2002.
- Previsto no LOG_CORRECOES: 30 linhas, uma por célula, como na P14 da v21 (23, mais 4 se a P1 for "a", mais 3 se a P2 for "a").
- Formato: mesmas abas e colunas. Nenhuma linha nova na VEICULOS e nenhuma marca de dúvida.

## Perguntas ao Alexandre
**P1. ELE1092 (Escort e Verona 1992–1996, Logus e Pointer 1993–1996).** As 4 linhas já estavam "duvidoso" antes, pela marca: o texto diz "VOLKSWAGEM:" e a leitura juntou Logus e Pointer com a FORD. A faixa "->" está no texto.
- a) Grava o ANO_FIM das 4 e não mexe na SITUACAO nem no MOTIVO.
- b) Deixa as 4 como estão.
- **Recomendo a):** a dúvida é da marca, não do ano, e nada novo é marcado.

**P2. ELE1068 Uno.** O texto diz "Uno 1.1 Brio/1.3/1.5/1.6R 19/84->1995". A VEICULOS leu "1995 em diante".
- a) Na APLICACAO, troca só "19/84" por "1984". Na VEICULOS, o Uno fica 1984–1995: o ANO_INICIO muda de 1995 para 1984 e o ANO_FIM fica 1995.
- b) Deixa como está, e o Uno segue "1995 em diante".
- **Recomendo a):** a mesma célula traz "Uno Mille 1.0 1984->1995". [SUPOSIÇÃO] "19/84" é 1984 digitado errado.
- Se for "a", o ANO_INICIO também muda, e a decisão "1) a" falava só do fim.

## Arquivos
- `SIMULACAO_v22_T-0017.xlsx`, com as abas:
  - LEIA;
  - ANTES_DEPOIS, uma linha por célula, com a coluna ENTRA;
  - FICAM;
  - SEM_VEICULOS;
  - LOG_CORRECOES_PREVISTO.
- `numeros_v22.json`: as contagens.
- `analise_v22.json`: as linhas da VEICULOS e os trechos do texto.
- `analisar_v22.py` e `simular_v22.py`: os scripts, que só leem a base.
