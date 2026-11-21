# T-0019 · Simulação dos 3 PDFs 2027 com a v19 da base

Simulação (regra 3): vai ao Alexandre antes do PR. Gerado com `PYTHONHASHSEED=0` sobre o main `ad63e05` (#64: SUNRISE no FORNECEDORES, `FORNECEDOR_RE`, "#N/A" no `refs_de`), com as mudanças do gerador sem commit no worktree `catalogo-grafico/T-0019-pdfs-v19` (`geradores.diff`).

- **Antes** = PDFs do main `3ceffef` (`catalogo_grafico/entregas/`, gerados com a base anterior à v19).
- **main+v19** = código do main com a base v19, só para separar o efeito da base do efeito do gerador.

## Arquivos
- `Catalogo_BAP_2027_A4_grafica_SIMULACAO_v19.pdf`: 56 págs.
- `Catalogo_BAP_2027_Completo_Digital_SIMULACAO_v19.pdf`: 308 págs. (antes 317), 5,9 MB.
- `Catalogo_BAP_2027_Linha_Moto_SIMULACAO_v19.pdf`: 17 págs.
- Pranchas antes | depois (150 ppi):
  - `01`: A4 p. 23, com "+";
  - `02`: SCE14004, p. 113 antes e p. 110 depois;
  - `03a` e `03b`: a antiga 303/304, que agora é 294/295;
  - `04`: rodas, p. 283 antes e p. 275 depois;
  - `05`: Linha Moto, p. 8.

## Contagens (A4 / Digital / Moto)
| Item | Antes (3ceffef) | main+v19 | Depois |
|---|---|---|---|
| "em Diante" escrito | 31 / 1.162 / 8 | 31 / 969 / 8 | 0 / 1 / 0 (*a*) |
| "AAAA+" | 0 / 1 (*b*) / 0 | 0 / 1 / 0 | 445 / 4.229 / 8 |
| … vindos de "em Diante" | | | 37 / 969 / 8 (*c*) |
| … vindos de ">" e "->" sem fim | | | 408 / 3.005 / 0 |
| … vindos de "AAAA →" sem fim | | | 0 / 254 / 0 (*d*) |
| "+" seguido de letra ou "(" (com espaço) | | | 4 / 21 / 0 |
| "1999->2008" (faixa) | 0 / 45 / 0 | 0 / 45 / 0 | 0 / 0 / 0 (vira "1999–2008") |
| SUNRISE | 4 / 4 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| AUTOIMPACT, "#N/A", ", APLICAÇÃO REVISADA" | 0 | 0 | 0 |
| Aplicação repetida (detector do RD-0222, janela 80) | 0 / 109 / 0 | 0 / 6 / 0 | 0 / 4 / 0 (*e*) |

- (*a*) "Eclipse Cross 1.5 L 16V · em Diante", sem ano: fica.
- (*b*) "Palio Weekend (1996+)" já vinha assim do cadastro.
- (*c*) No A4 são 37 e não 31 porque o texto mais curto cabe mais na aplicação cortada do A4.
- (*d*) No antes e no main+v19, esses 254 "→" saíam no Digital como **caractere sem desenho** (a Poppins não tem a seta).
- (*e*) Os 4 do detector (FAC6349, FAR6541, FCB6154, FSE6117) são variantes parecidas, sem veículo repetido. Exemplos: 2P/4P, G2/G3, SE/XE, 6X2/6X4, suspensão metálica/pneumática.
- Pela regra do gerador ficam **0 veículos repetidos**. 212 itens tiveram o veículo repetido tirado, entre eles 106 dos 109 da lista; os outros 3 são FAC6349 e FCB6154 (as variantes acima) e FLU6530 (já sem repetição na v19).

## O que mudou no gerador
1. **v19:** sai o corte do ", APLICAÇÃO REVISADA": com a v19 ele não pegava nada (0 casos). Sai também o `SEM_CODIGO`: o "#N/A" agora sai no `refs_de` do main (#64). As notas "[provisório, RD-0193]" saem (`montar.py`).
2. **RD-0222:** `fraga_complementos.aplicacao_unica`. Cada veículo aparece uma vez na aplicação, na ordem do 1º. A comparação usa a montadora e o texto normalizado, com as datas comparadas como no PDF ("1993 até 1995" = "1993–1995"). Vale para os 3 PDFs e cobre a repetição do Fraga e a da própria base (ex.: FSE6167, LO-2002 do PAF0104, Commander do FAC6069).
   - Conferência: dos 204 itens do Digital cuja aplicação mudou, todo trecho que saiu está no resto da mesma aplicação. Os 6 casos marcados pelo teste automático eram, revistos à mão, repetição real ou só a mudança de data.
3. **"AAAA+"** em `datas.em_diante` (`para_pdf`), num lugar só. Viram "+":
   - "2015 em Diante", "2015>", "03/2015>", "2008->" e "2025 →" sem ano depois;
   - o "+" fica colado ao ano, e letra ou "(" logo depois ganha um espaço ("2001>GM" = "2001+ GM").
   - Ficam como estão: "1999->2008" e "1999 → 2008", que são faixa ("1999–2008"); ">1994"; e o ">" com número que não é ano ("09/1993>1201" = "09/1993–1201", como antes).
   - O `cross.py:39` troca "em diante" por ">", e esse ">" passa pelo mesmo `para_pdf`.
4. **SUNRISE:** a v19 já tirou a referência da base. A `TRAVA_PDF` agora é `re.compile(G.FORNECEDOR_RE, re.I)` (RD-0226), com o comentário atualizado (RD-0227). Teste da trava: "Pruduct Pn Sunrise", "Sun-Rise" e "AUTO.IMPACT" param o build; "Sunroof" não para.
5. **Pág. 303 (designer-ux):** sem mexer na paginação. Com a aplicação sem repetição, as palhetas se rearrumaram sozinhas:
   - p. 294: MF18 a MF22 (MF21 e MF22 juntas);
   - p. 295: MF24, MF26 e MF27;
   - nenhuma página com uma linha só.

## Para a v21 (como a regra deu)
- BV12 (p. 280) e MF16 (p. 293): "2008–2025+".
- PAF0116 (p. 115): "1933–2005+".

## confere2 (antes x depois)
- Palavra proibida: 0, nos 3 PDFs. A busca procurou USD, BAP BOX, R$, ANTERIOR, PN: -/0, #N/A, AUTOIMPACT, SUNRISE, Diferencial BAP, Itens parecidos, Selo, FOB, MOQ, estoque, preço, custo e fornecedor.
  - O "Custo" encontrado 2 vezes no Digital é "GMC 3500 HD Custom", falso positivo.
  - "Verifique a disponibilidade e estoque" é o rodapé interno de sempre e não entrou na contagem.
- Referência repetida no EQUIVALE A: 0 / 0 / 0.
- Aplicação repetida: 0 pela regra do gerador.
- Sobreposição de linhas nas páginas que mudam: igual ao antes (21 / 40 / 2), sem sobreposição nova. Há uma antiga, de fora desta tarefa: o subtítulo de 4 linhas do SCE14002 no cartão de destaque.
- A4 em múltiplo de 4: sim (56).

## txtcmp (páginas com texto diferente)
| PDF | Antes x depois | main+v19 x depois |
|---|---|---|
| A4 | 31 de 56 | 24 de 56 (só "+"; na p. 53 o quadro "FZ25 (2018+)") |
| Digital | 305 de 317→308 | 300 (as páginas andam: 9 a menos) |
| Moto | 3 de 17 (p. 7, 8, 12) | 3 (só "+") |

Por item (main+v19 x depois):
- A4: só datas.
- Moto: só datas.
- Digital: 924 itens só com datas e 204 com veículo repetido tirado. Nenhuma referência ou "Leve também" mudou, fora as datas e a leitura do MF-25/KJ26 na conferência.
- O FUR6334 agora cabe inteiro no cartão de destaque e, pela regra de antes, não se repete na tabela.
