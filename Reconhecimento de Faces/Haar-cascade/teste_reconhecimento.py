import cv2 as cv

# Initialization of WebCam 
webcam = cv.VideoCapture(2)

# Initialization of Cascade Classifier
face_detect = cv.CascadeClassifier("Reconhecimento de Faces/Haar-cascade/haarcascade_frontalface_default.xml")

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("Reconhecimento de Faces/Haar-cascade/Modelo Treinado/Modelo_treinado.yml")

nomes_pessoas = ["", "Thallys"]
count = 0
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
        serial, confianca = recognizer.predict(faces_gray[y:y+b,x:x+a])
        print(confianca)
        if confianca > 50:
            # Writing the person name over the box image
            cv.putText(frame, nomes_pessoas[serial],(x,y-40),cv.FONT_HERSHEY_SIMPLEX,0.8,(50,50,225),2)
            # Crating the retangle with the dimensions of (x,y) and (x+a,y+b)
            cv.rectangle(frame, (x,y), (x+a,y+b),(50,50,225),1)
        else:
            # Writing the person name over the box imagce
            cv.putText(frame, "Nao reconhecido", (x,y-40), cv.FONT_HERSHEY_SIMPLEX, 1,(50,50,225),2)
            # Crating the retangle with the dimensions of (x,y) and (x+a,y+b)
            cv.rectangle(frame, (x,y), (x+a,y+b),(50,50,225),1)
    # Open de WebCam and Take the Pictures
    cv.imshow("Recolhimento de Dados", frame)

    # If 'q' is press, the windows close. 
    tecla = cv.waitKey(1)
    if tecla == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()



