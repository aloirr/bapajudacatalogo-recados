# T-0014 · listas travadas com a placa e filtros sempre à esquerda (R-20261120-130300) · SIMULAÇÃO

Chromium (Playwright), deviceScaleFactor 2, site local com o produtos.json do branch (v17, com o campo "ve"). Placa **AAA0A00, falsa**, só de teste; rota do serviço interceptada (HONDA "CIVIC LXS 1.8", 2008, 1.8). Nenhuma consulta real. Busca "amortecedor".

- placa-listas-travadas-1366 / -390: com a placa, Marca, Modelo, Ano, Motor e Versão travadas (disabled), em cinza (texto --texto-2 #5B625E sobre --fundo #F4F5F4, contraste 5,8:1), com os valores da placa (Honda · Civic · 2008 · 1.8 · LXS; 5 produtos). Coluna de filtros à esquerda (1366) e "Filtrar" (390) sempre. No 390 a faixa está aberta ("Alterar veículo") para mostrar as 5 listas.
- depois-do-x-listas-todos-1366 / -390: depois do ✕ da placa, as listas voltam para "Todas as marcas", "Todos os modelos", "Todos os anos", "Todos os motores", "Todas as versões" (710 produtos). A Marca fica editável na hora; Modelo, Ano, Motor e Versão abrem em cascata, cada uma depois da escolha anterior.
- A coluna Sistema/Família/Linha/Categoria aparece sempre, mesmo com uma opção só (o RD-0005 foi desfeito).

As fotos são ilustrativas. Confira sempre a aplicação antes da compra.
