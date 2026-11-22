# T-0022 · Simulação das telas do login (passo 1, regra 3)

Só simulação: nada daqui entra em `site/` nem no `main`. São páginas HTML estáticas e de mentira. Nenhuma chama serviço: a
única chamada externa é a fonte Poppins do Google Fonts, igual à do site.
Os usuários, as empresas e as logos dos clientes são fictícios. O fundo do catálogo é uma cópia congelada da busca
"bomba" do site atual: dados públicos do catálogo, sem preço e sem estoque.

Para abrir: `python3 -m http.server 8010 -d <esta pasta>` e depois http://localhost:8010/login.html.
Os parâmetros dos prints são `?menu=aberto`, que abre o botão do canto, e `?dialogo=dlg-novo|dlg-editar|dlg-senha|dlg-desativar`.

## Telas e prints (`prints/`, cada um em 1366 e em 390 px)

| # | Print | Página | O que mostra |
|---|---|---|---|
| 1 | 01-login | login.html | Login: logo da BAP, usuário, senha (com "Mostrar") e "Entrar". Ajuda: "Esqueceu a senha? Fale com a BAP para receber uma nova senha." |
| 1 | 02-login-erro | login-erro.html | Erro: "Usuário ou senha incorretos." A mensagem não diz qual dos dois está errado |
| 1 | 03-login-bloqueado | login-bloqueado.html | Limite de tentativas: "Muitas tentativas seguidas. Aguarde 15 minutos e tente de novo." |
| 2 | 04-catalogo-cliente-fechado | catalogo.html | Catálogo depois do login, com o botão do canto fechado (logo da empresa e nome) |
| 2 | 05-catalogo-cliente-aberto | catalogo.html?menu=aberto | Botão aberto, para o cliente: "Trocar senha" e "Sair" |
| 2 | 06-catalogo-admin-fechado | catalogo-admin.html | Admin, botão fechado. Sem logo própria, usa a da BAP |
| 2 | 07-catalogo-admin-aberto | catalogo-admin.html?menu=aberto | Admin, botão aberto: "Criar usuários" e "Catálogos em PDF" (grupo Administração), "Trocar senha" e "Sair" |
| 3 | 08-trocar-senha | trocar-senha.html | Senha atual, nova senha e confirmação |
| 3 | 09-trocar-senha-obrigatoria | trocar-senha-obrigatoria.html | Troca obrigatória no 1º acesso: só "Nova senha" e "Confirmar" (a sessão já foi aberta com a senha inicial); sem menu, só "Sair" |
| 4 | 10-usuarios-lista | usuarios.html | Criar usuários: busca, "+ Criar usuário" e a lista (empresa e logo, nome, usuário, situação, último acesso, ações) |
| 4 | 11-usuarios-novo | ?dialogo=dlg-novo | Criar usuário: nome, empresa, usuário, senha inicial ("Gerar" e "Mostrar") e logo |
| 4 | 12-usuarios-editar | ?dialogo=dlg-editar | Editar: nome, empresa e logo (trocar ou remover). O usuário fica só para leitura |
| 4 | 13-usuarios-trocar-senha | ?dialogo=dlg-senha | Trocar a senha de um usuário (nova senha inicial; ele troca no próximo acesso) |
| 4 | 14-usuarios-desativar | ?dialogo=dlg-desativar | Confirmação de desativar; o foco começa no "Cancelar" |
| 5 | 15-pdfs | pdfs.html | Catálogos em PDF: Completo Digital e A4 gráfica, com arquivo, tamanho, data e "Baixar PDF" |
| 5 | 16-pdfs-menu-aberto | pdfs.html?menu=aberto | A mesma tela, com o botão do canto aberto |
| 6 | 17-sessao-expirada | sessao-expirada.html | Volta ao login com o aviso "Sua sessão terminou. O acesso vale 5 horas." |

São 34 prints. Os de página inteira são fullPage. Os do catálogo, os das janelas e os de menu aberto mostram só a tela visível.
Conferido em todos os prints: em 390 px, `scrollWidth <= 390`, sem rolagem para o lado; um `h1` por página; `alt` em toda
imagem; alvos de toque com 44 px ou mais (o único abaixo é o input de arquivo escondido, que é acionado pelo rótulo
"Enviar logo").

## Escolhas de layout

- **Visual do site:** usa o `styles.css` do site, copiado sem mudança, e um `sim.css` novo, feito só com as variáveis do
  `:root`. O cabeçalho é o mesmo degradê escuro do catálogo; a fonte é Poppins; os botões são os `.bt` e `.bt-claro`.
- **Login, troca obrigatória e sessão expirada:** sem cabeçalho e sem menu, porque não há nada para navegar. Usam o fundo
  da faixa do início (`--fundo-faixa`, com a linha verde embaixo) e um cartão branco no centro, com a logo escura da BAP e
  "Catálogo online". O rodapé é o de sempre, sem o "voltar ao topo".
- **Erro e aviso:** o erro fica numa caixa vermelha clara acima dos campos (`role="alert"`). A sessão expirada usa uma
  caixa verde clara (`role="status"`), porque é um aviso e não um erro.
