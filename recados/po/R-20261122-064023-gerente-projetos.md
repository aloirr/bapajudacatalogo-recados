---
id: R-20261122-064023-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0022
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T06:40:23+00:00
---
# Pedido de merge: PR #123 (o site lê o corpo do 204), head 97eacb14bc2a509d9bfbd3b65c761cbb3dff9595

Peço autorização para o merge do PR #123 (T-0022). Ele destrava o #120.

- Head: 97eacb14bc2a509d9bfbd3b65c761cbb3dff9595. Branch: web-site/T-0022-corpo-204. Um commit sobre o main d900add.
- Arquivos: site/entrar/comum.js (o api() lê o corpo também no 204) e site/app.js (o /contar lê o corpo do 204). São do web-site. Não há mudança visual; a FICHA e a TRAVA não foram tocadas.
- A causa: o Chrome Headless Shell 153 do CI marca net::ERR_ABORTED o fetch que recebe 204 sem ler o corpo. O Chromium 157 local não faz isso. Decidi consertar na origem, no site, sem abrir exceção no vigia dos testes. O branch testes/T-0022-abortado fica de reserva e não vai a PR.
- revisor-codigo: LIBERADO. Reproduziu no Chrome 153: o main d900add FALHA com os 3 erros do CI e o head 97eacb1 PASSA.
- corretor-redundancias: LIBERADO. O RD-0409 e o RD-0410 ficaram MANTIDOS: o comentário nos 2 arquivos e a leitura em 2 lugares, porque o /contar não pode usar o api() (outra origem, sem cookie, keepalive).
- CI no 97eacb1: site, conferir e GitGuardian em success. Observação: este CI ainda roda sem --login. A prova da correção é a reprodução no 153, e o CI do #120 confirma depois do merge.
- Merge: squash com expectedHeadSha e 'Agente: web-site' (T-0022).

Depois do merge, peço que você atualize o branch do #120 com o main (ou rode o CI de novo) e me mande o pedido com o SHA.
