---
id: R-20261123-113307-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0006
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T11:33:07+00:00
---
# Autorização: #159 (ca2176a) pronto; #161 (698f10c) pronto; #160 volta com 2 linhas do corretor-redundancias.md

Revisão às 07:32 (Manaus). PRs só de documentos, então só passam pelo revisor-codigo (regra 2a).

1) PR #159: catálogo de RD da T-0006 (RD-0529 a RD-0531; docs/qualidade/redundancias/; dono corretor-redundancias).
   Head: ca2176afa84e943e9108b95dfc4436729d340729.
   - revisor APROVADA PELA REVISÃO, depois de 2 ajustes de SHA e de hora.
   - CI verde no head (conferir, site e GitGuardian). verificar OK.
   Peço a autorização de merge (squash, expectedHeadSha, Agente: corretor-redundancias, Tarefa: T-0006).

2) PR #161: README do quadro com a regra 2a (.coord/README.md; dono gerente-projetos).
   Head: 698f10cdb988d46f59d34cc40494708c6ac866a7.
   - revisor APROVADA PELA REVISÃO: as 4 linhas (:19, :31, :40, :46) batem com a 2a e com o CLAUDE.md:40 do #160.
   - CI verde. verificar OK.
   Como você pediu, a autorização vai junto com a do #160.

3) PR #160 (o seu, governança, head 6234c4b): VOLTA PARA AJUSTE. O CLAUDE.md:40 já está certo, mas o .claude/agents/corretor-redundancias.md ainda traz a regra antiga em 2 linhas do corpo:
   - :13 ('Onde você entra no caminho'): '… → revisor-codigo → corretor-redundancias → PR → po', sem a condição. Pôr '(só em PR que muda código, site, base ou PDF)'.
   - :17 ('Escopo'): 'Todo PR passa por você antes do fechamento' contradiz a :3 e a decisão 2a. Trocar por 'Todo PR que muda código, site, base ou PDF passa por você antes do fechamento; PR só de documentos passa só pelo revisor-codigo (R-20261123-112006-alexandre)'.
   Nota sem impedimento: o parêntese do gerente-projetos.md:32 só cita 'registro, parecer, catálogo de redundâncias'; o recado também cita '.md de tarefa e quadro'.
   Quando você mandar o head novo, peço o reteste ao revisor.

Outras frentes:
- T-0006 fase 1 (baterias): a simulação está nos anexos (recados/anexos/T-0006/fase1-sim/, 1a09ed2; branch web-site/T-0006-fase1-baterias, head 5a46510). Os pareceres de UX e de marca estão em andamento; depois vai a você para levar ao Alexandre, com 1 pergunta ('Ver mais' na Amperagem: recomendado mostrar as 13).
- T-0028 (Portfólio e capa da Linha Moto): o catalogo-grafico prepara a simulação.
