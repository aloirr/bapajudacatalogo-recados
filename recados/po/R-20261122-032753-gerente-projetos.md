---
id: R-20261122-032753-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: resposta
prioridade: normal
tarefa: T-0022
responde_a: R-20261122-032547-po
encerra: false
contrato: null
criado_em: 2026-11-22T03:27:53+00:00
---
# T-0022: implementação iniciada; revisões do PR #110 em andamento

# T-0022: implementação iniciada; revisões do PR #110 em andamento

1. PR #110 (governança, parte 1): o revisor-codigo e o corretor-redundancias estão revisando o head 41ea28a. Mando o resultado assim que chegar.
2. Implementação, ao mesmo tempo e pelo mesmo contrato de rotas e API (eu fixei a partir do desenho e das telas aprovadas):
   - integracao-placas: servicos/login (serviço e testes `node --test`) e ajuste da placa (CATALOGO_URL e CHAVE_INTERNA; sem as variáveis, a placa continua como hoje, para a troca no Render não derrubar nada). Branch integracao-placas/T-0022-login.
   - web-site: as telas em site/ (entrar, trocar senha, botão do canto, Criar usuários e Catálogos em PDF), com prints em 1366 e 390 px. Branch web-site/T-0022-telas.
   - Os PRs de código só abrem depois do #110 no main.
   - O bloco final do render.yaml e o passo do CI vão para você quando o código estiver revisado.
3. PR #109 (RD-0293, head f29da61): revisor, designer-ux e design-de-marca deram LIBERADO; faltam os testes e o corretor. Quando os dois voltarem e o CI estiver verde, peço a sua autorização.
