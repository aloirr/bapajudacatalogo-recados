# T-0024 · Simulação da página de catálogos do admin com os 7 materiais (v2)

| Campo | Valor |
|---|---|
| Feita por | `web-site` |
| v1 | 22/11/2026, 04h34 (horário de Manaus) |
| v2 | 22/11/2026, 04h40 (horário de Manaus): aplica o parecer de UX (`docs/ux/pareceres/T-0024-simulacao.md`, f88b952) e o de marca (`docs/marca/pareceres/T-0024-simulacao.md`, MC-0013, 7c54cee) |
| Base | main 942cf1c |

É **só a simulação** (regra 3). Nada em `site/`, em `servicos/` ou no `render.yaml` foi alterado. Não houve commit nem push.

## Como abrir

```
python3 -m http.server 8024 -d t0024-sim
```

| Endereço | O que é |
|---|---|
| http://localhost:8024/admin/pdfs/ | a tela nova (v2) |
| http://localhost:8024/admin/pdfs/estados.html | os estados da tela nova |
| http://localhost:8024/admin/pdfs/index_v1.html | a v1, para comparar |
| http://localhost:8024/admin/pdfs/antes.html | a tela de hoje |

- O `sim-mock.js` responde `/api/eu` e `/api/pdfs` sem o serviço de login.
- O `conta-sim.js` é a cópia do `conta.js` com o item do menu "Catálogos e materiais".
- Esses dois arquivos são só da simulação.
- O CSS do site está copiado sem mudança. O que é novo está em `admin/pdfs/sim.css`.
- Os tamanhos e as datas são **de exemplo**. A faixa verde do alto existe só na simulação.

## Prints (Playwright, Chromium)

| Tela | 1366 px | 390 px |
|---|---|---|
| Antes (hoje: 2 PDFs) | `prints/antes_1366.png` | `prints/antes_390.png` |
| Depois v1 (7 cartões; frase da T-0022 no Completo Digital) | `prints/depois_v1_1366.png` | `prints/depois_v1_390.png` |
| **Depois v2** (6 cartões e 7 arquivos; para o Alexandre) | `prints/depois_1366.png` | `prints/depois_390.png` |
| Depois v2, com o menu da conta aberto | `prints/depois_menu_1366.png` | `prints/depois_menu_390.png` |
| Estados v2 | `prints/estados_1366.png` | `prints/estados_390.png` |

A página de estados mostra:
- um PowerPoint em falta, com só o botão dele desabilitado;
- um PDF em falta;
- os Lubrificantes com datas diferentes;
- a lista vazia;
- o erro;
- o carregando.

### Conferências da v2 (depois e estados, em 1366 e 390 px)
- Não há rolagem para o lado: o `scrollWidth` é 1366 e 390.
- Há um único `h1`.
- Nenhum botão tem menos de 48 px de altura. Nenhum botão sai do cartão nem corta o texto.
- Toda imagem tem `alt`.
- A palavra "Tipo" não aparece na tela.
- O texto não tem "R$", "preço" nem "estoque".
- Não há erro de script nem erro no console.
- O par de botões dos Lubrificantes:
  - em 1366 px, fica lado a lado;
  - em 390 px, fica um embaixo do outro.
- O nome acessível dos botões é "Baixar PDF · Lubrificantes e Químicos" e "Baixar PowerPoint · Lubrificantes e Químicos".
- No menu aberto, os itens são "Criar usuários", "Catálogos e materiais" e "Trocar senha".

Também conferi o par de botões em outras larguras:

| Largura | Par de botões |
|---|---|
| 1920 e 1280 px | lado a lado |
| 1100 e 1024 px | um embaixo do outro: o cartão tem 1/3 de largura e é mais estreito |
| 900 px | lado a lado: 2 colunas |
| 768 e 641 px | um embaixo do outro |

Em todas essas larguras, os botões ficam dentro do cartão.

## O que mudou da v1 para a v2

