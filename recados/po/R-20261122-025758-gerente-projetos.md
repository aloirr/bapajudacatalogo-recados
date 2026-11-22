---
id: R-20261122-025758-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0019
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T02:57:58+00:00
---
# Simulação do RD-0293 no PDF: 1 pergunta ao Alexandre (Digital passa a 311 páginas)

# Simulação: composição do kit repetida no PDF (RD-0293, T-0019)

- **Branch:** `catalogo-grafico/T-0019-rd0293-sim`, commit 540b1df. Nada foi gravado nas entregas.
- **Pranchas** em `recados/anexos/T-0019/rd0293-540b1df/` (A4 p.20, Digital p.112, a p.113 que sai, sumário p.2 e p.87).

## O que muda
- **15 embreagens pesadas:** EMB1047071R, EMB3400700639R, EMB6085R, EMB6126R, EMB6146R, EMB6236R, EMB6261R, EMB6343R, EMB6453R, EMB6535R, EMB6550R, EMB6585R, EMB6635R, EMB6852R e EMB827483R.
  - Antes: "395MM 18 estrias plato/disco/mancal · c/ platô, disco, rol. e mancal".
  - Depois: "395MM 18 estrias · c/ platô, disco, rol. e mancal", igual à base v27 e ao site.
- **A4:** continua com 56 páginas. Só a p.20 muda: os subtítulos ficam mais curtos e a tabela ganha uma linha (o EMB6635R entra).
- **Digital:** passa de **312 para 311 páginas**.
  - Na p.112 cabem os 17 itens da família, e a página de continuação sai.
  - Da Servo e Cilindro de Embreagem em diante, o número de cada página diminui 1, também no sumário.
  - Fora isso, o texto e a posição de cada palavra são iguais.
- **Linha Moto:** não muda.
- **Testes:** os 3 testes do gerador passaram, com 3 casos novos. Só a família Embreagem Remanufaturada muda.

## Observação (catalogo-dados, não entra nesta pergunta)
Na base v27, o DETALHE_CATALOGO do EMB6146R ainda repete ("330MM 10 estrias plato/disco · c/ platô e disco"). O PDF não usa esse campo. Fica para a próxima versão da base.

## Pergunta ao Alexandre (para copiar e colar)
```
RD-0293: composição do kit nas embreagens pesadas (15 itens; A4 p.20, Digital p.112)
O PDF repetia: "395MM 18 estrias plato/disco/mancal · c/ platô, disco, rol. e mancal". Como fica?
a) "395MM 18 estrias · c/ platô, disco, rol. e mancal" (igual à base v27 e ao site)  <- recomendado
b) "395MM 18 estrias plato/disco/mancal" (fica a escrita da descrição)
Nas duas, o Digital passa de 312 para 311 páginas (a família Embreagem cabe numa página só) e o A4 continua com 56.
Resposta recomendada: 1) a
```

## Depois do "aprovado"
O catalogo-grafico regera os PDFs a partir deste branch. Depois vêm testes, designer-ux, design-de-marca, revisor e corretor, e o pedido da sua autorização.
