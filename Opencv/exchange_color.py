import cv2

kamera = cv2.VideoCapture(0)

while True:
    _, img = kamera.read()
    cv2.imshow("Rasm", img)
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Kulrang", frame)

    frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

kamera.release()
cv2.destroyAllWindows()
