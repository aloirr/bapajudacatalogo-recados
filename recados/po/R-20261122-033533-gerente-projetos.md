---
id: R-20261122-033533-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: alta
tarefa: T-0019
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-22T03:35:33+00:00
---
# Pedido de autorização de merge: PR #109 no commit 1953f021b9296405c679e65bfd2ee6db4ea9c2f0

# Pedido de autorização de merge: PR #109 no commit 1953f021b9296405c679e65bfd2ee6db4ea9c2f0

**T-0019, RD-0293.** A composição do kit aparece uma vez só nas 15 embreagens pesadas. O A4 continua com 56 páginas e o Digital passa a 311. Foi a opção "a" do Alexandre (R-20261122-030552-alexandre).

## Conferência
- **PR #109:** branch catalogo-grafico/T-0019-rd0293-sim, head 1953f021b9296405c679e65bfd2ee6db4ea9c2f0, mergeable_state clean.
- **Arquivos:** 11, todos em `catalogo_grafico/`:
  - gerador/detalhe.py, teste_bloco_b_pdf.py e LEIA_GERADOR.md;
  - entregas/Catalogo_BAP_2027_A4_grafica.pdf e Completo_Digital.pdf;
  - simulacoes/T-0019/rd0293/.
- **CI verde no head:** conferir, site e GitGuardian.

## Revisões
| Quem | Head | Resultado |
|---|---|---|
| testes | f29da61 | PASSOU nos 5 itens: 23 testes; páginas A4 56, Digital 311 e Moto 17; 0 quebra no meio; 0 palavra proibida; AUTOIMPACT por último; nenhum código some; "Leve também" idêntico; gerar_site sem [PARADO]. O 1953f02 não muda os PDFs nem os subtítulos (SHA-256 igual nas 4.648 linhas). |
| designer-ux | f29da61 | LIBERADO: as p.20 do A4 e 2, 87 e 112 do Digital são idênticas pixel a pixel às pranchas aprovadas. entregas/ não muda no 1953f02. |
| design-de-marca | f29da61 | LIBERADO: logo, fontes, cores e tag NOVO iguais ao main. entregas/ não muda no 1953f02. |
| revisor-codigo | 1953f02 | LIBERADO (reteste); 3 testes do gerador OK. |
| corretor-redundancias | 1953f02 | LIBERADO (reteste): RD-0327 a RD-0330 CORRIGIDOS e RD-0293 CORRIGIDO. |

## Merge
Com a sua autorização, faço squash com expectedHeadSha 1953f021b9296405c679e65bfd2ee6db4ea9c2f0 e a mensagem "T-0019: composição do kit dita uma vez nas embreagens pesadas (RD-0293); Digital com 311 páginas (T-0019)", trailer "Agente: catalogo-grafico".
