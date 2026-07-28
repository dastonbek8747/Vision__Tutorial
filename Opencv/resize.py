import cv2

img = cv2.imread("../Images/dogs.png")
print(img.shape)
print(img.size)
cv2.imshow("dogs", img)

# birinchi width beriladi keyin height beriladi bunda
resized_img = cv2.resize(img, (100, 200))
cv2.imshow("resized_dogs", resized_img)

# bunda birinchi berilgani y oqi boyicha qirqadi ikkinchisi esa x oqi boyicha qirqadi
cropped_img = img[100:300, 100:500]
cv2.imshow("cropped_dogs", cropped_img)

# rasmni aylantirish
# | `cv2.ROTATE_90_CLOCKWISE`        | 90° o'ngga |
# | `cv2.ROTATE_90_COUNTERCLOCKWISE` | 90° chapga |
# | `cv2.ROTATE_180`                 | 180°       |

rotate_img = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("rotated_dogs", rotate_img)

# rasmni akslantirsh yani rasmdagi masalan inson chapga qarayotgan bolsa uni onga aylantirish
# | `0`        | Vertikal (yuqori ↔ past) yani yuqoriga qaragan rasmni pastga aylantirib qoyadi |
# | `1`        | Gorizontal (chap ↔ o'ng)  chap bolsa onga onga qaragan bolsa chapga qaratadi |
# | `-1`       | Ikkala tomonga     hammasini teskarisiga otkazib tashlaydi |


akslantirilgan_img = cv2.flip(img, 1)
cv2.imshow("akslantirilgan_img", akslantirilgan_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
