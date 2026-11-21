# T-0019 · simulação B (B8, B9, B10 e "Leve também" por sistema)

Pedido: R-20261121-190649-alexandre (bloco B e "Leve também" por sistema só em simulação). Branch `catalogo-grafico/T-0019-sim-b`, sobre o main `8de7a6d`. **Nada foi trocado em `entregas/`.** Gerado com `PYTHONHASHSEED=0`, um processo por PDF; a trava não deu `[PARADO]`.

- **Antes:** os PDFs do main `8de7a6d` em `catalogo_grafico/entregas/`.
- **Depois:** cada item gerado sozinho, com a chave `SIM_B` (`gerador/sim_b.py`): `SIM_B=B8`, `B9`, `B10` ou `LT`; sem `SIM_B`, as quatro juntas. As chaves são só desta simulação: depois do "aprovado", saem e fica o código aprovado.
- **Pranchas:** 150 ppi, antes à esquerda e depois à direita.

## Páginas e números de página
| Mudança | A4 (56) | Digital (308) | Linha Moto (17) | Muda número de página? |
|---|---|---|---|---|
| B8, última linha da aplicação | 56 | 308 | 17 | não |
| B8, marca e código juntos | 56 | **312** | 17 | **sim, no Digital**: a partir de Pivô de Suspensão (p.29 vira p.30) até o fim (Rolamentos Moto p.305 vira p.309). No A4 e no Moto, não |
| B9 | 56 | 308 | 17 | não (A4 p.21; Digital p.110 e 111) |
| B10 | 56 | 308 | 17 | não (só A4 p.20; no Digital e no Moto não há tag NOVO sobre texto) |
| "Leve também" por sistema | 56 | 308 | 17 | não (A4 p.43 e 44; Digital p.254 a 274; Moto igual) |
| As quatro juntas | 56 (múltiplo de 4) | 312 | 17 | como a B8 |

O Digital cresce 4 páginas por causa da B8 nas referências: com a marca presa ao código, a referência que antes quebrava no meio ("Cofap / GP32986") desce inteira para a linha de baixo e a célula EQUIVALE A ganha uma linha em várias linhas da tabela. Se o Digital não puder crescer, a alternativa é ligar a B8 das referências só no A4 e no Moto (as páginas não mudam lá).

## B8 · espaço inseparável
- **Referências:** `digital2.refs_juntas`: o espaço entre a marca (1 palavra; 2 nas marcas de 2 nomes do `fraga_complementos.DUAS`, como "Magneti Marelli") e o código vira espaço inseparável. Vale no Digital, no Moto e no A4 (tabela e destaques). O resto quebra como antes: entre as referências e dentro de código com espaço ("Sachs 3400 700 639").
- **Última linha:** `digital2.sem_viuva`, no fim do `markup` (toda aplicação dos 3 PDFs) e na frase "Aplicações também para" do A4: o último espaço vira inseparável; se a palavra de antes é só um separador ("·", "/", "-"), prende mais um, para a linha não começar com o separador.
- `01` A4 p.13: "Chery." sozinho; agora "e Chery.".
- `02` Digital p.17 (AMT7500): "ABS" sozinho; agora "s/ ABS".
- `03` Digital p.4: "Cofap / GP32986" e "TRW / G38002D"; agora "Cofap GP32986" e "TRW G38002D".
- `04` Digital p.281 (antes) e p.285 (depois; a página andou 4): "Autoimpact / PU14"; agora "Autoimpact PU14".
- [SUPOSIÇÃO] Não prendi o "·" à referência de antes (a linha ainda pode começar com "·"); se quiser, é uma troca a mais no `refs_juntas`.

## B9 · subtítulo do SCE14002 (RD-0252)
- `detalhe._tail` recebe a aplicação do item (`detalhe.aplicar` → `compacto` → `_tail`). Na hora de completar o texto cortado com a DESCRICAO, sai o trecho de **5 ou mais palavras seguidas** que estão todas na aplicação. Trecho curto fica: com a regra "qualquer palavra da aplicação", mudavam 19 itens e alguns perdiam informação ("Serv./estac. 16/24 agrale/ford/", "âmbar reto)"); com 5 palavras, só muda o SCE14002.
- SCE14002: "Servo embreagem cilindro curto s/ indicador MBB LS 1630 1929 1932 1934 LS1941 VWC 16210 17240 1730 - 111693" vira "Servo embreagem cilindro curto s/ indicador".
- `05` A4 p.21 e `06` Digital p.110: o subtítulo cai de 4 para 2 linhas e a faixa do código dos 5 cartões volta à altura normal (a mesma do SCE14010 e dos outros).
- Observação: o DETALHE_CATALOGO da base tem "s/ indicador **desgaste**"; o subtítulo ainda vem do texto antigo cortado ("sem indicador…"). Trocar a fonte do subtítulo é outra tarefa.

