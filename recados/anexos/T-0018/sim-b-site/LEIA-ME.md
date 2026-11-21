# Simulação T-0017, bloco B11 e "Leve também" por sistema (21/11/2026)

Pedido: R-20261121-190649-alexandre (bloco B, item "s/ ABS" do AMT7500; decisão 4, "Leve também" pelo sistema).
É só simulação: esta pasta não vai para o `main` nem para o Render.

## B11: "Outros veículos e detalhes" com o veículo de cada detalhe

- Hoje, o detalhe sem veículo vira um item solto: no AMT7500, "s/ ABS" aparece duas vezes (uma do Strada e outra do Palio Weekend), sem dizer de qual é.
- Proposta: o detalhe vai no mesmo item do veículo a que pertence, que é o veículo de antes no mesmo bloco da aplicação (" ; ").
  - O veículo vem em negrito, sem a marca do começo do bloco, e os detalhes vêm depois dos dois-pontos, separados por " · ".
  - AMT7500: "**Strada 01/2001–12/2020**: Adventure · s/ ABS · exc. Locker / Cabine Dupla / Prato Pequeno · c/ barra estab." e "**Palio Weekend Adventure 2000–2007**: s/ ABS".
- O layout geral não muda: a mesma seção, a mesma lista, com menos itens. A ficha impressa ("Aplicação completa") não muda.
- A linha conta como veículo quando é a 1ª do bloco, tem ano ou é coberta pela tabela. Senão, é detalhe do veículo de antes.
- Muda em **794 produtos**, de 3.089 com a seção (lista: `outros-veiculos.csv`). [SUPOSIÇÃO] Quando o texto da base mistura veículo e detalhe sem ano ("Diant Esq / Porsche Cayenne"), o veículo pode ser lido como detalhe. Exemplo: o TER5597056 fica com "Q7: Diant Esq / Porsche Cayenne · …".
- Outra opção, mais curta: tirar só a linha repetida, e o "s/ ABS" aparece uma vez. Ela não diz de qual veículo é o "Adventure" nem o "exc. Locker", por isso não foi a escolhida.
- Prints: `prints/antes-AMT7500-apl-1366.png`, `prints/depois-AMT7500-apl-1366.png` e as mesmas em 390 px.

## "Leve também" por sistema (lado do site)

- **De onde vem:** do campo `oj` do JSON, que é a coluna OFERECA_JUNTO da base, copiada do catálogo na v11. O `app.js` só lê os códigos (`listaCodigos`) e filtra pelo veículo e pelo UNIVERSAL de outra família (`servemNoVeiculo`). Os PDFs calculam o "Leve também" deles no `oferta.py`, e por isso os dois podem dar resultados diferentes.
- **CUB60235:** no site, ele **não tem "Leve também"**: a OFERECA_JUNTO dele está vazia na v25. O par com o ROL32008 e o ROL32009 vem só dos PDFs (`oferta.py`). Com a regra nova, os dois saem (conferido no `doSistema` do site: ROL32008 sai e ROL32009 sai).
- **Regra simulada:** a peça só oferece outra do mesmo sistema ou de um sistema compatível (`SIS_COMPAT`, no `app.js`). O item fora do catálogo ou sem sistema fica, como hoje.
- **Tabela:** é a mesma do rascunho do catalogo-grafico (`oferta.SIS_COMPAT`, worktree sim-b, ainda sem commit). Ela vai da origem para os sistemas aceitos e não é simétrica: o semi-eixo oferece o cubo, e o cubo não oferece o rolamento de câmbio.

  | Origem | Aceita |
  |---|---|
  | SUSPENSÃO | SUSPENSÃO, DIREÇÃO |
  | DIREÇÃO | DIREÇÃO, SUSPENSÃO |
  | TRANSMISSÃO | TRANSMISSÃO, CÂMBIO E DIFERENCIAL, RODAGEM |
  | CÂMBIO E DIFERENCIAL | CÂMBIO E DIFERENCIAL, TRANSMISSÃO |
  | RODAGEM | RODAGEM, FREIO |
  | FREIO | FREIO, RODAGEM, QUÍMICOS |
  | ARREFECIMENTO | ARREFECIMENTO, MOTOR, QUÍMICOS |
  | MOTOR | MOTOR, ARREFECIMENTO, FILTRAÇÃO, ELÉTRICA |
  | ELÉTRICA | ELÉTRICA, MOTOR, LUBRIFICANTES |
  | FILTRAÇÃO | FILTRAÇÃO, MOTOR, LUBRIFICANTES |
  | LUBRIFICANTES | LUBRIFICANTES, FILTRAÇÃO, ELÉTRICA |
  | QUÍMICOS | QUÍMICOS, ARREFECIMENTO, FREIO |

- **Por que só o SISTEMA da base não basta:** a base põe todos os 194 rolamentos em RODAGEM, inclusive os de câmbio e diferencial. Só com o SISTEMA, **nenhum** produto do site muda e o cubo continua oferecendo o rolamento de câmbio.
  - O rolamento ganha os sistemas que o texto dele diz (DESCRICAO, DETALHE_CATALOGO e a POSICAO dos DADOS_ADICIONAIS), com a mesma leitura do catalogo-grafico (`sistemas_de` no `gerar_site.py`). Vai para o JSON no campo `ss`, só o nome do sistema, em 132 rolamentos. O resultado é igual ao do catalogo-grafico nos 194.
  - [SUPOSIÇÃO] O melhor é a base trazer esse sistema (v26, catalogo-dados). Aí o site e os PDFs leem a coluna e não o texto.
- **Resultado:** **40 produtos** do site têm o "Leve também" alterado (de 1.974 com a seção). Saem 59 itens, e em 36 produtos a seção some. A lista completa está em `leve-tambem.csv`:
  - 28 cubos de roda deixam de oferecer o rolamento de câmbio ou diferencial: CUB60001, CUB60002, CUB60003, CUB60004, CUB60009, CUB60010, CUB60013, CUB60014, CUB60015, CUB60016, CUB60017, CUB60021, CUB60022, CUB60023, CUB60024, CUB60029, CUB60037, CUB60041, CUB60053, CUB60058, CUB60107, CUB60108, CUB60114, CUB60122, CUB60123, CUB60133, CUB60142 e CUB60202;
  - 12 rolamentos deixam de oferecer o cubo ou o rolamento de roda: ROL1000, ROL102949/102910, ROL104949/104911, ROL32007, ROL32008, ROL32009, ROL32213, ROL501349/501310, ROL6003-2RS (alternador), ROL6306-2RS, ROL6306-2Z e ROL802048/802011.
- Prints: `prints/antes-CUB60009-oj-*.png` e `prints/depois-CUB60009-oj-*.png` (a seção some), e `prints/*-CUB60002-oj-*.png` (sai o ROL32007 e fica o ROL6203-2RS).
- **Bateria:** passa toda, menos "campos do JSON": o campo `ss` ainda não está na lista do `testar_site.mjs` (do `testes`). Se a regra for aprovada, ele entra.
