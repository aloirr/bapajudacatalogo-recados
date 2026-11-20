PRONTO T-0016c

Os três ajustes do po entraram, e os 5 arquivos de teste passam (162 testes, 0 falhas). Não fiz commit, push nem PR.

O patch vai abaixo, sobre o head e6831bf10b28e9af251eda8b15a6d4d940821d3f, e substitui o T-0016b. Foi gerado com `git diff -U1 --diff-algorithm=histogram e6831bf`; o sha256 começa com 25d660cae415116b. Num clone limpo nesse commit, `git apply` deixa a árvore idêntica à minha cópia: 13 arquivos.

```diff
diff --git a/.claude/agents/gerente-projetos.md b/.claude/agents/gerente-projetos.md
index 29e9b50..6c599bb 100644
--- a/.claude/agents/gerente-projetos.md
+++ b/.claude/agents/gerente-projetos.md
@@ -36,3 +36,3 @@ Você coordena o time do repositório `aloirr/bapajudacatalogo`. Fala em **portu
    - corpo: pedido literal do Alexandre, o que foi feito, testes (com o resultado), prints, [SUPOSIÇÕES], o que ficou de fora;
-   - **merge só com a autorização do `po`** (R-20261120-111308-alexandre), inclusive os de governança: confira que a autorização em recado traz o número e o SHA do head, que o CI está verde e que as revisões saíram LIBERADO; aí você executa o merge pela integração do GitHub (`merge_pull_request` com `merge_method: "squash"` e `expectedHeadSha`). O guardião (`.claude/hooks/guarda-merge-mcp.mjs`) confere de novo e barra o merge sem a autorização do `po` para aquele número e SHA.
+   - **merge só com a autorização do `po`** (R-20261120-111308-alexandre), inclusive os de governança: confira que a autorização em recado traz o número e o SHA do head, que o CI está verde e que as revisões saíram LIBERADO; aí você executa o merge pela integração do GitHub (`merge_pull_request` com `merge_method: "squash"`, `expectedHeadSha` de 40 caracteres e `commit_message` com a tarefa e, no fim, "Agente: <dono>", R-20261120-131230-alexandre). O guardião (`.claude/hooks/guarda-merge-mcp.mjs`) confere de novo e barra o merge sem a autorização do `po` para aquele número e SHA.
 8. **Devolver ao po:** mude a situação para `EM APROVAÇÃO` no quadro e escreva no Registro da tarefa o link do PR e o resumo.
diff --git a/.claude/hooks/guarda-bash-lib.mjs b/.claude/hooks/guarda-bash-lib.mjs
index 5a20e50..d1ac760 100644
--- a/.claude/hooks/guarda-bash-lib.mjs
+++ b/.claude/hooks/guarda-bash-lib.mjs
@@ -2,3 +2,3 @@
 // Usada por .claude/hooks/guarda-bash.mjs (PreToolUse/PostToolUse) e pelos testes
-// (.claude/hooks/guarda-bash.test.mjs). Sem dependências externas.
+// (.claude/hooks/guarda-agente.test.mjs, guarda-recado.test.mjs e guarda-merge-mcp.test.mjs). Sem dependências externas.
 //
@@ -23,5 +23,57 @@ import {
   PESSOAS, podeAlterar, classificarMudancas, remetenteDoRecado, remetenteDoConteudo, ehAnexoDeRecado,
-  relativoPorJuncao, MOTIVO_CLONE_DE_RECADOS,
+  relativoPorJuncao, MOTIVO_CLONE_DE_RECADOS, juncoesDeRecados, cloneDosRecados,
 } from '../../scripts/coord-lib.mjs';
 
+// ───────────────────────────── comum aos hooks (RD-0027) ─────────────────────────────
+
+/** JSON do hook pelo stdin. null = vazio ou ilegível (cada hook decide: o de merge bloqueia, os outros seguem com {}). */
+export function lerEntradaDoHook(stdin = process.stdin) {
+  return new Promise((ok) => {
+    let txt = '';
+    stdin.setEncoding('utf8');
+    stdin.on('data', (d) => (txt += d));
+    stdin.on('end', () => {
+      try { const j = JSON.parse(txt); ok(j && typeof j === 'object' && !Array.isArray(j) ? j : null); } catch { ok(null); }
+    });
+    stdin.on('error', () => ok(null));
+  });
+}
+
+/** BAP_GUARDA=off (variável do processo do Claude Code, que o agente não altera) desliga os guardiões. */
+export const guardaDesligada = (env = process.env) => String(env.BAP_GUARDA || '').toLowerCase() === 'off';
+
+/**
+ * Junções de recados (ADR 0035) e, sem junção, o clone do repositório de recados ANEXADO à sessão (T-0016, B1): na nuvem
+ * o clone fica ao lado do repositório de código, sem junção. Com `clone` preenchido, o Write/Edit e o Bash que gravam
+ * dentro dele e o git que grava nele são bloqueados para os agentes (só o node scripts/coord.mjs grava lá).
+ */
+export function juncoesComClone(raiz, { env = process.env, juncoes = juncoesDeRecados(raiz), clone = () => cloneDosRecados({ env, raiz }) } = {}) {
+  if (juncoes?.clone) return juncoes;
+  const c = clone();
+  return c ? { mapas: juncoes?.mapas || [], clone: barras(c) } : (juncoes || { mapas: [], clone: null });
+}
+
+/**
+ * Anexos no clone de recados (T-0016c, decisão do po de 20/11/2026): o po e o gerente-projetos copiam prints, planilhas e
+ * patches para recados/anexos/** e publicam com git (pull, add, commit, push). Recados e lidos continuam só pelo coord.mjs.
+ */
+export const ANEXADORES = ['po', 'gerente-projetos'];
+export const GIT_DE_ANEXO = new Set(['pull', 'add', 'commit', 'push']);
+export const PASTA_ANEXOS = 'recados/anexos';
+/** O caminho absoluto está DENTRO de <clone>/recados/anexos/ (não a própria pasta)? */
+export function ehAnexoNoClone(abs, clone) {
+  const base = `${barras(clone).replace(/\/+$/, '')}/${PASTA_ANEXOS}/`;
+  const a = barras(abs);
+  return a.toLowerCase().startsWith(base.toLowerCase()) && a.length > base.length && !a.slice(base.length).split('/').includes('..');
+}
+/** Argumentos do git depois do subcomando (sem as opções globais -C, -c, --git-dir...). */
+export function argsDoGit(palavras) {
+  const i = palavras.findIndex((w) => !w.incerto && /(^|\/)git(\.exe)?$/i.test(w.valor));
+  let k = i + 1;
+  while (k < palavras.length && palavras[k].valor.startsWith('-')) k += /^(-C|-c|--git-dir|--work-tree|--namespace)$/.test(palavras[k].valor) ? 2 : 1;
+  return palavras.slice(k + 1);
+}
+/** Nome do comando (sem VAR=... e sem caminho). */
+const nomeDoComando = (palavras) => barras(palavras.find((w) => !/^[A-Za-z_][A-Za-z0-9_]*=/.test(w.valor))?.valor || '').split('/').pop().toLowerCase();
+
 // ───────────────────────────── caminhos ─────────────────────────────
@@ -336,3 +388,6 @@ function alvosGit(args, ctx, res) {
     if (v === '-C') { res.cwdGit = args[i + 1] && !args[i + 1].incerto ? args[i + 1].valor : null; i += 2; continue; }
-    if (['-c', '--git-dir', '--work-tree', '--namespace'].includes(v)) { i += 2; continue; }
+    // T-0016 (B1): --git-dir/--work-tree também apontam o repositório (o clone de recados, por exemplo).
+    if (v === '--git-dir' || v === '--work-tree') { res.cwdGit = args[i + 1] && !args[i + 1].incerto ? args[i + 1].valor : null; i += 2; continue; }
+    if (/^--(git-dir|work-tree)=/.test(v)) { res.cwdGit = args[i].incerto ? null : v.replace(/^[^=]*=/, ''); i++; continue; }
+    if (['-c', '--namespace'].includes(v)) { i += 2; continue; }
     i++;
@@ -683,3 +738,3 @@ function soLeituraPorArgumentos(nome, args) {
  */
-export function analisarComando({ comando, agente, cwd, raiz, regras, somenteLeitura = [], permitidos = new Set(), amb, juncoes = { mapas: [], clone: null } }) {
+export function analisarComando({ comando, agente, cwd, raiz, regras, somenteLeitura = [], permitidos = new Set(), amb, juncoes = { mapas: [], clone: null }, gitNoClone = null }) {
   const violacoes = [];
@@ -732,3 +787,14 @@ export function analisarComando({ comando, agente, cwd, raiz, regras, somenteLei
         soLeitura = false;
-        acusar(`git ${r.gitSub} @ ${cwdCmd}`, `git ${r.gitSub} no clone de recados: ${MOTIVO_CLONE_DE_RECADOS}`);
+        // T-0016c: anexos (recados/anexos/**) do po e do gerente-projetos: pull, add, commit e push conferidos por gitNoClone.
+        const semGitDir = !cmd.palavras.some((w) => /^--(git-dir|work-tree)/.test(w.valor) || /^GIT_/.test(w.valor));
+        const anexo = gitNoClone && ANEXADORES.includes(agente) && GIT_DE_ANEXO.has(r.gitSub) && juncoes.clone && semGitDir
+          ? gitNoClone({ sub: r.gitSub, args: argsDoGit(cmd.palavras), cwd: cwdCmd, clone: juncoes.clone })
+          : MOTIVO_CLONE_DE_RECADOS;
+        if (anexo) acusar(`git ${r.gitSub} @ ${cwdCmd}`, `git ${r.gitSub} no clone de recados: ${anexo}`);
+      }
+      // T-0016 (B1): com o clone de recados presente, git que grava numa pasta incerta (cd $X, cd ~/..., git -C $X) pode
+      // ser o clone: bloqueado (escreva a pasta por extenso).
+      if (r.gitSub && !GIT_LEITURA_NO_CLONE.has(r.gitSub) && r.gitSub !== 'clone' && cwdCmd === null && juncoes.clone) {
+        soLeitura = false;
+        acusar(`git ${r.gitSub} @ ?`, `git ${r.gitSub} numa pasta incerta ($VAR, ~ ou $(...)), que pode ser o clone de recados (${MOTIVO_CLONE_DE_RECADOS}): escreva a pasta por extenso`);
       }
@@ -746,2 +812,4 @@ export function analisarComando({ comando, agente, cwd, raiz, regras, somenteLei
           const j = relativoPorJuncao(a, juncoes);
+          // T-0016c: arquivo em recados/anexos/** do clone, pelo po ou pelo gerente-projetos (cp, mkdir...; ln não).
+          if (j?.clone && ehAnexoNoClone(a, juncoes.clone) && ANEXADORES.includes(agente) && nomeDoComando(cmd.palavras) !== 'ln') continue;
           if (j?.clone) { acusar(a, `"${t.alvo.valor}": ${MOTIVO_CLONE_DE_RECADOS}`); continue; }
diff --git a/.claude/hooks/guarda-bash.mjs b/.claude/hooks/guarda-bash.mjs
index 6d0da27..f165136 100644
--- a/.claude/hooks/guarda-bash.mjs
+++ b/.claude/hooks/guarda-bash.mjs
@@ -40,3 +40,3 @@
 //        po@bapajuda.invalid em comando de outro agente).
-//    Mensagens e casos: .claude/hooks/guarda-merge-lib.mjs e guarda-merge.test.mjs.
+//    Mensagens e casos: .claude/hooks/guarda-merge-lib.mjs, guarda-merge-mcp.test.mjs e guarda-recado.test.mjs.
 //  - Guardião v6 (T-0050): o bloqueio "recado em nome do Alexandre" vale SÓ para comando que cria, altera,
@@ -52,3 +52,4 @@
 //    caminho de verdade do clone segue as regras de .coord/recados, o git que grava no clone é bloqueado e a foto do
-//    PostToolUse inclui o git status do clone (juncoesDeRecados; casos em guarda-juncao.test.mjs).
+//    PostToolUse inclui o git status do clone (juncoesDeRecados). T-0016 (B1): sem junção, o clone ANEXADO à sessão
+//    (cloneDosRecados) conta como clone de recados: Bash que grava nele e git que grava nele são bloqueados (juncoesComClone).
 //  - Guardião v7 (T-0122), PreToolUse, também ANTES da liberação da sessão manual: `gh api` só de LEITURA (GET/HEAD;
@@ -56,7 +57,7 @@
 //    opção desconhecida e gh api escondido em bash -c/node -e são bloqueados (conferirGhApi em guarda-merge-lib.mjs;
-//    casos em guarda-gh-api.test.mjs). Das ferramentas MCP, só as de merge têm hook: .claude/hooks/guarda-merge-mcp.mjs.
-// Detalhes e casos: .claude/hooks/guarda-bash-lib.mjs e .claude/hooks/guarda-bash.test.mjs.
+//    casos em guarda-agente.test.mjs). Das ferramentas MCP, só as de merge têm hook: .claude/hooks/guarda-merge-mcp.mjs.
+// Detalhes: .claude/hooks/guarda-bash-lib.mjs; casos: guarda-agente.test.mjs, guarda-recado.test.mjs e guarda-merge-mcp.test.mjs.
 import { readFileSync, statSync } from 'node:fs';
 import { join } from 'node:path';
-import { RAIZ, carregarDonos, agenteDaSessao, juncoesDeRecados } from '../../scripts/coord-lib.mjs';
+import { RAIZ, carregarDonos, agenteDaSessao } from '../../scripts/coord-lib.mjs';
 import {
@@ -65,3 +66,3 @@ import {
   arquivoFoto, arquivoAcusados, arquivoRecadosDaSessao, ehRecadoDoAlexandre,
-  lerJson, gravarJson, apagarArquivo, limparAntigos,
+  lerJson, gravarJson, apagarArquivo, limparAntigos, lerEntradaDoHook, guardaDesligada, juncoesComClone,
 } from './guarda-bash-lib.mjs';
@@ -69,3 +70,3 @@ import {
   conferirMerge, conferirGhApi, consultarPrGh, lerRecadosDoGerente, motivosRecadoFalso, mensagemRecadoFalso,
-  motivosIndiceDeRecados, mensagemIndiceDeRecados, vigiarRecados,
+  motivosIndiceDeRecados, mensagemIndiceDeRecados, vigiarRecados, conferirGitDeAnexo,
 } from './guarda-merge-lib.mjs';
@@ -75,16 +76,5 @@ const lerDoRepo = (rel) => { try { return readFileSync(join(RAIZ, rel), 'utf8');
 
-function lerEntrada() {
-  return new Promise((ok) => {
-    let txt = '';
-    process.stdin.setEncoding('utf8');
-    process.stdin.on('data', (d) => (txt += d));
-    process.stdin.on('end', () => {
-      try { ok(JSON.parse(txt || '{}')); } catch { ok({}); }
-    });
-  });
-}
+if (guardaDesligada()) process.exit(0);
 
-if ((process.env.BAP_GUARDA || '').toLowerCase() === 'off') process.exit(0);
-
-const entrada = await lerEntrada();
+const entrada = (await lerEntradaDoHook()) ?? {};
 if (entrada.tool_name && entrada.tool_name !== 'Bash') process.exit(0);
@@ -123,3 +113,3 @@ try {
 
-const juncoes = juncoesDeRecados(RAIZ);
+const juncoes = juncoesComClone(RAIZ);
 
@@ -131,2 +121,4 @@ if (evento === 'PreToolUse') {
     permitidos: permitidosDe(acusados), amb, juncoes,
+    // T-0016c: anexos do po e do gerente-projetos no clone de recados (pull, add, commit e push conferidos).
+    gitNoClone: (p) => conferirGitDeAnexo({ agente, ...p }),
   });
diff --git a/.claude/hooks/guarda-donos.mjs b/.claude/hooks/guarda-donos.mjs
index 82d190a..e863527 100644
--- a/.claude/hooks/guarda-donos.mjs
+++ b/.claude/hooks/guarda-donos.mjs
@@ -22,19 +22,13 @@
 //    (mesmas regras) e o resto do clone (.git, .github, README) é bloqueado.
+//  - T-0016 (B1): sem junção, o clone ANEXADO à sessão (cloneDosRecados, na nuvem ao lado do repositório) é bloqueado
+//    inteiro para os agentes: recado só pelo node scripts/coord.mjs. E, em qualquer pasta, o texto gravado por outro
+//    agente não leva "de: po"/"de: alexandre" nem o autor po@/alexandre@bapajuda.invalid (motivoConteudoForjado).
 //  - sessão manual local (sem agente) → liberado. Desligar tudo: variável BAP_GUARDA=off.
-import { readFileSync } from 'node:fs';
-import { join, resolve } from 'node:path';
+import { readFileSync, realpathSync } from 'node:fs';
+import { join, resolve, dirname } from 'node:path';
 import {
-  PESSOAS, RAIZ, caminhoRelativo, podeAlterar, agenteDaSessao, juncoesDeRecados, relativoPorJuncao, MOTIVO_CLONE_DE_RECADOS,
+  PESSOAS, RAIZ, caminhoRelativo, podeAlterar, agenteDaSessao, relativoPorJuncao, MOTIVO_CLONE_DE_RECADOS,
 } from '../../scripts/coord-lib.mjs';
-
-function lerEntrada() {
-  return new Promise((ok) => {
-    let txt = '';
-    process.stdin.setEncoding('utf8');
-    process.stdin.on('data', (d) => (txt += d));
-    process.stdin.on('end', () => {
-      try { ok(JSON.parse(txt || '{}')); } catch { ok({}); }
-    });
-  });
-}
+import { lerEntradaDoHook, guardaDesligada, juncoesComClone, ehAnexoNoClone, ANEXADORES } from './guarda-bash-lib.mjs';
+import { motivoConteudoForjado } from './guarda-merge-lib.mjs';
 
@@ -45,5 +39,5 @@ const bloquear = (msg) => {
 
-if ((process.env.BAP_GUARDA || '').toLowerCase() === 'off') process.exit(0);
+if (guardaDesligada()) process.exit(0);
 
-const entrada = await lerEntrada();
+const entrada = (await lerEntradaDoHook()) ?? {};
 const { agente } = agenteDaSessao({ argumento: process.argv[2], entrada });
@@ -56,2 +50,7 @@ if (!alvo) process.exit(0);
 
+// T-0016 (B1): texto que forja recado ou commit do po/Alexandre, em qualquer pasta (dentro ou fora do repositório).
+const textos = [ti.content, ti.new_string, ti.new_source, ...(Array.isArray(ti.edits) ? ti.edits.map((e) => e?.new_string) : [])];
+const forjado = motivoConteudoForjado({ agente, textos });
+if (forjado) bloquear(forjado);
+
 let rel = caminhoRelativo(alvo, RAIZ);
@@ -59,3 +58,17 @@ if (rel === null) {
   // ADR 0035: escrita direta no clone de recados (por fora da junção) segue as regras de .coord/recados.
-  const j = relativoPorJuncao(resolve(RAIZ, alvo), juncoesDeRecados(RAIZ));
+  const juncoes = juncoesComClone(RAIZ);
+  const j = relativoPorJuncao(resolve(RAIZ, alvo), juncoes);
+  // T-0016c: anexo (recados/anexos/**) do clone, pelo po ou pelo gerente-projetos. O caminho de verdade (realpath da
+  // pasta mais próxima que existe) também tem de cair nos anexos: link simbólico para recados/<destino> não vale.
+  if (j?.clone && ANEXADORES.includes(agente) && ehAnexoNoClone(resolve(RAIZ, alvo), juncoes.clone)) {
+    const completo = resolve(RAIZ, alvo);
+    let pasta = dirname(completo);
+    let real = null;
+    for (let i = 0; i < 30 && !real && pasta !== dirname(pasta); i++) { try { real = realpathSync(pasta); } catch { pasta = dirname(pasta); } }
+    let cloneReal = juncoes.clone;
+    try { cloneReal = realpathSync(juncoes.clone); } catch { /* sem realpath: o léxico */ }
+    let alvoReal = null; // o próprio arquivo, se já existe, pode ser um link simbólico
+    try { alvoReal = realpathSync(completo); } catch { /* arquivo novo */ }
+    if (real && ehAnexoNoClone(`${real}${completo.slice(pasta.length)}`, cloneReal) && (!alvoReal || ehAnexoNoClone(alvoReal, cloneReal))) process.exit(0);
+  }
   if (j?.clone) bloquear(`"${alvo}": ${MOTIVO_CLONE_DE_RECADOS}.`);
diff --git a/.claude/hooks/guarda-merge-lib.mjs b/.claude/hooks/guarda-merge-lib.mjs
index aace76f..1aeea37 100644
--- a/.claude/hooks/guarda-merge-lib.mjs
+++ b/.claude/hooks/guarda-merge-lib.mjs
@@ -1,12 +1,13 @@
 // Guardião v5 (T-0044) — trava do `gh pr merge` no Bash (PreToolUse do guarda-bash.mjs).
-// Funções puras + acesso ao gh e aos recados injetável (testes: .claude/hooks/guarda-merge.test.mjs).
+// Funções puras + acesso ao gh e aos recados injetável (testes: guarda-merge-mcp.test.mjs e guarda-recado.test.mjs).
 // Sem dependências externas.
 //
-// Regras (doc 07, recados R-20261101-151135 e R-20261101-165024 do Alexandre):
+// Regras (R-20261120-111308-alexandre e R-20261120-131230-alexandre):
 //  a) só o gerente-projetos, na sessão principal, executa `gh pr merge` (subagente nunca; identidade
 //     só por fonte confiável: BAP_AGENTE=gerente-projetos ou sessão local com agent_type);
-//  b) o comando é exatamente `gh pr merge <N> -R aloirr/bapajudacatalogo --squash --match-head-commit <sha>`
-//     (+ opcionais --body/--subject), sem prefixo (env, sudo, VAR=...), sem $VAR/$(...)/glob, um
+//  b) o comando é exatamente `gh pr merge <N> -R aloirr/bapajudacatalogo --squash --match-head-commit <sha de 40>
+//     --body "... T-nnnn ... Agente: <dono>"` (+ opcional --subject), sem prefixo (env, sudo, VAR=...), sem $VAR/$(...)/glob, um
 //     merge por comando; --admin, --auto, --merge, --rebase e qualquer outra opção são bloqueados;
