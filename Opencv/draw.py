import cv2

image = cv2.imread("../Images/dogs.png")

cv2.imshow("", image)

line_image = cv2.line(image, (100, 0), (200, 250), thickness=3, color=(255, 0, 0))
cv2.imshow("Line", line_image)

circle_image = cv2.circle(img=image, center=(300, 300), radius=30, color=(0, 255, 0), thickness=-1)
cv2.imshow("Circle", circle_image)

rectangle_image = cv2.rectangle(img=image, pt1=(100, 100), pt2=(200, 200), color=(0, 0, 255), thickness=-1)
cv2.imshow("Rectangle", rectangle_image)

write_text_image = cv2.putText(img=image, color=(255, 0, 0), thickness=5, text="Salom Doston", org=(100, 300),
                               fontScale=1,fontFace=cv2.FONT_ITALIC)
# | Parametr        | Nima qiladi?                                   | Misol                      | Eslab qolish         |
# | --------------- | ---------------------------------------------- | -------------------------- | -------------------- |
# | **`img`**       | Qaysi rasm ustiga yozish kerakligini bildiradi | `img=image`                | 📷 Qaysi rasm?       |
# | **`text`**      | Qanday matn yozilishini bildiradi              | `"Salom Doston"`           | 📝 Nima yoziladi?    |
# | **`org`**       | Matn qayerdan boshlanishini bildiradi `(x, y)` | `(300, 300)`               | 📍 Qayerga yoziladi? |
# | **`fontFace`**  | Matnning shrift turini tanlaydi                | `cv2.FONT_HERSHEY_SIMPLEX` | 🔤 Qanday shrift?    |
# | **`fontScale`** | Matnning kattaligini belgilaydi                | `1`, `2`, `0.5`            | 🔠 Qanchalik katta?  |
# | **`color`**     | Matn rangini belgilaydi (BGR)                  | `(255,0,0)`                | 🎨 Qanday rang?      |
# | **`thickness`** | Harflarning qalinligini belgilaydi             | `1`, `2`, `3`              | ✏️ Qanchalik qalin?  |

cv2.imshow("Write Text", write_text_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
