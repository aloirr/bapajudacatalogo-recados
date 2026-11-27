---
id: R-20261127-145105-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: alta
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T14:51:05+00:00
---
# RETOMADA — estado na pausa

# RETOMADA — estado na pausa (gerente-projetos, 27/11/2026 ~10:52 Manaus)

Pausa pedida pelo po (limite semanal ~93%). Não há nada no meio do caminho: nenhum push pela metade e nenhum PR aberto.

## No main (c5272fb77848a54f2c176048da8099f33b4044f8)
- #228: base v29 (418ede0)
- #230: testar_site e prints (bfbf1c6)
- #229: site v29 (601d714)
- #231: RD-0702 (c5272fb)
- Deploy do #229 no Render: success às 14:19Z.
- A branch catalogo-dados/T-0040-v29 foi mantida (simulação cf9db10).

## T-0040 v30: simulação aguardando o Alexandre
- **Pacote:** R-20261127-144829-gerente-projetos, com 20 perguntas (8 do site e 12 da base).
- **Base:** catalogo-dados/T-0040-v30 @ 317f5838d061c7a31aaefeae5734ec7cf94b543b, com base_v30.py, aprovar_v30.sh e dados/T-0040/v30/ (BASE_simulada_v30.xlsx e antes_depois_v30.xlsx).
  - Próximo passo: com as respostas, ajustar base_v30.py; depois `bash dados/scripts/aprovar_v30.sh R-…`, push, revisor e corretor, PR e merge.
  - O aprovar exige o origin/main ainda na v29.
- **Site:** web-site/T-0040-v30 @ 3b250fe628e25f0d026aabec7d9d53843f4d5eb3. Traz:
  - o `vo` com a lista dos ocultos [FAB, MOD];
  - o aviso "Aplicação em revisão; consulte o vendedor.";
  - o aplCartao com "FORD - …";
  - a moto primeiro, corrigida;
  - o JUH70025, o FAR6388 e a marca pelo catálogo (23 tabelas).

  Próximo passo: aplicar as respostas (ANO_DUVIDA a/b, palhetas e baterias, impressão e as outras), gerar o JSON com a v30 aprovada no main, PR, revisor e corretor, merge e deploy.
- **Prints:** testes/T-0040-v30-simulacao @ cf2aa9f973470671e41d55b578b12bed1239b703, em testes/prints/T-0040-v30/.
- **testar_site:** acusa o `vo` e o `ve` sem linha sem ano. Atualizar para a v30 depois do aprovado.
- **Pareceres v30:**
  - designer-ux LIBERADO (designer-ux/T-0040 490fe48);
  - design-de-marca LIBERADO (design-de-marca/T-0040 f3b4987; MC-0051 é sugestão para o Alexandre);
  - corretor: T-0040 sem achado aberto (corretor-redundancias/T-0040 8717b29; próximo RD-0703).

## Registro da T-0040 (no fim, combinado)
- O que entra:
  - tarefa .coord/tarefas/T-0040.md;
  - quadro;
  - PRs dos pareceres: designer-ux/T-0040, design-de-marca/T-0040 e corretor-redundancias/T-0040.

## Pendências de base (para depois)
- Perdas de detalhe no site: CRU5280, CRU512022, ROL15106/15250, INT16639/16652 e SFR30034.
- VEL7520 em Palio Fire 2005.
- VEL7507: o texto cita Agrale, Tohatsu e Mercury.
- POL1712:
  - a linha "AUDI A6 1998–2001";
  - o "4.0 7TCA" vira "7TCA".
- FCB6266: "Van 310 D" sai como 1997+.
- FAC6194: Titan Tractor.
- 1.187 pares da Fraga sem correspondência (aba DE_PARA da v29).
- RD-0699: linhas Gol duvidosas duplicadas no JUH70025 e no SFR30017.
- Parati do JUH70025 sem ano (linha 22810, duvidoso).
- VEL7561 (Caravan) e INT16533 (Express): conferir a marca.
- CXD13062: a ordem das linhas (melhoria).
- Formato do aplCartao sem a faixa de anos (sugestão de UX, outra tarefa).

## IDs dos subagentes (para retomar com SendMessage, se a sessão continuar)
- catalogo-dados: a04f6f0eaf9dbd732 (v30) e a5edd55a29b9a7645 (v29)
- web-site: a044897e8d830da6e
- testes: ac431f528b2e008a9
- revisor: a82629a1339a1fb4e (site/testes) e a15ef9aaa3d19430d (base)
- corretor: a7f89b7cd7e2d675e
- UX: a3bb770cfbf736d31
- marca: a3ad448c2b51ffb66
