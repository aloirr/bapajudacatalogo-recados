# T-0045 · SIMULAÇÃO dos PDFs: achados UX-T45-12 e 14

Branch `catalogo-grafico/T-0045-sim-pdf`, commits 6dd084e e ed98b0d. Muda só `catalogo_grafico/gerador/digital2.py` (e o LEIA_GERADOR.md). Os dados são os do main; a geração única com a v31 vem depois do aprovado (R-20261127-194728-alexandre, item 3). O A4 não muda.

Revisões: designer-ux 🟢 e design-de-marca LIBERADO, os dois no ed98b0d (o ajuste MC-0055, aviso legal no tamanho padrão, foi fechado).

## O que muda (Digital e Linha Moto)
1. **Botões (UX-T45-12).**
   - O "VOLTAR AO SUMÁRIO" sai do alto da página e vai para uma barra no rodapé, junto com o link do site: primeiro o "Voltar", depois o site.
   - A barra fica no mesmo lugar em todas as páginas. No sumário, ela tem só o site.
   - As aberturas ganham o link do site.
   - O nº da página vai para o canto direito.
   - As áreas de toque têm 9 mm de altura, com 3,2 mm de folga entre os dois links.
2. **Aplicação longa (UX-T45-14).**
   - Quando a Aplicação desce 3 linhas ou mais abaixo de "Leve também" e "Equivale a", as primeiras linhas ficam na coluna e o resto vai até a margem direita, formando um "L".
   - A continuação de um item só volta para a página anterior.

## Efeito
- Linha Moto: de 17 para 16 páginas. A p8, que tinha 1 item, sai.
- Digital: de 311 para 278 páginas.
- Nenhuma palavra de produto entra ou sai.
- Links: 0 erros. Os 124 do sumário e das aberturas levam à página certa.
- Sem preço e sem estoque. O "uso interno" está em todas as páginas.

## Para saber, e que não muda aqui
Nas aberturas, o texto branco sobre a faixa verde dá 2,9:1 de contraste. Isso já era assim antes e fica para a simulação do verde.

## Arquivos
- `Catalogo_BAP_2027_Completo_Digital_SIM-T0045.pdf` e `Catalogo_BAP_2027_Linha_Moto_SIM-T0045.pdf`: os PDFs simulados.
- `folha-contato-T0045-pdf.png`: as páginas antes e depois, e os rodapés.
- `<PDF>-pNNN-antes.png` e `-depois.png`: os prints das páginas, a 70 dpi.
- `rodape-*.png`: os rodapés a 150 ppi. As áreas de link aparecem marcadas em vermelho só no print, não no PDF.
