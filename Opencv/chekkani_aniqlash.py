# | Usul          | Qanday ishlaydi                             | Afzalligi                               | Kamchiligi                                        |
# | ------------- | ------------------------------------------- | --------------------------------------- | ------------------------------------------------- |
# | **Sobel**     | X va Y gradientlarini hisoblaydi            | Sodda, gradient yo'nalishini ham beradi | Shovqinga sezgir, chekkalar qalin bo'lishi mumkin |
# | **Laplacian** | Ikkinchi tartibli gradientni hisoblaydi     | Barcha yo'nalishdagi chekkalarni topadi | Shovqinga juda sezgir                             |
# | **Canny**     | Blur → Sobel → NMS → Threshold → Hysteresis | Juda aniq va ingichka chekkalar         | Ichki algoritmi murakkabroq                       |

import cv2

img = cv2.imread("../Images/all_animals.png")

cv2.imshow("Original", img)
dx_oqi = cv2.Sobel(img, cv2.CV_32F, 1, 0)
dy_oqi = cv2.Sobel(img, cv2.CV_32F, 0, 1)
combined = cv2.magnitude(dx_oqi, dy_oqi)
combined = cv2.convertScaleAbs(combined)
cv2.imshow("combined", combined)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap_combined = cv2.convertScaleAbs(lap)
cv2.imshow("lap", lap_combined)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