| # | Pedido | O que foi feito |
|---|---|---|
| UX 1 | Tirar a linha "Tipo" | Saiu dos cartões. O tipo fica no ícone, na extensão e no botão. |
| UX 2 | Tirar o contador e a frase dos grupos | O grupo agora é só o `h2`: "Catálogos" e "Apresentações e materiais". |
| UX 3 | Textos de estado | Ver a tabela abaixo. |
| UX 4 | Nome da página | Mudou no `h1`, na trilha, no `<title>` e no item do menu (`conta-sim.js`). |
| UX 5 | Alternativa B | Um cartão só para "Lubrificantes e Químicos". Ver abaixo. |
| Marca MC-0013 | Frase do Completo Digital | "Para enviar aos clientes e ver na tela." passou a **"Todos os itens, para ver na tela."** |

- O nome da página na v2 é **"Catálogos e materiais"**, com o subtítulo "Sempre a versão mais nova de cada arquivo.". **O Alexandre decide** entre esse nome e o de hoje, "Catálogos em PDF".
- **A troca da frase do Completo Digital vai ao Alexandre como mudança.** A frase antiga foi aprovada nas telas da T-0022 (decisão 9 a). Para comparar:
  - antes: `prints/antes_*.png` e `prints/depois_v1_*.png`;
  - depois: `prints/depois_*.png`.
  - A pergunta do `design-de-marca` vai junto: ele quer um catálogo completo para mandar aos clientes? Isso seria outro material, sem a marca de uso interno, numa tarefa do `catalogo-grafico`.

Textos de estado (no passo 2, no `pdfs.js` e no `index.html`):

| Estado | Texto |
|---|---|
| Arquivo em falta (cartão de 1 arquivo) | "Este arquivo não está disponível agora. Tente de novo mais tarde." |
| Arquivo em falta (cartão de 2 arquivos) | "O PowerPoint não está disponível agora." ou "O PDF não está disponível agora." Só aquele botão fica desabilitado. |
| Lista vazia | "Nenhum arquivo por enquanto." |
| Erro | "Não foi possível carregar os arquivos agora. Atualize a página em instantes." |
| Carregando | "Carregando os arquivos…" |

## Organização da tela (v2)

- **"Catálogos"** (`h2`): Completo Digital, A4 gráfica e Linha Moto.
- **"Apresentações e materiais"** (`h2`): Portfólio de Produtos, Lubrificantes e Químicos (os 2 arquivos num cartão) e Kit Filtros.
- São 3 e 3 cartões, e nenhum cartão fica sozinho na linha em 1366 px.
- Cada cartão tem:
  - o ícone "PDF";
  - o título (`h3`, 18 px);
  - a frase de uso;
  - o arquivo, o tamanho e a data ("Atualizado em");
  - o botão no pé do cartão.
- O tamanho abaixo de 1 MB aparece em KB ("249 KB").
- Colunas: 3 a partir de 1024 px, 2 no tablet e 1 até 640 px.

### O cartão dos Lubrificantes (alternativa B, item 5 do parecer de UX)

| Elemento | Como fica |
|---|---|
| Título | "Lubrificantes e Químicos" |
| Ícone | o "PDF", igual ao dos outros cartões |
| Frase | "A apresentação comercial: em PDF para ver ou enviar, em PowerPoint para editar." |
| Arquivo | "BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial (.pdf e .pptx)". Se um arquivo faltar, só a extensão do que existe. |
| Tamanho | "PDF 6,6 MB · PowerPoint 7,3 MB" |
| Atualizado em | Uma data só, quando as duas são iguais. Diferentes: "PDF 14/11/2026 15:20 · PowerPoint 10/11/2026 09:00". |
| Botões | "Baixar PDF" é o principal (`.bt`). "Baixar PowerPoint" é o secundário (`.bt .bt-claro`, que já existe no `styles.css`). |

