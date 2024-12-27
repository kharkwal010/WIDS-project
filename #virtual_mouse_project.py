#virtual mouse

import numpy as np
import cv2 as cv
import mediapipe as mp
import time
import pyautogui
import hand_detection_module as hdm
import math
pyautogui.FAILSAFE = False
##############################################################################################
w_cam, h_cam = 640, 420
s_width, s_height = pyautogui.size()
rframe = 100

########### (for smoothening):
smooth = 8
c_locx , c_locy = 0, 0
p_locx , p_locy = 0, 0
##############################################################################################

detector = hdm.handDetector(detectionCon= 0.75 , maxHands= 1)

video = cv.VideoCapture(0)
video.set(3, w_cam)
video.set(4, h_cam)
ptime = 0


while True:
    success, img = video.read()
    img = cv.flip(img, 1)
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv.rectangle(img, (rframe, rframe), (w_cam - rframe, h_cam - rframe), (255, 0, 0), 5)
    cv.putText(img, f"FPS = {int(fps)}", (20, 70), 1, cv.FONT_HERSHEY_COMPLEX, (255, 0, 0), 2)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    if lmlist:
        finger, count = detector.up_finger(lmlist)
        
    ###################(find the coordinates of the tips)#########---------> 1: index
    
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        x3 = np.interp(x1, (rframe, w_cam - rframe), (0 , s_width))
        y3 = np.interp(y1, (rframe, w_cam - rframe), (0 , s_width))
        
        if finger[1] == 1 and finger[2] == 0:
            cv.circle(img, (x1 , y1), 10, (0, 0, 255), cv.FILLED)
            c_locx = p_locx + (x3 - p_locx) / smooth
            c_locy = p_locy + (y3 - p_locy) / smooth

            pyautogui.moveTo(c_locx, c_locy)
            p_locx = c_locx
            p_locy = c_locy
        if finger[1] == 1 and finger[2] == 1:
            length = math.hypot((x1 - x2), (y1 - y2))
            cv.line(img, (x1, y1), (x2, y2), (0, 0 , 255), 2)
            cv.circle(img, ((x1 + x2) // 2 ,(y1 + y2) // 2 ), 10, (0, 0, 255), cv.FILLED)

            if length < 25:
                cv.circle(img, ((x1 + x2) // 2 ,(y1 + y2) // 2 ), 10, (0, 255, 255), cv.FILLED) 
                
                pyautogui.click(c_locx, c_locy)
            
         

            print(length)
        
 
    cv.imshow("video",img)

    if cv.waitKey(10) & 0xFF==ord('d'):
        break                   #10 sec se jyada hua aur d press kiya to video band

video.release()
cv.destroyAllWindows()
