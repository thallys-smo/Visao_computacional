# Questão 2: Enunciado

Agora vamos reduzir a resolução de níveis de cinza da imagem. Para isto, vamos usar uma função de nome transformaImg, já disponibilizada a seguir. Comente o que cada linha da função está exercendo.

Carregue o arquivo de imagem xRay_hand.tif.

Reduza a escala de níveis de cinza da imagem xRay_hand.tif de 256 níveis para a resoluções abaixo. Mostre todas as imagens usando janelas de mesmo tamanho, assim como foi feito/explicado no exercício anterior.

128
64
16
4
2
Comente os resultados obtidos.

Explique:

Qual o motivo da transformação da variável img para float32 no início da função dada?
Qual o motivo da linha res = 255*(res - res.min())/(res.max() - res.min()) antes do retorno para uint8?


def transformaImg(img, grayLevel):
  '''
  Descrição: Transforma uma imagem para uma nova escala de cinza.

  Entrada:
    - img: Imagem de entrada (uint8).
    - grayLevel: Nova escala de níveis de cinza desejada (uint8).

  Saída:
    - res: Imagem com nova escala de cinza (uint8)
  '''

  img_in = img.copy().astype('float32')

  res = np.round( img_in * (grayLevel - 1) / 255.)

  res = 255*(res - res.min())/(res.max() - res.min())

  res = res.astype('uint8')

  return res


Seu código começa aqui

Seu código termina aqui

Comentários: