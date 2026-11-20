# T-0014 · aplicação em tabela no detalhe do produto (R-20261120-130900) · SIMULAÇÃO

Chromium (Playwright), deviceScaleFactor 2, site local com o produtos.json do branch (v17, com o campo "ve").

- janela-AMT7183-1366 / -390: "+ Detalhes" do AMT7183. A aplicação vira tabela Marca · Modelo · Cilindrada · Versão · Ano (Honda · Civic · — · — · 2006–2011) e, embaixo, "Ver aplicação completa", que abre o texto original.
- janela-CXD13062-1366 / -390: o CXD13062, com 7 veículos (Gol G5/G6/G7, Saveiro, Voyage, Fox Cross, Fox).
- No celular (até 480 px) a tabela vira uma lista por veículo, sem rolar de lado: 1ª linha "Volkswagen Gol G5" em negrito e 2ª linha "Cilindrada — · Ano 2006–2011" em cinza (14 px); se faltam os dois, a 2ª linha não aparece. No 1366 e no PDF, a tabela.
- pdf-A4-CXD13062.pdf e pdf-A4-CXD13062-pagina1-1.png: "Salvar em PDF" (A4) com a tabela; no PDF o texto completo não vai.
- Produto sem "ve" continua com o texto de hoje.

**SIMULAÇÃO:** Marca, Modelo e Versão são do campo "ve". Cilindrada e Ano ainda não existem na base por veículo: saem do trecho da aplicação onde o modelo aparece (do modelo até o próximo modelo, até 120 caracteres); o ano da base (an), se houver, vale primeiro. Ano solto sem faixa ("08/2022") vira "—" (decisão da v19). Quando o modelo tem várias versões (Gol G5, G6, G7), o ano e a cilindrada só valem no pedaço da própria versão; fora dele, "—". Sem achar: "—".

## Cobertura (3619 produtos com "ve", 12251 linhas)
- Cilindrada: 4574 linhas (37%).
- Ano: 7909 linhas (65%).

As fotos são ilustrativas. Confira sempre a aplicação antes da compra.
