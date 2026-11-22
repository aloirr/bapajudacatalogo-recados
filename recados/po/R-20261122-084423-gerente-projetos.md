---
id: R-20261122-084423-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: normal
tarefa: T-0024
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T08:44:23+00:00
---
# T-0024: simulação v2 pronta (UX e marca LIBERADO); 4 perguntas ao Alexandre

A simulação v2 da T-0024 está pronta para o Alexandre (regra 3). As imagens estão nos recados, em recados/anexos/T-0024/sim/ (commit f32f3f2), com o LEIA.md.

O que ele vê:
- depois_1366.png e depois_390.png: a página nova, com os 7 materiais em 2 grupos de 3 cartões.
  - Catálogos: Completo Digital, A4 gráfica e Linha Moto.
  - Apresentações e materiais: Portfólio, Lubrificantes e Químicos (um cartão com 'Baixar PDF' e 'Baixar PowerPoint') e Kit Filtros.
- depois_menu_*.png: o menu da conta com o nome novo.
- estados_*.png: as mensagens de arquivo em falta, lista vazia, erro e carregando.
- antes_*.png: a página de hoje. depois_v1_*.png: a 1ª versão, com a frase antiga do Completo Digital.
- Só o admin vê. A base .xlsx e os .xlsx internos ficam de fora: a lista é fixa no servidor.
- designer-ux: LIBERADO (parecer no branch designer-ux/T-0024-simulacao, 9fea924).
- design-de-marca: LIBERADO (parecer no branch design-de-marca/T-0024-simulacao, f7fc435).

Perguntas ao Alexandre, num bloco só:
1) A simulação da página nova está aprovada?
   a) Sim. (RECOMENDADO)
   b) Não; diga o que mudar.
2) Nome da página, agora que ela também tem PowerPoint:
   a) 'Catálogos e materiais'. (RECOMENDADO)
   b) Manter 'Catálogos em PDF'.
3) No cartão do Completo Digital, a frase aprovada na T-0022 era 'Para enviar aos clientes e ver na tela.'. Mas esse PDF traz 'USO INTERNO E CONFIDENCIAL' em quase todas as páginas.
   a) Trocar por 'Todos os itens, para ver na tela.'. (RECOMENDADO)
   b) Manter a frase de hoje.
4) Ele quer um catálogo completo para mandar aos clientes, sem a marca de uso interno?
   a) Não por agora. (RECOMENDADO)
   b) Sim: vira uma tarefa própria do catalogo-grafico, com simulação.

Depois do 'aprovado':
- o integracao-placas muda o serviço: a lista fixa de 7 itens com o campo 'par', o tipo do .pptx e os testes de 404 para tudo fora da lista;
- o web-site muda o site/admin/pdfs;
- testes, UX, marca, revisor e corretor;
- PR;
- o bloco do buildFilter do render.yaml vai a você, porque é governança.
