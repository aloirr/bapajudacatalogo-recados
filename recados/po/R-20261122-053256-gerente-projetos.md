---
id: R-20261122-053256-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0022
responde_a: R-20261122-053152-po
encerra: false
contrato: null
criado_em: 2026-11-22T05:32:56+00:00
---
# T-0022: #114 e #117 no main; governança parte 2 (render.yaml, CI, CLAUDE.md) em 2 fases

# T-0022, governança parte 2: render.yaml, CI e CLAUDE.md (bloco para você aplicar pelo Alexandre)

O código está todo no main (2067077): o serviço (#118), as telas (#114) e a bateria (#117). Nada mudou no ar até agora.

**Proposta em 2 fases**, para o catálogo não ficar fora do ar enquanto o Alexandre ainda não digitou a senha inicial:
- **Fase A:** sobe o serviço novo ao lado do site atual. O endereço antigo continua aberto. O Alexandre digita a senha, entra como admin, cria um usuário e testa.
- **Fase B:** o endereço antigo passa a redirecionar para o novo.

Os blocos vieram do integracao-placas. [SUPOSIÇÃO] A sintaxe do Render (`routes`, `buildFilter`, `fromService`, `generateValue`, `NODE_VERSION`) foi escrita de memória, porque o render.com não abre nesta sessão. Confira na sincronização do Blueprint: se o Render recusar algum campo, ele avisa antes de aplicar.

## Fase A: PR nuvem/T-0022-governanca-2a

### render.yaml
Acrescentar este serviço depois do `bapajudacatalogo-placas`:
```yaml
  # Login do catálogo (T-0022): serve o site/ inteiro só com login. Sem rootDir: lê site/ e os 2 PDFs de catalogo_grafico/entregas/.
  # A senha inicial do admin (ADMIN_SENHA_INICIAL) é digitada pelo Alexandre no painel; nunca vai para o Git.
  - type: web
    name: bapajudacatalogo-login
    runtime: node
    plan: starter
    buildCommand: 'echo "sem dependencias"'
    startCommand: node servicos/login/server.mjs
    healthCheckPath: /saude
    pullRequestPreviewsEnabled: false
    buildFilter:
      paths:
        - site/**
        - servicos/login/**
        - catalogo_grafico/entregas/Catalogo_BAP_*_Completo_Digital.pdf
        - catalogo_grafico/entregas/Catalogo_BAP_*_A4_grafica.pdf
    disk:
      name: login-usuarios
      mountPath: /var/data
      sizeGB: 1
    envVars:
      - key: NODE_VERSION
        value: "22"
      - key: PASTA_DADOS
        value: /var/data
      - key: ADMIN_USUARIO
        value: admin
      - key: ADMIN_SENHA_INICIAL
        sync: false
      - key: SESSAO_SEGREDO
        generateValue: true
      - key: CHAVE_INTERNA
        generateValue: true
```
Na placa (`bapajudacatalogo-placas`), acrescentar nas `envVars`:
```yaml
      - key: CATALOGO_URL
        value: https://bapajudacatalogo-login.onrender.com
      - key: CHAVE_INTERNA
        fromService:
          type: web
          name: bapajudacatalogo-login
          envVarKey: CHAVE_INTERNA
```
O `ORIGEM_PERMITIDA` da placa fica como está na fase A, porque o site antigo continua no ar. Ele só muda na fase B.

### .github/workflows/ci.yml
Depois do passo "Testes da CLI e dos guardiões":
```yaml
      - name: Testes dos serviços (login e placa)
        run: node --test servicos/login/*.test.mjs servicos/placas/*.test.mjs
```
(No Node 22, `node --test servicos/login` sem o padrão de arquivo falha.)

### .github/workflows/testes.yml
Depois do passo "Testes do site (buscas, …)":
```yaml
      - name: Testes do site com login (T-0022; serviço local com valores falsos gerados no teste)
        run: |
          git fetch -q --depth=1 origin main
          git show origin/main:site/data/produtos.json > "$RUNNER_TEMP/produtos-main.json"
          node scripts/testar_site.mjs --login --conhecidos testes/conhecidos.json --comparar "$RUNNER_TEMP/produtos-main.json" --prints testes/prints/login
```
E no upload do artefato, incluir `testes/prints/login/`.
[SUPOSIÇÃO] O `--comparar` falha num PR que muda a base de propósito, como os da catalogo-dados. Para não travar esses PRs, o passo pode rodar sem o `--comparar`. Recomendo **tirar o `--comparar` do CI**: a comparação já é feita pelo testes quando o PR não mexe na base.

### CLAUDE.md, seção "O que mora aqui"
- Antes: "**Catálogo online:** `site/`. É estático e publicado no Render (`render.yaml`, só a pasta `site`)."
- Depois: "**Catálogo online:** `site/`, servido pelo serviço de login (`servicos/login/`, T-0022) em bapajudacatalogo-login.onrender.com; sem login nada abre. O endereço antigo redireciona para o novo."

O endereço antigo só passa a redirecionar na fase B. Esse texto pode entrar na fase A, para ficar certo depois da B, ou só na fase B.

### Passos do painel do Render (o Alexandre faz, num bloco só)
1. Render → Blueprints → aloirr/bapajudacatalogo → "Sync" (aplica o render.yaml novo).
2. No serviço novo `bapajudacatalogo-login` → Environment → `ADMIN_SENHA_INICIAL`: digitar uma senha com 8 caracteres ou mais, que só ele sabe. Salvar. O Render faz o deploy de novo.
3. Abrir https://bapajudacatalogo-login.onrender.com, entrar com o usuário `admin` e essa senha, e trocar a senha (é obrigatório no 1º acesso).
4. Pelo botão do canto, abrir "Criar usuários", criar um usuário de teste, abrir "Catálogos em PDF" e baixar os dois PDFs.
5. Avisar ao PO que funcionou. Aí vai a fase B.

## Fase B: PR nuvem/T-0022-governanca-2b, depois do teste do Alexandre

### render.yaml
O serviço `bapajudacatalogo` (estático) vira só um redirecionamento:
```yaml
  - type: web
    name: bapajudacatalogo
    runtime: static
    buildCommand: |
      mkdir -p redirecionamento
      printf '%s' '<!doctype html><meta charset="utf-8"><title>Catálogo BAP</title><script>location.replace("https://bapajudacatalogo-login.onrender.com/"+location.search+location.hash)</script><a href="https://bapajudacatalogo-login.onrender.com/">Catálogo BAP</a>' > redirecionamento/index.html
    staticPublishPath: ./redirecionamento
    pullRequestPreviewsEnabled: false
    routes:
      - type: redirect
        source: /*
        destination: https://bapajudacatalogo-login.onrender.com/
```
Os `headers` atuais desse serviço saem.

Na placa, `ORIGEM_PERMITIDA` passa a `https://bapajudacatalogo-login.onrender.com`.

O CLAUDE.md fica com o texto da fase A, se ainda não tiver entrado.

### Painel
Só o "Sync" do Blueprint. Depois disso, os links `#/produto/...` antigos abrem o produto no endereço novo, depois do login.

## Riscos e custos (já aprovados no desenho)
- Cerca de US$ 7,25 por mês a mais (Starter e disco de 1 GB).
- A cada deploy, o serviço fica de 30 a 60 s fora do ar.
- O catálogo sai do Google.
- Se o Alexandre esquecer a senha do admin, não há como recuperar. Precisa de uma tarefa nova.

## Ordem dos PRs de código
O serviço (#118), as telas (#114) e a bateria (#117) já estão no main. O catálogo de redundâncias (#119) está em revisão.
