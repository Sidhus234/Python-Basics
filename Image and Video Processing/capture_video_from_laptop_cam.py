"""
Captures the video from laptop web-cam and displays it
"""
import cv2
import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    time.sleep(3)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(100)

    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