- O espaço fixo (`&nbsp;`) mantém "PowerPoint 7,3 MB" numa linha só. A quebra cai no "·".
- Os 2 botões ficam lado a lado no computador e um embaixo do outro em 390 px, com a largura toda.
- **Medida do par de botões no cartão de 1/3 (330 px por dentro):**
  - com o padding de 26 px e o texto de 16 px, os 2 botões somam 345 px e não cabem;
  - no par, o padding cai para 12 px e o texto para 14 px, a medida do `.bt-mini`. A altura continua 48 px, e os 2 somam uns 310 px;
  - onde o cartão é mais estreito (de 1024 a 1199 px e no tablet), o `flex-wrap` põe o segundo botão embaixo.
  - O `designer-ux` confere essa medida no reteste.
- **Um arquivo em falta:** só o botão dele fica desabilitado, e a frase dele aparece acima dos botões. O outro botão continua funcionando.
- **A junção vem da lista fixa do serviço, e não do navegador.**
  - Os 2 itens dos Lubrificantes têm o mesmo `par: "lubrificantes"`.
  - O `pdfs.js` junta os itens com o mesmo `par` num cartão, na ordem da lista: o primeiro é o principal, o segundo é o secundário.
  - O navegador nunca lê o nome do arquivo para decidir isso.
  - **A API continua com 7 itens.**

## Lista proposta (lista FIXA do serviço, na ordem da tela)

| Grupo | id | Título (API) | Arquivo (padrão) | Tipo | Par |
|---|---|---|---|---|---|
| catalogos | `completo-digital` | Completo Digital | `Catalogo_BAP_<ano>_Completo_Digital.pdf` (hoje 2027) | pdf | não |
| catalogos | `a4-grafica` | A4 gráfica | `Catalogo_BAP_<ano>_A4_grafica.pdf` (hoje 2027) | pdf | não |
| catalogos | `linha-moto` | Linha Moto | `Catalogo_BAP_<ano>_Linha_Moto.pdf` (hoje 2027) | pdf | não |
| materiais | `portfolio` | Portfólio de Produtos | `Portfolio_Produtos_BAP_AUTOPARTS.pdf` | pdf | não |
| materiais | `lubrificantes-pdf` | Lubrificantes e Químicos | `BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial.pdf` | pdf | `lubrificantes` |
| materiais | `lubrificantes-pptx` | Lubrificantes e Químicos | `BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial.pptx` | pptx | `lubrificantes` |
| materiais | `kit-filtros` | Kit Filtros | `Kit_Filtros_BAP.pdf` | pdf | não |

- Os nomes dos arquivos foram conferidos em `catalogo_grafico/entregas/` no 942cf1c.
- Os 3 catálogos têm o ano no nome. O serviço continua escolhendo o de ano mais alto entre os que casam.
- Os outros 4 arquivos não têm ano. A regex deles é o nome exato, e "a versão mais nova" é o arquivo que está no main.
- **[SUPOSIÇÃO]** O `catalogo-grafico` mantém esses 4 nomes. Se o ano entrar no nome, a regex ganha o `(\d{4})` e o `buildFilter` muda junto.

## O que muda no serviço (`servicos/login/server.mjs`, dono `integracao-placas`)

1. **A lista fixa `PDFS`** passa de 2 para 7 itens, cada um com `grupo` e `tipo`. Os 2 dos Lubrificantes também têm `par`:
   ```js
   { id: 'completo-digital', titulo: 'Completo Digital', grupo: 'catalogos', tipo: 'pdf', re: /^Catalogo_BAP_(\d{4})_Completo_Digital\.pdf$/ },
   { id: 'a4-grafica', titulo: 'A4 gráfica', grupo: 'catalogos', tipo: 'pdf', re: /^Catalogo_BAP_(\d{4})_A4_grafica\.pdf$/ },
   { id: 'linha-moto', titulo: 'Linha Moto', grupo: 'catalogos', tipo: 'pdf', re: /^Catalogo_BAP_(\d{4})_Linha_Moto\.pdf$/ },
   { id: 'portfolio', titulo: 'Portfólio de Produtos', grupo: 'materiais', tipo: 'pdf', re: /^Portfolio_Produtos_BAP_AUTOPARTS\.pdf$/ },
   { id: 'lubrificantes-pdf', titulo: 'Lubrificantes e Químicos', grupo: 'materiais', tipo: 'pdf', par: 'lubrificantes', re: /^BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial\.pdf$/ },
   { id: 'lubrificantes-pptx', titulo: 'Lubrificantes e Químicos', grupo: 'materiais', tipo: 'pptx', par: 'lubrificantes', re: /^BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial\.pptx$/ },
   { id: 'kit-filtros', titulo: 'Kit Filtros', grupo: 'materiais', tipo: 'pdf', re: /^Kit_Filtros_BAP\.pdf$/ },
   ```
   - Todas as regex são ancoradas (`^...$`), com o ponto escapado, sem `/`, sem `..` e sem curinga além do ano.
   - O desenho final do campo `par` é do `integracao-placas` com o `web-site`.
