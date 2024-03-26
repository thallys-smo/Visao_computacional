
## Questão 4: Aplicação

Você faz parte de um projeto cujo objetivo é rastrear a trajetória de uma bola de cor verde em um vídeo. Sua tarefa será gerar um vídeo que detecte e isole uma bola utilizando visão computacional.

Sua tarefa será fazer o pré-processamento da imagem, passando um filtro passa-baixa e entregando os frames para o restante do código em HSV. Em seguida, no código já pronto, será aplicada uma máscara levando em consideração níveis de verde claro até escuro.

Caso queira obter mais informações sobre o projeto, visite esse blog.

Exercício:

Aplique um filtro Gaussiano de modo a eliminar altas frequências e focar em objetos estruturais da imagem. Converta o frame filtrado de RGB para HSV.
Obs: Varie o tamanho do kernel e verifique o resultado.

Dicas:

Utilize a função cv.GaussianBlur.
Caso rode o código novamente, certifique-se sempre que excluir o arquivo "ball_tracking_example_out_compressed.mp4" antes de gerar um novo. Sobrescrever o arquivo pode causar erro.
Ex:

cv.GaussianBlur(myImg,(ksize,ksize),0)


Execute este código se quiser ver o vídeo original

```bash
mp4 = open("ball_tracking_example.mp4",'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""

""" % data_url)
```

```bash
path_comp = 'ball_tracking_example_out_compressed.mp4'
if os.path.exists(path_comp):
  os.remove(path_comp)

path_comp = 'ball_tracking_example_out.mp4'
if os.path.exists(path_comp):
  os.remove(path_comp)

greenLower = (29,86,6) #verde escuro
greenUpper = (64, 255, 162) #verde claro
# Cria o objeto VideoCapture
vs = cv.VideoCapture( "ball_tracking_example.mp4")
# Defina o codec e cria o objeto VideoWriter. A saída é armazenada no arquivo 'ball_tracking_example_out.mp4'.
out = cv.VideoWriter("ball_tracking_example_out.mp4",cv.VideoWriter_fourcc(* "MP4V" ), 20.0, (432,240))

#Percorre todos os frames
while True:
  # Leitura do frame
  ret, frame = vs.read()
  # Caso nao tenha mais nenhum frame
  if frame is None :
    break
  frame = cv.resize(frame,(432,240)) # Para processar mais rápido o frame

  ## -- Seu código começa AQUI -- input frame ##
  blurred =
  hsv =
  ## -- Seu código termina AQUI -- output hsv ##

  mask = cv.inRange(hsv, greenLower, greenUpper)
  mask = cv.erode(mask, None, iterations = 2)
  mask = cv.dilate(mask, None, iterations = 2)
  res = cv.bitwise_and(frame, frame, mask = mask)
  # Escreve o frame no arquivo
  out.write(res)

out.release()

os.system(f"ffmpeg -i ball_tracking_example_out.mp4 -vcodec libx264 ball_tracking_example_out_compressed.mp4")     
```
```bash
# Execute este código se quiser ver o vídeo original
mp4 = open("ball_tracking_example_out_compressed.mp4",'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""

""" % data_url)
```

 