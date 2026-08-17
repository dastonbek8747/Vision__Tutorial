from face_recognition import face_encodings, face_locations, compare_faces
import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
import pickle

kamera = cv.VideoCapture(0)
detektor = FaceDetector()
while True:
    ret, frame = kamera.read()
    if not ret:
        print("Kamera ochilmadi !")
        break
    frame, face = detektor.findFaces(frame)
    # print(face)
    if face:
        print("Faces aniqlandi .............................................")
        location = face_locations(frame)
        encoding = face_encodings(face_image=frame, known_face_locations=location)
        print(encoding)
        if encoding:
            user_name = input("Enter your name: ")
            with open(f"./Faceses/{user_name}.pkl", "wb") as f:
                pickle.dump(encoding, f)

    print(
        " Yuz muvaffaqiyatli tarzda saqlandi !\n--------------------------------------------------------------------------------------")
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv.destroyAllWindows()
