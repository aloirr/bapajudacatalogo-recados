---
id: R-20261122-073729-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: normal
tarefa: T-0022
responde_a: R-20261122-072626-alexandre
encerra: false
contrato: null
criado_em: 2026-11-22T07:37:29+00:00
---
# #126 no main (548ce73); PAUSA: o que ficou no main, o que ficou parado e o que falta

Último recado antes da PAUSA (pedido do Alexandre, R-20261122-072626). Não há rondas agendadas, nenhum agente trabalhando e nenhum PR aberto do gerente. A retomada é só com um novo pedido do Alexandre.

## 1. O que ficou no main (main 548ce73c9fe74f6e514f4b20d12010e9d8012e83, #126)
- T-0022, login do catálogo:
  - código: serviço #118, telas #114, bateria #117, corpo do 204 #123;
  - governança: fase A #120 e fase B #126 (o endereço antigo redireciona e a placa usa o login);
  - registros: #121 e #124;
  - catálogo de RD-0401 a RD-0414: #125.
- T-0023, tarefa da grafia "BAP AUTOPARTS": #122.

## 2. O que ficou parado (branch e SHA, nada pela metade no main)
- catalogo-grafico/T-0023-grafia, c9fbf3ec5570d1492e4484e2ed077a66d1c07559: a grafia nas 19 linhas do gerador (simulação APROVADA pelo Alexandre) e a correção do MC-0010 (logo escuro no cabeçalho de Lubrificantes). Nenhuma entrega foi gerada de novo.
- designer-ux/T-0023-parecer, 27eaf4f9fd63b0bdace9cca31ca61756264fc89a: parecer de UX da simulação (LIBERADO).
- design-de-marca/T-0023-parecer, d227e724668d1cf97f232e8b2d18569bf9b36e9b: parecer de marca da simulação (LIBERADO; aponta o MC-0010).
- testes/T-0022-abortado, b59476e1ba7defee01625fb203ad9490d4fc95c3: RESERVA, não usar. A correção certa entrou no #123.
- As simulações estão nos anexos dos recados: recados/anexos/T-0023/sim/ e recados/anexos/T-0023/mc0010/.

## 3. O que falta (próximos passos, para o Alexandre)
A) Repositórios públicos: o Alexandre decidiu mantê-los públicos (R-20261122-073402-alexandre), ciente do risco. Fica registrar isso na T-0022. A regra 2 vale com atenção redobrada: tudo o que entra nos dois repositórios fica público.
B) T-0023, perguntas ao Alexandre:
   1) A simulação do MC-0010 (recados/anexos/T-0023/mc0010/) está aprovada?
      a) Sim. (RECOMENDADO)
      b) Não.
   2) PDF de Lubrificantes: as fotos vêm de entradas/bap/, que não está no Git (vem do OneDrive). Trocar uma linha para usar pptimg/, que já está no repositório? Testado: as imagens saem iguais pixel a pixel.
      a) Sim, gerar aqui. (RECOMENDADO)
      b) Ele gera na máquina dele.
   3) .pptx de Lubrificantes: falta o apply_theme.js, que não está no repositório.
      a) Ele manda o arquivo.
      b) O catalogo-grafico escreve um pequeno que dá o mesmo tema, já testado byte a byte. (RECOMENDADO)
      c) Copiar o tema só desta vez.
   4) Kit Filtros: o gerador só roda na máquina dele.
      a) Trocar só o autor do PDF atual, sem mexer nas páginas. (RECOMENDADO)
      b) Ele gera de novo na máquina dele.
   Depois: nova geração do A4, do Digital e da Linha Moto (saem iguais aqui) e de Lubrificantes. Em seguida, testes, revisor, corretor e PR com os dois pareceres, e a correção de 2 LEIA do gerador que estão errados.
C) T-0022, depois da fase B:
   - registro do #126 e dos critérios na tarefa e no quadro; os RD-0415 a RD-0417 no catálogo (próximo livre: RD-0418);
   - README.md:19 e :66 desatualizados ("só a pasta site/ vai para o ar");
   - placa: um teste para "serviço fechado com a chave certa"; a reserva "sem as 2 variáveis" deixou de servir com o catálogo fechado (servicos/placas/server.mjs:56-57, README:32 e :40);
   - previews.generation no lugar de pullRequestPreviewsEnabled (nome antigo);
   - conferir no Sync se o Render aceitou o buildFilter no site estático.
D) Acesso do gerente ao Render: só quando houver necessidade concreta. Ele aprova na tela dele, ou libera direto no ambiente BapAjudaCatalogo-GP.
E) Erro meu registrado: o corpo do commit do #122 saiu com "R-20261122-065*-po". O certo é R-20261122-065637-po, e está corrigido na T-0023.
