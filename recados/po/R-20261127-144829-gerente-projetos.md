---
id: R-20261127-144829-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: entrega
prioridade: alta
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T14:48:29+00:00
---
# T-0040 v30: simulação (base + site) para o Alexandre, com 20 perguntas

# T-0040 · v30: simulação para o Alexandre (base + site)

Nada disso está no main nem na base real; é só simulação.

## Onde ver
- **Prints (antes = site no ar; depois = v30):** https://github.com/aloirr/bapajudacatalogo/tree/testes/T-0040-v30-simulacao/testes/prints/T-0040-v30
- **Planilha da base:** `dados/T-0040/v30/antes_depois_v30.xlsx`, na branch `catalogo-dados/T-0040-v30` (317f583). Abas: RESUMO, APLICADAS, DIVERGENCIAS, NAO_RESOLVIDO, SEM_APLICACAO e PONTOS_ALEXANDRE.
  https://github.com/aloirr/bapajudacatalogo/raw/catalogo-dados/T-0040-v30/dados/T-0040/v30/antes_depois_v30.xlsx
- **Site da simulação:** branch `web-site/T-0040-v30` (3b250fe).

## Base: o que a pesquisa muda
- **Entram 1.115 linhas da pesquisa:**
  - 928 com o ano completado;
  - 187 com o ano trocado.
- **Ficam como estão:** 24.
- **Não entram:** 94.
  - 85 conflitos novos: o ano atual não cabe na faixa pesquisada.
  - 6 conflitos sem resolução.
  - 3 com ano inválido (ex.: 2027).
- **Não resolvidas na pesquisa:** 2.941 (ficam como estão).
- **JUH70025:** recebe "1.6 L", "1.8 L" e "2.0 L" na VERSAO das 3 linhas do Gol.

| VEICULOS (40.902 linhas) | v29 (no ar) | v30 |
|---|---|---|
| Sem ano | 2.574 | 2.002 |
| Só ano inicial | 1.562 | 1.037 |
| Só ano final | 43 | 25 |
| Com início e fim | 36.723 | 37.838 |

## Site: o que muda (1a e 2a)
- **Veículo sem ano:** sai da tabela, da lista Marca/Modelo/Ano e do filtro "Meu veículo". Continua na base.
- **Produto que fica sem nenhuma aplicação visível:** mostra "Aplicação em revisão; consulte o vendedor." na página e no cartão.
- **Universais (FLU15001, FLU15002) e óleos "conforme manual":** continuam com o texto, sem o aviso.
- **Cartão do produto com veículo oculto:** resume só os modelos visíveis, por exemplo "FORD - Escort / Verona / Royale / Courier · FIAT - …".
- **Na impressão do produto com veículo oculto:** a "Aplicação completa" sai, porque citaria os veículos ocultos.
- **Peças de moto:** continuam em primeiro lugar ("titan", "filtro titan").

| Site | Hoje (v29) | v30 |
|---|---|---|
| Veículos com ano na tela | 31.815 | 32.219 |
| Linhas sem ano na tela | 2.606 | 510 |
| Produtos com tabela de veículos | 4.037 | 3.943 |
| Produtos com o aviso | — | 199 |
| "gol 2010" | 97 | 99 |
| "polo 2026" | 34 | 34 |
| Ford › Ka | 131 | 119 |

Correções de tela que vieram junto:
- **JUH70025:** cada cilindrada do Gol agora fica na sua linha.
- **Passat e Parati:** deixaram de aparecer como Ford. A marca foi corrigida em 23 tabelas, por exemplo Civic (Honda), Stilo (Fiat) e Logus (VW).

## Perguntas para o Alexandre

