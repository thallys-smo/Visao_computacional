import cv2 as cv
import numpy as np
from PIL import Image
import os

recognizer = cv.face.LBPHFaceRecognizer_create()

# Path of the Images to train the model
path = "Reconhecimento de Faces/Haar-cascade/dados_faces"

def get_image(path):
    # Take the path of with image
    image_path = [os.path.join(path,f) for f in os.listdir(path)]
    faces, ids = [],[]

    for image_path in image_path:
        face_image = Image.open(image_path).convert('L')
        face_array = np.array(face_image, 'uint8')
        Id = (os.path.split(image_path)[-1].split(".")[1])
        Id = int(Id)
        faces.append(face_array)
        ids.append(Id)
        cv.imshow("Trainamento", face_array)
        cv.waitKey(2)

    return ids, faces

IDs, faces_dados = get_image(path)

recognizer.train(faces_dados, np.array(IDs))
recognizer.write("Reconhecimento de Faces/Haar-cascade/Modelo Treinado/Modelo_treinado.yml")

cv.destroyAllWindows()

print("Treinamento Completo")
