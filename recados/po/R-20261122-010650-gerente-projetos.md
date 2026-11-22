---
id: R-20261122-010650-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0019
responde_a: R-20261122-010035-alexandre
encerra: false
contrato: null
criado_em: 2026-11-22T01:06:50+00:00
---
# B8 sem corte: pranchas finais do #99 no e33cfff (2 perguntas ao Alexandre)

# B8 sem corte: pranchas finais no #99, commit e33cfff (para o Alexandre ver de novo)

Commit e33cfff088065c658ab60ea815b872badd3c7dab, no branch catalogo-grafico/T-0019-pdf-v26-b (PR #99). A coluna da referência do A4 não foi alargada (REF_MAIS = 0): alargada, ela tirava 2 produtos das tabelas (BAN9518 e ABS4531) e cortava aplicações em 13 páginas.

Pranchas, antes (f52e409) e depois (e33cfff) lado a lado: `recados/anexos/T-0019/b8-final-e33cfff/`
- A4_p021.png: "Kongsberg" numa linha e "1000504869AMK" inteiro na de baixo (antes: "100050486 / 9AMK").
- A4_p029.png: "Zetec" / "Rocam/Supercharger(98.)", e as listas quebram depois da vírgula ("Ecosport," / "Focus"), não no meio da palavra.
- A4_p044.png: "FAG" numa linha e o código inteiro na de baixo (antes sobrava um dígito sozinho). **Diferença para a prancha aprovada:** lá o FAG cabia na mesma linha, porque a coluna estava mais larga.
- Digital_p083.png: o código original longo da Caixa de Direção quebra logo depois da "/".
- Digital_p147.png: as mesmas quebras na vírgula do cartão da Bomba d'Água.

Resultado:
- quebras no meio da palavra: A4 de 9 para 0, Digital de 7 para 0, Moto 0;
- páginas: A4 56, Digital 312, Moto 17 (iguais);
- só mudam essas 5 páginas.

## Uma perda pequena: Digital p.147
No cartão de destaque do BDA50003, a lista "Celta,Corsa,Prisma…" agora quebra na vírgula, não na letra, e gasta uma linha a mais. O cartão termina em "Onix 1.0 L 8V · 2012 até 2015 … (+ outras aplicações)" e sai o "· Onix 1.4 L 8V · 2012 até 2016". O produto está na tabela da mesma página, com a aplicação inteira, antes e depois.

## Perguntas ao Alexandre
1. A B8 sem corte como nas 5 pranchas (FAG da p.44 em cima do código): **a) aprovado (recomendação do gerente)**; b) diga o que muda.
2. Cartão do BDA50003 no Digital p.147: **a) aceitar o "(+ outras aplicações)" no cartão, como nos outros cartões longos; a aplicação inteira fica na tabela (recomendação do gerente)**; b) aumentar o limite de linhas dos cartões (muda a altura dos cartões em outras páginas do Digital e pede nova simulação).

## Enquanto isso
Testes, designer-ux, design-de-marca, revisor e corretor estão no e33cfff. O merge espera o "aprovado" dele e depois a sua autorização, com o número e o SHA.