### A. Site
1. **Linhas com ano marcado como duvidoso:** são 2.040 linhas em 904 produtos. Hoje o site já as recebe sem ano, e a simulação também as esconde. Com isso, 25 produtos ficam só com o aviso, como CXD13032, SEH80006, SEH80007, SEH80011 e TER5596015.
   - **BCE3001:** Ford Ka e Ford Fiesta "1993 em diante", com ano herdado de outro modelo. Escondendo, somem. Sem esconder, aparecem como "Ford Ka · —", sem ano.
   - **CXD13032:** Fiat Linea 2008–2016 e Punto 2007–2017, porque "08/16" pode ser mês/ano. Escondendo, só o aviso. Sem esconder, aparece "Punto 1.4 / 1.6 / 1.8 · 2007–2017", com o ano vindo do texto.
   - **SEH80006:** Renault Master 2004–2013, porque "04/12" pode ser mês/ano. Escondendo, só o aviso. Sem esconder, aparece "Renault Master 2.5 · Diesel Com ABS · 2004–2012".
   - **A pergunta:** esconder também essas linhas (a) ou só as sem ano nenhum (b)? O web-site e o designer-ux recomendam (b).
2. **Busca digitada:** "ka" continua achando o BCE3001 pelo texto, embora a tabela não mostre o Ka. Fica assim?
3. **Impressão:** a "Aplicação completa" sai do produto com veículo oculto. Confirma?
4. **Palhetas, baterias e rodas sem aplicação** (ex.: KI20, ROD8005): mostrar o aviso ou esconder a seção, como hoje? O designer-ux recomenda esconder, porque o cliente escolhe pela medida.
5. **Óleos e fluidos "conforme manual":** continuam com o texto, sem o aviso, mesmo estando na lista "sem aplicação". Confirma?
6. **Linhas sem ano que vêm só do texto:** sobram 510 na tela. Ocultar também?
7. **Texto do aviso:** o design-de-marca sugere "Aplicação em revisão. Confirme com a BAP.", porque o vendedor também usa o catálogo. Mantém o seu texto ou troca?
8. **VEL7561 (Caravan → Chevrolet) e INT16533 (Express → Renault):** a marca foi corrigida pelo catálogo. Confere?

### B. Base (aba PONTOS_ALEXANDRE)
9. **Regra de conflito:**
   - a linha sem ano recebe a faixa inteira;
   - a linha com um ano só ganha a ponta que falta, se o ano couber na faixa;
   - em conflito, a pesquisa decide quando concorda com um dos lados.

   Aprova?
10. **Os 85 conflitos novos** (ex.: CXD13007 Classic, atual 2016 em diante e pesquisa 2002–2012): trocar pelo ano da pesquisa, manter ou pesquisar de novo?
11. **Os 6 conflitos sem resolução** (ex.: CL18 L200, CUB60027 Vectra): manter?
12. **Faixa que termina em 2025 ou 2026:** entra como veio, porque o veículo está em produção. Confirma?
13. **Linha duvidosa que ganhou ano:** passa a "separado", e volta ao site?
14. **ANO_DUVIDA:** limpar a marca quando a pesquisa confirmou a faixa?
15. **Fonte de loja:** vale igual à de fabricante?
16. **Linhas "manter_atual":** também entram no LOG_CORRECOES?
17. **Ano final 2027 (INT16501 Nivus, T-Cross e Taos):** pôr 2026?
18. **Faixa de um ano só (60) e faixa de mais de 30 anos (33, quase todas da 3-RHO):** entram como vieram?
19. **"Sem aplicação":** vale a conta do site ou a lista produtos_sem_aplicacao.csv? A conta do site dá 199 produtos com o aviso; a lista tem 397, e só 131 deles estão no site.
20. **JUH70025:** confirma "1.6 L", "1.8 L" e "2.0 L" na VERSAO do Gol?

## Revisões da simulação
- designer-ux: LIBERADO (490fe48).
- design-de-marca: o MC-0052 (marca no cartão) foi aplicado; o reteste está em andamento.
- testes: os prints foram conferidos.
- O testar_site vai ser ajustado para a v30 depois do aprovado.
- O revisor-codigo e o corretor revisam o código no PR, depois do aprovado.

## Depois do "aprovado"
- **Base:** aprovar_v30.sh, PR, revisão e merge.
- **Site:** gerar o JSON com a v30, ajustar o testar_site, PR, revisão e merge.
- **Deploy e registro:** depois dos dois merges.
