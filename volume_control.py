import cv2
import mediapipe as mp
import time
import numpy as np
import trackingmodule as tm
import math
import pycaw #python library that allows to change volume [for windows]
import osascript #python library that allows to change volume [for macOS]


'''Basic Code to check the working of the webcam
cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()

    cv2.imshow("Window",img)
    cv2.waitKey(1)
'''

widthCameraFrame, heightCameraFrame = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, widthCameraFrame)
cap.set(4, heightCameraFrame)

currentTime =0
previousTime =0

detector = tm.handDetector(detectionConfidence=0.8)  #increasing hand detection confidence 

#osascript integration

min_volume = 0
max_volume = 100
volper =0




while True:
    success,img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)

    if (len(lmList)!= 0):
        #print(lmList[4],lmList[8])

        x1,y1 = lmList[4][1], lmList[4][2]
        x2,y2 = lmList[8][1], lmList[8][2]

        cx, cy = ((x1+x2)//2) , ((y1+y2)//2)

        cv2.circle(img, (x1,y1),5,(0,0,255),cv2.FILLED)
        cv2.circle(img, (x2,y2),5,(0,0,255),cv2.FILLED)

        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)

        cv2.circle(img, (cx,cy),5,(255,0,0),cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        #print(length)

        if length<50:
            cv2.circle(img, (cx,cy),5,(0,0,255),cv2.FILLED)


        #hand distance 30- 300
        #volume range 0 - 100

        vol = np.interp(length,[30,290],[min_volume,max_volume])
        print(int(length),vol)
        master_volume = "set volume output volume " + str(vol) #osascript integration
        osascript.osascript(master_volume)

        volper = np.interp(length,[30,290],[min_volume,max_volume])
        cv2.putText(img,f'Volume {int(volper)} %',(30,60),cv2.FONT_HERSHEY_SIMPLEX,
                0.5,(0,0,255),1)



    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime

    cv2.putText(img,f'FPS:{int(fps)}',(30,40),cv2.FONT_HERSHEY_SIMPLEX,
                0.5,(0,0,255),1)

    cv2.imshow("Window",img)
    cv2.waitKey(1)

'''
Pending - Increase FPS after osascript integration
Integrate this script with voice command activation automation with siri?
Fix Aesthetics of the landmarks and better colour schemes
'''