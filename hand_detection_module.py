import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=float(self.detectionCon),
            min_tracking_confidence=float(self.trackCon),
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return lmList

    def up_finger(self, lmList):
        tips = [8, 12, 16, 20]      #for fingers other than thumb

        while True:
            fingerup = []       
            if len(lmList) != 0:

                if lmList[4][1] > lmList[3][1]:
                    fingerup.append(1)
                else:
                    fingerup.append(0)
                for finger in tips:

                    if lmList[finger][2] < lmList[finger - 2][2]:
                        fingerup.append(1)
                    else:
                        fingerup.append(0)
                count = fingerup.count(1) 

            return fingerup, count
                
            
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)  # Use default camera
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    detector = handDetector()

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture frame. Exiting...")
            break

        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if lmList:
            fingerup, count = detector.up_finger(lmList)
            print(count)
        # if len(lmList) != 0:
        #     print("Tip of Thumb (ID 4):", lmList[4])  # Example: Tip of the thumb

        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime

        cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('d'):  # Press 'd' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
