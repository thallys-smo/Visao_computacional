import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
local_img = "/home/thallys/Documentos/Graduação/Visão Computacional/Visao_computacional/Lista 1/Arquivos/flower.png"

'''Leitura e recolhimento de dados da imagem'''

#leitura de imagem
img = cv.imread(local_img) 

# pega as dimensões da imagem
dimensao = img.shape 

# Altura, largura e canais da imagem
altura  = img.shape[0]
largura = img.shape[1]
canais  = img.shape[2]

print('Dimensão da imagem         : ',dimensao)
print('Altura da imagem           : ',altura)
print('Largura da imagem          : ',largura)
print('Número de canais da imagem : ',canais)

# Mostra imagem original

cv.imshow('Original',img) 
cv.waitKey(0) 

'''Redimensionando o tamanho da imagem'''

# Redimensionamento 1: 280 x 280

nova_altura  = 280
nova_largura = 280
novo_dimensao = (nova_altura, nova_largura)
redimensionamento_1 = cv.resize(img, novo_dimensao, interpolation= cv.INTER_LINEAR)

# Redimensionamento 2: 200 x 200

nova_altura  = 200
nova_largura = 200
novo_dimensao = (nova_altura, nova_largura)
redimensionamento_2 = cv.resize(img, novo_dimensao, interpolation= cv.INTER_LINEAR)

# Redimensionamento 3: 125 x 125

nova_altura  = 125
nova_largura = 125
novo_dimensao = (nova_altura, nova_largura)
redimensionamento_3 = cv.resize(img, novo_dimensao, interpolation= cv.INTER_LINEAR)

# Redimensionamento 4: 100 x 100

nova_altura  = 100
nova_largura = 100
novo_dimensao = (nova_altura, nova_largura)
redimensionamento_4 = cv.resize(img, novo_dimensao, interpolation= cv.INTER_LINEAR)

# Redimensionamento 5: 50 x 50

nova_altura  = 50
nova_largura = 50
novo_dimensao = (nova_altura, nova_largura)
redimensionamento_5 = cv.resize(img, novo_dimensao, interpolation= cv.INTER_LINEAR)

# Mostrando imagens redimensionadas

cv.imshow('Redimensionada 280 x 280', redimensionamento_1)
cv.waitKey(0) 

cv.imshow('Redimensionada 200 x 200', redimensionamento_2)
cv.waitKey(0)

cv.imshow('Redimensionada 125 x 125', redimensionamento_3)
cv.waitKey(0)

cv.imshow('Redimensionada 100 x 100', redimensionamento_4)
cv.waitKey(0)

cv.imshow('Redimensionada   50 x 50', redimensionamento_5)
cv.waitKey(0)

# Plotando todas as imagens juntas

plt.figure(figsize=(15, 7)) 
plt.subplot(231),plt.imshow(img),plt.title('512 x 512')
plt.subplot(232),plt.imshow(redimensionamento_1),plt.title('280 x 280')
plt.subplot(233),plt.imshow(redimensionamento_2),plt.title('200 x 200')
plt.subplot(234),plt.imshow(redimensionamento_3),plt.title('125 x 125')
plt.subplot(235),plt.imshow(redimensionamento_4),plt.title('100 x 100')
plt.subplot(236),plt.imshow(redimensionamento_5),plt.title('50 x 50')
plt.show()