## B10 · tag NOVO (proposta do designer-ux)
- `digital2.novo_desce`: quando o código e a tag NOVO não cabem juntos na coluna do código, a tag desce para a linha de baixo, sem mudar a largura das colunas. Com tags (DIANT., C/ ABS...), vai na frente delas; sem tags, fica na 1ª linha da descrição curta, com o texto recuado (`digital2.novo_na_sobra`); sem as duas, sozinha. Mesma regra na tabela do A4 e do Digital.
- `07` A4 p.20: EMB3400700639R, EMB3400700648R e EMB3400700649R: a tag NOVO saiu de cima de "MB" e "VOLVO" e foi para a linha "395MM 18 estrias" / "400MM 18 estrias". As linhas não crescem e a página segue com os mesmos itens.
- Conferência (palavra NOVO sobre outra palavra): A4 3 no main, 0 depois; Digital e Moto 0 e 0.
- Os destaques (cartões) não mudam: a tag fica no canto e o código já diminui para caber; nenhum caso nos 3 PDFs.

## "Leve também" por sistema
- `oferta.sis_ok`: a peça oferecida é do mesmo sistema do item ou de um compatível. Vale na busca do par (`_pares`: a peça de outro sistema nem entra, e a busca segue para o próximo alvo da linha) e no par que veio pronto (`_por_sistema`, para o do `cross.py`).
- **O SISTEMA da base sozinho não muda nada:** cada linha do catálogo tem um SISTEMA só, e os pares de sistemas diferentes que existem hoje são os das REGRAS (pivô → terminal, semi-eixo → cubo...). O ROL32008 e o ROL32009 estão em **RODAGEM** na base, como o CUB60235. Por isso, no rolamento, o sistema sai do texto dele (POSICAO dos DADOS_ADICIONAIS, DESCRICAO e DETALHE_CATALOGO): câmbio, diferencial, coroa, pinhão → "CÂMBIO E DIFERENCIAL"; cardã, semi-eixo, embreagem → TRANSMISSÃO; roda, cubo → RODAGEM; alternador, polia, tensor → MOTOR. Pode ter mais de um (ROL15106/15250: cubo e diferencial). Sem nada no texto, fica o SISTEMA da base.
- [SUPOSIÇÃO] O melhor lugar para isso é a base (um SISTEMA certo nos rolamentos de câmbio e diferencial, pelo `catalogo-dados`); aqui o PDF só lê o texto.

### Tabela de compatíveis (proposta, origem → aceitos)
| Sistema do item | Pode oferecer |
|---|---|
| SUSPENSÃO | SUSPENSÃO, DIREÇÃO |
| DIREÇÃO | DIREÇÃO, SUSPENSÃO |
| TRANSMISSÃO | TRANSMISSÃO, CÂMBIO E DIFERENCIAL, RODAGEM (semi-eixo → cubo e rolamento de roda) |
| CÂMBIO E DIFERENCIAL (rolamento, pelo texto) | CÂMBIO E DIFERENCIAL, TRANSMISSÃO |
| RODAGEM | RODAGEM, FREIO (cubo → sensor ABS) |
| FREIO | FREIO, RODAGEM, QUÍMICOS (fluido DOT) |
| ARREFECIMENTO | ARREFECIMENTO, MOTOR, QUÍMICOS |
| MOTOR | MOTOR, ARREFECIMENTO, FILTRAÇÃO, ELÉTRICA |
| ELÉTRICA | ELÉTRICA, MOTOR, LUBRIFICANTES (vela → óleo 4T) |
| FILTRAÇÃO | FILTRAÇÃO, MOTOR, LUBRIFICANTES |
| LUBRIFICANTES | LUBRIFICANTES, FILTRAÇÃO, ELÉTRICA |
| QUÍMICOS | QUÍMICOS, ARREFECIMENTO, FREIO |
| ACESSÓRIOS | ACESSÓRIOS |
| OUTROS | OUTROS |

Não é simétrica de propósito: o semi-eixo oferece o cubo, mas o cubo não oferece o rolamento do cardã nem o do câmbio.

