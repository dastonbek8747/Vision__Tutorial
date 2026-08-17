import cv2
from cvzone.FaceDetectionModule import FaceDetector

detector = FaceDetector()
kamera = cv2.VideoCapture("../Videos/E43A inside the Retail store in USA #2.mp4")
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
while True:
    ret, frame = kamera.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break
    frame, face = detector.findFaces(frame, draw=True)
    if face:
        print(f"FACE:\n{face}")
        for i in range(len(face)):
            frame = cv2.circle(frame, (face[i]['center'][0], face[i]['center'][1]), 100, (0, 0, 255), thickness=7)
            # frame=cv2.rectangle(frame,pt1=)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
