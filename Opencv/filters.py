# import cv2
#
# img = cv2.imread("../Images/dogs.png")
#
# cv2.imshow("dogs", img)
#
# blur_img = cv2.blur(img, (5, 5))
# cv2.imshow("blur", blur_img)
#
# gaussian_blur_img = cv2.GaussianBlur(img, (5, 5), 0)
# cv2.imshow("gaussian_blur", gaussian_blur_img)
#
# median_blur_img = cv2.medianBlur(img, ksize=5)
# cv2.imshow("median_blur", median_blur_img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread("../Images/nature.png")
cv2.imshow("nature", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)


# Yashil rang oralig'i
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

cv2.imshow("Original", img)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
