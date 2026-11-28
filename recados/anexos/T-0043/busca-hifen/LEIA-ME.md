# T-0043 · SIMULAÇÃO da busca: C40 = C-40 (pergunta 47)

Branch `web-site/T-0043-busca-hifen`, commit 660ad52. Muda só `site/app.js`. Os dados são os do main: o JSON do site não muda.

## A regra
Duas palavras vizinhas que o produto escreve com hífen ou espaço também valem juntas na busca:
- "C-40" e "C 40" = C40;
- "Pick-Up" e "Pick Up" = PICKUP;
- "S-10" = S10;
- "T Cross" = TCROSS.

Exceções, para não juntar o que não é a mesma palavra:
- número com número não junta;
- número com ponto, vírgula ou barra não junta: "1.6" continua diferente de "16";
- com espaço, o conectivo não junta: "4 E 6" e "96 A 05" ficam como estão;
- com espaço, a letra solta depois de uma palavra não junta: "GM C-10" não vira GMC, e "K112 CL S" não vira CLS.

## Efeito
São 54 buscas reais, comparadas no `compara-busca.txt`. Mudam 31.

As 55 buscas do teste do site, com códigos, referências, veículo e ano, ficam iguais: mesmos produtos e mesma ordem.

| Busca | Antes | Depois |
|---|---|---|
| chevrolet c40 1990 | 1 | 3 (volta o ROL15101/15245 e o ROL15103/15243) |
| c40 | 5 | 8 (igual a "c-40") |
| s10 | 135 | 139 (igual a "s-10") |
| f1000 | 16 | 35 |
| f4000 | 20 | 44 |
| pickup | 3 | 65 (igual a "pick-up" e a "pick up") |
| corsa pickup | 1 | 27 |
| hrv | 6 | 37 |
| crv | 5 | 50 |
| tcross | 0 | 31 (igual a "t-cross") |
| mercedesbenz | 0 | 183 |

- **Ficam iguais:** "1.6", "16", "gol 1.6", "gmc", "cls", "up", "up!", "parabrisa" e "frasle".
- **Duas buscas trazem menos produtos:**
  - "rolamento f4000" passa de 449 para 10;
  - "pastilha hrv" passa de 204 para 3.

  Antes, nenhum produto tinha todas as palavras, e a tela mostrava a lista dos mais próximos. Agora mostra só os produtos que casam com todas.
- **Limite:** 4 produtos escrevem "HR V" e "CR V" com espaço (JUH70170, JUH70150, JUH70200 e JUH70284). Eles não entram em "hrv", por causa da exceção da letra solta. Se a base passar a escrever "HR-V", eles entram.
- **"Meu veículo":** não muda.

## Prints
O antes (main) e o depois, em 1366 e 390 px:
- `chevrolet-c40-1990-*`
- `c40-*`
- `pickup-*`
- `tcross-*`

Em 390 px, nenhum print tem rolagem para o lado.
