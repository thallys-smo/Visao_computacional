import cv2 as cv
import mediapipe as mp

# Iniciating the OpenCv and Mediapipe

webcam = cv.VideoCapture(0)

# Inicialization of Mediapipe
sol_recon_face = mp.solutions.face_detection
reconition_face = sol_recon_face.FaceDetection()
draw_face = mp.solutions.drawing_utils

while True:
    # Reading infomations of webcam
    veri, frame = webcam.read() 
    # Veri
    if not veri:
        break
    # Recotinzing the faces inside of mediapipe
    list_face = reconition_face.process(frame)
    
    if list_face.detections:
        for rosto in list_face.detections:
            # Draw the face in the image
            draw_face.draw_detection(frame, rosto)
    
    cv.imshow("Face in the Webcam", frame)
    
    # If ESC (== 27) is press, stop loop
    if cv.waitKey(5) == 27:
        break


# Desativating the Webcam, is need to do it. 
webcam.release()
cv.destroyAllWindows()