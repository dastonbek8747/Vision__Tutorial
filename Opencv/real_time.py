# # import cv2
# #
# # kamera = cv2.VideoCapture(0)
# #
# # while True:
# #     ret, frame = kamera.read()
# #     print(ret)
# #     cv2.imshow("frame", frame)
# #     frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# #     cv2.imshow("NEW",frame)
# #     if cv2.waitKey(1) & 0xFF == ord('m'):
# #         break
# #
# # kamera.release()
# # cv2.destroyAllWindows()
# import cv2
#
# # 1. O'qish — rasmni xotiraga yuklash
# img = cv2.imread("../Images/dogs.png")
#
# # 2. Xossalarni tekshirish
# print(img.shape)  # (480, 640, 3) — 480 balandlik, 640 kenglik, 3 kanal (rangli)
# print(img.size)   # 921600 — jami piksel elementlari (480*640*3)
#
# # 3. Ko'rsatish — ekranda ochish
# cv2.imshow("Rasm", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # 4. Saqlash — o'zgartirilgan yoki xuddi shu rasmni faylga yozish
# cv2.imwrite("Images/news_.png", img)
#


import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("frame", frame)
    counter_images = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.Canny(counter_images, 80, 100)
    cv2.imshow("Chekka", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
