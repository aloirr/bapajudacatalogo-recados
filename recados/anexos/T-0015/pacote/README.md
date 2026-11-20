# T-0015 · O que entra no `.coord/README.md` (dono: `gerente-projetos`, num PR dele)

## 1. Primeira linha do arquivo

"time de 8 agentes" → "time de 11 agentes".

## 2. Três linhas novas na tabela "O time"

Entram logo depois da linha do `testes`, nesta ordem (a do `revisor-codigo` fica entre o `design-de-marca` e o `corretor-redundancias`, que é a ordem do caminho):

```markdown
| `designer-ux` | Visual e experiência do site e do PDF: tokens, componentes, especificação de tela e página, revisão de UX (🔴/🟡/🟢) de toda mudança de tela, PDF ou marca, antes do `revisor-codigo`. Só especifica e aponta; não edita `site/` nem `catalogo_grafico/`. | `docs/ux/` |
| `design-de-marca` | Guardião da marca BAP (logo, verde, Poppins, tom de voz) no site e nos PDFs. Em toda mudança de tela, PDF ou marca, junto com o `designer-ux` e antes do `revisor-codigo`. Só lê e aponta; o manual só tem o que o Alexandre aprovou. | `docs/marca/` |
| `corretor-redundancias` | Corta o que se repete ou sobra (telas do site, PDF, código, CI, docs, tarefas). Passa em todo PR, depois do `revisor-codigo` e antes do PR. Só lê e aponta (RD-nnnn). | `docs/qualidade/redundancias/` |
```

## 3. Frase do caminho

Abaixo do desenho de "O caminho de um pedido" (e nos passos 4 a 8):

> Caminho: dono → `testes` → `designer-ux` e `design-de-marca` (em mudança de tela, PDF ou marca) → `revisor-codigo` → `corretor-redundancias` → PR → `po` → Alexandre. O `po` autoriza todos os merges, inclusive os de governança, e o `gerente-projetos` executa (R-20261120-111308-alexandre); as simulações de tela e de PDF continuam indo ao Alexandre.

Também ajustar, pela mesma regra, o passo 8 ("Só com **"aprovado"** do Alexandre… O merge é dele.") e a última linha do desenho ("o Alexandre faz o merge no main").
