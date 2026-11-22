# T-0022: desenho curto do serviço de login (integracao-placas, 21/11 ~23h)

## Achado que muda o plano
O serviço da placa baixa `ORIGEM_PERMITIDA/data/produtos.json` para conferir os códigos do `/contar` (servicos/placas/server.mjs L45-49). Com o login, esse arquivo responderia 401 e o `/contar` deixaria de contar. Solução: o login ganha uma rota interna `/interno/codigos`, que só devolve os códigos e exige uma chave interna gerada pelo Render (`generateValue` + `fromService`). Ninguém digita nem vê essa chave.

## Arquitetura
- **Serviço novo `bapajudacatalogo-login`** (Node, sem dependências, como a placa):
  - serve o site inteiro, roda da raiz do repositório e não usa rootDir;
  - um buildFilter limita o deploy a site/**, servicos/login/** e os 2 PDFs.
- **Rotas abertas:** só a tela de login, o CSS dela e a checagem de saúde.
- **Todo o resto exige sessão:** página, app.js, produtos.json e fotos. Sem sessão, a página leva ao login e o resto responde 401.
- **Só para o admin:** "Criar usuários", "Catálogos em PDF" e o download dos 2 PDFs (lista fixa). Para os outros usuários, essas rotas respondem 404.
- **Arquivos servidos:** só os de site/, com trava contra "../". A base (dados/*.xlsx) fica no disco do serviço, mas nunca é servida, e isso entra em teste.
- **O site estático atual:** vira só um redirecionamento grátis para o endereço novo. Os links #/produto/... já enviados continuam valendo.
- **Serviço da placa:** ganha o ORIGEM_PERMITIDA novo, mais `CATALOGO_URL` e `CHAVE_INTERNA`. As chamadas continuam sem cookie (credentials: omit).

## Dados (disco persistente /var/data, 1 GB)
- **usuarios.json:** gravação segura; senha com hash scrypt (sal de 16 bytes, comparação em tempo constante); mínimo de 8 caracteres.
- **Logos:** PNG, JPG ou WEBP, até 200 KB, com o tipo conferido pelos primeiros bytes; SVG não entra. Sem logo, usa a da BAP.
- **Sessão:**
  - cookie assinado (HMAC), HttpOnly, Secure, SameSite=Lax, válido por 5 h;
  - desativar o usuário ou trocar a senha dele derruba a sessão na hora;
  - nos POST, o Origin é conferido.
- **Primeiro admin:**
  - `ADMIN_SENHA_INICIAL` digitada pelo Alexandre no painel (sync: false);
  - troca obrigatória no 1º acesso;
  - sem a variável e sem usuários, o catálogo fica fechado (503).
- **Limite de tentativas:** 5 erros por usuário em 15 min e 20 por IP; a mensagem é sempre a mesma.
- **Log:** nunca leva senha, hash, cookie, segredo nem IP inteiro.

## Pastas e donos (propostos)
- `servicos/login/`: integracao-placas (mesmo tipo de trabalho da placa). Os ajustes na placa também são dele.
- Telas em `site/`: web-site.
- Testes do serviço: `node --test` em servicos/login/, pelo integracao-placas.
- Bateria do site com usuário de teste local: testes.
- Pôr os testes do login no CI mexe em `.github/`, que é governança do Alexandre.

## render.yaml (governança; PR do PO)
- **Serviço novo:** web, node, plan starter, startCommand `node servicos/login/server.mjs`, healthCheckPath `/saude`, buildFilter, disco `login-usuarios` de 1 GB em /var/data.
  - Variáveis: PASTA_DADOS, ADMIN_USUARIO, ADMIN_SENHA_INICIAL (sync: false), SESSAO_SEGREDO (generateValue) e CHAVE_INTERNA (generateValue).
- **Placa:** ORIGEM_PERMITIDA com o endereço novo, CATALOGO_URL e CHAVE_INTERNA (fromService).
- **Estático atual:** staticPublishPath para uma pasta mínima e uma rota de redirecionamento /* para o endereço novo.
- **No painel, o Alexandre só digita a senha inicial do admin.**

## Custo
[SUPOSIÇÃO: tabela do Render]
- Starter US$ 7 + disco US$ 0,25 = cerca de US$ 7,25 por mês a mais.
- Com a placa, o total fica em cerca de US$ 14,50 por mês.

## Riscos
- Serviço com disco não tem deploy sem queda: o catálogo fica de 30 a 60 s fora a cada mudança no site (já acontece com a placa).
- O catálogo fechado sai do Google e perde a prévia de link no WhatsApp.
- Uma sessão roubada vale até 5 h, ou até o usuário ser desativado.

## Perguntas ao Alexandre (recomendação marcada)
1. Endereço: a) novo, bapajudacatalogo-login.onrender.com, e o antigo redireciona; b) manter o antigo, recriando o serviço (minutos fora, e o nome pode não ser liberado). **Recomendado: a.**
2. "Cache por 5 horas": a) a sessão vence 5 h depois do login, mesmo com uso; b) vence depois de 5 h sem uso. **Recomendado: a.**
3. Busca por placa: a) continua direto do navegador, só com a origem nova; b) passa pelo login, para proteger a franquia paga da API (mais trabalho; tarefa própria depois). **Recomendado: a.**
