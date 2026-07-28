# import cv2
# from cvzone.HandTrackingModule import HandDetector
# from cvzone.FaceMeshModule import FaceMeshDetector
#
# hand_detetor = HandDetector()
# face_detector = FaceMeshDetector()
# kamera = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = kamera.read()
#     hand, frame = hand_detetor.findHands(frame, draw=False)
#     frame, face = face_detector.findFaceMesh(frame)
#     print(hand)
#     if hand:
#         lmList = hand[0]['lmList']
#         for l in lmList:
#             x, y, z = l
#             cv2.circle(frame, (x, y), 10, (200, 0, 0))
#     cv2.imshow("Frame", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# kamera.release()
# cv2.destroyAllWindows()


import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceMeshModule import FaceMeshDetector

hand_detector = HandDetector()

face_detektor = FaceMeshDetector()

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    if not ret:
        break
    hand, frame = hand_detector.findHands(frame)
    frame, face = face_detektor.findFaceMesh(frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