### Contagem
- **78 "Leve também" mudam nos 3 PDFs**, em **68 itens**: Digital 68 (49 cubos e 19 rolamentos), A4 10 (CUB60002, 60003, 60004, 60009, 60013, 60014, 60015 na p.43; ROL1000, ROL102949/102910 e ROL104949/104911 na p.44), Linha Moto 0.
- Exemplo pedido: CUB60235 "ROL32008 · ROL32009" vira "ABS4517 · ABS4557" (Digital p.262, `10`); ROL32008 e ROL32009 "CUB60131"/"CUB60000" viram "—" (Digital p.265, `11`). A4: `08` p.43 e `09` p.44.
- 22 itens ficam com "—" porque não sobra par do mesmo sistema: os 19 rolamentos da lista (câmbio, diferencial, alternador) e os cubos CUB60068, CUB60209 e CUB60229.
- Fica para outra tarefa: alguns rolamentos sem texto que diga onde vão continuam em RODAGEM pela base e ainda são oferecidos para cubos (ex.: ROL608-2Z, "ferramentas elétricas", no CUB60097 e no CUB60152).

| Item | Linha | Digital p. | No A4 | Antes | Depois |
|---|---|---|---|---|---|
| CUB60001 | Cubo de Roda | 254 | — | ROL84887 | ROL78349/78310 |
| CUB60002 | Cubo de Roda | 254 | sim | ROL32007 · ROL6203-2RS | ROL6203-2RS · ROL6203-2Z |
| CUB60003 | Cubo de Roda | 254 | sim | ROL84887 | ROL6203-2RS · ROL6203-2Z |
| CUB60004 | Cubo de Roda | 254 | sim | ROL32007 · ROL6203-2RS | ROL6203-2RS · ROL6203-2Z |
| CUB60009 | Cubo de Roda | 255 | sim | ROL1000 · ROL32009 | ROL4529A |
| CUB60010 | Cubo de Roda | 255 | — | ROL84887 | ROL3577 |
| CUB60013 | Cubo de Roda | 255 | sim | ROL84887 | ROL6203-2RS · ROL6203-2Z |
| CUB60014 | Cubo de Roda | 255 | sim | ROL1000 · ROL32007 | ROL4529A |
| CUB60015 | Cubo de Roda | 255 | sim | ROL1000 | ABS4523 |
| CUB60016 | Cubo de Roda | 255 | — | ROL102949/102910 · ROL501349/501310 | ROL48548/48510 · ROL6303-2RS |
| CUB60017 | Cubo de Roda | 255 | — | ROL1000 | ABS4523 |
| CUB60021 | Cubo de Roda | 255 | — | ROL1000 · ROL32007 | ROL4529A |
| CUB60022 | Cubo de Roda | 255 | — | ROL1000 | ABS4501 |
| CUB60023 | Cubo de Roda | 255 | — | ROL102949/102910 · ROL501349/501310 | ROL48548/48510 · ROL6303-2RS |
| CUB60024 | Cubo de Roda | 255 | — | ROL102949/102910 · ROL104949/104911 | ROL48548/48510 · ROL6303-2RS |
| CUB60029 | Cubo de Roda | 256 | — | ROL102949/102910 · ROL104949/104911 | ROL48548/48510 · ROL6303-2RS |
| CUB60037 | Cubo de Roda | 256 | — | ROL1000 | ABS4501 |
| CUB60039 | Cubo de Roda | 256 | — | ROL32008 · ROL32009 | ABS4517 · ABS4557 |
| CUB60041 | Cubo de Roda | 256 | — | ROL1000 · ROL32009 | ROL4529A |
| CUB60042 | Cubo de Roda | 256 | — | ROL32008 · ROL32009 | ABS4501 · ABS4517 |
| CUB60053 | Cubo de Roda | 257 | — | ROL104949/104911 · ROL6303-2RS | ROL6303-2RS · ROL6303-2Z |
| CUB60055 | Cubo de Roda | 257 | — | ROL32009 | ROL0036 |
| CUB60058 | Cubo de Roda | 257 | — | ROL1000 · ROL32007 | ABS4500 · ABS4501 |
| CUB60064 | Cubo de Roda | 257 | — | ROL102949/102910 · ROL104949/104911 | ROL48548/48510 · ROL6303-2RS |
| CUB60068 | Cubo de Roda | 257 | — | ROL104949/104911 | — |
| CUB60069 | Cubo de Roda | 257 | — | ROL32009 | ROL0036 |
| CUB60082 | Cubo de Roda | 258 | — | ROL104949/104911 · ROL15106/15250 | ROL15106/15250 · ROL25590/25522 |
| CUB60093 | Cubo de Roda | 258 | — | ROL32009 · ROL4529A | ROL4529A |
| CUB60097 | Cubo de Roda | 258 | — | ROL32008 · ROL608-2Z | ROL608-2Z |
| CUB60107 | Cubo de Roda | 258 | — | ROL102949/102910 · ROL104949/104911 | ROL48548/48510 · ROL6303-2RS |
| CUB60108 | Cubo de Roda | 258 | — | ROL104949/104911 | ROL6303-2RS · ROL6303-2Z |
| CUB60114 | Cubo de Roda | 259 | — | ROL1000 · ROL32007 | ABS4500 |
| CUB60122 | Cubo de Roda | 259 | — | ROL1000 · ROL32007 | ABS4500 |
| CUB60123 | Cubo de Roda | 259 | — | ROL1000 · ROL212049/212011 | ROL212049/212011 · ROL218248/218210 |
| CUB60133 | Cubo de Roda | 259 | — | ROL1000 · ROL32007 | ABS4523 |
| CUB60142 | Cubo de Roda | 259 | — | ROL84887 | ROL3577 |
| CUB60149 | Cubo de Roda | 260 | — | ROL102949/102910 · ROL104949/104911 | ROL368A/362A · ROL48548/48510 |
| CUB60152 | Cubo de Roda | 260 | — | ROL84887 | ROL608-2Z |
| CUB60153 | Cubo de Roda | 260 | — | ROL32009 · ROL32007 | ROL45449/45410 |
| CUB60154 | Cubo de Roda | 260 | — | ROL1000 · ROL11949/11910 | ROL11949/11910 · ROL32213 |
| CUB60159 | Cubo de Roda | 260 | — | ROL84887 | ROL6203-2RS · ROL6203-2Z |
| CUB60162 | Cubo de Roda | 260 | — | ROL32007 | ROL6202-2RS · ROL6202-2Z |
| CUB60171 | Cubo de Roda | 260 | — | ROL32008 | ROL32213 · ROL368A/362A |
| CUB60181 | Cubo de Roda | 261 | — | ROL1000 | ROL32213 · ROL368A/362A |
| CUB60192 | Cubo de Roda | 261 | — | ROL32009 · ROL32007 | ROL212049/212011 · ROL218248/218210 |
| CUB60202 | Cubo de Roda | 261 | — | ROL102949/102910 · ROL501349/501310 | ROL6303-2RS · ROL6303-2Z |
| CUB60209 | Cubo de Roda | 261 | — | ROL807046/807010 | — |
| CUB60229 | Cubo de Roda | 262 | — | ROL6003-2RS · ROL6205-2RS | — |
| CUB60235 | Cubo de Roda | 262 | — | ROL32008 · ROL32009 | ABS4517 · ABS4557 |
| ROL1000 | Rolamentos | 264 | sim | CUB60015 · CUB60017 | — |
| ROL102949/102910 | Rolamentos | 264 | sim | CUB60202 · CUB60016 | — |
| ROL104949/104911 | Rolamentos | 264 | sim | CUB60107 | — |
| ROL30205 | Rolamentos | 265 | — | CUB60131 · CUB60142 | — |
| ROL30206 | Rolamentos | 265 | — | CUB60142 | — |
| ROL30306 | Rolamentos | 265 | — | CUB60135 | — |
| ROL32007 | Rolamentos | 265 | — | CUB60131 | — |
| ROL32008 | Rolamentos | 265 | — | CUB60131 | — |
| ROL32009 | Rolamentos | 265 | — | CUB60000 | — |
| ROL32010 | Rolamentos | 265 | — | CUB60026 · CUB60044 | — |
| ROL32307 | Rolamentos | 266 | — | CUB60135 | — |
| ROL501349/501310 | Rolamentos | 267 | — | CUB60202 · CUB60016 | — |
| ROL6003-2RS | Rolamentos | 269 | — | CUB60003 · CUB60009 | — |
| ROL6003-2RS-C3 | Rolamentos | 269 | — | CUB60003 · CUB60009 | — |
| ROL6003-2Z | Rolamentos | 269 | — | CUB60003 · CUB60009 | — |
| ROL6306-2RS | Rolamentos | 273 | — | CUB60135 | — |
| ROL6306-2RS-C3 | Rolamentos | 273 | — | CUB60135 | — |
| ROL6306-2Z | Rolamentos | 273 | — | CUB60135 | — |
| ROL802048/802011 | Rolamentos | 274 | — | CUB60202 · CUB60016 | — |

## Conferência
- Páginas: A4 56, Digital 312 (308 sem a B8 das referências), Moto 17. Tamanho: 13,2 MB, 5,9 MB e 0,8 MB. Aviso de uso interno em todas (56, 312 e 17).
- Texto sobreposto (pares de palavras que se cruzam, contra o main, as 4 mudanças juntas): A4 381 → 379 (saem os da tag NOVO), Digital 403 → 403, Moto 66 → 66; nenhum par novo.
- Unittests (`teste_fraga_complementos`, `teste_autoimpact_pdf`): OK.

## Pranchas
`01` a `04` B8 · `05` e `06` B9 · `07` B10 · `08` a `11` "Leve também".
