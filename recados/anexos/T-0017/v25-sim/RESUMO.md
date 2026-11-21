# T-0017 · v25 da base unificada: SIMULAÇÃO (nada gravado)

Pedido: R-20261121-112900-alexandre, item 4 ("coloque o palio no amt7500 assim como na internet. Olhe os catalagos unificados antigos para validar"). Base de partida: v24 (sha256 `a77de850…04d2`).

## 1. Busca nos catálogos antigos
- **O que procurei:** o AMT7500 e as referências dele (Nakata HG33004, Cofap GP30120, Monroe 94176 e SP176), em 33 arquivos. Cada linha de planilha, registro de JSON ou linha de texto com um deles conta como um registro.
- **O que achei:** 47 registros. **Nenhum tem Palio nem Siena.**

| Onde | Registros | Com Palio ou Siena |
|---|---|---|
| dados/versoes v8, v9, v10, v11 e v12 | 2 + 2 + 2 + 4 + 4 | 0 |
| catalogo_grafico/gerador/entradas (as duas bases antigas, complementos_fraga, aplicacoes_site_bap e _2, cuíca, interruptores, catálogo de pivô) | 6 | 0 |
| catalogo_grafico/gerador/digital_data.json | 3 | 0 |
| catalogo_grafico/entregas (auditoria de 23/10, conferência e alterações da Fraga, catálogos 2027 em PDF e as outras entregas) | 21 | 0 |
| docs/legado (agente, historico/ e recados/) | 3 | 0 |

- **O que cada fonte diz do AMT7500:**
  - **Bases v8 a v12 e bases de entrada:** sempre o mesmo texto, "FIAT - Strada · 01/2001–12/2020 · Adventure · Sem ABS · Exceto Locker / Cabine Dupla / Prato Pequeno · Com barra estabilizadora", com Nakata HG33004, Cofap GP30120, Monroe 94176 e SP176. A origem é a LINHA_ORIGEM 422 do CATALOGO_BAP_AGENTE_PRONTO.xlsx, que não está no repositório. As 5 bases trazem só a linha dele, e sem Palio.
  - **digital_data.json:** o mesmo Strada Adventure s/ ABS.
  - **complementos_fraga:** só a referência "MONROE SP176".
  - **Conferência com a Fraga (13/11):** "IGUAL", só Strada (1.3, 1.4, 1.6 e 1.8).
  - **Auditoria de 23/10 e docs/legado:** o caso AMT7014 × AMT7500 (Strada c/ ABS × s/ ABS) e a Cofap GP30120 e a Monroe 94176 repetidas nos dois. Nenhum Palio.
  - **Catálogos 2027 em PDF:** só Strada. O "Palio Weekend" que aparece perto do AMT7500 nos destaques é o texto do AMT7001, da coluna vizinha.
- **Fora do script:** os catálogos 2026 em PDF, que foram apagados do repositório, conferidos no histórico do Git. Também só Strada.
- **Conclusão da busca:** nenhum catálogo antigo tem Palio no AMT7500. Por isso vale a regra do Alexandre:
  - entra o que o anúncio da Cofap GP30120 diz, "Palio Weekend Adventure 2000–2007 s/ ABS";
  - o "Palio, Siena" do anúncio da Nakata HG33004 **não entra**, porque nenhum catálogo antigo confirma.
- O script para se algum catálogo antigo trouxer Palio.

## 2. Antes e depois
| Código | Aba · linha | Coluna | Antes | Depois |
|---|---|---|---|---|
| AMT7500 | PRODUTOS · 1156 | APLICACAO | FIAT - Strada 01/2001–12/2020 · Adventure · s/ ABS · exc. Locker / Cabine Dupla / Prato Pequeno · c/ barra estab. | FIAT - Strada 01/2001–12/2020 · Adventure · s/ ABS · exc. Locker / Cabine Dupla / Prato Pequeno · c/ barra estab. **; FIAT - Palio Weekend Adventure 2000–2007 · s/ ABS** |

- O trecho entra no fim, com " ; " e "FIAT - ", como na v24. O resto da célula não muda.
- O ano tem 4 dígitos e o intervalo usa "–". O "2000/2007" do anúncio vira 2000–2007.

## 3. Linha nova da VEICULOS (no fim da aba)
| CODIGO_BAP | FABRICANTE | MODELO | VERSAO | ANO_INICIO | ANO_FIM | ORIGEM | SITUACAO | MOTIVO | CILINDRADA | ANO_DUVIDA |
|---|---|---|---|---|---|---|---|---|---|---|
| AMT7500 | FIAT | Palio Weekend | Adventure | 2000 | 2007 | automático | separado | (vazio) | (vazio) | (vazio) |

- Modelo e versão como na linha do Palio Weekend Adventure do AMT7506 (FIAT, Palio Weekend, Adventure).
- CILINDRADA vazia: o anúncio não diz o motor.
- [SUPOSIÇÃO] ORIGEM "automático", como todas as 17.291 linhas da aba, porque a linha sai do texto da APLICACAO. A fonte fica no LOG_CORRECOES.
- "separado", sem MOTIVO e sem ANO_DUVIDA: nada marcado como duvidoso.

## 4. Fonte
- Anúncios na internet da Cofap GP30120, a mesma Cofap do AMT7500: "Palio Weekend Adventure 2000/2007".
- O Alexandre aceitou essa fonte **neste caso** (R-20261121-112900-alexandre, item 4: "coloque o palio no amt7500 assim como na internet").
- O LOG_CORRECOES vai dizer isso nas 2 linhas.

## 5. O que não muda
- **AMT7014 (c/ ABS):** não recebe o Palio, porque o Alexandre não pediu. O DIFERENCIAL e o ITEM_PARECIDO dele ("AMT7500 s/ ABS") ficam.
- **No AMT7500:** o DIFERENCIAL (s/ ABS), o ITEM_PARECIDO (AMT7014 c/ ABS), as referências e o OFEREÇA JUNTO (KAP11121) ficam.
  - [SUPOSIÇÃO] O KAP11121 é kit do Strada ("Strada 2008 / 2012 · STRADA 1999 / 2007"). Ele continua no "Leve também" pelo Strada.
  - Ver se ele serve no Palio Weekend é outra tarefa.
- **Outros produtos:** nenhum muda, e nenhum sai.
- **Formato:** mesmas abas e colunas. Só muda 1 célula APLICACAO, e a VEICULOS ganha 1 linha.
- **Previsto no LOG_CORRECOES:** 2 linhas, uma APLICACAO e uma VEICULO_NOVO. O LEIA-ME ganha o bloco da v25.

## 6. No site (depois de gravada)
- **Muda:** só o AMT7500.
  - O campo "a" ganha o trecho do Palio Weekend Adventure.
  - O filtro "Meu veículo" (campo "ve") ganha FIAT Palio Weekend Adventure. Os anos não vão para o site.
- **Não muda:** nenhum outro produto, as referências, a ficha, a TRAVA e a FICHA.
