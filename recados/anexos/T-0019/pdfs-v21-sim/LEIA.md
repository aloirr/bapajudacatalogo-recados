# T-0019 · Simulação D dos 3 PDFs 2027 com a base v21

Esta é uma simulação (regra 3) e vai ao Alexandre antes do PR. Foi gerada com `PYTHONHASHSEED=0` sobre o main `92170da` (base v21), no worktree `catalogo-grafico/T-0019-pdfs-v21`. As mudanças do gerador estão sem commit (`geradores.diff`).

- **Antes:** os PDFs do main `92170da` em `catalogo_grafico/entregas/`, gerados com a v19 (PR #70).
- **main+v21:** o código do main com a v21. Serve só para separar o efeito da base do efeito do gerador. O código do gerador não mudou entre `fc62222` e `92170da`.

## Arquivos
- `Catalogo_BAP_2027_A4_grafica_SIMULACAO_v21.pdf`: 56 págs., que é múltiplo de 4. Tem 13,2 MB.
- `Catalogo_BAP_2027_Completo_Digital_SIMULACAO_v21.pdf`: 308 págs. (antes 308). Tem 5,9 MB.
- `Catalogo_BAP_2027_Linha_Moto_SIMULACAO_v21.pdf`: 17 págs. (antes 17).
- `pranchas/`: antes e depois da mesma página, a 150 ppi.
  - `01`: A4, p. 23, com o rodapé novo.
  - `02`: Digital, p. 110, com o SCE14002.
  - `03a`: Digital, p. 150, sem o "nan" (P3).
  - `03b`: Digital, p. 93, com o "Cofap:" agora como "Cofap KJH…" (P7).
  - `04`: Digital, p. 107. As 3 linhas falsas do CRU100 ("HYUNDAI", "KIA MOTORS", "Veículo") saem (P13). O CRU100 (p. 105) não muda.
  - `05`: Linha Moto, p. 8, com o rodapé novo.
- `conferencias.json`: a saída do confere2.

## Contagens (A4 / Digital / Moto)
| Item | Antes (v19) | Depois (v21) |
|---|---|---|
| Páginas | 56 / 308 / 17 | 56 / 308 / 17 |
| Rodapé "Verifique a disponibilidade e estoque…" | 54 / 306 / 15 | 0 / 0 / 0 |
| Rodapé "Consulte a disponibilidade na sua região." | 0 | 54 / 306 / 15 |
| "estoque" no texto | 54 / 306 / 15 (só no rodapé) | 0 / 0 / 0 |
| "nan" | 0 / 18 / 0 | 0 / 0 / 0 |
| "Cofap:" | 1 / 37 / 0 | 0 / 0 / 0 |
| "RT#" | 9 / 139 / 0 | 0 / 0 / 0 |
| Itens das Cruzetas | 38 | 35 (P13) |
| "AAAA+" | 445 / 4.229 / 8 | 445 / 4.230 / 8 |
| SUNRISE, AUTOIMPACT, "#N/A" | 0 | 0 |

## confere2 (antes x depois)
- **Palavras proibidas: 0 nos 3 PDFs.** A busca não diferencia maiúscula de minúscula e procurou: USD, BAP BOX, R$, ANTERIOR, "PN: -/0", #N/A, AUTOIMPACT, SUNRISE, Diferencial BAP, Itens parecidos, Selo, FOB, MOQ, estoque, preço, custo, fornecedor, ranking, nan, "Cofap:", RT# e "Marca Ref".
  - Há 3 falsos positivos de "preço" no A4. São o texto institucional ("preço acessível", "preço competitivo"), igual ao antes.
  - "vendedor" aparece 13 vezes no A4 e 32 no Digital. É o "Aplicação em cadastro — consulte o vendedor BAP" do catálogo interno, igual ao antes.
- **Referência repetida no EQUIVALE A:** 0 / 0 / 0.
- **Aplicação repetida:** 0 pela regra do gerador.
  - O detector de janela 80 acha 4 itens: FAC6349, FAR6541, FCB6154 e FSE6117. São as mesmas variantes parecidas de antes, sem veículo repetido.
  - Mais 3 parecem repetidos no texto, mas não são: PAF0104 e PAF0498S têm um com "diant." e um sem; o ABS4526 tem um "Simples" e um "Dupla". Estavam iguais no antes.
- **"estoque" no rodapé:** 0.
- **Sobreposição de linhas:** igual ao antes (42 / 41 / 8). Não há sobreposição nova. O subtítulo do SCE14002 não encosta mais na aplicação.

## O que mudou no gerador (`geradores.diff`)
1. **Rodapé** (R-20261120-212000-alexandre, "3) a"):
   - O `digital2.OBS_DISP` agora é "Consulte a disponibilidade na sua região.".
   - O A4 e a Linha Moto usam o mesmo rodapé.
   - O `LEIA_GERADOR.md` foi atualizado.
2. **`fraga_complementos._norm`:** o "até" sem um ano antes vira o marcador "ATE" (">1994" e "até 1995"). Com isso, "Gol >1994" e "Gol até 1995" ficam diferentes de "Gol 1994" e "Gol 1995".
   - "1993 até 1995" continua igual a "1993–1995".
   - O trecho que só tem "até 2008" continua ficando sempre, como o trecho que só tem o ano.
   - O texto não muda: main+v21 x depois dá 0 diferença por causa disso.
3. **Cartão de destaque (`print_cat.cards`, A4 e Digital):** quando o subtítulo não cabe, a faixa do código cresce nos 5 cartões da linha. A aplicação tem o mesmo corte de antes.
   - Isso vale para o SCE14002 (4 linhas) e para o ROL6202-2RS (p. 263, que encostava de leve).
   - No A4, o texto não muda. No Digital, as linhas seguintes andam: 1 item passa da p. 110 para a 111, e alguns rolamentos passam para a página seguinte entre a 263 e a 267. O texto dessas páginas, somado, é o mesmo.
4. **"nan" dos interruptores (a mais, pela P3):** 7 interruptores do Digital (INT16527, 16571, 16621, 16537 e outros) vêm do `digital_data.json`, e não da base. Lá estava "AGRALE nan" e "ZF nan".
   - O `digital2` agora tira o "nan" depois da montadora, e a marca fica, como na P3.
   - As outras 11 ocorrências já saíam pela base v21.

## txtcmp (páginas com texto diferente, sem contar o rodapé)
| PDF | Antes x depois | main+v21 x depois |
|---|---|---|
| A4 | 5 de 56: p. 12, 16, 19, 31 e 38 | 0 |
| Digital | 45 de 308 | 12: p. 110 e 111, 150 e 151, 178 a 180, 263 a 267 |
| Moto | 0 (só o rodapé, em 15 páginas) | 0 |

Por item (antes x depois):
- **A4**
  - p. 12 e 16: referências de 10 itens (9 com "RT#" e 1 com "Cofap:", P7 e P8).
  - p. 19: Cruzetas, de 38 para 35 itens (P13).
  - p. 31 e 38: a lista "Aplicações também para…" dos interruptores muda de ordem, porque a contagem de montadoras mudou com a P3.
- **Digital**
  - Referências de 177 itens: 139 com "RT#" e 37 com "Cofap:" (P7 e P8), mais o CRUSPL90. Ficam nas p. 52 a 63, 93 a 98 e 107.
  - "nan" tirado: 18 ocorrências em 17 interruptores (P3), nas p. 150, 151 e 178 a 182.
  - P13: saem as 3 linhas falsas, na p. 107. A contagem de itens muda nas p. 2, 84, 105 e 106.
  - Aplicação de 8 itens:
    - CXD13179 (p. 82): o 1996 da v20, "Fora da Frota Nacional 1996+", entra junto com o 1960+;
    - FAC6349, FCB6328 e FCB6451 (p. 209, 220 e 222): sai o veículo repetido;
    - FAC6227, FAC6301 e FSE6117 (p. 208, 209 e 227): veículo quebrado no meio ("175- 178 CV" vira "175-178 CV");
    - FAG6317 (p. 211): sai o "- DE" sem ano (P5);
    - FSE6215 (p. 230): sai o "Contnua.." e fica "VW 23250".
  - Cartão de destaque: SCE14002 (p. 110 e 111) e ROL6202-2RS (p. 263 a 267), só com mudança de posição.
- **Moto:** só o rodapé.

## Observação (fora desta tarefa)
- SCE14002: a aplicação mostra "1929–19321934", que é o texto da base. Não foi mexido.
- O Digital tem 308 páginas, acima das ~200 do padrão. É o mesmo tamanho de antes.
