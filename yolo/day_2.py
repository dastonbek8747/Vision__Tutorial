import cv2
from ultralytics.models import YOLO

kamera = cv2.VideoCapture("../Videos/thailand stree.mp4")
model = YOLO("yolo26n.pt")
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
while True:
    ret, frame = kamera.read()
    if not ret:
        print("Kamera_ochilmadi !")
        break
    frame = cv2.resize(frame, (800, 600))
    frame = cv2.flip(frame, 1)

    mashinalar_soni = 0
    insonlar_soni = 0
    mototsikllar_soni = 0
    object_frame = model(frame)
    for obj in object_frame:
        for i in obj.boxes:
            class_id = int(i.cls[0])
            if class_id == 0:
                insonlar_soni += 1
            elif class_id == 2:
                mashinalar_soni += 1
            elif class_id == 3:
                mototsikllar_soni += 1
    cv2.putText(img=frame, thickness=1, color=(255, 0, 0), text=f"Insonlar soni: {insonlar_soni}",
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, org=(10, 50))
    cv2.putText(img=frame, thickness=1, color=(255, 0, 0), text=f"Mashinalar soni: {mashinalar_soni}",
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, org=(10, 100))
    cv2.putText(img=frame, thickness=1, color=(255, 0, 0), text=f"Mototsiklar soni: {mototsikllar_soni}",
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, org=(10, 150))
    cv2.imshow("yolo object", object_frame[0].plot())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
