#painter
import numpy as np
import mediapipe as mp
import cv2 as cv
import os
import hand_detection_module as hdm

###########################################################
draw_colour = (255, 0, 255)
###########################################################

folder = "header"
my_list = [f for f in os.listdir(folder) if f.endswith(('.png', '.jpg'))]
overlay = []

detector = hdm.handDetector(detectionCon= 0.75)
# Load and append images
for impath in my_list:
    image = cv.imread(f"{folder}/{impath}")
    overlay.append(image)

print(f"Loaded {len(overlay)} images.")

# Define a header to display above the video
header = overlay[0]
header = cv.resize(header, (1280, 152))  # Resize header to match video frame width

video = cv.VideoCapture(0)
video.set(3, 1280)  # Set width
video.set(4, 720)   # Set height

#####################################################################################################
img_canvas = np.zeros((720, 1280, 3), np.uint8)
brush_thickness = 15
eraser_thickness = 50
xp, yp = 0, 0
#####################################################################################################

while True:
    success, img = video.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, False)
    if lmlist:
        fingerup, count = detector.up_finger(lmlist)
        # print(fingerup)
    if not success:
        break



    # Overlay the header on top of the video frame
    img[0:152, 0:1280] = header
    
    if lmlist:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        ##################(selection)#######################
        if fingerup[1] and fingerup[2] == 1:
            if y1 < 152:
                if 256< x1 < 512:
                    draw_colour = (255 , 0, 255)
                    header = overlay[0]
                    header = cv.resize(header, (1280, 152))  # Resize header to match video frame width
                elif 512 < x1 < 768:
                    draw_colour = (255 , 0, 0) 
                    header = overlay[1]
                    header = cv.resize(header, (1280, 152))  # Resize header to match video frame width
                elif 768 < x1 < 1024:
                    draw_colour = (0 , 255 , 0) 
                    header = overlay[2]
                    header = cv.resize(header, (1280, 152))  # Resize header to match video frame width
                elif 1024 < x1:
                    draw_colour = (0 , 0 , 0) 
                    header = overlay[3]
                    header = cv.resize(header, (1280, 152))  # Resize header to match video frame width
                
                       
            cv.line(img, (x1,y1), (x2,y2), draw_colour, 15, cv.FILLED)

        ##################(detection)#######################
        if fingerup[1] == 1  and fingerup[2] != 1:
            cv.circle(img, (x1,y1), 15, draw_colour, cv.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1 
            
            if draw_colour == (0, 0, 0):
                cv.line(img, (xp, yp), (x1, y1), draw_colour, eraser_thickness, cv.FILLED)
                cv.line(img_canvas, (xp, yp), (x1, y1), draw_colour, eraser_thickness, cv.FILLED)
                xp, yp = x1, y1 
            else:
                cv.line(img, (xp, yp), (x1, y1), draw_colour, brush_thickness, cv.FILLED)
                cv.line(img_canvas, (xp, yp), (x1, y1), draw_colour, brush_thickness, cv.FILLED)
                xp, yp = x1, y1 

        imgGray = cv.cvtColor(img_canvas, cv.COLOR_BGR2GRAY)
        _, imgInv = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)
        imgInv = cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)
        img = cv.bitwise_and(img,imgInv)
        img = cv.bitwise_or(img,img_canvas)

        xp, yp = x1, y1 


            
    # Display the video feed with the header
    img = cv.addWeighted(img, 0.5, img_canvas, 0.5, 0)
    cv.imshow("video", img)
    # cv.imshow("canvas", img_canvas)

    # Break on pressing 'd'
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
