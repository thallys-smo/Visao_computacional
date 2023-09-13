# Filtragem de imagens coloridas

Filtro passa-baixa.

1. Carregue a imagem rgb_blocks_ruidosa.bmp. Ela é uma imagem colorida que foi degrada com ruído Gaussiano. 
2. Filtre a imagem com o filtro da média de kernel 7x7 utilizando a função cv.blur().
3. Converta a imagem original (com ruído) de RGB para HSV. Mostre os canais da imagem ruidosa separadamente em um subplot. Coloque título em todas elas. Use colormap='gray' para mostrar os canais. 
4. Dentre as componentes HSV, escolha a mais adequada para ser filtrada. Utilize o mesmo filtro do item 2. Mostre o canal escolhido antes e depois da filtragem. Use colormap='gray'.
5. Recomponha a imagem HSV com esta componente filtrada e reconverta para RGB. Mostre a imagem resultante. O que se pode concluir?

Dicas:

- Você pode utilizar a função np.stack para empilhar os diferentes canais. O argumento axis especifica em qual dimensão as imagens serão empilhadas. Caso seja especificado como -1, a última dimensão será utilizada.

np.stack((A,B),axis=-1)
cv.blur(myImg,(kSize,kSize))

Filtro passa-alta.

Como vimos no exercício anterior, em algumas aplicações é útil trabalhar com a imagem no formato HSV e escolher o canal adequado para o processamento desejado.

Veremos um exemplo agora com filtro passa-alta, para detectar bordas em uma imagem colorida. O objetivo é ressaltar em preto as bordas desta imagem.

1. Carregue e mostre a imagem rgb_stripes.bmp. Ela é uma imagem colorida contendo listras em diferentes cores.
2. Converta a imagem RGB para HSV. Mostre os canais separadamente (use colormap='gray'). Você pode estudar os valores de cada canal para entender como eles se compõem para formar a imagem final, se desejar.
3. Utilize o kernel filtro_pa disponibilizado no código e faça testes para responder à pergunta: qual canal é mais adequado para atingir o objetivo de detectar bordas?
4. A partir da escolha do canal feita anteriormente, plote o histograma do canal após aplicar o filtro passa-alta e selecione um threshold adequado para binarizar esta imagem. Mostre a imagem binarizada e o valor de threshold encontrado.
5. Por fim, utilize a imagem binarizada do item anterior como uma máscara a ser usada com o propósito de destacar na imagem original onde foram detectadas as bordas. Esse destaque deve estar na cor preta.
6. Reconverta a imagem HSV obtida no item anterior (ou seja, já com as bordas destacadas em preto) para RGB e mostre a imagem final colorida com as bordas destacadas.

Dicas:

A biblioteca numpy possui algumas facilidades na hora de trabalhar com matrizes. Caso desejar, você pode implementar a seguinte ideia tanto em binarização quanto na aplicação de máscaras:

array_1 = np.ones((3,3))
array_2 = np.array([[10,20,10],
                    [20,10,20],
                    [10,20,10]])
array_1[array_2>15]=0
print(array_1)