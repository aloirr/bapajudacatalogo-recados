---
id: R-20261122-082614-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: normal
tarefa: T-0022
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T08:26:14+00:00
---
# T-0022: previews.generation no render.yaml (governança); bloco pronto, recomendo não mexer agora

Último arremate da T-0022. O render.yaml usa pullRequestPreviewsEnabled: false em 2 serviços: no bapajudacatalogo (linha 12) e no bapajudacatalogo-login (linha 59). A placa usa rootDir e não tem o campo.

[SUPOSIÇÃO] Pela referência oficial do Render (render-oss/skills, field-reference), esse é o nome antigo. O atual é:
    previews:
      generation: off
O revisor não conseguiu abrir o render.com, porque o proxy bloqueia. O nome antigo continua funcionando: o Sync da fase A e o da fase B passaram com ele.

Pergunta:
1) O que fazer com o campo?
   a) Deixar como está e fechar a pendência. Funciona, e trocar não muda nada no ar. Se o Render avisar que o campo saiu de uso, trocamos. (RECOMENDADO)
   b) Trocar agora. O bloco: nas 2 linhas, 'pullRequestPreviewsEnabled: false' vira as 2 linhas acima, com a mesma indentação dos outros campos do serviço. Num PR seu, com revisor e corretor, e conferido no Sync.

Os outros arremates da T-0022 estão no #131 (registro e README) e no #127 (placa), que já entrou.
