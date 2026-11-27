---
id: R-20261127-150336-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: alta
tarefa: T-0040
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-27T15:03:36+00:00
---
# RETOMADA — estado na pausa (v30 aprovada, não iniciada)

# RETOMADA — estado na pausa (atualização: v30 aprovada)

Este recado completa o R-20261127-145105-gerente-projetos, que continua valendo para todo o estado.

- **v30 APROVADA pelo Alexandre:** "aprovado v30, tudo como recomendado" (ponte R-20261127-150252-alexandre, via po).
- **Por que não comecei:** pelo aviso do po, o limite semanal chegaria a 99% em 15 a 25 min a partir das 14:50Z. Para não deixar push pela metade, nenhuma frente da v30 foi iniciada. Não houve commit, push nem merge depois do R-20261127-145105.
- **Antes de começar, preciso das 20 respostas escritas uma a uma.** O corpo do R-20261127-150252-alexandre veio só com os títulos do modelo, sem o texto. Várias perguntas não tinham recomendação no pacote: 2, 3, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18 e 20. Entendo "como recomendado" assim [SUPOSIÇÃO, para o po confirmar]:
  - 1: ocultar só as linhas sem ano nenhum, o grupo (b) fica visível;
  - 4: palhetas, baterias e rodas sem aplicação escondem a seção, sem o aviso;
  - 7: o texto do aviso fica o do Alexandre;
  - as demais: como propostas na simulação (a regra de conflito como está, a impressão sem a "Aplicação completa", os óleos com o texto, o 2027 vira 2026, a VERSAO do JUH70025 etc.);
  - os 85 conflitos novos e os 6 sem resolução: manter como estão.
- **Ao retomar:**
  1. **catalogo-dados:** ajustar o base_v30.py às respostas e rodar `bash dados/scripts/aprovar_v30.sh R-20261127-150252-alexandre` na catalogo-dados/T-0040-v30 (317f583); depois push, revisor e corretor, PR e pedido de merge.
  2. **web-site:** na web-site/T-0040-v30 (3b250fe), aplicar o 1 (só o grupo a) e o 4; depois do merge da base, gerar o JSON com a v30 do main; o testes atualiza o testar_site para o `vo`; depois PR, revisões, merge e deploy.
  3. **Registro final da T-0040.**
