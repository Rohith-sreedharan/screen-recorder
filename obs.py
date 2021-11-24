import pyautogui as pu
import cv2
import numpy as np 

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Rohithaditya_screen_rec.avi"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow('Screen1', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Screen1", 480, 370)
while True:
    img = pu.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Screen1", frame)
    if cv2.waitKey(1) == ord("q"):
        break
out.release()
cv2.destroyAllWindows()