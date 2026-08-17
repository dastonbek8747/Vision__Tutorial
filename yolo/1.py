import cv2
from ultralytics.models import YOLO

model = YOLO("yolo26n.pt")
kamera = cv2.VideoCapture("../Videos/Tokyo kochalarida.mp4")

while True:
    ret, frame = kamera.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    objects = model(frame)
    # for i in objects:
    #     write_object = i.plot()
    # print(objects)
    write_object = objects[0].plot()
    
    cv2.imshow("Frame", write_object)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
