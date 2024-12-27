#finger counting
import numpy as np
import mediapipe as mp
import cv2 as cv
import time
import hand_detection_module as hdm

##########################################(only for right hand)##########################################
########################################( wo bhi seedha haath ya left ka ulta)###########################

detector =  hdm.handDetector(detectionCon= 0.75)
video = cv.VideoCapture(0)
tips = [8, 12, 16, 20]      #for fingers other than thumb

while True:
    fingerup = []
    success, img = video.read()
    detector.findHands(img)
    lmlist = detector.findPosition(img)
    # print(lmlist)
    if len(lmlist) != 0:

        if lmlist[4][1] > lmlist[3][1]:
            fingerup.append(1)
        else:
            fingerup.append(0)
        for finger in tips:

            if lmlist[finger][2] < lmlist[finger - 2][2]:
                fingerup.append(1)
            else:
                fingerup.append(0)
             
    count = fingerup.count(1)  
    print(count)
                
 


    
    cv.imshow("video", img)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()