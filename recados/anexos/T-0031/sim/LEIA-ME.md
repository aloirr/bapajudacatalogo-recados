# T-0031 · item 4a · Aplicações suspeitas da Linha Pesada (simulação)

Base conferida: `dados/BASE_BAP_UNIFICADA_PRODUTOS_BAP.xlsx` (igual à v27), lida só para conferir. Nada foi gravado.

Planilha: `SIMULACAO_T-0031_aplicacoes_linha_pesada.xlsx`

| Aba | O que tem |
|---|---|
| ANTES_E_DEPOIS | O pedido: BIE20042 (Doblò nas Bieletas). LINHA PESADA -> LEVE e a linha "FORD Cargo" da aba VEICULOS sai do filtro do site (separado -> duvidoso, com MOTIVO). |
| CONFERIDO_SEM_MUDANCA | FAC6260 (Ford Focus e Volvo V40 nos Filtros de Cabine): está certo segundo a fonte, e nada muda na base. |
| MESMA_CAUSA_FORA_DO_PEDIDO | Mais 5 itens com o mesmo erro ("Cargo" do Doblò lido como caminhão Ford Cargo): BOR11030, AMT7084, AMT7115, BAN9513, BAN9516. Só entram se o Alexandre aprovar. |
| EFEITO_NOS_PDFS | As páginas do Portfólio que mudam. O Catálogo 2027 e o Kit Filtros não mudam. |

Causa: o gerador antigo da classificação (`catalogo_grafico/gerador/taxo.py`, regra HEAVY) marca a linha como pesada quando lê a palavra "Cargo". Ele não sabe que "Doblò Cargo" é a versão de carga do Fiat Doblò, um utilitário leve.

Sem preço e sem estoque. O script `simular_T-0031.py` refaz a planilha a partir da base: `python3 -I simular_T-0031.py <base.xlsx> <saida.xlsx>`.