-//  c) o hook consulta `gh pr view N -R aloirr/bapajudacatalogo --json files,headRefOid,changedFiles`:
+//  c) o hook consulta `gh pr view N -R aloirr/bapajudacatalogo --json files,headRefOid,changedFiles,state,statusCheckRollup`
+//     (PR aberto e CI do PR verde, T-0016 B3):
 //     TODO merge (com ou sem caminho de governança, R-20261120-111308-alexandre; T-0016) exige um recado do po
@@ -14,6 +15,7 @@
 //     nome R-...-po.md ou R-...-alexandre.md, `de:` igual ao remetente do nome e `id` igual ao nome) com o texto
-//     "autorizo o merge do PR #N no commit <sha>", SHA compatível com o --match-head-commit e com o
-//     headRefOid atual;
-//  d) os recados vêm do que está PUBLICADO no main do repositório de recados (clone anexado: git fetch e leitura de
-//     origin/main, nunca da árvore de trabalho; sem clone, a API do GitHub). Não deu para ler = nenhuma autorização.
+//     "autorizo o merge do PR #N no commit <sha de 40>", SHA igual ao --match-head-commit e ao headRefOid atual;
+//  d) os recados vêm do que está PUBLICADO no main do repositório de recados (clone anexado: origin do clone =
+//     github.com/aloirr/bapajudacatalogo-recados, git fetch e leitura de origin/main, nunca da árvore de trabalho, e o
+//     commit que trouxe o recado tem o autor <remetente>@bapajuda.invalid; sem clone, a API do GitHub). Não deu para
+//     ler = nenhuma autorização.
 //  gh fora do ar, sem login, resposta inválida ou lista de arquivos incompleta → BLOQUEADO
@@ -43,8 +45,15 @@ export const PASTA_AUTORIZACOES = 'recados/gerente-projetos';
 export const AUTORIZADORES = ['po', 'alexandre'];
-export const SHA_VALIDO = /^[0-9a-f]{7,40}$/i;
-/** "autorizo o merge do PR #N no commit <sha>" (maiúsculas/minúsculas e espaços livres; sha entre crases aceito). */
-export const RE_AUTORIZACAO = /(?<!n[aã]o\s{1,3})(?<![a-z])autorizo\s+o\s+merge\s+do\s+PR\s+#(\d+)\s+no\s+commit\s+`?([0-9a-f]{7,40})`?(?![0-9a-z])/gi;
+/** SHA do head: sempre os 40 caracteres (T-0016, B2: um SHA curto pode casar com outro commit). */
+export const SHA_VALIDO = /^[0-9a-f]{40}$/i;
+/** "autorizo o merge do PR #N no commit <sha de 40>" (maiúsculas/minúsculas e espaços livres; sha entre crases aceito). */
+export const RE_AUTORIZACAO = /(?<!n[aã]o\s{1,3})(?<![a-z])autorizo\s+o\s+merge\s+do\s+PR\s+#(\d+)\s+no\s+commit\s+`?([0-9a-f]{40})`?(?![0-9a-z])/gi;
+/** Regra do merge, uma vez só, para o rodapé das mensagens (RD-0028). */
+export const REGRA_MERGE =
+  'Todo merge: recado do po (ou do Alexandre) em recados/gerente-projetos do aloirr/bapajudacatalogo-recados com ' +
+  '"autorizo o merge do PR #N no commit <sha de 40>" (R-20261120-111308-alexandre); squash com a tarefa (T-nnnn) e ' +
+  '"Agente: <dono>" no corpo (R-20261120-131230-alexandre). Mande ao po o resumo (número, SHA do head, arquivos, CI e ' +
+  'revisões LIBERADO) e espere a autorização dele; aprovação genérica não vale.';
 
 const CABECALHO = '[guardião BAP] BLOQUEADO (gh pr merge):';
-const MODELO = `gh pr merge <N> -R ${REPO_OFICIAL} --squash --match-head-commit <sha> [--subject "<título do squash>"] --body "Agente: <dono da tarefa>"`;
+const MODELO = `gh pr merge <N> -R ${REPO_OFICIAL} --squash --match-head-commit <sha de 40> [--subject "<título do squash>"] --body "<resumo> (T-nnnn)\n\nAgente: <dono da tarefa>"`;
 
