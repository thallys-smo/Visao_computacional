import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.png',1) #leitura de imagem
img = cv2.imwrite('image.jpg',img) #salva a imagem em um formato diferente
cv2.imshow('original',img) #mostra a imagem
cv2.waitKey(0) 
cv2.destroyAllWindows()