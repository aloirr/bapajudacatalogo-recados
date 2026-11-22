---
id: R-20261122-075532-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: aviso
prioridade: alta
tarefa: T-0022
responde_a: R-20261122-073402-alexandre
encerra: false
contrato: null
criado_em: 2026-11-22T07:55:32+00:00
---
# Complemento do alerta: a base .xlsx com dado interno também está pública (não estava no alerta)

Complemento ao alerta R-20261122-073016. O Alexandre decidiu manter os repositórios públicos sabendo do produtos.json, das fotos e dos PDFs. Mas o alerta não citava a BASE.

O que está público no aloirr/bapajudacatalogo (conferi agora, sem abrir os valores):
- dados/BASE_BAP_UNIFICADA_PRODUTOS_BAP.xlsx e as 20 versões em dados/versoes/:
  - na aba PRODUTOS, a coluna DADOS_ADICIONAIS tem cerca de 490 menções a CUSTO, 441 a FORNECEDOR e 502 a ESTOQUE;
  - REFERENCIAS_CRUZADAS tem 152 menções a FORNECEDOR;
  - STATUS_CADASTRO cita ESTOQUE em 1.790 linhas;
  - LOG_CORRECOES e LEIA-ME citam CUSTO, ESTOQUE e PREÇO.
- É justamente o que a TRAVA do gerar_site.py impede de ir para o site: nomes de fornecedor, custo e estoque. No GitHub público, isso fica aberto para qualquer um.
- O README.md:65-66 ainda diz 'o repositório é privado'. Vou corrigir isso nos arremates da T-0022, com a decisão do Alexandre.

Pergunta ao Alexandre, num bloco só:
1) Sabendo que a base com custo e fornecedor está pública:
   a) Tornar privado só o aloirr/bapajudacatalogo. O recados pode continuar público para economizar actions. Antes, conferir o acesso do Render ao repositório privado. (RECOMENDADO)
   b) Manter público assim mesmo.
   c) Outra saída, por exemplo tirar a base do Git. Isso é grande, porque o gerar_site.py e a regra 4 dependem dela.

Enquanto ele não responde, sigo a T-0023 e os arremates que não dependem disso.
