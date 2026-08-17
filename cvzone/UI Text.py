import cv2
import cvzone

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    # cvzone.putTextRect(
    #     frame,
    #     "",
    #     (150,200),
    #     # scale=10
    # )
    # cvzone.cornerRect(frame, (100, 100, 200, 200))
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()

cv2.destroyAllWindows()
