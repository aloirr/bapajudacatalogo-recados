---
id: R-20261128-002839-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: alta
tarefa: T-0045
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-28T00:28:39-04:00
---
# RETOMADA — estado na pausa

# RETOMADA — estado na pausa (28/11/2026, 00:30 Manaus)

Pausa pedida pelo Alexandre no recado R-20261128-002524-alexandre. Desde então, nenhum PR e nenhum merge. O que estava rodando parou num ponto seguro: só houve commit e push nos branches das tarefas. Ficaram intactos o main (faadcc7), o site e a base. Retomamos só com o "retomar" do Alexandre.

## No ar
- **main:** faadcc7, do #247. A tela do produto tem os botões no rodapé e a largura única.
- **Site:** bapajudacatalogo-login.onrender.com, com login. Usa o JSON da base v31 (#245).
- **Base:** v31 (#244). A v32 está no branch e ainda não entrou no main.
- **PDFs em entregas/:** os mesmos de antes da pausa. A geração única espera a v32.

## Frentes, por ordem de retomada
| # | Frente | Branch / head | Aprovação | Já feito | Falta, na ordem |
|---|---|---|---|---|---|
| 1 | PR curto da T-0045 (RD-0767, RD-0769, overflow só na tela e toque de 44 px na trilha) | web-site/T-0045-rd0767 · 99cf5d4 | item 116 do R-20261128-000107-alexandre | no 9b334f2: designer-ux 🟢, design-de-marca LIBERADO e testes PASSOU. O revisor devolveu um achado de gravidade baixa (a 390 px, em 1.101 produtos, a área de toque cobria 4 px do código); a correção está no 99cf5d4 | 1) medir os 4.419 produtos a 390 e a 1366 px no 99cf5d4, além do A4 do VEL7520 e do testar_site; 2) reteste curto do designer-ux; 3) revisor; 4) corretor; 5) PR; 6) autorização do po; 7) merge |
| 2 | v32 da base (T-0047) | catalogo-dados/T-0047-v32 · 4281efa | P1–P6 no R-20261127-224247-alexandre; P7 no item 111 do R-20261128-000107-alexandre | `--refazer` gravado (10 células, 6 linhas no LOG_CORRECOES, nenhuma mudança de formato); testes PASSOU | 1) revisor (parado na pausa: começar de novo); 2) corretor; 3) PR, só com a base; 4) autorização; 5) merge. Depois: o JSON da v32 com a ficha P4–P6 (web-site) e a geração única dos PDFs |
| 3 | T-0032, onda 2 + onda 1 dos treinamentos | catalogo-grafico/T-0032-onda2b · 4105e7b | onda 2 e 6 motivos na decisão 93 (item 5 do R-20261127-224247-alexandre); onda 1, Fornecedor e ATENÇÃO nos itens 113–115 do R-20261128-000107-alexandre | designer-ux 🟢 no 917a2ec; design-de-marca LIBERADO no 4105e7b; os 20 PPTX/PDF estão em entregas/ (71 MB) | 1) revisor (parado na pausa: começar de novo); 2) corretor; 3) PR, que no corpo cita o onda2-sim com o Onboarding s16 e s23 (decisão 93); 4) autorização; 5) merge |
| 4 | Busca com hífen e "todas as palavras" (T-0043) | web-site/T-0043-busca-hifen · 44774e1 (já traz o main) | itens 118 e 119 do R-20261128-000107-alexandre | o compara-busca.txt saiu do site; o testar_site passou no web-site | 1) bateria completa do testes, com a T-0033 inteira (parada na pausa: começar de novo); 2) revisor; 3) corretor; 4) PR; 5) autorização; 6) merge |
| 5 | Pareceres em docs (só revisor) | design-de-marca/T-0045-simulacao · 005cbe1; design-de-marca/T-0045-pr-curto · f33eef6 (sai do anterior); design-de-marca/T-0032-onda2b-final · 5af057b; corretor-redundancias/T-0045-tela · dc53802; corretor-redundancias/T-0043-repetidas · cff1a45 | — | pareceres gravados | juntar num PR de documentos por dono, depois dos PRs 1 a 4 |
| 6 | PDFs da T-0045 (botões no rodapé, Aplicação em "L") | catalogo-grafico/T-0045-sim-pdf · ed98b0d | R-20261127-224247-alexandre | simulação aprovada | entra na geração única, depois da v32 |
| 7 | T-0046 (anos da Fraga) | catalogo-dados/T-0046-lista · c58e2cc | R-20261127-225955-alexandre | lista de 3.069 linhas | parada até voltar o anos_pesquisa_T0046.csv (backlog); depois, a simulação da v33 |

**Não iniciadas, todas com simulação antes:**
- T-0053, posição do BIE20062;
- T-0054, HR V e CR V passando a HR-V e CR-V;
- T-0006, fases 2 e 3;
- T-0048, lote 1;
- lista A da T-0037 e rolamentos "Motos Honda";
- T-0052.

**Próximo PR de registro (gerente):**
- a seção "Backlog do Alexandre (manual)";
- as tarefas T-0052, T-0053 e T-0054;
- os rodapés fora do padrão (.pagina-busca com 96 px e .sb-corpo com 104 px);
- os 3 achados de dado: as versões "*", o R113 como Mercedes e a caixa alta do VEL7520;
- os relatórios dos testes da T-0043 e da T-0045.

**Anotações, sem decisão pendente:**
- O "TRW PN: 0" no BIE20014 é um dado antigo, que o site já esconde.
- O nome do contar_duvidoso confunde: ele conta a SITUACAO "duvidoso", não o ANO_DUVIDA.
- Os PDFs dos treinamentos embutem a fonte Inter-Bold, que vem da conversão.

## Decisões abertas
Nenhuma do Alexandre. Ao retomar, as autorizações de merge dos PRs 1 a 4 ficam com o po, conforme a regra de Merge e o R-20261128-000107-alexandre.

## Backlog do Alexandre (manual), conforme o R-20261128-001543-alexandre
- sessão local da Fraga (o CSV da T-0046);
- conferir o site com login;
- cover_40 e cover_11;
- domínio;
- segredos e painel do Render.

## Rondas e agentes
- O gerente não tem nenhuma ronda nem reserva do catálogo. O único lembrete que tinha foi apagado às 00:17.
- Nenhum agente do catálogo está rodando. Não sobrou servidor local.
- Os worktrees das frentes 1 a 4 estão limpos, nos heads da tabela.
