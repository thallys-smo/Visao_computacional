## 1.1 Prewitt e Sobel (Nota 1.5/10)

Aplicar os detectores de bordas verticais e horizontais de Prewitt na imagem wirebond_mask.tif. Mostre a imagens original e as resultantes em um subplot.

Aplicar os detectores de bordas verticais e horizontais de Sobel na imagem wirebond_mask.tif. Mostre a imagens original e as resultantes em um subplot.

Comente os resultados encontrados.

Dicas:

Nós criamos uma lista contendo os kernels de cada método. Note que vários kernels foram fornecidos abaixo. Alguns serão utilizados no próximo exercício também.
Você pode criar um laço de repetição para pegar cada kernel da lista. Segue abaixo um exemplo de um for loop em uma lista.

## 1.2 Sobel e Laplaciano (Nota 1.5/10)

Leia a imagem house.tif. Mostre a imagem na tela.

Aplique todos os detectores de bordas de Sobel na imagem lida no item 1. Mostre as imagens resultantes em um subplot.
Para cada kernel, aplique um threshold no resultado do filtro a fim de tentar manter somente as bordas que aquele filtro foi desenvolvido para detectar. Nas dicas deixamos um valor sugerido.
Some o resultado obtido por cada kernel em uma variável chamada sobel_sum.
Aplique o detector de bordas Laplaciano na imagem house.tif. Mostre em um subplot a imagem original, a soma de todos os resultados de Sobel (sobel_sum) e o resultado do Laplaciano. Coloque título nas imagens. O que se pode concluir?