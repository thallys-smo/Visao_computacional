import cv2 as cv
#from libtiff import TIFF
import numpy as np
from matplotlib import pyplot as plt

# Função de Transformação da Escala de Cinza da imagem

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

'''Leitura e recolhimento de dados da imagem'''

# Local da Imagem
local_img = "/home/thallys/Documentos/Graduação/Visão Computacional/Visao_computacional/Lista 1/Arquivos/xRay_hand.tif"

# Leitura de imagem
img = plt.imread(local_img,0) 

# Transformando os tons de cinza da imagem

img_128 = transformaImg(img, 128)
img_64  = transformaImg(img, 64)
img_16  = transformaImg(img, 16)
img_4   = transformaImg(img, 4)
img_2   = transformaImg(img, 2)

# Mostrando a imagens alterada

plt.imshow(img,cmap='gray')
plt.title('256 níveis de cinza')
plt.show()

plt.imshow(img_128,cmap='gray')
plt.title('128 níveis de cinza')
plt.show()

plt.imshow(img_64,cmap='gray')
plt.title('64 níveis de cinza')
plt.show()

plt.imshow(img_16,cmap='gray')
plt.title('16 níveis de cinza')
plt.show()

plt.imshow(img_4,cmap='gray')
plt.title('4 níveis de cinza')
plt.show()

plt.imshow(img_2,cmap='gray')
plt.title('2 níveis de cinza')
plt.show()

# Plotando todas as imagens juntas

plt.figure(figsize=(15, 7)) 

plt.subplot(2,3,1)
plt.imshow(img,cmap='gray')
plt.title('256 níveis de cinza')

plt.subplot(2,3,2)
plt.imshow(img_128, cmap='gray')
plt.title('128 níveis de cinza')

plt.subplot(2,3,3)
plt.imshow(img_64,cmap='gray')
plt.title('64 níveis de cinza')

plt.subplot(2,3,4)
plt.imshow(img_16,cmap='gray')
plt.title('16 níveis de cinza')

plt.subplot(2,3,5)
plt.imshow(img_4,cmap='gray')
plt.title('4 níveis de cinza')

plt.subplot(2,3,6)
plt.imshow(img_2,cmap='gray')
plt.title('2 níveis de cinza')

plt.show()
