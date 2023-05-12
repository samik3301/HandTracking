import cv2
import mediapipe as mp
import time
import trackingmodule as tm  #can import the tracking module upon any project now


cap = cv2.VideoCapture(0) #webcam is at 0
detector = tm.handDetector()

pTime =0
cTime =0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    handPos= detector.findPosition(img)
    if len(handPos) != 0:
        print(handPos[4])   #can track any landmark id [ 4 is the thumb tip ]

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int((fps))),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)

    cv2.imshow("Window",img)
    cv2.waitKey(1)
