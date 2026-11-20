# T-0014 · versão final (prints) · 20/11/2026

Branch web-site/T-0014-cartao-pdf, worktree /home/user/wt-T-0014. Chromium (Playwright), deviceScaleFactor 2, site local (python3 -m http.server).
Placa nos prints: **AAA0A00, falsa**, só de teste. A rota do serviço de placas foi interceptada no Playwright e devolveu um veículo de exemplo (HONDA, "CIVIC LXS 1.8", modelo_lista ["CIVIC"], ano_modelo 2008, motor 1.8). Nenhuma consulta real.

## O que está pronto (1 linha cada)
- Início sem abas, 2 campos lado a lado (busca geral e placa, menor), cada um com o seu botão: inicio-sem-abas-1366 / -1536 / -390.
- Lista "amortecedor" sem a lateral, foto do cartão 50% menor (150 → 75 px; celular 110 → 55 px), texto do cartão ≥ 12 px: lista-amortecedor-1366 (8 por linha) / -1536 (9 por linha) / -390 (2 por linha).
- Barra horizontal de filtros (Sistema, Família, Linha, Categoria) fechada: filtros-fechados-1366 / -1536 / -390.
- Um filtro aberto (Família, caixas de marcar com contagem; fecha com Esc e clique fora): filtro-aberto-1366 / -1536 / -390.
- Etiquetas: "Placa: AAA0A00" (X tira o veículo) e embaixo o veículo em partes (Honda Civic · 2008 · 1.8 · LXS), o termo e um filtro marcado, "Limpar tudo": etiquetas-placa-termo-filtro-1366 / -1536 / -390.
- Filtro marcado (Linha: Pesada, 3 produtos) e a lista depois do X dele (710 produtos): lista-antes-de-tirar-filtro-* e lista-apos-tirar-filtro-* (1366, 1536, 390).
- Cartões com "+ Detalhes" (busca "palheta"): cartoes-palheta-1366 / -390.
- Foto ampliada a partir do cartão (sem abrir o produto): foto-ampliada-do-cartao-1366 / -390.
- Janela do CL14 aberta pelo "+ Detalhes": janela-CL14-pelo-detalhes-1366 / -390.

## O que ainda falta
- Nada da tela. Commit final 4e79846 feito (sem push). A bateria do main falha só nos 2 passos das abas (o testes faz a versão nova).

As fotos são ilustrativas. Confira sempre a aplicação antes da compra.