2. **`acharPdf`:** trocar a ordenação para `Number(m[1] || 0)`. Nos nomes sem ano, `Number(undefined)` dá `NaN`.
   - A conferência de hoje continua: o caminho real tem de ser igual ao caminho pedido (sem link simbólico) e tem de ser um arquivo.
3. **`GET /api/pdfs`:** devolve os **7 itens**, cada um com `id`, `titulo`, `grupo`, `tipo`, `par` (ou `null`), `arquivo`, `tamanho` e `data`.
   - Ele continua só para o admin. O usuário comum recebe 404.
4. **`Content-Type` do download** (`baixarPdf`): sai de um mapa fixo pelo `tipo` da lista, nunca pela extensão do pedido.
   - `pdf` → `application/pdf`;
   - `pptx` → `application/vnd.openxmlformats-officedocument.presentationml.presentation`.
   - O resto fica igual: `Content-Disposition: attachment`, `Cache-Control: private, no-store`, `nosniff` e a rota `/admin/pdfs/baixar/:id`.
5. **Comentários:** "os 2 PDFs" passa a "os 7 arquivos da lista", no `server.mjs` e no comentário do serviço no `render.yaml`.
6. **Testes** (`servicos/login/login.test.mjs`):
   - admin: os 7 ids dão 200, com o `Content-Type` certo;
   - usuário comum: 404 na página, na API e nos 7 downloads;
   - id fora da lista: 404;
   - os nomes dos `.xlsx` e dos `.png` de `entregas/`: 404, como id e codificados (com `%2F`, `..` e `%2e%2e`);
   - a base `BASE_BAP_UNIFICADA_PRODUTOS_BAP.xlsx` e qualquer caminho para `dados/`: 404;
   - o `Aplicacoes_Catalogo_Online_Antes_Depois_*.pdf`: 404, porque é PDF mas não está na lista.

## O que muda no site (`site/`, dono `web-site`, no passo 2, depois do "aprovado")

- **`site/admin/pdfs/pdfs.js`:**
  - os grupos, com um `h2` cada;
  - o cartão com `h3`;
  - a junção pelo `par`, com o botão principal e o secundário e a desabilitação de um botão só;
  - o tamanho em KB abaixo de 1 MB;
  - as frases de uso do `USO`, com o Completo Digital como "Todos os itens, para ver na tela." (MC-0013);
  - os textos de estado da tabela acima;
  - o nome acessível " · <título>", no lugar de " do <título>".
- **`site/admin/pdfs/index.html`:** o `<title>`, a trilha, o `h1` e o subtítulo com o nome escolhido, e "Carregando os arquivos…".
- **`site/conta.js:71`:** o item do menu, se o nome mudar.
- **`site/admin/admin.css`:** o bloco do `sim.css`, sem a faixa da simulação. A regra `.pdf h2` (admin.css:86) sai. O CSS do ícone "PPT" da v1 não entra, porque o cartão B usa o ícone "PDF".
- `docs/DADOS_DO_SITE.md` não muda: o `produtos.json` fica igual.

## `buildFilter` do `render.yaml` (governança: vai como bloco ao PO)

