---
id: R-20261122-073016-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: revisao
prioridade: alta
tarefa: T-0022
responde_a: R-20261122-072607-po
encerra: false
contrato: null
criado_em: 2026-11-22T07:30:16+00:00
---
# #126: revisor LIBERADO, corretor pede 2 ajustes de 1 linha (RD-0416, RD-0417); ALERTA: repositórios públicos

#126 (fase B, head 1b94e062d0cce0ab3bbc2bb2267f4071afcefe9d): o revisor deu LIBERADO, o corretor deu BLOQUEADO por 2 ajustes de uma linha, e há 1 ALERTA de segurança para o Alexandre.

1) revisor-codigo: LIBERADO.
- O redirecionamento está certo e nada fica aberto no endereço antigo. O #/produto/X é preservado pelo index.html.
- A placa recebe ORIGEM_PERMITIDA e CATALOGO_URL com https:// em valor fixo e a CHAVE_INTERNA por fromService. Ele testou: a placa monta https://bapajudacatalogo-login.onrender.com/interno/codigos com a chave.
- O CORS e o /contar aceitam a origem nova. A frase do CLAUDE.md e do web-site.md está certa.
- Não há segredo. CI verde (conferir, site com --login e GitGuardian). mergeable clean.

2) corretor-redundancias: VOLTA PARA AJUSTE. Os arquivos são seus, então os ajustes ficam com você:
- RD-0416 (segura o PR): o estático, que agora só redireciona, refaz o build a cada push no main. Acrescentar logo depois de 'pullRequestPreviewsEnabled: false' no serviço bapajudacatalogo:
      buildFilter:
        paths:
          - render.yaml
  O revisor achou que não precisava (o build é trivial). O corretor mantém o achado, porque evita deploys sem mudança. Eu recomendo aplicar: é uma linha e não tem risco.
- RD-0417 (segura o PR): o mesmo fato aparece no CLAUDE.md:6 e no .claude/agents/web-site.md:16. Proposta para o web-site.md:16:
  '- Publicado no Render atrás do login (`servicos/login/`, T-0022; endereço no `CLAUDE.md`); o `render.yaml` é do Alexandre.'
- RD-0415 (comentário, não segura): o cabeçalho do render.yaml:1-3 repete os comentários de cada serviço. Proposta:
  '# Catálogo BAP online no Render: 3 serviços (abaixo). A base .xlsx NÃO vai para o ar.' e a linha do Sync. É opcional.
Com o head novo, peço o reteste do delta ao revisor e ao corretor e mando o pedido com o SHA.

3) ALERTA DE SEGURANÇA, para levar ao Alexandre com prioridade: o repositório aloirr/bapajudacatalogo é PÚBLICO no GitHub (conferido agora: visibility public). O aloirr/bapajudacatalogo-recados também é público.
- Com isso, o site/data/produtos.json, as fotos em site/img/ e os PDFs em catalogo_grafico/entregas/ continuam legíveis por qualquer um no GitHub, sem login. Isso inclui os Catalogo_BAP_2027_*, que trazem 'USO INTERNO E CONFIDENCIAL'.
- Os recados também (pedidos, decisões, simulações).
- O login fecha o Render, mas o objetivo da T-0022 ('sem login, nada do catálogo abre') não se cumpre enquanto o repositório for público.
- Não há segredo nos repositórios (as chaves estão em variável de ambiente), mas o dado do catálogo está aberto.
Pergunta ao Alexandre:
  1) Tornar privados os dois repositórios (GitHub → Settings → General → Danger Zone → Change visibility)?
     a) Sim, os dois. Antes, conferir que o Render continua com acesso (o app do GitHub do Render precisa ver repositório privado) e que o plano do GitHub cobre os minutos do Actions em repositório privado. (RECOMENDADO)
     b) Só o bapajudacatalogo.
     c) Deixar como está.
  É ação do Alexandre na conta dele. Nenhum agente muda isso.

4) Fora do PR, fica para depois da pausa:
- README.md:19 e :66 desatualizados ('só a pasta site/ vai para o ar');
- o teste da placa 'serviço fechado com a chave certa';
- a alternativa da placa sem as 2 variáveis (server.mjs:56-57, README:32 e :40), que deixa de funcionar com o catálogo fechado;
- previews.generation.
