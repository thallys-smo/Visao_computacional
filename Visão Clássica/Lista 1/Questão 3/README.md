# Questão 3: Enunciado

3) Alargamento de contrastre e binarização

1. Visualize a imagem palavrascruzadas.pnge mostre seu histograma utilizando a função:
'''
    plt.hist(myImg.flatten(),bins=XX,density=False,range=(0,255))
'''
2. Agora vamos fazer um alargamento de contraste na imagem. Para isto, vamos usar uma função de nome alargCont, já disponibilizada a seguir. Comente o que cada linha da função está exercendo.

3. Defina um limiar (threshold) para binarização na imagem com ajuste de contraste. Você pode encontrá-lo através do método do vale: observe o histograma e encontre a intensidade em que grandes grupos se separam, formando um vale. Este valor será seu threshold.

4. Utilizando o limiar encontrado no item 2, implemente um código (com técnicas regulares de programação Python) que realize a operação de transformação da imagem lida no item 1 para uma imagem binária. O objetivo é separar ao máximo as peças (contendo letras) do fundo da imagem. Apresente a imagem binarizada resultante. //

- Outra forma de binarizar a imagem é utilizando algoritmos que buscam um limiar (threshold) de forma automática. É o caso, por exemplo, do método de Otsu (informações sobre o método aqui)

A função cv.threshold (exemplos aqui) - permite fazer uso dessa técninca ao passar os argumentos conforme abaixo.
th_value,img = cv.threshold(myImg, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
em que th_value receberá o valor do threshold encontrado e img a imagem binarizada

5. Implemente um código (utilizando a função cv.threshold com método de Otsu) que realize a operação de binarização da imagem com ajuste de contraste do item 2. Apresente a imagem binarizada resultante.

6. Comente os resultados, comparando as duas formas de encontrar o limiar (threshold).
<code>
def alargCont(img):
  '''
  Entrada:
    - img: Imagem de entrada (uint8).

  Saída:
    - img_out: Imagem com largamento de contraste (uint8)
  '''

  img = img.astype('float')
  valMax = img.max()
  valMin= img.min()

  img_out = (img-valMin)*((255)/(valMax-valMin))
  img_out = img_out.astype('uint8')

  return img_out

Seu código começa AQUI

Seu código termina AQUI
</code>.


'''