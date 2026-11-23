---
id: R-20261123-142820-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pergunta
prioridade: alta
tarefa: T-0030
responde_a: null
encerra: false
contrato: null
criado_em: 2026-11-23T14:28:20+00:00
---
# T-0030: RD-0541 mexe na FICHA. Corrigir ou MANTIDO?

O revisor liberou o #173 (web-site, rótulos 'Ah' e 'CCA') e o #174 (testes), e o testes deu PASSOU. O corretor achou o RD-0541 (média) no #173.

- RD-0541: o rótulo da ficha passa a ser decidido em 2 lugares. A FICHA do gerar_site.py já define os rótulos de tela, como 'Código de barras' e 'Peso líquido (kg)'. O PR acrescenta um segundo mapa só na tela, o ROTULO_FICHA, no site/app.js.
- A correção do corretor põe o rótulo na própria FICHA: (r'^C20\(AH\)$', 'Ah') e (r'^CCA-18°$', 'CCA'). O padrão não muda e a lista branca não afrouxa, mas o produtos.json muda nesses 2 rótulos e o filtro passa a ler as chaves novas.
- O seu R-20261123-135656-po diz: 'Se a troca exigir mexer na FICHA, pare e me avise.' Por isso a decisão é sua.

Recomendo MANTIDO, com este motivo: o pedido proibia mexer na FICHA, e a solução na tela deixa o JSON e a FICHA intactos, com um risco menor. Se preferir corrigir, o web-site faz a troca e o PR volta ao testes e ao revisor.

Os achados RD-0542 e RD-0543 (baixos: uma linha do doc e um comentário que repetem texto) eu já mandei o web-site corrigir no #173.

Resposta: a) MANTIDO (recomendo)  b) corrigir na FICHA
