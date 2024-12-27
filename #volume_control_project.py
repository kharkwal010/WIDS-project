import numpy as np 
import mediapipe as mp
import cv2 as cv
import time
import hand_detection_module as hdm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
###########################
wcam, hcam = 640, 480
###########################


video = cv.VideoCapture(0)
ptime = 0
detector = hdm.handDetector()
video.set(3, wcam)
video.set(4, hcam)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volume_range = (volume.GetVolumeRange())
min_vol = volume_range[0]
max_vol = volume_range[1]


while True:
    success, img = video.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    volPer = 0
    if len(lmlist) != 0:
        x1, y1  = lmlist[4][1] ,lmlist[4][2]     #thumb
        x2, y2  = lmlist[8][1] ,lmlist[8][2]     #index

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv.circle(img, (x1, y1), 10, (0, 255, 0), cv.FILLED)
        cv.circle(img, (x2, y2), 10, (0, 255, 0), cv.FILLED)
        cv.circle(img, (cx, cy), 10, (0, 255, 0), cv.FILLED)
        cv. line(img, (x1,y1), (x2,y2), (0,255,0),3)

        length = math.hypot((x1 - x2), (y1 - y2))
        vol = np.interp(length, [20, 170], [min_vol, max_vol])
        # volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [20, 170], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)
        #################range of length = 20, 170
        if length < 25  or length > 170:
            cv.circle(img, (cx, cy), 10, (0, 0, 255), cv.FILLED)
           
    cv.putText(img, f"fps = {int(fps)}", (20, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255 , 0 , 0), 2)
    cv.putText(img, f"volume = {int(volPer)}%", (20, 80), cv.FONT_HERSHEY_COMPLEX, 0.5, (255 ,0  , 255), 1)
    cv.imshow('video', img)
    if len(lmlist) != 0:
        print(length)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()