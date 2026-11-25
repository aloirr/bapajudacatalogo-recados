---
id: R-20261125-010242-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: normal
tarefa: T-0034
responde_a: R-20261124-232429-po
encerra: false
contrato: null
criado_em: 2026-11-25T01:02:42+00:00
---
# T-0034 no ar: #194, #195 e #196 com merge; publicação no Render com sucesso

Merges (squash, com expectedHeadSha, autorização R-20261124-232429-po):
- #194 (fd76490) → a3c0493007060a40a5d0c2ae665a98a11a0322ce
- #195 (7756c47) → 0150358a7b973db2de753a90eaf66bae5e42356b
- #196 (f6a0c26) → 7b4ccfd484a93c156c877d8fe0b81fb3c184f087 (main atual)

Render (bapajudacatalogo-login): deploy do 7b4ccfd com SUCESSO às 23:27 UTC (19:27 Manaus), segundo o status de deployment no GitHub.
Não consegui abrir o site daqui: o proxy desta sessão bloqueia o onrender.com. Peço uma conferência rápida no ar:
1) entrar como bap.vendedor e abrir Estoque: só 6 colunas, sem R$, com 'Posição de … às …';
2) entrar como admin: 23 colunas; na Criar usuários aparece a caixa 'Pode ver o estoque';
3) um cliente não vê o item e recebe 404 em /estoque.
Se a aba disser 'Estoque indisponível no momento.', a planilha da BAP Central não carregou; me avise.

Próximos passos: PR de registro (pareceres de UX, marca e corretor, a tarefa, o quadro e o ROADMAP) e, depois, os 4 itens para a fila. Depois disso, a T-0033 continua parada até você chamar.
