import cv2 as cv

# Initialization of WebCam 
webcam = cv.VideoCapture(2)

# Initialization of Cascade Classifier

face_detect = cv.CascadeClassifier("Reconhecimento de Faces/Haar-cascade/haarcascade_frontalface_default.xml")

id = input("Entre com o ID:")
count,num_pictures = 0,500 # Counter adn number of photos

while True:
    verificador, frame = webcam.read()
    # Check if the frame is ok
    if not verificador:
        break
    # Chaging the Color to Gray, is needed to Cascade Classifier Algorit
    faces_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 
    faces = face_detect.detectMultiScale(faces_gray, 1.3, 5)
    for (x,y,a,b) in faces:
        count = count + 1
        # Salving the pictures in 'dados_faces'
        # Reconhecimento de Faces/Haar-cascade/dados_faces
        # /home/thallys/Documentos/Visao_computacional/Reconhecimento de Faces/Haar-cascade/dados_faces
        cv.imwrite('Reconhecimento de Faces/Haar-cascade/dados_faces/User.'+ str(id)+"."+str(count)+".jpg",faces_gray[y:y+b,x:x+a])
        # Crating the retangle with the dimensions of (x,y) and (x+a,y+b)
        cv.rectangle(frame, (x,y), (x+a,y+b),(50,50,225),1)

        print("Imagem " + str(count) + " retirada")

    # Open de WebCam and Take the Pictures
    cv.imshow("Recolhimento de Dados", frame)

    # If 'q' is press, the windows close. 
    tecla = cv.waitKey(1)
    if count > 500:
        break
    
    # if tecla == ord('q'):
    #     break

webcam.release()
cv.destroyAllWindows()

print("Recolhimento de Dados foi Completado")

