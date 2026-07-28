# import cv2 as cv
#
# image = cv.imread('Images/big.png')
#
# cv.imshow("image", image)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
#
#
#
import cv2

kamera = cv2.VideoCapture("../Videos/Baliq.mp4")

while True:
    ret, frame = kamera.read()
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('l'):
        break

kamera.release()
cv2.destroyAllWindows()
