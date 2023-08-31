# Formatos de imagens

Estes são alguns dos formatos existentes para imagens coloridas:

- O formato BMP - Windows Bitmap. Um formato de arquivo utilizado pra simples imagens sem compressão. Guarda a informação de quantos pixels a imagem contém e a cor de cada um expressa por 3 canais, cada um podendo assumir valor de 0 a 255 (para codificação em 8 bits).

- O formato JPG tem seu nome por utilizar o padrão de compressão JPEG (Joint Photographic Experts Group) para imagens de qualidade fotográfica. É um dos métodos mais populares de compactação de imagens na Internet. Seu sistema de codificação divide a imagem em blocos e os compara com padrões base da transformada discreta do cosseno (DCT) e estabelece o peso da presença de cada um desses padrões em cada bloco.

- O formato GIF (Graphic Interchange Format). É freqüentemente usado para fazer pequenas animações e filmes curtos de baixa resolução para a Internet. Ideal para gráficos, logos e desenhos. Nesse padrão de compressão as cores são representadas por um conjunto de até 256 cores.

*** Mais detalhes no capítulo 8 - Compressão de Imagem e Marca d'Água do livro: Gonzalez and Woods, Digital Image Processing 4th.

**Exercício**

1. Faça a leitura da imagem borboleta.bmp.
2. Faça a leitura da imagem no formato .gif(borboleta.gif),
3. Utilizando a imagem do item 1, salve-a no formato .jpg. Em seguida, leia esta imagem novamente em uma outra variável.
4. Agora, compare o tamanho dos arquivos das imagens, imprimindo a quantidade de bytes de cada um.
5. Apresente as três imagens lado a lado em um tamanho que seja possível observar os detalhes nos valores dos pixels. Comente sobre as diferenças de memória utilizada e características visuais.

**Dicas:**

Você pode utilizar a função cv.imwrite para salvar as imagens. Utilize os.path.getsize para calcular o tamanho do arquivo da imagem. Para carregar imagens .gif é necessário utilizar outra função do OpenCV em vez de imread. Para tanto, utilize a função cv.VideoCapture, conforme exemplo a seguir.