from cvzone.PoseModule import PoseDetector
import cv2

kamera = cv2.VideoCapture("../Videos/E43A inside the Retail store in USA #2.mp4")
detector = PoseDetector()


while True:
    ret, frame = kamera.read()
    frame = detector.findPose(frame)
    llm_list, bboxinfo = detector.findPosition(frame, draw=False)
    if llm_list:
        print(f"Landmarks: {llm_list}")
        cv2.circle(frame, center=(llm_list[0][0], llm_list[0][1]), radius=15, color=(0, 0, 255))
    cv2.imshow("Frame", frame)
    # cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()


# Indeks	Bo'g'im	Indeks	Bo'g'im
# 0	Burun	17	Chap kichik barmoq
# 1-6	Ko'z atrofi (chap-o'ng)	18	O'ng kichik barmoq
# 7-8	Quloqlar	19	Chap ko'rsatkich barmoq
# 9-10	Og'iz burchaklari	20	O'ng ko'rsatkich barmoq
# 11	Chap yelka	21-22	Bosh barmoqlar
# 12	O'ng yelka	23	Chap son
# 13	Chap tirsak	24	O'ng son
# 14	O'ng tirsak	25	Chap tizza
# 15	Chap bilak	26	O'ng tizza
# 16	O'ng bilak	27	Chap to'piq
# ...		28	O'ng to'piq