import cv2

img = cv2.imread("../Images/dogs.png")
cv2.imshow("", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
ret, binary = cv2.threshold(gray_image, 150, 200, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