O `render.yaml` é do Alexandre. Este é o bloco proposto para o serviço `bapajudacatalogo-login`:

```yaml
    buildFilter:
      paths:
        - site/**
        - servicos/login/**
        - catalogo_grafico/entregas/Catalogo_BAP_*_Completo_Digital.pdf
        - catalogo_grafico/entregas/Catalogo_BAP_*_A4_grafica.pdf
        - catalogo_grafico/entregas/Catalogo_BAP_*_Linha_Moto.pdf
        - catalogo_grafico/entregas/Portfolio_Produtos_BAP_AUTOPARTS.pdf
        - catalogo_grafico/entregas/BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial.pdf
        - catalogo_grafico/entregas/BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial.pptx
        - catalogo_grafico/entregas/Kit_Filtros_BAP.pdf
```

E o comentário acima do serviço:

```yaml
  # Login do catálogo (T-0022, T-0024): serve o site/ inteiro só com login. Sem rootDir: lê site/ e os 7 arquivos da lista fixa de catalogo_grafico/entregas/.
```

## Riscos e cuidados

- **Só a lista fixa abre.**
  - O serviço nunca lista nem serve a pasta `entregas/` inteira.
  - Ele não aceita nome de arquivo vindo do navegador, só o `id` da lista.
  - Não entra "tudo que é .pdf/.pptx".
- **`dados/` nunca entra.** A `PASTA_PDFS` continua sendo só `catalogo_grafico/entregas/`, e nenhuma regex casa com a base `.xlsx`.
- **Ficam de fora os arquivos internos de `entregas/`:**
  - os 6 `.xlsx`: Alteracoes, Auditoria, Conferencia, Encartelados, Fotos_pendentes e Itens_sem_aplicacao;
  - os 2 `.png` de simulação;
  - o `Aplicacoes_Catalogo_Online_Antes_Depois_*.pdf`.
- **O `buildFilter` não protege nada.**
  - Sem `rootDir`, o Render baixa o repositório inteiro, e os `.xlsx` e a base de `dados/` existem no disco do serviço.
  - O `buildFilter` só decide quando o serviço é publicado de novo.
  - Quem protege é a lista fixa, com os testes do item 6. [SUPOSIÇÃO] O Render se comporta como hoje (T-0022).
- **Uso interno:** o Completo Digital, o A4 e a Linha Moto trazem "USO INTERNO E CONFIDENCIAL". A página é só do admin, e a frase do Completo Digital deixou de falar em clientes (MC-0013).
- **Preço e estoque:**
  - conferi o texto dos 6 PDFs e dos 11 slides do .pptx, e não há preço nem estoque;
  - o "custo" que aparece é do veículo "GMC ... Custom";
  - o "preço acessível" é texto institucional, sem valor.
- **Os 7 arquivos somam uns 44 MB.** O download continua em stream (`pipeline`).
- **Nome com ano novo:** se aparecer, por exemplo, `Portfolio_..._2027.pdf`, o cartão mostra "Este arquivo não está disponível agora" até a lista mudar. Nunca abre um arquivo errado.
- **Observação fora da T-0024:** em 320 px, o botão da conta no cabeçalho passa 20 px da tela (`scrollWidth` 340). A tela de hoje (`antes.html`) também tem isso. Em 390 px não acontece.

## Arquivos da simulação

| Arquivo | O que é |
|---|---|
| `admin/pdfs/index.html` | a tela v2 |
| `admin/pdfs/estados.html` | os estados v2 |
| `admin/pdfs/sim.css` | o CSS novo da v2 |
| `admin/pdfs/index_v1.html` e `admin/pdfs/sim_v1.css` | a v1 |
| `admin/pdfs/antes.html` e `admin/pdfs/pdfs.js` | a tela de hoje (cópia do site) |
| `sim-mock.js` | as respostas de exemplo da API |
| `conta-sim.js` | o menu com o nome novo |
| `styles.css`, `conta.js`, `entrar/` e `assets/` | cópias do site, sem mudança |
| `prints/` | os prints da tabela acima |
