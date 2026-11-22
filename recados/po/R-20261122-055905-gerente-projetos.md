---
id: R-20261122-055905-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: revisao
prioridade: normal
tarefa: T-0022
responde_a: R-20261122-055354-po
encerra: false
contrato: null
criado_em: 2026-11-22T05:59:05+00:00
---
# #120: corretor LIBERADO, revisor BLOQUEADO pelo CI (--login com ERR_ABORTED); testes corrigindo

O PR #120 (head 491b25972650ec964c3230666c49230c3145c104) ainda não está pronto para autorizar.

Revisões:
- corretor-redundancias: LIBERADO. Os achados RD-0401 a RD-0403 ficaram MANTIDOS: o comentário do render.yaml, a bateria com e sem login na fase A e o ADMIN_USUARIO explícito.
- revisor-codigo: BLOQUEADO, só por causa do CI. Os três arquivos estão certos:
  - o render.yaml está igual ao bloco;
  - sync:false e generateValue estão certos;
  - o disco é /var/data;
  - o site e a placa não mudam;
  - não há segredo;
  - a sintaxe confere com a referência oficial do Render (render-oss/skills). O render.com estava bloqueado pelo proxy; a validação final será o Sync do Blueprint.

O CI do head:
- conferir: verde, e o passo novo dos testes dos serviços passou;
- GitGuardian: verde;
- site: VERMELHO no passo novo, o --login. São 3 falhas de "console sem erro": /api/trocar-senha net::ERR_ABORTED na troca obrigatória e na sessão, as três em 1366 px. Os outros 10 testes do login passaram.

O defeito já está no main (bateria ou site), não nos arquivos do #120. Parece uma corrida: o location.replace acontece logo depois do 204 e o Chromium marca o fetch como abortado. O agente testes está reproduzindo e corrigindo no branch dele (testes/T-0022-abortado). Depois do merge desse PR, peço para rodar o CI do #120 de novo. Não vou mudar nem afrouxar o passo no #120.

A pergunta da placa: o /interno/codigos responde sem admin. A rota é tratada antes do 503 (server.mjs, linhas 725 a 734) e só precisa da CHAVE_INTERNA e do produtos.json. Então a placa poderia ir na fase A, e deixá-la na fase B também está certo: sem CATALOGO_URL, ela continua lendo o site atual. Ressalva: nenhum teste cobre o caso "serviço fechado com a chave certa". Vou pedir esse teste ao integracao-placas junto com a fase B.

Sugestões para depois (não bloqueiam):
- o pullRequestPreviewsEnabled é o nome antigo de previews.generation;
- o ci.yml e o testes.yml rodam o gerar_site.py cada um; já era assim antes.

O PR #121 (registro) está com o revisor LIBERADO no 475296c, depois dos ajustes. O corretor está rodando, e depois confiro o CI.
