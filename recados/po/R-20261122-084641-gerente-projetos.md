---
id: R-20261122-084641-gerente-projetos
de: gerente-projetos
para: [po]
cc: []
tipo: pedido
prioridade: normal
tarefa: T-0024
responde_a: R-20261122-084553-alexandre
encerra: false
contrato: null
criado_em: 2026-11-22T08:46:41+00:00
---
# T-0024: bloco do buildFilter do render.yaml (governança)

Bloco para o render.yaml, no serviço bapajudacatalogo-login. É o buildFilter de hoje, nas linhas 48 a 53, mais 5 caminhos:

    buildFilter:
      paths:
        - site/**
        - servicos/login/**
        - catalogo_grafico/entregas/Catalogo_BAP_*_Completo_Digital.pdf
        - catalogo_grafico/entregas/Catalogo_BAP_*_A4_grafica.pdf
        - catalogo_grafico/entregas/Catalogo_BAP_*_Linha_Moto.pdf
        - catalogo_grafico/entregas/Portfolio_Produtos_BAP_AUTOPARTS.pdf
        - catalogo_grafico/entregas/BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial.pdf
        - catalogo_grafico/entregas/BAP_Lubrificantes_e_Quimicos_Apresentacao_Comercial.pptx
        - catalogo_grafico/entregas/Kit_Filtros_BAP.pdf

Observação: o buildFilter só decide quando o serviço é publicado de novo. Quem protege o acesso é a lista fixa do servidor: só o admin baixa, e só esses 7 arquivos. Os .xlsx internos de entregas/ e a base de dados/ continuam fora.

Ordem sugerida: o PR do código (serviço e página) entra primeiro; o seu PR do render.yaml vem logo depois. O render.yaml sozinho não muda nada visível: só faz o serviço ser publicado de novo quando esses arquivos mudarem.
