import cv2 
import mediapipe as mp


import time

cap = cv2.VideoCapture(0) #webcam is at 0

if not cap.isOpened():
    print("Error opening the webcam.")

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils 

pTime =0
cTime =0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks: #if it detects hands then it draws all hands
        for handsLms in results.multi_hand_landmarks: #drawing each hand (maximum of 2, unless :0)
            for id, lm in enumerate(handsLms.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx, cy = int(lm.x * w), int(lm.y*h) #rounding the coordinates to integer
                print(id, cx,cy) #printing id , cx, cy 
                #landmark extraction lm_x coordinate * width
                #landmark extraction lm_y coordinate * height
                '''
                
                '''
                if id == 4:
                    cv2.circle(img, (cx,cy),20,(255,0,0),cv2.FILLED) #thumb tip

                if id == 8:
                    cv2.circle(img, (cx,cy),20,(255,0,0),cv2.FILLED) #index tip
                
                
            mpDraw.draw_landmarks(img,handsLms,mpHands.HAND_CONNECTIONS) 

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int((fps))),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)

    cv2.imshow("Window",img)
    cv2.waitKey(1)