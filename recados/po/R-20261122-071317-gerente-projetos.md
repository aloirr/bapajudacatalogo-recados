---
id: R-20261122-071317-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: normal
tarefa: T-0023
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T07:13:17+00:00
---
# T-0023: simulação da grafia pronta (LIBERADO por UX e marca); 3 perguntas ao Alexandre

Simulação da T-0023 pronta para o Alexandre (regra 3). As imagens estão no repositório de recados, em recados/anexos/T-0023/sim/ (commit 460a903).

O que mudou: no gerador, "BAP Auto Parts" e "BAP AUTO PARTS" passam a "BAP AUTOPARTS" em 3 tipos de lugar. São 19 linhas em 7 arquivos, no branch catalogo-grafico/T-0023-grafia, commit 7c7c4db.
- Barra do topo e título. Arquivo a_A4_barra_do_topo_par.png.
- Texto visível. Arquivos b_A4_pag02_institucional_par.png, c2 e c5 ("A BAP AUTOPARTS", em "Quem somos") e c3 e c6 ("Gerente Comercial · BAP AUTOPARTS").
- Autor nos metadados do A4, do Digital, da Linha Moto, do PDF e do .pptx de Lubrificantes e do Kit Filtros. A tabela de antes e depois está no LEIA.md.
- A capa de Lubrificantes (c1 e c4) não traz o nome escrito: nela muda só o autor do arquivo. Por isso a página "Quem somos" vai junto.
- O endereço www.bapautoparts.com.br e o @bapautoparts não mudam.

Conferência:
- Não sobrou nenhum "auto parts" com espaço, em qualquer caixa, no gerador.
- Nenhuma quebra de linha mudou e as capas ficaram iguais.
- Os quadros cinza e as cores estranhas do .pptx são da geração na nuvem (fotos e tema que não estão aqui). Estão iguais no antes e no depois.
- designer-ux: LIBERADO, sem ajuste (parecer no branch designer-ux/T-0023-parecer, 27eaf4f).
- design-de-marca: LIBERADO. O parecer está no branch design-de-marca/T-0023-parecer.

Perguntas ao Alexandre, num bloco só:
1) A simulação da grafia está aprovada?
   a) Sim. Gero de novo as entregas que mudam: A4, Digital, Linha Moto, PDF e .pptx de Lubrificantes. (RECOMENDADO)
   b) Não. Diga o que mudar.
2) O design-de-marca achou um problema que já existe na entrega de hoje (MC-0010): no cabeçalho das págs. 2 a 10 do PDF de Lubrificantes, o logo branco fica sobre fundo branco e só aparece o círculo verde. O recorte está em MC-0010_logo_cabecalho_lubrificantes_atual.png. A correção é usar o logo escuro nesse cabeçalho, o mesmo que o .pptx já usa.
   a) Corrigir junto, na mesma nova geração, com simulação dessa página antes. (RECOMENDADO)
   b) Abrir uma tarefa própria para depois.
   c) Deixar como está.
3) Kit Filtros: o gerador dele tem caminhos fixos de outra máquina e não roda na nuvem. Nele, a troca é só no autor do arquivo.
   a) Deixo o código trocado e o PDF do Kit Filtros fica para a próxima vez que ele for gerado. (RECOMENDADO)
   b) Ajustar os caminhos agora e gerar de novo.

Depois do "aprovado", a ordem é:
1. O catalogo-grafico gera as entregas.
2. Testes, revisor e corretor.
3. Abro o PR e mando o pedido com o SHA.
