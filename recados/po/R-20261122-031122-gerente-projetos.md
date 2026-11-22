---
id: R-20261122-031122-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0022
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T03:11:22+00:00
---
# T-0022: desenho do login e simulação das telas, com 9 perguntas ao Alexandre num bloco só

# T-0022, passo 1: desenho do login e simulação das telas (para o Alexandre)

Anexos em `recados/anexos/T-0022/`:
- `desenho.md`: o desenho curto do serviço (integracao-placas).
- `sim-telas/prints/`: 17 telas, em 1366 e 390 px.
  - Login, erro e bloqueio.
  - Catálogo com o botão do canto fechado e aberto, para o cliente e para o admin.
  - Trocar senha, incluindo a troca obrigatória do 1º acesso.
  - Criar usuários: lista, criar, editar, trocar senha e desativar.
  - Catálogos em PDF.
  - Sessão expirada.
- `sim-telas/LEIA.md`: as escolhas de layout e as suposições.

## Revisões
- **designer-ux:** LIBERADO (parecer no branch designer-ux/T-0022-parecer-simulacao, 97ac1b5).
- **design-de-marca:** LIBERADO com ajustes (parecer no branch design-de-marca/T-0022-simulacao, 60ea1b1).
- Os ajustes que mudam o que o Alexandre vê já estão nos prints:
  - a logo do cliente fica menor que a da BAP;
  - o logo não fica cinza na linha de usuário desativado;
  - melhor contraste e foco visível;
  - textos mais diretos.
- Os dois estão conferindo os prints novos. Se acharem algo, eu aviso.

## Resumo do desenho
- **Serviço novo:** serve o site inteiro, e só com login. Sem sessão, nada abre: página, produtos.json, fotos e PDFs.
- **PDFs:** só para o admin, sempre a versão do main.
- **Sessão:** vale 5 h.
- **Senha:** hash scrypt, mínimo de 8 caracteres e troca obrigatória no 1º acesso.
- **Logo do cliente:** PNG, JPG ou WEBP, até 1 MB.
- **Tentativas:** limite por usuário e por IP.
- **Endereço:** o antigo passa a redirecionar para o novo, e os links #/produto/... já enviados continuam valendo.
- **Serviço da placa:** ganha a origem nova e uma chave interna gerada pelo Render, para continuar contando as peças mais abertas.
- **Pasta e donos:** `servicos/login/` com dono integracao-placas [SUPOSIÇÃO]. As telas ficam com o web-site.
- **Custo:** cerca de **US$ 7,25 por mês** a mais (Starter + disco de 1 GB) [SUPOSIÇÃO: tabela do Render]. O total com a placa fica em cerca de US$ 14,50 por mês.
- **Riscos:**
  - a cada deploy, 30 a 60 s fora do ar;
  - o catálogo sai do Google e perde a prévia de link no WhatsApp;
  - com um admin só, se o Alexandre esquecer a senha, a volta é pela senha inicial no painel do Render.

## Governança (sua, depois do "aprovado")
- **render.yaml:** serviço novo `bapajudacatalogo-login`, com disco e as variáveis ADMIN_USUARIO, ADMIN_SENHA_INICIAL (sync: false), SESSAO_SEGREDO e CHAVE_INTERNA (as duas últimas geradas pelo Render).
  - Placa: ORIGEM_PERMITIDA, CATALOGO_URL e CHAVE_INTERNA (fromService).
  - Estático atual: vira redirecionamento.
  - O bloco completo está em `desenho.md`.
- **donos.json:** `servicos/login/**`, com dono integracao-placas.
- **No painel, o Alexandre só digita a senha inicial do admin.**

## Perguntas ao Alexandre (para copiar e colar; recomendações marcadas)
```
T-0022, login do catálogo
1) Endereço: a) novo (bapajudacatalogo-login.onrender.com) e o antigo redireciona; b) manter o antigo, recriando o serviço (minutos fora, e o nome pode não ser liberado)
2) Sessão de 5 h: a) vence 5 h depois do login, mesmo em uso; b) vence depois de 5 h sem uso
3) Busca por placa: a) continua como hoje, direto do navegador; b) só para quem está logado (tarefa própria depois)
4) Celular, botão do canto: a) só a logo da empresa; b) faixa fina com logo e nome abaixo do cabeçalho
5) Menus do admin: a) só dentro do botão do canto; b) também no menu de cima
6) Moldura da logo do cliente: a) retângulo deitado; b) quadrado ou círculo
7) Usuário sem logo: a) logo inteiro da BAP, pequeno; b) só o símbolo "b" no círculo verde (precisa da arte)
8) Cores de erro (vermelho #B42318 e fundo #FDECEA), só no site, para erro e botão de desativar: a) aprovar; b) não
9) Aprovar o desenho e as telas como simulados: a) sim; b) dizer o que muda
Recomendado: 1) a  2) a  3) a  4) a  5) a  6) a  7) a  8) a  9) a
```

## Depois do "aprovado"
1. Você abre o PR de governança.
2. O integracao-placas faz o serviço e os testes dele. O web-site faz as telas. O testes adapta a bateria ao login.
3. Revisões: designer-ux, design-de-marca, revisor e corretor.
4. Peço a sua autorização.
5. Você leva ao Alexandre os passos do painel.
