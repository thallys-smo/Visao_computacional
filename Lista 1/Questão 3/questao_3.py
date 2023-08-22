import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
local_img = "/home/thallys/Documentos/Graduação/Visão Computacional/Visao_computacional/Lista 1/Arquivos/palavrascruzadas.png"
'''Leitura e recolhimento de dados da imagem'''

#leitura de imagem
img = cv.imread(local_img) 
cv.imshow('Original',img) 
cv.waitKey(0) 
XX = 256
plt.figure()
plt.hist(img.flatten(),bins=XX,density=False,range=(0,255))
plt.xlim([0, 80]) 
plt.show() 
''' 
XX = 256
n, bins, patches = plt.hist(img.flatten(),bins=XX,density=False,range=(0,255))
plt.plot(bins)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
'''