- **Botão do canto (computador):** fica à direita do menu, com a logo da empresa numa moldura branca deitada
  (48 × 30 px, com 3 px de folga, sem cortar a logo; não passa da área do logo da BAP, MC-0002), o nome, a empresa e uma
  seta. O fundo do botão é um véu escuro (`--escuro` a 30%): o branco dá 7,7:1 até na ponta verde do cabeçalho. Aberto, mostra um cartão branco com uma logo maior, o nome,
  a empresa e o usuário, mais a etiqueta "Admin" quando for o caso. A altura do cabeçalho não muda: 66 px.
- **Botão do canto (celular, 390 px):** só a logo, numa moldura de 40 × 26 px, com 44 px de toque. O texto "Catálogo online" ao lado da logo da BAP
  some quando o usuário está logado, para caber sem rolagem. O menu aberto ocupa a largura da tela.
- **Acessibilidade do botão:** o padrão é "disclosure": um botão com `aria-expanded` e uma lista de links, e o Esc fecha.
  Não é `role="menu"`. O nome e a empresa continuam no nome acessível do botão no celular. Dentro do cartão branco, o
  foco é `--verde-txt` (o `.topo` põe contorno branco). O "Mostrar"/"Ocultar" da senha não tem `aria-label` nem
  `aria-pressed`: o texto visível muda e o `aria-controls` aponta o campo. O "Gerar" se chama "Gerar senha".
- **Campo Usuário do login:** `autocapitalize="none"`, `autocorrect="off"`, `spellcheck="false"` e `required`.
- **Criar usuários:** tabela no computador; abaixo de 900 px, cada usuário vira um cartão com rótulos. Criar, editar e
  trocar a senha abrem uma janela (`dialog`), que ocupa a tela cheia no celular. A confirmação de desativar é uma janela
  pequena também no celular.
- **Desativar, não apagar:** o cadastro e a logo ficam guardados e o botão "Reativar" volta o acesso. O admin não aparece
  com "Desativar" na própria linha. A linha desativada fica com o texto em `--texto-2`; a logo não é recolorida (MC-0003).
- **Textos neutros:** as janelas usam o nome da pessoa, não "ela" ("Maria Exemplo não entra mais no catálogo…").
- **Lista:** a coluna "Usuário" fica em Poppins 500 (MC-0005); o nome da BAP aparece como "BAP Autoparts".
- **Páginas do admin:** a faixa escura do topo leva a trilha "Catálogo › …" (em `--branco`) e a etiqueta "Só o
  administrador vê esta página", sem caixa alta e sem subtítulo que repita o aviso. A etiqueta "Admin" do menu é branca no
  `--escuro`.
- **Catálogos em PDF:** dois cartões lado a lado, um embaixo do outro no celular. Cada cartão mostra o uso, o nome do
  arquivo (que quebra depois do "_" no celular), o tamanho e a data. Os tamanhos são os das entregas atuais: 5,6 MB e
  12,6 MB. A data é fictícia.
- **Logo da BAP no cartão do login:** `alt="bap componentes de qualidade"`, como no site (MC-0006).
- **Cores novas** (propostas ao design-de-marca, como variáveis): `--erro: #B42318` (6,57:1 no branco) e
  `--erro-claro: #FDECEA` (o `--erro` sobre ela dá 5,75:1). São usadas no erro do login e no botão "Desativar".

## Suposições

- Senha com pelo menos 8 caracteres: só o tamanho, sem regra de símbolo, número ou maiúscula (desenho do serviço).
- [SUPOSIÇÃO] Bloqueio de 15 minutos depois de várias tentativas erradas.
- Logo em PNG, JPG ou WEBP, com até 1 MB. O serviço reduz a imagem ao guardar (desenho do serviço). A dica pede
  "De preferência deitada, com fundo branco ou transparente."
- [SUPOSIÇÃO] Depois do login de novo, o usuário volta para a página onde estava. Se o código não fizer isso, sai a frase
  "Entre de novo para continuar de onde parou".
- [SUPOSIÇÃO] O nome de usuário não muda depois de criado.
- [SUPOSIÇÃO] Há um admin só; a tela não cria outro admin.
- [SUPOSIÇÃO] Trocar a senha de um usuário ou desativá-lo encerra a sessão aberta dele.
- [SUPOSIÇÃO] O botão "Gerar" cria a senha inicial no navegador do admin, que a envia ao cliente por um canal seguro.
  A senha nunca é guardada em texto.

## Arquivos

- `*.html`: as telas. `sim.css` e `sim.js` são só da simulação; `sim.js` apenas abre e fecha o menu, as janelas e o
  "Mostrar".
- `styles.css`, `assets/` e `img/`: cópias do site (50 fotos da busca congelada). `logos/`: logos fictícias dos clientes.
- `_ferramentas/`: `montar.py` gera as páginas e `prints.mjs` tira os prints e confere a largura. `_ref/` guarda os prints
  e o HTML de referência do site atual.

## Revisão (22/11/2026)

O `designer-ux` e o `design-de-marca` deram LIBERADO. Os ajustes que mudam o que se vê já estão nos prints: MC-0002 a
MC-0007 e os ★1 a ★6 da UX, mais o foco no menu, os atributos do campo Usuário, o "Mostrar" acessível e o "+ Criar
usuário". Ficam para o código, no passo 2: os estados de sucesso, de erro nos campos, de busca vazia e de PDF
indisponível; a senha gerada visível e sem letras que confundem; e qualquer 401 no meio do uso levando à sessão expirada.
