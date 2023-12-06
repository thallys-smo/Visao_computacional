# Questão 1: Enunciado

1) Resolução espacial (Nota: 2.0/10.0)
Carregue o arquivo de imagem flower.png e mostre seu tamanho.
Agora, vamos utilizar a função cv.resize para mudar a resolução espacial da imagem lida. Pesquise sobre essa função e utilize-a para reduzir o tamanho da imagem para:
280x280
200x200
125x125
100x100
50x50
Mostre todas as imagens usando janelas do mesmo tamanho. Lembre-se que o tamanho real da imagem foi definido no item anterior com cv.resize, mas você pode escolher qual o tamanho mostrar na tela, em polegadas (a imagem será ajustada para se adequar ao tamanho escolhido). Para isto, faremos uso do figsize juntamente com subplot.

Comente os resultados.

Dica: Use o argumento figsize em plt.figure(figsize=(largura,altura)), sendo largura e altura dadas em polegadas. Um bom número para se trabalhar é de 5 polegadas por imagem, assim em um plot de 1 linha por 5 colunas, uma sugestão seria utilizar plt.figure(figsize=(25,5)).