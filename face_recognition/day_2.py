from face_recognition import face_encodings, face_locations, compare_faces, face_distance
import pickle
from cvzone.FaceDetectionModule import FaceDetector
import cv2
import os

kamera = cv2.VideoCapture(0)
detector = FaceDetector()

know_face_encodings = []
know_face_names = []

for file in os.listdir("Faceses"):
    if file.endswith(".pkl"):
        with open(os.path.join("Faceses", file), "rb") as f:
            encoding = pickle.load(f)
            # print(file)
            know_face_encodings.append(encoding)
            know_face_names.append(file[:-4])

print("YOZILGAN YUZLAR ENDOCING KODI \n", know_face_encodings)
print("YOZILGAN YUZLAR ISMI \n", know_face_names)

while True:
    ret, frame = kamera.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Frame", frame)
    face_location = face_locations(frame)
    encoding_face = face_encodings(face_image=frame, known_face_locations=face_location)
    solishtirish = compare_faces(known_face_encodings=know_face_encodings, face_encoding_to_check=encoding_face)
    print(solishtirish)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