@@ -317,3 +326,3 @@ export function mensagemGhApi(erros) {
     'Aceito: gh api <endpoint> (sem -f/-F/--input), gh api -X GET <endpoint> -f q=... e gh api graphql -f query=\'query { ... }\'. ' +
-    'Para gravar no GitHub use o comando próprio do gh (gh pr create/comment/edit, gh issue ...); merge só pelo gh pr merge, com as regras do v5.\n' +
+    'Para gravar no GitHub use o comando próprio do gh (gh pr create/comment/edit, gh issue ...); merge só pelo gh pr merge ou pelo merge_pull_request da integração do GitHub, os dois conferidos pelo guardião (T-0016).\n' +
     'Não contorne o bloqueio (script, alias, outra ferramenta): se precisar gravar pela API, peça ao gerente-projetos ou ao Alexandre por recado.'
@@ -349,2 +358,3 @@ export function validarComandoMerge({ palavras, tirados = [], estranho = false,
   const shas = [];
+  const corpos = [];
   const posicionais = [];
@@ -370,2 +380,3 @@ export function validarComandoMerge({ palavras, tirados = [], estranho = false,
         if (nome === '--match-head-commit') shas.push(valor);
+        if (nome === '--body') corpos.push(valor);
         continue;
@@ -385,2 +396,3 @@ export function validarComandoMerge({ palavras, tirados = [], estranho = false,
         if (valor !== null && c === 'R') repos.push(valor);
+        if (valor !== null && c === 'b') corpos.push(valor);
         break;
@@ -400,4 +412,6 @@ export function validarComandoMerge({ palavras, tirados = [], estranho = false,
   else if (shas.length > 1) erros.push('--match-head-commit repetido: informe um SHA só');
-  else if (!SHA_VALIDO.test(shas[0])) erros.push(`--match-head-commit "${shas[0]}" não é um SHA (7 a 40 caracteres hexadecimais; prefira os 40)`);
+  else if (!SHA_VALIDO.test(shas[0])) erros.push(`--match-head-commit "${shas[0]}" não é o SHA completo (40 caracteres hexadecimais)`);
   else sha = shas[0].toLowerCase();
+  if (corpos.length > 1) erros.push('--body repetido: informe o corpo do squash uma vez só');
+  else erros.push(...errosDoCorpoDoSquash(corpos[0], '--body'));
   let pr = null;
@@ -423,4 +437,38 @@ export function motivoIdentidade({ agente, origem = '', subagente = false }) {
 
-/** SHA curto (7+) é prefixo do SHA completo? */
-export const shaCompativel = (curto, completo) => Boolean(curto && completo && SHA_VALIDO.test(curto) && String(completo).toLowerCase().startsWith(String(curto).toLowerCase()));
+/** Os dois são o mesmo SHA de 40 caracteres? (T-0016, B2: SHA curto não vale) */
+export const shaCompativel = (a, b) => Boolean(a && b && SHA_VALIDO.test(a) && SHA_VALIDO.test(b) && String(a).toLowerCase() === String(b).toLowerCase());
+
+/** Tarefa do quadro no corpo do squash. */
+export const RE_TAREFA = /\bT-\d{4}\b/;
+const RE_AGENTE = /^\s*Agente:[ \t]*(\S+)[ \t]*$/i;
+
+/** Linhas do último bloco (separado por linha em branco) do corpo do squash: o bloco de trailers do commit. */
+export function ultimoBlocoDaMensagem(mensagem) {
+  const blocos = [];
+  let atual = [];
+  for (const linha of String(mensagem || '').replace(/\r\n?/g, '\n').split('\n')) {
+    if (linha.trim() === '') { if (atual.length) blocos.push(atual); atual = []; } else atual.push(linha);
+  }
+  if (atual.length) blocos.push(atual);
+  return blocos.length ? blocos[blocos.length - 1] : [];
+}
+
+/**
+ * Corpo do commit do squash (R-20261120-131230-alexandre): cita a tarefa (T-nnnn) e tem, no último bloco, um único
+ * "Agente: <dono>" do time (ou alexandre). Vale para o --body do gh pr merge e o commit_message do MCP. Função pura.
+ */
+export function errosDoCorpoDoSquash(corpo, opcao) {
+  const texto = String(corpo ?? '');
+  if (!texto.trim()) return [`falta o corpo do squash (${opcao}) com a tarefa (T-nnnn) e, no fim, "Agente: <dono da tarefa>" (R-20261120-131230-alexandre)`];
+  const erros = [];
+  if (!RE_TAREFA.test(texto)) erros.push(`o corpo do squash (${opcao}) não cita a tarefa (T-nnnn)`);
+  const nomes = ultimoBlocoDaMensagem(texto).map((l) => l.match(RE_AGENTE)).filter(Boolean).map((m) => m[1].toLowerCase());
+  if (!nomes.length) erros.push(`o corpo do squash (${opcao}) não termina com "Agente: <dono da tarefa>"`);
+  else if (nomes.length > 1) erros.push(`o corpo do squash (${opcao}) tem ${nomes.length} "Agente:" no último bloco: um só`);
+  else if (!PESSOAS.includes(nomes[0])) erros.push(`"Agente: ${nomes[0]}" não é do time`);
+  return erros;
+}
+
+/** "Agente: <nome>" do corpo do squash (já validado) ou null. */
+export const agenteDoCorpo = (corpo) => ultimoBlocoDaMensagem(corpo).map((l) => l.match(RE_AGENTE)).find(Boolean)?.[1].toLowerCase() ?? null;
 
@@ -459,4 +507,2 @@ export function autorizacoesDeMerge(recados, { remetentes = AUTORIZADORES } = {}
 }
-/** Só as do Alexandre (compatibilidade com os testes herdados). */
-export const autorizacoesDoAlexandre = (recados) => autorizacoesDeMerge(recados, { remetentes: ['alexandre'] });
 
@@ -473,3 +519,3 @@ export function decidirMerge({ pr, sha, consulta, autorizacoes }) {
   const erros = [];
-  if (!/^[0-9a-f]{40}$/.test(head)) return { ok: false, governanca: [], erros: [`o gh não devolveu o headRefOid do PR #${pr} (falha fechada)`] };
+  if (!SHA_VALIDO.test(head)) return { ok: false, governanca: [], erros: [`o gh não devolveu o headRefOid do PR #${pr} (falha fechada)`] };
   if (typeof consulta.total === 'number' && consulta.total > arquivos.length)
@@ -492,4 +538,4 @@ export function decidirMerge({ pr, sha, consulta, autorizacoes }) {
       ? `há autorização para o PR #${pr}, mas no commit ${doPr.map((a) => a.sha).join(', ')}, que não é o head atual (${head}): o PR mudou depois da aprovação. NÃO faça o merge; avise o po`
-      : `não há recado do po (ou do Alexandre) em ${PASTA_AUTORIZACOES} com "autorizo o merge do PR #${pr} no commit ${head}"`;
-    erros.push(`${motivo}. Mande ao po o resumo (número, SHA do head, arquivos, CI e revisões LIBERADO) e espere a autorização dele por recado; aprovação genérica não vale${lista}`);
+      : `não há autorização para o PR #${pr} no commit ${head}`;
+    erros.push(`${motivo}${lista}`);
   }
@@ -536,3 +582,28 @@ export const ONDE_PROCURA_GH = 'PATH; no Windows também %ProgramFiles%\\GitHub
 /**
- * `gh pr view N -R aloirr/bapajudacatalogo --json files,headRefOid,changedFiles` (timeout de 20 s).
+ * Situação do CI pelo statusCheckRollup do `gh pr view` (T-0016, B3; mesma regra de avaliarChecks: tudo concluído com
+ * só success, T-0016c). CheckRun: status/conclusion; StatusContext: state. Lista vazia = o CI não rodou. Função pura.
+ */
+export function avaliarRollup(rollup) {
+  if (!Array.isArray(rollup)) return { verde: false, detalhe: 'resposta sem statusCheckRollup' };
+  if (!rollup.length) return { verde: false, detalhe: 'nenhum check no head (o CI não rodou)' };
+  const nome = (c) => c?.name || c?.context || '?';
+  const falhos = [];
+  const pendentes = [];
+  for (const c of rollup) {
+    if (c?.__typename === 'StatusContext' || (c?.state !== undefined && c?.status === undefined)) {
+      const st = String(c?.state || '').toLowerCase();
+      if (st !== 'success') (st === 'pending' || st === 'expected' ? pendentes : falhos).push(`${nome(c)}: ${st || '?'}`);
+      continue;
+    }
+    if (String(c?.status || '').toLowerCase() !== 'completed') { pendentes.push(nome(c)); continue; }
+    const conc = String(c?.conclusion || '').toLowerCase();
+    if (!CONCLUSOES_VERDES.includes(conc)) falhos.push(`${nome(c)}: ${conc || '?'}`);
+  }
+  if (falhos.length) return { verde: false, detalhe: `vermelho (${falhos.slice(0, 5).join('; ')}${falhos.length > 5 ? '; ...' : ''})` };
+  if (pendentes.length) return { verde: false, detalhe: `ainda rodando (${pendentes.slice(0, 5).join('; ')}${pendentes.length > 5 ? '; ...' : ''})` };
+  return { verde: true, detalhe: `${rollup.length} check(s) verdes` };
+}
+
+/**
+ * `gh pr view N -R aloirr/bapajudacatalogo --json files,headRefOid,changedFiles,state,statusCheckRollup` (timeout de 20 s).
  * BAP_GH_SIMULADO=<arquivo.mjs>: roda esse script no lugar do gh (só nos testes; a variável é do
@@ -544,3 +615,3 @@ export function consultarPrGh(pr, { env = process.env, timeout = 20000, platafor
   if (!simulado && !gh) return { ok: false, erro: `gh não encontrado (${ONDE_PROCURA_GH})` };
-  const args = ['pr', 'view', String(pr), '-R', REPO_OFICIAL, '--json', 'files,headRefOid,changedFiles'];
+  const args = ['pr', 'view', String(pr), '-R', REPO_OFICIAL, '--json', 'files,headRefOid,changedFiles,state,statusCheckRollup'];
   let saida;
@@ -561,2 +632,4 @@ export function consultarPrGh(pr, { env = process.env, timeout = 20000, platafor
       total: typeof j.changedFiles === 'number' ? j.changedFiles : undefined,
+      estado: String(j.state || '').toLowerCase(), mesclado: String(j.state || '').toUpperCase() === 'MERGED',
+      ciPr: avaliarRollup(j.statusCheckRollup),
     };
@@ -565,5 +638,5 @@ export function consultarPrGh(pr, { env = process.env, timeout = 20000, platafor
 
-/** git no clone de recados (sem prompt de senha; 20 s). */
-const gitDoClone = (clone) => (args) => execFileSync('git', ['-C', clone, ...args], {
-  encoding: 'utf8', timeout: 20000, stdio: ['ignore', 'pipe', 'pipe'], windowsHide: true, maxBuffer: 16 * 1024 * 1024,
+/** git no clone de recados (sem prompt de senha; prazo por chamada: o que resta do prazo total). */
+const gitDoClone = (clone) => (args, { timeout = 20000 } = {}) => execFileSync('git', ['-C', clone, ...args], {
+  encoding: 'utf8', timeout, stdio: ['ignore', 'pipe', 'pipe'], windowsHide: true, maxBuffer: 16 * 1024 * 1024,
   env: { ...process.env, GIT_TERMINAL_PROMPT: '0' },
@@ -571,17 +644,144 @@ const gitDoClone = (clone) => (args) => execFileSync('git', ['-C', clone, ...arg
 export const REF_PUBLICADA = 'refs/remotes/origin/main';
+/** URL do origin do clone de recados (T-0016, B1): só o GitHub do aloirr/bapajudacatalogo-recados (https ou ssh). */
+export const RE_ORIGIN_RECADOS = /^(https:\/\/github\.com\/|ssh:\/\/git@github\.com\/|git@github\.com:)aloirr\/bapajudacatalogo-recados(\.git)?\/?$/i;
+/** Domínio do autor dos commits do coord.mjs (<agente>@bapajuda.invalid; scripts/coord.mjs). */
+export const DOMINIO_AUTOR = 'bapajuda.invalid';
 
 /**
- * Recados do po e do Alexandre PUBLICADOS no main do repositório de recados, pelo clone anexado (T-0016): primeiro
- * `git fetch` (força origin/main = o main do GitHub, desfazendo ref adulterada), depois a leitura de origin/main.
- * Nunca lê a árvore de trabalho nem o main local (que um agente poderia alterar sem publicar).
- * fetch que falha = exceção (quem chama devolve nenhum recado: falha fechada).
+ * Motivo para recusar o origin do clone (T-0016, B1) ou null. O git aplica url.<x>.insteadOf e pushInsteadOf na hora:
+ * vale a URL efetiva (git ls-remote --get-url e git remote get-url --push), que tem de ser o GitHub do repositório de
+ * recados. Assim origin trocado (git remote set-url) e insteadOf para outro lugar são recusados. Função pura.
  */
-export function recadosPublicadosNoClone(clone, { git = gitDoClone(clone) } = {}) {
-  git(['fetch', '-q', '--no-tags', 'origin', `+refs/heads/main:${REF_PUBLICADA}`]);
-  const nomes = git(['ls-tree', '--name-only', `${REF_PUBLICADA}:${PASTA_AUTORIZACOES}`])
+export function motivoOriginDoClone({ urls = [], urlFetch = '', urlPush = '', simulado = '' }) {
+  const lista = urls.map((u) => String(u).trim()).filter(Boolean);
+  if (lista.length !== 1) return `o clone de recados tem ${lista.length} URL(s) no remote.origin.url (precisa de uma só)`;
+  // BAP_RECADOS_ORIGIN_SIMULADO (só nos testes, como o BAP_GH_SIMULADO; variável do processo do Claude Code, que o
+  // agente não altera): a URL exata do repositório falso no lugar do GitHub.
+  const aceita = (u) => (simulado ? u === simulado : RE_ORIGIN_RECADOS.test(u));
+  for (const [nome, u] of [['remote.origin.url', lista[0]], ['URL efetiva do fetch', urlFetch], ['URL efetiva do push', urlPush]]) {
+    if (!aceita(String(u || '').trim())) return `${nome} do clone de recados é "${String(u || '').trim()}", não github.com/aloirr/bapajudacatalogo-recados (origin trocado ou insteadOf)`;
+  }
+  return null;
+}
+
+/** URLs do origin do clone (configurada e efetivas) para o motivoOriginDoClone; ilegível = vazio (recusado). */
+function urlsDoOrigin(g, env) {
+  const ler = (args) => { try { return g(args); } catch { return ''; } };
+  return {
+    urls: ler(['config', '--get-all', 'remote.origin.url']).split(/\r?\n/),
+    urlFetch: ler(['ls-remote', '--get-url', 'origin']),
+    urlPush: ler(['remote', 'get-url', '--push', 'origin']),
+    simulado: String(env.BAP_RECADOS_ORIGIN_SIMULADO || '').trim(),
+  };
+}
+
+const ehCaminhoDeAnexo = (rel) => /^recados\/anexos\/[^/]/.test(rel) && !rel.split('/').includes('..');
+
+/**
+ * git do po e do gerente-projetos para publicar anexos (T-0016c): só pull, add, commit e push, e só com recados/anexos/**.
+ *  - add: só caminhos (sem -A, -u, ., glob nem $VAR) dentro de recados/anexos/;
+ *  - commit: só -m/-q (sem -a, --author, --amend nem caminho), e tudo o que está staged em recados/anexos/;
+ *  - pull: só --rebase/-q (e origin main); push: só `origin HEAD:main` (ou `origin main`), sem --force, e os commits a
+ *    publicar (origin/main..HEAD) só com recados/anexos/** e com o autor <agente>@bapajuda.invalid;
+ *  - pull e push: o origin do clone é o GitHub do aloirr/bapajudacatalogo-recados (motivoOriginDoClone, B1-b).
+ * @returns {string|null} motivo do bloqueio
+ */
+export function conferirGitDeAnexo({ agente, sub, args = [], cwd, clone, git = gitDoClone(clone), env = process.env }) {
+  const g = (a) => git(a, { timeout: 10000 });
+  const base = barras(clone).replace(/\/+$/, '');
+  const c = barras(cwd).replace(/\/+$/, '');
+  if (c !== base && !c.toLowerCase().startsWith(`${base.toLowerCase()}/`)) return 'pasta fora do clone';
+  const cwdRel = c.slice(base.length).replace(/^\/+/, '');
+  if (cwdRel.split('/')[0].toLowerCase() === '.git') return 'git de anexo só na pasta do clone (git -C <clone>), não no .git';
+  const fora = (lista) => lista.filter((r) => !ehCaminhoDeAnexo(r));
+  if (args.some((a) => a.incerto)) return 'sem $VAR, $(...), glob ou ~ no git de anexo: escreva tudo por extenso';
+  const v = args.map((a) => a.valor);
+  const origem = () => motivoOriginDoClone(urlsDoOrigin(g, env));
+  try {
+    if (sub === 'add') {
+      const caminhos = v.filter((x) => x !== '--');
+      if (!caminhos.length || caminhos.some((x) => x.startsWith('-') || /[*?[]/.test(x))) return 'git add de anexo só com os caminhos, sem opções nem glob';
+      const ruins = fora(caminhos.map((x) => posix.normalize(posix.join(cwdRel, x)).replace(/\/+$/, '')));
+      return ruins.length ? `git add só de recados/anexos/** (veio ${ruins.slice(0, 3).join(', ')}); recados e lidos só pelo node scripts/coord.mjs` : null;
+    }
+    if (sub === 'commit') {
+      for (let i = 0; i < v.length; i++) {
+        if (['-m', '--message', '-qm'].includes(v[i])) { i++; continue; }
+        if (/^--message=/.test(v[i]) || v[i] === '-q' || v[i] === '--quiet') continue;
+        return `git commit de anexo só com -m e -q (veio ${v[i]}): nada de -a, --author, --amend nem caminho`;
+      }
+      const staged = g(['diff', '--cached', '--name-only', '--no-renames']).split(/\r?\n/).map((x) => x.trim()).filter(Boolean);
+      const ruins = fora(staged);
+      return ruins.length ? `há arquivo staged fora de recados/anexos/ (${ruins.slice(0, 3).join(', ')}): o commit de anexo leva só anexos` : null;
+    }
+    if (sub === 'pull') {
+      const ok = v.every((x) => /^(--rebase|-q|--quiet|--ff-only)$/.test(x)) || (v.filter((x) => !x.startsWith('-')).join(' ') === 'origin main' && v.filter((x) => x.startsWith('-')).every((x) => /^(--rebase|-q|--quiet|--ff-only)$/.test(x)));
+      if (!ok) return 'git pull de anexo só com --rebase/-q (e origin main)';
+      return origem();
+    }
+    if (sub === 'push') {
+      const pos = v.filter((x) => !/^(-q|--quiet)$/.test(x));
+      if (!['origin HEAD:main', 'origin main', 'origin HEAD:refs/heads/main'].includes(pos.join(' '))) return 'git push de anexo só como git push origin HEAD:main (sem --force nem outro destino)';
+      const m = origem();
+      if (m) return m;
+      const arquivos = g(['diff', '--name-only', '--no-renames', `${REF_PUBLICADA}..HEAD`]).split(/\r?\n/).map((x) => x.trim()).filter(Boolean);
+      const ruins = fora(arquivos);
+      if (ruins.length) return `os commits a publicar mexem fora de recados/anexos/ (${ruins.slice(0, 3).join(', ')}): recados e lidos só pelo node scripts/coord.mjs`;
+      const autores = [...new Set(g(['log', '--format=%ae', `${REF_PUBLICADA}..HEAD`]).split(/\r?\n/).map((x) => x.trim().toLowerCase()).filter(Boolean))];
+      const alheios = autores.filter((a) => a !== `${agente}@${DOMINIO_AUTOR}`);
+      return alheios.length ? `os commits a publicar têm autor de outro (${alheios.join(', ')}): o anexo sai com o autor ${agente}@${DOMINIO_AUTOR}` : null;
+    }
+  } catch (e) {
+    return `não deu para conferir o clone de recados (${String(e?.message || e).split(/\r?\n/)[0].slice(0, 120)}): sem a conferência, bloqueado`;
+  }
+  return MOTIVO_SO_COORD;
+}
+const MOTIVO_SO_COORD = 'o clone de recados só muda pelo node scripts/coord.mjs (enviar, lido) e, nos anexos, pelo git add/commit/push conferido';
+
+/**
+ * Autor (e-mail) do commit que trouxe cada arquivo da pasta ao REF (o mais recente com status A). Saída de
+ * `git log --diff-filter=A --format=%x01%ae --name-only REF -- pasta`. Função pura.
+ * @returns {Map<string, string>} nome do arquivo → e-mail do autor
+ */
+export function autoresDosRecados(saida) {
+  const res = new Map();
+  for (const bloco of String(saida || '').split('\x01').slice(1)) {
+    const [email, ...arquivos] = bloco.split(/\r?\n/).map((l) => l.trim());
+    for (const a of arquivos.filter(Boolean)) {
+      const nome = a.split('/').pop();
+      if (!res.has(nome)) res.set(nome, String(email || '').toLowerCase());
+    }
+  }
+  return res;
+}
+
+/**
+ * Recados do po e do Alexandre PUBLICADOS no main do repositório de recados, pelo clone anexado (T-0016):
+ *  1. o origin do clone é o GitHub do aloirr/bapajudacatalogo-recados (motivoOriginDoClone);
+ *  2. `git fetch` (força origin/main = o main do GitHub, desfazendo ref adulterada) e leitura de origin/main, nunca da
+ *     árvore de trabalho nem do main local (que um agente poderia alterar sem publicar);
+ *  3. só vale o recado cujo commit de chegada ao main tem o autor <remetente>@bapajuda.invalid (o coord.mjs grava com
+ *     o nome do agente). O autor do git é texto livre: o que impede outro agente de forjá-lo são os guardiões (Write e
+ *     Bash no clone, "po@bapajuda.invalid" e "de: po" no comando e no conteúdo).
+ * Origin errado, fetch que falha ou prazo estourado = exceção (quem chama devolve nenhum recado: falha fechada).
+ */
+export function recadosPublicadosNoClone(clone, { git = gitDoClone(clone), prazo = 30000, agora = () => Date.now(), env = process.env } = {}) {
+  const fim = agora() + prazo;
+  const g = (args, max = 20000) => {
+    const resta = Math.min(max, fim - agora());
+    if (resta <= 0) throw new Error(`prazo de ${Math.round(prazo / 1000)} s para ler os recados estourado`);
+    return git(args, { timeout: resta });
+  };
+  const motivo = motivoOriginDoClone(urlsDoOrigin((args) => g(args, 5000), env));
+  if (motivo) throw new Error(motivo);
+  g(['fetch', '-q', '--no-tags', 'origin', `+refs/heads/main:${REF_PUBLICADA}`]);
+  const nomes = g(['ls-tree', '--name-only', `${REF_PUBLICADA}:${PASTA_AUTORIZACOES}`])
     .split(/\r?\n/).map((n) => n.trim())
     .filter((n) => /^R-[^/]+\.md$/i.test(n) && AUTORIZADORES.includes(remetenteDoRecado(n)));
+  if (!nomes.length) return [];
+  const autores = autoresDosRecados(g(['log', '--diff-filter=A', '--no-renames', '--format=%x01%ae', '--name-only', REF_PUBLICADA, '--', PASTA_AUTORIZACOES]));
   const res = [];
   for (const nome of nomes) {
-    try { res.push({ nome, texto: git(['show', `${REF_PUBLICADA}:${PASTA_AUTORIZACOES}/${nome}`]) }); } catch { /* ilegível: não autoriza */ }
+    if (autores.get(nome) !== `${remetenteDoRecado(nome)}@${DOMINIO_AUTOR}`) continue; // autor de outro: não autoriza
+    try { res.push({ nome, texto: g(['show', `${REF_PUBLICADA}:${PASTA_AUTORIZACOES}/${nome}`], 5000) }); } catch { /* ilegível: não autoriza */ }
   }
@@ -601,3 +801,3 @@ export function lerRecadosDoGerente(raiz, {
   if (clone) {
-    try { return lerClone(clone); } catch { return []; }
+    try { return lerClone(clone, { env }); } catch { return []; }
   }
@@ -647,3 +847,3 @@ export function conferirMerge({ comando, agente, origem = '', subagente = false,
       const d = decidirMerge({ pr: v.pr, sha: v.sha, consulta, autorizacoes: autorizacoesDeMerge(recados) });
-      erros.push(...d.erros);
+      erros.push(...errosDoPrNoGitHub(v.pr, consulta), ...d.erros);
       governanca = d.governanca;
@@ -656,2 +856,14 @@ export function conferirMerge({ comando, agente, origem = '', subagente = false,
 
+/**
+ * PR aberto e CI do PR verde (T-0016, B3: vale no terminal, pelo gh pr view, e no MCP, pela API REST). Consulta que
+ * falhou: o erro vem do decidirMerge. Função pura.
+ */
+export function errosDoPrNoGitHub(pr, consulta) {
+  if (!consulta?.ok) return [];
+  const erros = [];
+  if (consulta.mesclado || consulta.estado !== 'open') erros.push(`o PR #${pr} não está aberto (estado: ${consulta.mesclado ? 'já mesclado' : consulta.estado || 'desconhecido'})`);
+  if (!consulta.ciPr?.verde) erros.push(`o CI do PR #${pr} (head ${String(consulta.headRefOid).slice(0, 12)}) não está verde: ${consulta.ciPr?.detalhe || 'sem resposta'}. Espere o CI ficar verde`);
+  return erros;
+}
+
 export function mensagemMerge(erros) {
@@ -660,3 +872,3 @@ export function mensagemMerge(erros) {
     `Comando aceito (só o gerente-projetos, na sessão principal): ${MODELO}\n` +
-    `Todo merge: recado do po (ou do Alexandre) em ${PASTA_AUTORIZACOES} com "autorizo o merge do PR #N no commit <sha>" (R-20261120-111308-alexandre).\n` +
+    `${REGRA_MERGE}\n` +
     'Não contorne o bloqueio (gh api, alias, script, outro comando): se a regra impede o merge, avise o po por recado.'
@@ -964,2 +1176,14 @@ export function motivosRecadoFalso({ comando, agente, cwd = '' }) {
   const grava = escritas.length > 0 || opacos.length > 0 || coord;
+  // T-0016 (B1), antes da liberação da leitura (git commit e git -c contam como leitura no v6):
+  //  - GIT_DIR/GIT_WORK_TREE/GIT_CONFIG_*/GIT_*_EMAIL levam o git a outro repositório (o clone de recados) ou trocam o autor;
+  //  - o autor <po|alexandre>@bapajuda.invalid num comando que grava ou faz commit (--author, user.email) é forja.
+  if (agente !== 'alexandre' && /(^|[\s;&|(])(GIT_DIR|GIT_WORK_TREE|GIT_CONFIG[A-Z_]*|GIT_AUTHOR_EMAIL|GIT_COMMITTER_EMAIL)=/.test(String(comando)) && /\bgit\b/.test(t)) {
+    motivos.push(`GIT_DIR, GIT_WORK_TREE, GIT_CONFIG_* e GIT_AUTHOR/COMMITTER_EMAIL no comando não são aceitos (podem levar o git ao clone de recados ou trocar o autor): use git -C <pasta por extenso>; recado só com node scripts/coord.mjs enviar --de ${agente}`);
+    return motivos;
+  }
+  const autorAlheio = AUTORIZADORES.find((q) => q !== agente && new RegExp(`(^|[^a-z0-9._-])${q}@bapajuda\\.invalid\\b`).test(t));
+  if (autorAlheio && (grava || /\bcommit\b|--author|user\.email|\bconfig\b/.test(t))) {
+    motivos.push(`o autor ${autorAlheio}@bapajuda.invalid no comando: ${agente} não grava commit nem recado em nome de ${autorAlheio} (a autorização de merge vale pelo autor); use node scripts/coord.mjs enviar --de ${agente}`);
+    return motivos;
+  }
   if (!grava) return motivos; // só leitura: passa (v6)
@@ -973,16 +1197,22 @@ export function motivosRecadoFalso({ comando, agente, cwd = '' }) {
   // T-0016: a autorização de merge do po vale como a do Alexandre; ninguém mais grava recado como po.
-  if (agente !== 'po' && (/(^|[^a-z0-9_])de:\s*po\b/.test(t) || /\bpo@bapajuda\.invalid\b/.test(t))) {
-    motivos.push(`"de: po" ou o autor po@bapajuda.invalid no comando: ${agente} não cria recado em nome do po (a autorização de merge do po vale como a do Alexandre); use node scripts/coord.mjs enviar --de ${agente}`);
+  if (agente !== 'po' && /(^|[^a-z0-9_])de:\s*po\b/.test(t)) {
+    motivos.push(`"de: po" no comando: ${agente} não cria recado em nome do po (a autorização de merge do po vale como a do Alexandre); use node scripts/coord.mjs enviar --de ${agente}`);
     return motivos;
   }
-  if (!citaAlexandre) return motivos;
-  const opaco = opacos.find((o) => RE_ALEXANDRE.test(textoNormalizado(o.texto)) || citaRecados || pastaSuspeita(o.cwd));
-  if (opaco)
-    motivos.push(`script (bash -c, node -e, eval...) ou comando opaco (${opaco.motivo}) que pode gravar arquivo e cita alexandre${citaRecados ? ' e recados' : ''}: ${agente} não cria recado em nome do Alexandre; use node scripts/coord.mjs enviar --de ${agente} (para só ler, use ls/cat/grep/git show sem gravar)`);
-  // alvo: incerto, na pasta de recados, com nome de recado do Alexandre (*alexandre*.md: link simbólico
-  // para a pasta de recados) ou gravado numa pasta incerta/de recados (cd)
-  const nomeDeRecado = (v) => /alexandre[^/\\]*\.md$/i.test(barras(v).split('/').pop());
-  const escrita = escritas.find(({ alvo, cwd: c }) => alvo.incerto || RE_RECADOS.test(alvo.valor) || nomeDeRecado(alvo.valor) || pastaSuspeita(c));
-  if (escrita)
-    motivos.push(`comando que grava em "${escrita.alvo.valor}"${escrita.cwd === null ? ' (pasta incerta)' : RE_RECADOS.test(escrita.cwd || '') ? ` (na pasta ${escrita.cwd})` : ''} e cita alexandre: ${agente} não cria, altera, move nem apaga recado em nome do Alexandre; use node scripts/coord.mjs enviar --de ${agente}`);
+  // Remetentes que autorizam merge (alexandre e, desde a T-0016, po): o comando que grava e cita o remetente não cria,
+  // altera, move nem apaga recado dele.
+  const remetentes = [
+    { quem: 'alexandre', nome: 'o Alexandre', cita: citaAlexandre, re: RE_ALEXANDRE, arquivo: /alexandre[^/\\]*\.md$/i },
+    { quem: 'po', nome: 'o po', cita: /(^|[^a-z0-9_])po([^a-z0-9_@]|$)/.test(t), re: /(^|[^a-z0-9_])po([^a-z0-9_@]|$)/i, arquivo: /-po(\.[^/\\]*)?\.md$/i },
+  ].filter((r) => r.quem !== agente && r.cita);
+  for (const r of remetentes) {
+    const opaco = opacos.find((o) => r.re.test(textoNormalizado(o.texto)) || citaRecados || pastaSuspeita(o.cwd));
+    if (opaco)
+      motivos.push(`script (bash -c, node -e, eval...) ou comando opaco (${opaco.motivo}) que pode gravar arquivo e cita ${r.quem}${citaRecados ? ' e recados' : ''}: ${agente} não cria recado em nome d${r.nome}; use node scripts/coord.mjs enviar --de ${agente} (para só ler, use ls/cat/grep/git show sem gravar)`);
+    // alvo: incerto, na pasta de recados, com nome de recado do remetente (*alexandre*.md, *-po.md: link simbólico
+    // para a pasta de recados) ou gravado numa pasta incerta/de recados (cd)
+    const escrita = escritas.find(({ alvo, cwd: c }) => alvo.incerto || RE_RECADOS.test(alvo.valor) || r.arquivo.test(barras(alvo.valor).split('/').pop()) || pastaSuspeita(c));
+    if (escrita)
+      motivos.push(`comando que grava em "${escrita.alvo.valor}"${escrita.cwd === null ? ' (pasta incerta)' : RE_RECADOS.test(escrita.cwd || '') ? ` (na pasta ${escrita.cwd})` : ''} e cita ${r.quem}: ${agente} não cria, altera, move nem apaga recado em nome d${r.nome}; use node scripts/coord.mjs enviar --de ${agente}`);
+  }
   return motivos;
@@ -990,2 +1220,23 @@ export function motivosRecadoFalso({ comando, agente, cwd = '' }) {
 
+/**
+ * Conteúdo de Write/Edit/MultiEdit/NotebookEdit que forja recado ou commit do po ou do Alexandre (T-0016, B1): cabeçalho
+ * "de: po"/"de: alexandre" ou o autor po@bapajuda.invalid/alexandre@bapajuda.invalid, escrito por outro agente, em
+ * qualquer pasta (um script em /tmp ou na pasta do agente rodaria o git no clone de recados). Função pura.
+ * @returns {string|null} motivo do bloqueio
+ */
+export function motivoConteudoForjado({ agente, textos = [] }) {
+  if (!agente) return null;
+  for (const texto of textos) {
+    const s = String(texto ?? '');
+    for (const quem of AUTORIZADORES) {
+      if (quem === agente) continue;
+      const cabecalho = new RegExp(`^[ \\t]*de:[ \\t]*["']?${quem}["']?[ \\t]*$`, 'im');
+      const autor = new RegExp(`(^|[^a-z0-9._-])${quem}@${DOMINIO_AUTOR.replace('.', '\\.')}`, 'i');
+      if (cabecalho.test(s)) return `o texto tem "de: ${quem}": ${agente} não escreve recado em nome de ${quem}; use node scripts/coord.mjs enviar --de ${agente}`;
+      if (autor.test(s)) return `o texto tem o autor ${quem}@${DOMINIO_AUTOR}: ${agente} não grava commit em nome de ${quem} (o autor vale como assinatura do recado de autorização)`;
+    }
+  }
+  return null;
+}
+
 // ───────────────────────────── v6 (T-0050): git add/commit/stash de recados do Alexandre ─────────────────────────────
@@ -1090,3 +1341,3 @@ export function mensagemRecadoFalso(agente, motivos) {
     `${motivos.map((m) => ` - ${m}`).join('\n')}\n` +
-    'Recado do Alexandre (sobretudo "autorizo o merge do PR #N no commit <sha>") só ele escreve. Não contorne o bloqueio.'
+    'Recado do Alexandre ou do po (sobretudo "autorizo o merge do PR #N no commit <sha>") só o próprio remetente escreve. Não contorne o bloqueio.'
   );
@@ -1102,6 +1353,7 @@ export function mensagemRecadoFalso(agente, motivos) {
 //  b) aloirr/bapajudacatalogo, merge_method "squash" e expectedHeadSha de 40 caracteres (o próprio GitHub recusa o
-//     merge se o head mudou); commit_title/commit_message opcionais; qualquer outro parâmetro = bloqueado;
+//     merge se o head mudou); commit_message obrigatório, com a tarefa (T-nnnn) e "Agente: <dono>" no último bloco
+//     (R-20261120-131230-alexandre); commit_title opcional; qualquer outro parâmetro = bloqueado;
 //     auto-merge e merge de branch sem PR = bloqueados;
 //  c) o hook consulta o GitHub pela API REST (gh api, só leitura): PR aberto, head = expectedHeadSha e CI do head do
-//     PR verde (todos os check-runs concluídos com success/neutral/skipped). O CI do main não é conferido: o
+//     PR verde (todos os check-runs concluídos com success; neutral e skipped barram, T-0016c). O CI do main não é conferido: o
 //     ci.yml só roda em pull_request, e o main não tem check-run;
@@ -1125,5 +1377,5 @@ export const CHAVES_MERGE_MCP = {
 const RE_HEAD_SHA = /^\s*Head-SHA:[ \t]*([0-9a-zA-Z]+)[ \t]*$/gim;
-const RE_AGENTE = /^\s*Agente:[ \t]*(\S+)[ \t]*$/i;
 /** Conclusões de check-run que contam como verde. */
-export const CONCLUSOES_VERDES = ['success', 'neutral', 'skipped'];
+// T-0016c: só success. neutral e skipped barram (merge com neutral é decisão do Alexandre, como no caso do #29).
+export const CONCLUSOES_VERDES = ['success'];
 
@@ -1153,13 +1405,2 @@ export function tipoFerramentaMerge(ferramenta) {
 
-/** Linhas do último bloco da mensagem (bloco de trailers); [] se a mensagem tem um bloco só. Igual ao CI da T-0049. */
-export function ultimoBlocoDaMensagem(mensagem) {
-  const blocos = [];
-  let atual = [];
-  for (const linha of String(mensagem || '').replace(/\r\n?/g, '\n').split('\n')) {
-    if (linha.trim() === '') { if (atual.length) blocos.push(atual); atual = []; } else atual.push(linha);
-  }
-  if (atual.length) blocos.push(atual);
-  return blocos.length >= 2 ? blocos[blocos.length - 1] : [];
-}
-
 /**
@@ -1209,9 +1450,6 @@ export function validarEntradaMergeMcp(entrada) {
   }
-  // trailer "Agente:" no último bloco da mensagem: opcional; se houver, é um só e do time
-  let agenteDoCommit = null;
-  const nomes = ultimoBlocoDaMensagem(mensagem ?? '').map((l) => l.match(RE_AGENTE)).filter(Boolean).map((m) => m[1].toLowerCase());
-  if (nomes.length > 1) erros.push(`a commit_message tem ${nomes.length} "Agente:" no último bloco: no máximo um`);
-  else if (nomes.length === 1 && !PESSOAS.includes(nomes[0])) erros.push(`"Agente: ${nomes[0]}" não é do time`);
-  else if (nomes.length === 1) agenteDoCommit = nomes[0];
-  return { erros, pr, sha, agenteDoCommit };
+  // Corpo do squash (R-20261120-131230-alexandre): a tarefa (T-nnnn) e, no último bloco, um único "Agente: <dono>".
+  const doCorpo = errosDoCorpoDoSquash(mensagem, 'commit_message');
+  erros.push(...doCorpo);
+  return { erros, pr, sha, agenteDoCommit: doCorpo.length ? null : agenteDoCorpo(mensagem) };
 }
@@ -1248,3 +1486,5 @@ export function avaliarChecks(resposta) {
  */
-export function consultarPrRest(pr, { env = process.env, timeout = 15000, prazo = 80000, agora = () => Date.now(), plataforma = process.platform, existe } = {}) {
+// Prazos (T-0016): consulta REST 60 s no total (15 s por chamada) + recados 30 s = 90 s, abaixo do timeout de 120 s do
+// hook no .claude/settings.json; estourou = BLOQUEADO (falha fechada).
+export function consultarPrRest(pr, { env = process.env, timeout = 15000, prazo = 60000, agora = () => Date.now(), plataforma = process.platform, existe } = {}) {
   const simulado = String(env.BAP_GH_SIMULADO || '').trim();
@@ -1327,8 +1567,5 @@ export function conferirMergeMcp({ ferramenta, entrada, agente, origem = '', sub
       autorizadoPor = d.autorizadoPor;
-      if (consulta?.ok) {
-        if (consulta.mesclado || consulta.estado !== 'open') erros.push(`o PR #${v.pr} não está aberto (estado: ${consulta.mesclado ? 'já mesclado' : consulta.estado || 'desconhecido'})`);
-        if (!consulta.ciPr?.verde) erros.push(`o CI do PR #${v.pr} (head ${String(consulta.headRefOid).slice(0, 12)}) não está verde: ${consulta.ciPr?.detalhe || 'sem resposta'}. Espere o CI ficar verde`);
-      }
-      erros.push(...d.erros.map((e) => e.replace(/--match-head-commit/g, 'expectedHeadSha')));
+      erros.push(...errosDoPrNoGitHub(v.pr, consulta), ...d.erros.map((e) => e.replace(/--match-head-commit/g, 'expectedHeadSha')));
     }
+    if (!erros.length) return { ok: true, merge: true, pr, governanca, autorizacao, autorizadoPor, agenteDoCommit: v.agenteDoCommit };
   }
@@ -1342,4 +1579,5 @@ export function mensagemMergeMcp(erros) {
     'Chamada aceita (só o gerente-projetos, na sessão principal): merge_pull_request com owner "aloirr", repo "bapajudacatalogo", ' +
-    'pullNumber N, merge_method "squash" e expectedHeadSha <sha de 40 caracteres>; PR aberto, head = expectedHeadSha e CI do PR verde.\n' +
-    `Todo merge: recado do po (ou do Alexandre) em ${PASTA_AUTORIZACOES} do aloirr/bapajudacatalogo-recados com "autorizo o merge do PR #N no commit <sha>" (R-20261120-111308-alexandre).\n` +
+    'pullNumber N, merge_method "squash", expectedHeadSha <sha de 40 caracteres> e commit_message "<resumo> (T-nnnn)\\n\\nAgente: <dono>"; ' +
+    'PR aberto, head = expectedHeadSha e CI do PR verde.\n' +
+    `${REGRA_MERGE}\n` +
     'Não contorne o bloqueio (gh api, outra ferramenta, script): se a regra impede o merge, avise o po por recado.'
diff --git a/.claude/hooks/guarda-merge-mcp.mjs b/.claude/hooks/guarda-merge-mcp.mjs
index 76246b6..4cc9c50 100644
--- a/.claude/hooks/guarda-merge-mcp.mjs
+++ b/.claude/hooks/guarda-merge-mcp.mjs
@@ -6,3 +6,4 @@
 //  - só o gerente-projetos, na sessão principal, com identidade confiável (BAP_AGENTE ou sessão local);
-//  - owner/repo aloirr/bapajudacatalogo, merge_method "squash" e expectedHeadSha de 40 caracteres;
+//  - owner/repo aloirr/bapajudacatalogo, merge_method "squash", expectedHeadSha de 40 caracteres e commit_message com a
+//    tarefa (T-nnnn) e "Agente: <dono>" (R-20261120-131230-alexandre);
 //  - pela API REST do GitHub (gh api, só leitura): PR aberto, head = expectedHeadSha e CI do PR verde;
@@ -10,42 +11,39 @@
 //    aloirr/bapajudacatalogo-recados (recados/gerente-projetos), com o mesmo N e o SHA do head.
-// Qualquer falha de consulta = BLOQUEADO (exit 2, falha fechada). Ferramenta que não é merge passa sem consultar nada.
-// Desligar: variável BAP_GUARDA=off (do processo do Claude Code, que o agente não altera), como nos outros guardiões.
-import { RAIZ, agenteDaSessao } from '../../scripts/coord-lib.mjs';
-import { conferirMergeMcp, consultarPrRest, lerRecadosDoGerente, tipoFerramentaMerge } from './guarda-merge-lib.mjs';
-
-function lerEntrada() {
-  return new Promise((ok) => {
-    let txt = '';
-    process.stdin.setEncoding('utf8');
-    process.stdin.on('data', (d) => (txt += d));
-    process.stdin.on('end', () => {
-      try { ok(JSON.parse(txt || '{}')); } catch { ok({}); }
-    });
-  });
-}
-
-if ((process.env.BAP_GUARDA || '').toLowerCase() === 'off') process.exit(0);
-
-const entrada = await lerEntrada();
-const ferramenta = String(entrada.tool_name || '');
-if (!tipoFerramentaMerge(ferramenta)) process.exit(0);
-if ((entrada.hook_event_name || 'PreToolUse') !== 'PreToolUse') process.exit(0);
-
-const { agente, origem } = agenteDaSessao({ argumento: process.argv[2], entrada });
-const r = conferirMergeMcp({
-  ferramenta, entrada: entrada.tool_input, agente, origem,
-  subagente: Boolean(String(entrada.agent_id || '').trim()),
-  consultarPr: (pr) => consultarPrRest(pr),
-  lerRecados: () => lerRecadosDoGerente(RAIZ),
-});
-if (!r.ok) {
-  process.stderr.write(r.mensagem + '\n');
+// Falha fechada: consulta que falha, entrada ilegível ou exceção = BLOQUEADO (exit 2; exit 1 não bloquearia).
+// Ferramenta que não é merge passa sem consultar nada. Desligar: BAP_GUARDA=off, como nos outros guardiões.
+const bloquear = (msg) => {
+  process.stderr.write(`${msg}\n`);
   process.exit(2);
+};
+
+try {
+  const { RAIZ, agenteDaSessao } = await import('../../scripts/coord-lib.mjs');
+  const { conferirMergeMcp, consultarPrRest, lerRecadosDoGerente, tipoFerramentaMerge } = await import('./guarda-merge-lib.mjs');
+  const { lerEntradaDoHook, guardaDesligada } = await import('./guarda-bash-lib.mjs');
+
+  if (guardaDesligada()) process.exit(0);
+  const entrada = await lerEntradaDoHook();
+  // O matcher só chama este hook nas ferramentas de merge: sem ler a entrada, não dá para conferir.
+  if (!entrada) bloquear('[guardião BAP] BLOQUEADO (merge pelo MCP do GitHub): entrada do hook ilegível; sem a conferência não há merge (falha fechada).');
+  const ferramenta = String(entrada.tool_name || '');
+  if (!tipoFerramentaMerge(ferramenta)) process.exit(0);
+  if ((entrada.hook_event_name || 'PreToolUse') !== 'PreToolUse') process.exit(0);
+
+  const { agente, origem } = agenteDaSessao({ argumento: process.argv[2], entrada });
+  const r = conferirMergeMcp({
+    ferramenta, entrada: entrada.tool_input, agente, origem,
+    subagente: Boolean(String(entrada.agent_id || '').trim()),
+    consultarPr: (pr) => consultarPrRest(pr),
+    lerRecados: () => lerRecadosDoGerente(RAIZ),
+  });
+  if (!r.ok) bloquear(r.mensagem);
+  process.stdout.write(JSON.stringify({
+    hookSpecificOutput: {
+      hookEventName: 'PreToolUse',
+      additionalContext: `[guardião BAP] merge do PR #${r.pr} conferido: head = expectedHeadSha, CI do PR verde, squash com "Agente: ${r.agenteDoCommit}" e autorização ${r.autorizacao} (de ${r.autorizadoPor}).`,
+    },
+  }) + '\n');
+  process.exit(0);
+} catch (e) {
+  bloquear(`[guardião BAP] BLOQUEADO (merge pelo MCP do GitHub): erro no guardião (${String(e?.message || e).split(/\r?\n/)[0].slice(0, 200)}); sem a conferência não há merge (falha fechada).`);
 }
-process.stdout.write(JSON.stringify({
-  hookSpecificOutput: {
-    hookEventName: 'PreToolUse',
-    additionalContext: `[guardião BAP] merge do PR #${r.pr} conferido: head = expectedHeadSha, CI do PR verde e autorização ${r.autorizacao} (de ${r.autorizadoPor}).`,
-  },
-}) + '\n');
-process.exit(0);
diff --git a/.claude/hooks/guarda-merge-mcp.test.mjs b/.claude/hooks/guarda-merge-mcp.test.mjs
index 96c1773..7b294e9 100644
--- a/.claude/hooks/guarda-merge-mcp.test.mjs
+++ b/.claude/hooks/guarda-merge-mcp.test.mjs
@@ -1,8 +1,9 @@
-// Testes do guardião de merge da T-0016 (R-20261120-111308-alexandre): autorização do po em recado, merge pela
-// integração do GitHub (guarda-merge-mcp.mjs) e leitura dos recados publicados no clone.
+// Testes do guardião de merge da T-0016 (R-20261120-111308-alexandre e R-20261120-131230-alexandre): autorização do po
+// em recado, merge pela integração do GitHub (guarda-merge-mcp.mjs) e pelo terminal (gh pr merge), leitura dos recados
+// publicados no clone e trava do clone de recados (guarda-donos.mjs e guarda-bash.mjs).
 // Rodar: node --test .claude/hooks/guarda-merge-mcp.test.mjs (sem rede; o gh é simulado por BAP_GH_SIMULADO e o
-// repositório de recados é um repositório git falso numa pasta temporária).
+// repositório de recados é um repositório git falso numa pasta temporária, aceito por BAP_RECADOS_ORIGIN_SIMULADO).
 import { test } from 'node:test';
 import assert from 'node:assert/strict';
-import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
+import { mkdtempSync, mkdirSync, writeFileSync, rmSync, readFileSync, copyFileSync } from 'node:fs';
 import { join, dirname } from 'node:path';
@@ -12,7 +13,10 @@ import { fileURLToPath } from 'node:url';
 import {
-  conferirMergeMcp, decidirMerge, autorizacoesDeMerge, autorizacoesDoAlexandre, recadosPublicadosNoClone,
-  lerRecadosDoGerente, motivosRecadoFalso, validarEntradaMergeMcp,
+  conferirMergeMcp, conferirMerge, decidirMerge, autorizacoesDeMerge, recadosPublicadosNoClone, lerRecadosDoGerente,
+  motivosRecadoFalso, motivoConteudoForjado, motivoOriginDoClone, validarEntradaMergeMcp, avaliarRollup, consultarPrGh,
+  errosDoCorpoDoSquash, DOMINIO_AUTOR,
 } from './guarda-merge-lib.mjs';
+import { AGENTES_DO_TIME } from '../../scripts/coord-lib.mjs';
 
 const AQUI = dirname(fileURLToPath(import.meta.url));
+const RAIZ = join(AQUI, '..', '..');
 const HOOK = join(AQUI, 'guarda-merge-mcp.mjs');
@@ -22,3 +26,4 @@ const FERRAMENTA = 'mcp__github__merge_pull_request';
 const GERENTE = { agente: 'gerente-projetos', origem: 'variável BAP_AGENTE' };
-const entrada = (extra = {}) => ({ owner: 'aloirr', repo: 'bapajudacatalogo', pullNumber: 42, merge_method: 'squash', expectedHeadSha: HEAD, ...extra });
+const CORPO = 'T-0016: guardião do merge (#42)\n\nAgente: gerente-projetos';
+const entrada = (extra = {}) => ({ owner: 'aloirr', repo: 'bapajudacatalogo', pullNumber: 42, merge_method: 'squash', expectedHeadSha: HEAD, commit_message: CORPO, ...extra });
 const verde = { verde: true, detalhe: '3 check(s) verdes' };
@@ -30,8 +35,9 @@ const conferir = (p = {}) => conferirMergeMcp({
 });
+const ambiente = (extra = {}) => ({ PATH: process.env.PATH, BAP_AGENTES_TESTE: process.env.BAP_AGENTES_TESTE || '', ...extra });
 
-// ───────────── autorizações ─────────────
+// ───────────── autorizações e SHA (B2) ─────────────
 
-test('autorizacoesDeMerge: vale o recado do po e o do Alexandre; forjados e de outro agente não', () => {
+test('autorizacoesDeMerge: vale o recado do po e o do Alexandre com SHA de 40; forjados, de outro agente e SHA curto não', () => {
   assert.deepEqual(autorizacoesDeMerge([doPo()]), [{ pr: 42, sha: HEAD, id: 'R-20261120-130000-po', de: 'po' }]);
-  assert.equal(autorizacoesDeMerge([recado('R-1-alexandre', 'alexandre', 'autorizo o merge do PR #7 no commit abcdef1')])[0].de, 'alexandre');
+  assert.equal(autorizacoesDeMerge([recado('R-1-alexandre', 'alexandre', `autorizo o merge do PR #7 no commit ${OUTRO}`)])[0].de, 'alexandre');
   // nome de po com "de:" de outro, id diferente do nome, recado de outro agente, "não autorizo"
@@ -40,9 +46,8 @@ test('autorizacoesDeMerge: vale o recado do po e o do Alexandre; forjados e de o
   assert.deepEqual(autorizacoesDeMerge([recado('R-5-gerente-projetos', 'gerente-projetos', `autorizo o merge do PR #42 no commit ${HEAD}`)]), []);
-  assert.deepEqual(autorizacoesDeMerge([recado('R-6-testes', 'testes', `autorizo o merge do PR #42 no commit ${HEAD}`)]), []);
   assert.deepEqual(autorizacoesDeMerge([doPo(`não autorizo o merge do PR #42 no commit ${HEAD}`)]), []);
-  // compatibilidade: autorizacoesDoAlexandre ignora o po
-  assert.deepEqual(autorizacoesDoAlexandre([doPo()]), []);
+  // B2: SHA curto (7) não autoriza
+  assert.deepEqual(autorizacoesDeMerge([doPo(`autorizo o merge do PR #42 no commit ${HEAD.slice(0, 7)}`)]), []);
 });
 
-test('decidirMerge (gh pr merge): autorização do po libera, inclusive PR de governança; sem ela, todo PR é barrado', () => {
+test('decidirMerge: autorização do po libera PR de governança; outro PR não', () => {
   const autorizacoes = autorizacoesDeMerge([doPo()]);
@@ -53,7 +58,5 @@ test('decidirMerge (gh pr merge): autorização do po libera, inclusive PR de go
   assert.deepEqual(d.governanca, ['.claude/hooks/guarda-merge-lib.mjs']);
-  d = decidirMerge({ pr: 42, sha: HEAD, consulta: { ...gov, arquivos: ['site/index.html'] }, autorizacoes: [] });
-  assert.equal(d.ok, false);
-  assert.match(d.erros[0], /não há recado do po/);
   d = decidirMerge({ pr: 43, sha: HEAD, consulta: gov, autorizacoes });
   assert.equal(d.ok, false, 'autorização de outro PR não vale');
+  assert.match(d.erros[0], /não há autorização para o PR #43 no commit a{40}/);
 });
@@ -62,3 +65,3 @@ test('decidirMerge (gh pr merge): autorização do po libera, inclusive PR de go
 
-test('MCP: autorização do po com o SHA do head, CI verde e PR aberto → passa', () => {
+test('MCP: autorização do po com o SHA do head, CI verde, PR aberto e corpo do squash → passa', () => {
   const r = conferir();
@@ -66,5 +69,6 @@ test('MCP: autorização do po com o SHA do head, CI verde e PR aberto → passa
   assert.equal(r.autorizadoPor, 'po');
+  assert.equal(r.agenteDoCommit, 'gerente-projetos');
   const gov = conferir({ consultarPr: () => consulta({ arquivos: ['.github/workflows/ci.yml'] }) });
   assert.equal(gov.ok, true, `governança também passa com o po: ${gov.mensagem}`);
-  const ale = conferir({ lerRecados: () => [recado('R-9-alexandre', 'alexandre', `autorizo o merge do PR #42 no commit ${HEAD.slice(0, 7)}`)] });
+  const ale = conferir({ lerRecados: () => [recado('R-9-alexandre', 'alexandre', `autorizo o merge do PR #42 no commit ${HEAD}`)] });
   assert.equal(ale.ok, true, ale.mensagem);
@@ -72,6 +76,7 @@ test('MCP: autorização do po com o SHA do head, CI verde e PR aberto → passa
 
-test('MCP: sem autorização, autorização em outro SHA ou de outro PR → barrado', () => {
+test('MCP: sem autorização, autorização em outro SHA, em SHA curto ou de outro PR → barrado', () => {
   let r = conferir({ lerRecados: () => [] });
   assert.equal(r.ok, false);
-  assert.match(r.mensagem, /não há recado do po/);
+  assert.match(r.mensagem, /não há autorização para o PR #42/);
+  assert.match(r.mensagem, /Todo merge: recado do po/, 'rodapé com a regra (REGRA_MERGE)');
   r = conferir({ lerRecados: () => [doPo(`autorizo o merge do PR #42 no commit ${OUTRO}`)] });
@@ -79,2 +84,4 @@ test('MCP: sem autorização, autorização em outro SHA ou de outro PR → barr
   assert.match(r.mensagem, /o PR mudou depois da aprovação/);
+  r = conferir({ lerRecados: () => [doPo(`autorizo o merge do PR #42 no commit ${HEAD.slice(0, 7)}`)] });
+  assert.equal(r.ok, false, 'B2: autorização com SHA curto não vale');
   r = conferir({ lerRecados: () => [doPo(`autorizo o merge do PR #41 no commit ${HEAD}`)] });
@@ -98,3 +105,3 @@ test('MCP: sem expectedHeadSha, SHA curto ou head diferente do expectedHeadSha 
   assert.match(r.mensagem, /o PR mudou/);
-  r = conferir({ entrada: entrada({ commit_message: `x\n\nHead-SHA: ${OUTRO}` }) });
+  r = conferir({ entrada: entrada({ commit_message: `T-0016 x\n\nHead-SHA: ${OUTRO}\nAgente: gerente-projetos` }) });
   assert.equal(r.ok, false, 'Head-SHA da mensagem diferente do expectedHeadSha');
@@ -130,4 +137,3 @@ test('MCP: parâmetros — squash obrigatório, repositório certo, nada de par
   assert.equal(conferir({ entrada: entrada({ admin: true }) }).ok, false);
-  assert.equal(conferir({ entrada: entrada({ commit_title: 'T-0016: guardião (#42)', commit_message: 'corpo\n\nAgente: gerente-projetos' }) }).ok, true);
-  assert.equal(conferir({ entrada: entrada({ commit_message: 'corpo\n\nAgente: fulano' }) }).ok, false);
+  assert.equal(conferir({ entrada: entrada({ commit_title: 'T-0016: guardião (#42)' }) }).ok, true);
   assert.equal(conferir({ ferramenta: 'mcp__github__enable_pr_auto_merge' }).ok, false);
@@ -138,5 +144,69 @@ test('MCP: parâmetros — squash obrigatório, repositório certo, nada de par
 
-// ───────────── recado falso em nome do po ─────────────
+test('squash (R-20261120-131230-alexandre): o corpo tem a tarefa e um único "Agente: <dono>" do time no fim', () => {
+  assert.deepEqual(errosDoCorpoDoSquash(CORPO, 'commit_message'), []);
+  assert.deepEqual(errosDoCorpoDoSquash('T-0017: busca por veículo\nAgente: web-site', '--body'), [], 'um bloco só também vale');
+  const casos = [
+    [undefined, /falta o corpo do squash/],
+    ['T-0016 sem trailer', /não termina com "Agente:/],
+    ['sem tarefa\n\nAgente: gerente-projetos', /não cita a tarefa/],
+    ['T-0016\n\nAgente: fulano', /não é do time/],
+    ['T-0016\n\nAgente: po\nAgente: testes', /2 "Agente:"/],
+  ];
+  for (const [corpo, re] of casos) {
+    const r = conferir({ entrada: entrada({ commit_message: corpo }) });
+    assert.equal(r.ok, false, String(corpo));
+    assert.match(r.mensagem, re);
+  }
+});
 
-test('recado falso: outro agente não grava "de: po" nem o autor po@bapajuda.invalid; o po grava', () => {
+// ───────────── merge pelo terminal (gh pr merge): B2 e B3 ─────────────
+
+const GH_MERGE = (sha = HEAD, corpo = '"T-0016: guardião\n\nAgente: gerente-projetos"') =>
+  `gh pr merge 42 -R aloirr/bapajudacatalogo --squash --match-head-commit ${sha} --body ${corpo}`;
+const conferirTerminal = (p = {}) => conferirMerge({
+  comando: GH_MERGE(), ...GERENTE, consultarPr: () => consulta(), lerRecados: () => [doPo()], ...p,
+});
+
+test('terminal: SHA de 40, corpo do squash, CI verde e autorização → passa; SHA curto, sem --body, CI vermelho ou PR fechado → barrado', () => {
+  let r = conferirTerminal();
+  assert.equal(r.ok, true, r.mensagem);
+  r = conferirTerminal({ comando: GH_MERGE(HEAD.slice(0, 7)) });
+  assert.equal(r.ok, false);
+  assert.match(r.mensagem, /não é o SHA completo/);
+  r = conferirTerminal({ comando: GH_MERGE(HEAD, '"sem agente"') });
+  assert.equal(r.ok, false);
+  assert.match(r.mensagem, /não cita a tarefa/);
+  r = conferirTerminal({ comando: `gh pr merge 42 -R aloirr/bapajudacatalogo --squash --match-head-commit ${HEAD}` });
+  assert.equal(r.ok, false);
+  assert.match(r.mensagem, /falta o corpo do squash \(--body\)/);
+  r = conferirTerminal({ consultarPr: () => consulta({ ciPr: { verde: false, detalhe: 'vermelho (conferir: failure)' } }) });
+  assert.equal(r.ok, false, 'B3: CI vermelho barra também no terminal');
+  assert.match(r.mensagem, /não está verde/);
+  r = conferirTerminal({ consultarPr: () => consulta({ estado: 'merged', mesclado: true }) });
+  assert.equal(r.ok, false);
+});
+
+test('terminal (B3): avaliarRollup e consultarPrGh leem o statusCheckRollup do gh pr view', () => {
+  assert.equal(avaliarRollup([{ __typename: 'CheckRun', name: 'conferir', status: 'COMPLETED', conclusion: 'SUCCESS' }, { __typename: 'StatusContext', context: 'x', state: 'SUCCESS' }]).verde, true);
+  assert.match(avaliarRollup([{ __typename: 'CheckRun', name: 'conferir', status: 'COMPLETED', conclusion: 'FAILURE' }]).detalhe, /vermelho/);
+  assert.match(avaliarRollup([{ __typename: 'CheckRun', name: 'conferir', status: 'IN_PROGRESS' }]).detalhe, /rodando/);
+  assert.match(avaliarRollup([{ __typename: 'StatusContext', context: 'x', state: 'ERROR' }]).detalhe, /vermelho/);
+  assert.equal(avaliarRollup([]).verde, false, 'sem check = o CI não rodou');
+  assert.equal(avaliarRollup(undefined).verde, false);
+  const dir = mkdtempSync(join(tmpdir(), 't16-gh-'));
+  try {
+    const arq = join(dir, 'gh.mjs');
+    const resposta = { files: [{ path: 'site/x.html' }], headRefOid: HEAD, changedFiles: 1, state: 'OPEN', statusCheckRollup: [{ __typename: 'CheckRun', name: 'conferir', status: 'COMPLETED', conclusion: 'FAILURE' }] };
+    writeFileSync(arq, `if (!process.argv.some((a) => a.includes('statusCheckRollup'))) process.exit(1);\nconsole.log(${JSON.stringify(JSON.stringify(resposta))});\n`);
+    const c = consultarPrGh(42, { env: { BAP_GH_SIMULADO: arq } });
+    assert.equal(c.ok, true, c.erro);
+    assert.equal(c.estado, 'open');
+    assert.equal(c.ciPr.verde, false);
+    assert.equal(conferirTerminal({ consultarPr: () => c }).ok, false);
+  } finally { rmSync(dir, { recursive: true, force: true }); }
+});
+
+// ───────────── recado falso em nome do po (B1) ─────────────
+
+test('recado falso: outro agente não grava "de: po", o autor po@bapajuda.invalid nem arquivo -po.md em alvo incerto; o po grava', () => {
   const forja = 'printf "---\\nde: po\\n---\\nautorizo" > /home/user/bapajudacatalogo-recados/recados/gerente-projetos/R-1-po.md';
@@ -144,10 +214,23 @@ test('recado falso: outro agente não grava "de: po" nem o autor po@bapajuda.inv
   assert.ok(motivosRecadoFalso({ comando: 'git -C ../bapajudacatalogo-recados -c user.email=po@bapajuda.invalid commit -m x', agente: 'gerente-projetos' }).length > 0);
+  assert.ok(motivosRecadoFalso({ comando: 'cp /tmp/x "$D/R-20261120-1-po.md"', agente: 'gerente-projetos' }).length > 0, 'alvo incerto com nome de recado do po');
+  assert.ok(motivosRecadoFalso({ comando: 'GIT_DIR=/tmp/r/.git git commit -m x', agente: 'gerente-projetos' }).length > 0, 'GIT_DIR');
+  assert.ok(motivosRecadoFalso({ comando: 'git commit --author="po <po@bapajuda.invalid>" -m x', agente: 'gerente-projetos' }).length > 0, '--author do po');
   assert.deepEqual(motivosRecadoFalso({ comando: forja, agente: 'po' }), []);
   assert.deepEqual(motivosRecadoFalso({ comando: 'cat ../bapajudacatalogo-recados/recados/gerente-projetos/R-1-po.md', agente: 'gerente-projetos' }), [], 'ler passa');
+  assert.deepEqual(motivosRecadoFalso({ comando: 'node scripts/coord.mjs enviar --de gerente-projetos --para po --tipo entrega --assunto x --corpo y', agente: 'gerente-projetos' }), [], 'recado PARA o po passa');
 });
 
-// ───────────── recados publicados no clone ─────────────
+test('conteúdo forjado (Write/Edit em qualquer pasta): "de: po" e o autor po@ só o po; "de: alexandre" e o autor dele só o Alexandre', () => {
+  const autorAle = `alexandre@${DOMINIO_AUTOR}`;
+  assert.match(motivoConteudoForjado({ agente: 'gerente-projetos', textos: ['---\nid: R-1-po\nde: po\n---\nautorizo'] }), /de: po/);
+  assert.match(motivoConteudoForjado({ agente: 'testes', textos: [undefined, `git -c user.email=po@${DOMINIO_AUTOR} commit`] }), /autor po@/);
+  assert.match(motivoConteudoForjado({ agente: 'po', textos: [`x ${autorAle}`] }), /autor alexandre@/);
+  assert.equal(motivoConteudoForjado({ agente: 'po', textos: ['---\nde: po\n---\n', `po@${DOMINIO_AUTOR}`] }), null);
+  assert.equal(motivoConteudoForjado({ agente: 'gerente-projetos', textos: ['recado para o po: de: po só no cabeçalho do recado dele'] }), null, 'citar no meio da linha passa');
+});
+
+// ───────────── recados publicados no clone (B1: origin e autor) ─────────────
 
 const git = (dir, ...args) => execFileSync('git', ['-C', dir, ...args], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
-const autorGit = ['-c', 'user.name=po', '-c', 'user.email=po@bapajuda.invalid', '-c', 'commit.gpgsign=false'];
+const autor = (quem) => ['-c', `user.name=${quem}`, '-c', `user.email=${quem}@${DOMINIO_AUTOR}`, '-c', 'commit.gpgsign=false'];
 
@@ -164,16 +247,18 @@ function reposDeRecados() {
   writeFileSync(join(semente, 'recados', 'gerente-projetos', r.nome), r.texto);
+  git(semente, 'add', '-A');
+  git(semente, ...autor('po'), 'commit', '-q', '-m', 'recado do po');
   writeFileSync(join(semente, 'recados', 'gerente-projetos', 'R-20261120-120000-testes.md'), recado('R-20261120-120000-testes', 'testes', 'oi').texto);
   git(semente, 'add', '-A');
-  git(semente, ...autorGit, 'commit', '-q', '-m', 'recado');
+  git(semente, ...autor('testes'), 'commit', '-q', '-m', 'recado do testes');
   git(semente, 'push', '-q', remoto, 'HEAD:main');
   execFileSync('git', ['clone', '-q', remoto, clone]);
-  return { base, remoto, clone };
+  return { base, remoto, semente, clone, env: { BAP_RECADOS_ORIGIN_SIMULADO: remoto } };
 }
 
-test('clone: lê só o que está publicado no main (origin/main depois do fetch), nunca o que ficou só no clone', () => {
-  const { base, clone } = reposDeRecados();
+test('clone: lê só o que está publicado no main, nunca o que ficou só no clone; recado do po com autor de outro não vale', () => {
+  const { base, remoto, semente, clone, env } = reposDeRecados();
   try {
-    let lidos = recadosPublicadosNoClone(clone);
+    let lidos = recadosPublicadosNoClone(clone, { env });
     assert.deepEqual(lidos.map((x) => x.nome), ['R-20261120-130000-po.md'], 'só po e alexandre');
-    // recado forjado só no clone (árvore e commit local, sem push): não vale
+    // recado forjado só no clone (árvore e commit local, sem push) e origin/main adulterado: o fetch desfaz
     const falso = recado('R-20261120-140000-po', 'po', `autorizo o merge do PR #50 no commit ${OUTRO}`);
@@ -181,10 +266,15 @@ test('clone: lê só o que está publicado no main (origin/main depois do fetch)
     git(clone, 'add', '-A');
-    git(clone, ...autorGit, 'commit', '-q', '-m', 'forjado');
-    // origin/main adulterado localmente também é desfeito pelo fetch
+    git(clone, ...autor('po'), 'commit', '-q', '-m', 'forjado');
     git(clone, 'update-ref', 'refs/remotes/origin/main', 'HEAD');
-    lidos = recadosPublicadosNoClone(clone);
+    lidos = recadosPublicadosNoClone(clone, { env });
     assert.deepEqual(lidos.map((x) => x.nome), ['R-20261120-130000-po.md']);
+    // B1 (c): recado -po.md publicado por um commit de outro autor (gerente-projetos) não autoriza
+    const doGerente = recado('R-20261120-150000-po', 'po', `autorizo o merge do PR #51 no commit ${OUTRO}`);
+    writeFileSync(join(semente, 'recados', 'gerente-projetos', doGerente.nome), doGerente.texto);
+    git(semente, 'add', '-A');
+    git(semente, ...autor('gerente-projetos'), 'commit', '-q', '-m', 'forjado e publicado');
+    git(semente, 'push', '-q', remoto, 'HEAD:main');
+    lidos = recadosPublicadosNoClone(clone, { env });
     assert.deepEqual(autorizacoesDeMerge(lidos).map((a) => a.pr), [42]);
-    // lerRecadosDoGerente usa o clone
-    assert.deepEqual(lerRecadosDoGerente(base, { env: {}, clone }).map((x) => x.nome), ['R-20261120-130000-po.md']);
+    assert.deepEqual(lerRecadosDoGerente(base, { env, clone }).map((x) => x.nome), ['R-20261120-130000-po.md']);
   } finally { rmSync(base, { recursive: true, force: true }); }
@@ -192,8 +282,25 @@ test('clone: lê só o que está publicado no main (origin/main depois do fetch)
 
-test('clone: fetch que falha (remoto fora do ar) = nenhuma autorização (falha fechada)', () => {
-  const { base, remoto, clone } = reposDeRecados();
+test('clone (B1 b): origin trocado, insteadOf para outro lugar ou remoto fora do ar = nenhuma autorização', () => {
+  const { base, remoto, clone, env } = reposDeRecados();
   try {
+    const gh = 'https://github.com/aloirr/bapajudacatalogo-recados';
+    assert.equal(motivoOriginDoClone({ urls: [gh], urlFetch: gh, urlPush: 'git@github.com:aloirr/bapajudacatalogo-recados.git' }), null);
+    assert.match(motivoOriginDoClone({ urls: [gh], urlFetch: '/tmp/falso.git', urlPush: gh }), /insteadOf/);
+    assert.match(motivoOriginDoClone({ urls: ['https://github.com/fulano/bapajudacatalogo-recados'] }), /não github.com/);
+    // origin trocado para um repositório falso (cópia com o recado do po): recusado
+    const falso = join(base, 'falso.git');
+    execFileSync('git', ['clone', '-q', '--bare', remoto, falso]);
+    git(clone, 'remote', 'set-url', 'origin', falso);
+    assert.throws(() => recadosPublicadosNoClone(clone, { env }), /remote.origin.url/);
+    assert.deepEqual(lerRecadosDoGerente(base, { env, clone }), []);
+    // insteadOf: o remote.origin.url continua certo, mas a URL efetiva vai para o falso
+    git(clone, 'remote', 'set-url', 'origin', remoto);
+    git(clone, 'config', `url.${falso}.insteadOf`, remoto);
+    assert.throws(() => recadosPublicadosNoClone(clone, { env }), /URL efetiva/);
+    git(clone, 'config', '--unset', `url.${falso}.insteadOf`);
+    assert.equal(recadosPublicadosNoClone(clone, { env }).length, 1);
+    // remoto fora do ar
     rmSync(remoto, { recursive: true, force: true });
-    assert.throws(() => recadosPublicadosNoClone(clone));
-    assert.deepEqual(lerRecadosDoGerente(base, { env: {}, clone }), []);
+    assert.throws(() => recadosPublicadosNoClone(clone, { env }));
+    assert.deepEqual(lerRecadosDoGerente(base, { env, clone }), []);
   } finally { rmSync(base, { recursive: true, force: true }); }
@@ -201,3 +308,3 @@ test('clone: fetch que falha (remoto fora do ar) = nenhuma autorização (falha
 
-// ───────────── o hook de verdade ─────────────
+// ───────────── os hooks de verdade ─────────────
 
@@ -219,12 +326,9 @@ else { console.error('404'); process.exit(1); }
 
-function rodarHook(tool_input, { env = {}, entradaExtra = {}, gh = {} } = {}) {
-  const { base, clone } = reposDeRecados();
+function rodarHook(tool_input, { env = {}, gh = {}, entradaBruta } = {}) {
+  const { base, clone, env: envClone } = reposDeRecados();
   try {
     const r = spawnSync(process.execPath, [HOOK], {
-      input: JSON.stringify({ hook_event_name: 'PreToolUse', tool_name: FERRAMENTA, tool_input, ...entradaExtra }),
+      input: entradaBruta ?? JSON.stringify({ hook_event_name: 'PreToolUse', tool_name: FERRAMENTA, tool_input }),
       encoding: 'utf8',
-      env: {
-        PATH: process.env.PATH, HOME: base, BAP_AGENTE: 'gerente-projetos', BAP_RECADOS_CLONE: clone,
-        BAP_GH_SIMULADO: ghSimulado(base, gh), ...env,
-      },
+      env: ambiente({ HOME: base, BAP_AGENTE: 'gerente-projetos', BAP_RECADOS_CLONE: clone, BAP_GH_SIMULADO: ghSimulado(base, gh), ...envClone, ...env }),
     });
@@ -234,3 +338,3 @@ function rodarHook(tool_input, { env = {}, entradaExtra = {}, gh = {} } = {}) {
 
-test('hook: merge com a autorização do po publicada passa (exit 0); sem expectedHeadSha, SHA diferente ou CI vermelho, exit 2', () => {
+test('hook MCP: autorização do po publicada passa (exit 0); CI vermelho e expectedHeadSha ausente saem com exit 2', () => {
   let r = rodarHook(entrada());
@@ -238,9 +342,2 @@ test('hook: merge com a autorização do po publicada passa (exit 0); sem expect
   assert.match(r.saida, /autorização R-20261120-130000-po \(de po\)/);
-  const { expectedHeadSha, ...semSha } = entrada();
-  r = rodarHook(semSha);
-  assert.equal(r.codigo, 2);
-  assert.match(r.erro, /falta o expectedHeadSha/);
-  r = rodarHook(entrada({ expectedHeadSha: OUTRO }), { gh: { head: OUTRO } });
-  assert.equal(r.codigo, 2, 'head e expectedHeadSha = OUTRO, mas o po autorizou o HEAD');
-  assert.match(r.erro, /o PR mudou depois da aprovação/);
   r = rodarHook(entrada(), { gh: { conclusao: 'failure' } });
@@ -248,14 +345,177 @@ test('hook: merge com a autorização do po publicada passa (exit 0); sem expect
   assert.match(r.erro, /não está verde/);
-  r = rodarHook(entrada(), { env: { BAP_AGENTE: 'web-site' } });
+  const { expectedHeadSha, ...semSha } = entrada();
+  r = rodarHook(semSha);
   assert.equal(r.codigo, 2);
-  r = rodarHook(entrada(), { entradaExtra: { agent_id: 'sub1', agent_type: 'gerente-projetos' } });
-  assert.equal(r.codigo, 2, 'subagente');
 });
 
-test('hook: ferramenta que não é merge passa sem consultar nada', () => {
-  const r = spawnSync(process.execPath, [HOOK], {
+test('hook MCP: entrada ilegível e exceção no guardião saem com exit 2 (falha fechada); ferramenta que não é merge passa', () => {
+  let r = rodarHook(null, { entradaBruta: '{isto não é json' });
+  assert.equal(r.codigo, 2, 'entrada ilegível');
+  assert.match(r.erro, /entrada do hook ilegível/);
+  r = rodarHook(null, { entradaBruta: '' });
+  assert.equal(r.codigo, 2, 'entrada vazia');
+  // exceção: o hook sozinho, sem as bibliotecas ao lado (o import falha)
+  const dir = mkdtempSync(join(tmpdir(), 't16-hook-'));
+  try {
+    mkdirSync(join(dir, '.claude', 'hooks'), { recursive: true });
+    copyFileSync(HOOK, join(dir, '.claude', 'hooks', 'guarda-merge-mcp.mjs'));
+    const s = spawnSync(process.execPath, [join(dir, '.claude', 'hooks', 'guarda-merge-mcp.mjs')], {
+      input: JSON.stringify({ hook_event_name: 'PreToolUse', tool_name: FERRAMENTA, tool_input: entrada() }), encoding: 'utf8', env: ambiente(),
+    });
+    assert.equal(s.status, 2, s.stderr);
+    assert.match(s.stderr, /erro no guardião/);
+  } finally { rmSync(dir, { recursive: true, force: true }); }
+  const n = spawnSync(process.execPath, [HOOK], {
     input: JSON.stringify({ hook_event_name: 'PreToolUse', tool_name: 'mcp__github__pull_request_read', tool_input: {} }),
-    encoding: 'utf8', env: { PATH: process.env.PATH, BAP_AGENTE: 'gerente-projetos', BAP_GH_SIMULADO: '/nao/existe.mjs' },
+    encoding: 'utf8', env: ambiente({ BAP_AGENTE: 'gerente-projetos', BAP_GH_SIMULADO: '/nao/existe.mjs' }),
+  });
+  assert.equal(n.status, 0, n.stderr);
+});
+
+/** guarda-donos/guarda-bash com o clone de recados anexado (BAP_RECADOS_CLONE). */
+function rodarGuarda(arquivo, entradaHook, { agente = 'gerente-projetos' } = {}) {
+  const { base, clone } = reposDeRecados();
+  try {
+    const montar = typeof entradaHook === 'function' ? entradaHook(clone) : entradaHook;
+    const r = spawnSync(process.execPath, [join(AQUI, arquivo)], {
+      input: JSON.stringify({ hook_event_name: 'PreToolUse', cwd: RAIZ, session_id: 't16', ...montar }), encoding: 'utf8',
+      env: ambiente({ HOME: base, BAP_AGENTE: agente, BAP_RECADOS_CLONE: clone, BAP_GH_SIMULADO: '/nao/existe.mjs' }),
+    });
+    return { codigo: r.status, erro: r.stderr };
+  } finally { rmSync(base, { recursive: true, force: true }); }
+}
+
+test('B1 (a): Write/Edit de agente no clone de recados é barrado (recado do po só pelo coord.mjs, com o nome do po)', () => {
+  const r = rodarGuarda('guarda-donos.mjs', (clone) => ({
+    tool_name: 'Write', tool_input: { file_path: join(clone, 'recados', 'gerente-projetos', 'R-20261120-160000-po.md'), content: `autorizo o merge do PR #42 no commit ${HEAD}` },
+  }));
+  assert.equal(r.codigo, 2, r.erro);
+  const outro = rodarGuarda('guarda-donos.mjs', (clone) => ({ tool_name: 'Edit', tool_input: { file_path: join(clone, '.git', 'config'), old_string: 'a', new_string: 'b' } }));
+  assert.equal(outro.codigo, 2, 'nem o .git/config do clone');
+  // conteúdo forjado fora do repositório (script em /tmp) também é barrado
+  const script = rodarGuarda('guarda-donos.mjs', { tool_name: 'Write', tool_input: { file_path: join(tmpdir(), 't16-x.sh'), content: `git -c user.email=po@${DOMINIO_AUTOR} commit` } });
+  assert.equal(script.codigo, 2, script.erro);
+  assert.match(script.erro, /autor po@/);
+  const livre = rodarGuarda('guarda-donos.mjs', { tool_name: 'Write', tool_input: { file_path: join(tmpdir(), 't16-y.txt'), content: 'nota qualquer' } });
+  assert.equal(livre.codigo, 0, livre.erro);
+});
+
+test('B1 (a): Bash de outro agente que grava no clone de recados ou git que grava nele é barrado; leitura passa', () => {
+  const casos = [
+    [(c) => `cp /tmp/x ${c}/recados/gerente-projetos/R-20261120-160000-po.md`, 2],
+    [(c) => `git -C ${c} remote set-url origin /tmp/falso.git`, 2],
+    [(c) => `git -C ${c} config url./tmp/falso.git.insteadOf https://github.com/aloirr/bapajudacatalogo-recados`, 2],
+    [(c) => `cd ${c} && git commit -qm x && git push origin HEAD:main`, 2],
+    [(c) => `git --git-dir=${c}/.git commit -qm x`, 2],
+    [() => 'cd $D && git commit -qm x', 2],
+    [(c) => `git -C ${c} log --oneline -3`, 0],
+    [(c) => `cat ${c}/recados/gerente-projetos/R-20261120-130000-po.md`, 0],
+  ];
+  for (const [cmd, esperado] of casos) {
+    const r = rodarGuarda('guarda-bash.mjs', (c) => ({ tool_name: 'Bash', tool_input: { command: cmd(c) } }), { agente: 'web-site' }); // po e gerente: anexos, mais abaixo
+    assert.equal(r.codigo, esperado, `${cmd('<clone>')}: ${r.erro}`);
+  }
+});
+
+// ───────────── CI (RD-0024) ─────────────
+
+test('ci.yml: BAP_AGENTES_TESTE é a mesma lista de AGENTES_DO_TIME (coord-lib.mjs)', () => {
+  const ci = readFileSync(join(RAIZ, '.github', 'workflows', 'ci.yml'), 'utf8');
+  const linha = ci.match(/BAP_AGENTES_TESTE:\s*(\S+)/);
+  assert.ok(linha, 'BAP_AGENTES_TESTE no ci.yml');
+  assert.deepEqual(linha[1].split(','), AGENTES_DO_TIME);
+});
+
+// ───────────── T-0016c: só success é verde ─────────────
+
+test('CI verde = só success (T-0016c): neutral e skipped barram no terminal e no MCP', () => {
+  for (const conclusao of ['NEUTRAL', 'SKIPPED']) {
+    const rollup = avaliarRollup([{ __typename: 'CheckRun', name: 'conferir', status: 'COMPLETED', conclusion: conclusao }]);
+    assert.equal(rollup.verde, false, conclusao);
+    assert.equal(conferirTerminal({ consultarPr: () => consulta({ ciPr: rollup }) }).ok, false, `terminal ${conclusao}`);
+  }
+  for (const conclusao of ['neutral', 'skipped']) {
+    const r = rodarHook(entrada(), { gh: { conclusao } });
+    assert.equal(r.codigo, 2, `MCP ${conclusao}`);
+    assert.match(r.erro, /não está verde/);
+  }
+});
+
+// ───────────── T-0016c: anexos do po e do gerente-projetos no clone ─────────────
+
+/** Clone de recados falso + hooks rodando sobre ele (origin aceito por BAP_RECADOS_ORIGIN_SIMULADO). */
+function comClone(fn) {
+  const { base, remoto, clone } = reposDeRecados();
+  const rodar = (arquivo, entradaHook, agente = 'gerente-projetos') => {
+    const r = spawnSync(process.execPath, [join(AQUI, arquivo)], {
+      input: JSON.stringify({ hook_event_name: 'PreToolUse', cwd: RAIZ, session_id: 't16c', ...entradaHook }), encoding: 'utf8',
+      env: ambiente({ HOME: base, BAP_AGENTE: agente, BAP_RECADOS_CLONE: clone, BAP_RECADOS_ORIGIN_SIMULADO: remoto, BAP_GH_SIMULADO: '/nao/existe.mjs' }),
+    });
+    return { codigo: r.status, erro: r.stderr };
+  };
+  const bash = (command, agente) => rodar('guarda-bash.mjs', { tool_name: 'Bash', tool_input: { command } }, agente);
+  try { fn({ base, remoto, clone, rodar, bash }); } finally { rmSync(base, { recursive: true, force: true }); }
+}
+const ANEXO = 'recados/anexos/T-0016/print.png';
+
+test('anexos: o po e o gerente-projetos copiam e publicam em recados/anexos/** (Write, mkdir, cp, add, commit, pull, push)', () => {
+  for (const agente of ['po', 'gerente-projetos']) {
+    comClone(({ clone, rodar, bash }) => {
+      let r = rodar('guarda-donos.mjs', { tool_name: 'Write', tool_input: { file_path: join(clone, 'recados', 'anexos', 'T-0016', 'nota.txt'), content: 'print do site' } }, agente);
+      assert.equal(r.codigo, 0, `${agente} Write: ${r.erro}`);
+      r = bash(`mkdir -p ${clone}/recados/anexos/T-0016 && cp /tmp/x.png ${clone}/${ANEXO}`, agente);
+      assert.equal(r.codigo, 0, `${agente} cp: ${r.erro}`);
+      r = bash(`git -C ${clone} pull --rebase -q`, agente);
+      assert.equal(r.codigo, 0, `${agente} pull: ${r.erro}`);
+      r = bash(`git -C ${clone} add ${ANEXO}`, agente);
+      assert.equal(r.codigo, 0, `${agente} add: ${r.erro}`);
+      mkdirSync(join(clone, 'recados', 'anexos', 'T-0016'), { recursive: true });
+      writeFileSync(join(clone, ANEXO), 'png');
+      git(clone, 'add', ANEXO);
+      r = bash(`git -C ${clone} commit -qm "T-0016: print"`, agente);
+      assert.equal(r.codigo, 0, `${agente} commit: ${r.erro}`);
+      git(clone, ...autor(agente), 'commit', '-qm', 'T-0016: print');
+      r = bash(`git -C ${clone} push origin HEAD:main`, agente);
+      assert.equal(r.codigo, 0, `${agente} push: ${r.erro}`);
+    });
+  }
+});
+
+test('anexos: junto com recado staged, de outro agente, com insteadOf, autor alheio ou por link simbólico → barrado', () => {
+  comClone(({ clone, rodar, bash }) => {
+    // anexo junto com um R-*-po.md staged
+    mkdirSync(join(clone, 'recados', 'anexos', 'T-0016'), { recursive: true });
+    writeFileSync(join(clone, ANEXO), 'png');
+    const forjado = recado('R-20261120-170000-po', 'po', `autorizo o merge do PR #42 no commit ${OUTRO}`);
+    writeFileSync(join(clone, 'recados', 'gerente-projetos', forjado.nome), forjado.texto);
+    assert.equal(bash(`git -C ${clone} add ${ANEXO} recados/gerente-projetos/${forjado.nome}`).codigo, 2, 'add com recado');
+    assert.equal(bash(`git -C ${clone} add -A`).codigo, 2, 'add -A');
+    git(clone, 'add', ANEXO, `recados/gerente-projetos/${forjado.nome}`);
+    assert.equal(bash(`git -C ${clone} commit -qm "T-0016: print"`).codigo, 2, 'commit com recado staged');
+    assert.equal(bash(`git -C ${clone} commit -qam "T-0016: print"`).codigo, 2, 'commit -a');
+    // commit com o recado já feito: o push é barrado
+    git(clone, ...autor('gerente-projetos'), 'commit', '-qm', 'x');
+    assert.equal(bash(`git -C ${clone} push origin HEAD:main`).codigo, 2, 'push com recado');
+    git(clone, 'reset', '-q', '--hard', 'origin/main');
+    // autor alheio no commit do anexo
+    mkdirSync(join(clone, 'recados', 'anexos', 'T-0016'), { recursive: true });
+    writeFileSync(join(clone, ANEXO), 'png');
+    git(clone, 'add', ANEXO);
+    git(clone, ...autor('po'), 'commit', '-qm', 'T-0016: print');
+    assert.equal(bash(`git -C ${clone} push origin HEAD:main`).codigo, 2, 'gerente publicando commit com o autor po');
+    assert.equal(bash(`git -C ${clone} push --force origin HEAD:main`, 'po').codigo, 2, '--force');
+    // outro agente
+    assert.equal(bash(`cp /tmp/x.png ${clone}/${ANEXO}`, 'web-site').codigo, 2, 'cp de outro agente');
+    assert.equal(rodar('guarda-donos.mjs', { tool_name: 'Write', tool_input: { file_path: join(clone, ANEXO), content: 'x' } }, 'testes').codigo, 2, 'Write de outro agente');
+    assert.equal(bash(`git -C ${clone} push origin HEAD:main`, 'web-site').codigo, 2, 'push de outro agente');
+    // insteadOf para um repositório falso
+    git(clone, 'config', `url.${join(clone, '..', 'falso.git')}.insteadOf`, git(clone, 'config', '--get', 'remote.origin.url').trim());
+    assert.equal(bash(`git -C ${clone} push origin HEAD:main`, 'po').codigo, 2, 'insteadOf no push');
+    assert.equal(bash(`git -C ${clone} pull --rebase`, 'po').codigo, 2, 'insteadOf no pull');
+    // link simbólico de dentro dos anexos para a caixa do gerente
+    execFileSync('ln', ['-s', join(clone, 'recados', 'gerente-projetos'), join(clone, 'recados', 'anexos', 'atalho')]);
+    const r = rodar('guarda-donos.mjs', { tool_name: 'Write', tool_input: { file_path: join(clone, 'recados', 'anexos', 'atalho', 'R-20261120-180000-po.md'), content: 'autorizo' } }, 'po');
+    assert.equal(r.codigo, 2, 'Write por link simbólico');
+    assert.equal(bash(`ln -s ${clone}/recados/gerente-projetos ${clone}/recados/anexos/outro`, 'po').codigo, 2, 'ln nos anexos');
   });
-  assert.equal(r.status, 0, r.stderr);
 });
diff --git a/.claude/hooks/guarda-recado.test.mjs b/.claude/hooks/guarda-recado.test.mjs
index 0fb84e7..53579eb 100644
--- a/.claude/hooks/guarda-recado.test.mjs
+++ b/.claude/hooks/guarda-recado.test.mjs
@@ -6,3 +6,3 @@
 // Parte 3: git add/commit/stash de recado do Alexandre já existente (liberado se intacto).
-// Os casos de recado falso do v5 continuam em guarda-merge.test.mjs (sem mudança).
+// Os casos de recado falso em nome do po (T-0016) ficam em guarda-merge-mcp.test.mjs.
 import { test, after } from 'node:test';
diff --git a/.claude/settings.json b/.claude/settings.json
index d0b4a91..39b0da3 100644
--- a/.claude/settings.json
+++ b/.claude/settings.json
@@ -75,3 +75,4 @@
             "type": "command",
-            "command": "node .claude/hooks/guarda-bash.mjs"
+            "command": "node .claude/hooks/guarda-bash.mjs",
+            "timeout": 120
           }
diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
index 5bfe309..041252d 100644
--- a/.github/workflows/ci.yml
+++ b/.github/workflows/ci.yml
@@ -1,2 +1,2 @@
-# CI do PR do Bap Ajuda catálogo (20/11/2026). Governança: mudança só com a autorização do Alexandre.
+# CI do PR do Bap Ajuda catálogo (20/11/2026). Merge: ver CLAUDE.md, Merge (R-20261120-111308-alexandre).
 name: ci
@@ -26,3 +26,3 @@ jobs:
         run: node scripts/coord.mjs verificar --base "origin/$BASE_REF"
-      - name: Governança (avisa; o merge exige a autorização do po)
+      - name: Governança (lista os caminhos de governança; não bloqueia)
         env:
@@ -30,3 +30,3 @@ jobs:
         run: |
-          node scripts/coord.mjs governanca --base "origin/$BASE_REF" || echo "::warning::PR com caminho de governança: precisa do recado do po 'autorizo o merge do PR #N no commit <sha>' (R-20261120-111308-alexandre)"
+          node scripts/coord.mjs governanca --base "origin/$BASE_REF" || echo "::warning::PR com caminho de governança: o po confere esses arquivos antes de autorizar o merge"
       - name: Python compila
diff --git a/CLAUDE.md b/CLAUDE.md
index 1d7a5c3..607a573 100644
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -39,5 +39,6 @@ Catálogo da **BAP AUTOPARTS**. Tudo é em **português do Brasil**: respostas,
   - `.claude/**`, `.coord/donos.json`, `render.yaml`, `.github/**`, `CLAUDE.md` e `.gitignore` são do **Alexandre**.
-- **Caminho:** pedido → `po` → tarefa → `gerente-projetos` → donos → `testes` → `designer-ux` e `design-de-marca` (em mudança de tela, PDF ou marca) → `revisor-codigo` → `corretor-redundancias` → PR → `po` → Alexandre.
+- **Caminho:** pedido → `po` → tarefa → `gerente-projetos` → donos → `testes` → `designer-ux` e `design-de-marca` (em mudança de tela, PDF ou marca) → `revisor-codigo` → `corretor-redundancias` → PR → `po` (autoriza o merge; as simulações vão ao Alexandre).
   - **Merge (R-20261120-111308-alexandre):** o `po` autoriza todos os merges, inclusive os de governança, depois de conferir o número, o SHA do head, os arquivos, o CI verde e as revisões LIBERADO; cada autorização fica em recado, com o número e o SHA. O `gerente-projetos` executa o merge.
-  - O guardião confere todo merge (pelo terminal e pela integração do GitHub): o SHA do head, o CI do PR verde e o recado do `po` (ou do Alexandre) 'autorizo o merge do PR #N no commit <sha>' (T-0016).
+  - Todo merge é squash, com expectedHeadSha e, no corpo, 'Agente: <dono>' e a tarefa (R-20261120-131230-alexandre).
+  - O guardião confere todo merge (pelo terminal e pela integração do GitHub): o SHA do head (40 caracteres), o CI do PR verde e esse recado do `po` (ou do Alexandre), publicado no `bapajudacatalogo-recados` (T-0016).
   - As simulações de tela e de PDF continuam indo ao Alexandre.
@@ -61,3 +62,3 @@ Catálogo da **BAP AUTOPARTS**. Tudo é em **português do Brasil**: respostas,
   - **Autorizado pelo Alexandre (20/11/2026):** gravar direto no `main` do `bapajudacatalogo-recados`, só em `recados/` e `lidos/`. O código deste repositório continua indo por branch e PR.
-- **Donos:** `.coord/donos.json` (a primeira regra que casa manda). Governança (`.claude`, `donos.json`, `coord*.mjs`, `.github`, `render.yaml`, `CLAUDE.md`, `.gitignore`) só com o recado do `po` "autorizo o merge do PR #N no commit <sha>" (R-20261120-111308-alexandre); o `gerente-projetos` executa.
+- **Donos:** `.coord/donos.json` (a primeira regra que casa manda). Governança (`.claude`, `donos.json`, `coord*.mjs`, `.github`, `render.yaml`, `CLAUDE.md`, `.gitignore`): merge como em **Merge**, acima.
 - Recado do celular: issue com o formulário **Recado** no `aloirr/bapajudacatalogo-recados` (conta domontecristo).
diff --git a/scripts/coord-lib.mjs b/scripts/coord-lib.mjs
index 49551f5..0a6944d 100644
--- a/scripts/coord-lib.mjs
+++ b/scripts/coord-lib.mjs
@@ -14,5 +14,5 @@ export const RAIZ = resolve(dirname(fileURLToPath(import.meta.url)), '..');
 
-// Time do Bap Ajuda catálogo (20/11/2026). BAP_AGENTES_TESTE (só nos testes; o CI passa os mesmos 11 nomes, T-0016)
-// troca a lista; fora dos testes ela nunca é definida.
-const AGENTES_DO_TIME = [
+// Time do Bap Ajuda catálogo (20/11/2026). BAP_AGENTES_TESTE (só nos testes; o CI passa os mesmos 11 nomes, T-0016;
+// guarda-merge-mcp.test.mjs confere) troca a lista; fora dos testes ela nunca é definida.
+export const AGENTES_DO_TIME = [
   'gerente-projetos',
@@ -735,3 +735,3 @@ export function agenteDaSessao({ argumento, entrada, env = process.env, raiz = R
 //   (REST compare) e baixa só os arquivos novos (blob a blob; muitos de uma vez, pelo tarball do commit). Os textos do
-//   cache são conferidos pelo hash do git; a lista que autoriza merge (guarda-merge) vem sempre direto do GitHub.
+//   cache são conferidos pelo hash do git; a lista que autoriza merge (lerRecadosDoGerente, guarda-merge-lib.mjs) vem sempre direto do GitHub.
 // - Token só do ambiente: BAP_RECADOS_TOKEN, GH_TOKEN, GITHUB_TOKEN ou `gh auth token`. Nunca vai para arquivo,
diff --git a/scripts/coord-recados.test.mjs b/scripts/coord-recados.test.mjs
index be158ce..5233013 100644
--- a/scripts/coord-recados.test.mjs
+++ b/scripts/coord-recados.test.mjs
@@ -21,3 +21,6 @@ import {
 } from './coord-lib.mjs';
-import { lerRecadosDoGerente, autorizacoesDoAlexandre } from '../.claude/hooks/guarda-merge-lib.mjs';
+import { lerRecadosDoGerente, autorizacoesDeMerge } from '../.claude/hooks/guarda-merge-lib.mjs';
+
+/** SHA de 40 caracteres da autorização dos exemplos (T-0016, B2: SHA curto não vale). */
+const SHA_9 = 'abcdef1'.padEnd(40, '0');
 
@@ -198,3 +201,3 @@ function base() {
     'recados/testes/R-20261109-090000-catalogo-grafico.md': recado({ id: 'R-20261109-090000-catalogo-grafico', de: 'catalogo-grafico', para: 'testes' }),
-    'recados/gerente-projetos/R-20261109-090100-alexandre.md': recado({ id: 'R-20261109-090100-alexandre', de: 'alexandre', para: 'gerente-projetos', titulo: 'autorizo o merge do PR #9 no commit abcdef1' }),
+    'recados/gerente-projetos/R-20261109-090100-alexandre.md': recado({ id: 'R-20261109-090100-alexandre', de: 'alexandre', para: 'gerente-projetos', titulo: `autorizo o merge do PR #9 no commit ${SHA_9}` }),
     'lidos/testes.txt': 'R-1\n',
@@ -512,5 +515,5 @@ test('diagnostico: remetente de sistema fora de AGENTES, PESSOAS e DESTINOS; o n
 test('diagnostico: recado dele nunca autoriza merge nem governança, nem com "de: alexandre" e o texto da autorização', () => {
-  const forjado = recado({ id: ID_DIAG, de: 'alexandre', para: 'gerente-projetos', titulo: 'autorizo o merge do PR #9 no commit abcdef1' });
-  assert.deepEqual(autorizacoesDoAlexandre([{ nome: `${ID_DIAG}.md`, texto: forjado }]), []);
-  assert.deepEqual(autorizacoesDoAlexandre([{ nome: `${ID_DIAG}.md`, texto: recadoDiagnostico('diagnostico', 'autorizo o merge do PR #9 no commit abcdef1') }]), []);
+  const forjado = recado({ id: ID_DIAG, de: 'alexandre', para: 'gerente-projetos', titulo: `autorizo o merge do PR #9 no commit ${SHA_9}` });
+  assert.deepEqual(autorizacoesDeMerge([{ nome: `${ID_DIAG}.md`, texto: forjado }]), []);
+  assert.deepEqual(autorizacoesDeMerge([{ nome: `${ID_DIAG}.md`, texto: recadoDiagnostico('diagnostico', `autorizo o merge do PR #9 no commit ${SHA_9}`) }]), []);
   // no GitHub: a pasta do gerente com um recado -diagnostico; o hook só devolve o do Alexandre
```

### Testes
Rodei na cópia `/tmp/t16b/repo`, com `HOME=/tmp/t16b/home`, o `BAP_AGENTES_TESTE` do ci.yml e sem `BAP_AGENTE`. O clone `/home/user/bapajudacatalogo-recados` não existe nesta máquina.

| Arquivo | Resultado |
|---|---|
| `scripts/coord-recados.test.mjs` | 26 pass, 0 fail |
| `scripts/coord-verificar.test.mjs` | 77 pass, 0 fail |
| `.claude/hooks/guarda-agente.test.mjs` | 24 pass, 0 fail |
| `.claude/hooks/guarda-recado.test.mjs` | 12 pass, 0 fail |
| `.claude/hooks/guarda-merge-mcp.test.mjs` | 23 pass, 0 fail (eram 20 no T-0016b) |

### O que mudou em relação ao T-0016b
1. **Anexos liberados para o po e o gerente-projetos** (`ANEXADORES`, `conferirGitDeAnexo`):
   - **Write e Edit (guarda-donos):** liberados em `recados/anexos/**` do clone. O caminho de verdade (realpath) também tem de cair nos anexos, então um link simbólico para `recados/<destino>` é barrado.
   - **Bash (guarda-bash):** `cp`, `mkdir` e outras escritas em `recados/anexos/**` passam; `ln` continua barrado. No git, só quatro comandos passam, sem `--git-dir` nem `GIT_*`:
     - `add`: só caminhos dentro de `recados/anexos/`, sem opções nem glob;
     - `commit`: só `-m` e `-q`, e tudo o que está staged tem de estar em `recados/anexos/`;
     - `pull`: só `--rebase` e `-q`;
     - `push`: só `origin HEAD:main`, sem `--force`. Os commits a publicar (`origin/main..HEAD`) só podem mexer em anexos e têm de ter o autor `<agente>@bapajuda.invalid`.
   - **Origin (B1-b):** a conferência vale também no `pull` e no `push`. Reaproveitei a mesma leitura das URLs (`urlsDoOrigin`).
   - **O que continua barrado:** outro papel e qualquer caminho staged fora dos anexos. Recados e lidos seguem só pelo `coord.mjs`.
   - **Testes novos:** anexo pelo po passa; anexo pelo gerente passa; anexo junto com `R-*-po.md` staged é barrado (`add`, `add -A`, `commit`, `commit -a`, `push`); outro agente é barrado; insteadOf barra o `push` e o `pull`. Também cobri o autor alheio no push, `--force`, o link simbólico e o `ln`.
   - **Teste B1 do Bash ajustado:** passou a rodar como `web-site`. O gerente agora pode fazer commit e push de anexo, e os casos dele ficaram nos testes de anexo.
2. **CLAUDE.md:** voltou a linha "As simulações de tela e de PDF continuam indo ao Alexandre". A linha do Caminho continua como no T-0016b.
3. **CI verde = só success** (`CONCLUSOES_VERDES = ['success']`), no terminal e no MCP. Teste novo: neutral e skipped barram nos dois caminhos.

### [SUPOSIÇÕES]
- **Autor do recado do celular:** mantido como no T-0016b, até a resposta do Alexandre.
- **Anexo pela pasta incerta:** o `git -C <clone>` de anexo exige a pasta por extenso, como o resto do B1. Um `cd ~/bapajudacatalogo-recados && git push` é barrado; use o caminho completo.
- **Nomes que travam:** um anexo com nome de recado (`*-po.md`) copiado pelo gerente é barrado pelo `motivosRecadoFalso`; pelo po, passa.

Fora do escopo e anteriores ao PR: iguais aos do T-0016b. Cópia local do patch (só nesta máquina): `/tmp/claude-0/-home-user-bapajudacatalogo/9f488143-bf2d-5874-b6b4-70bb8bce1aac/scratchpad/T-0016c.patch`.