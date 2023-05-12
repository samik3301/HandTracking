import cv2 
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode = False, maxHands = 3, modelC=1,detectionConfidence = 0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelC = modelC #new attribute added in the latest documentation , model complexicity
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        
        #again initialization all
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelC,
                                        self.detectionConfidence,self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils 

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks: #if it detects hands then it draws all hands
            for self.handsLms in self.results.multi_hand_landmarks: #drawing each hand (maximum of 2, unless :0)
                if draw: 
                    self.mpDraw.draw_landmarks(img,self.handsLms,self.mpHands.HAND_CONNECTIONS) 

        return img

    def findPosition(self,img, handNumber=0, draw= True):
        lmList = []
        if self.results.multi_hand_landmarks: #if it detects hands then it draws all hands
            myHand = self.results.multi_hand_landmarks[handNumber] #drawing each hand (maximum of 2, unless :0)
            for id, lm in enumerate(myHand.landmark):
                    #print(id,lm)
                    h,w,c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y*h) #rounding the coordinates to integer
                    #print(id, cx,cy) #printing id , cx, cy 
                    #landmark extraction lm_x coordinate * width
                    #landmark extraction lm_y coordinate * height
                    lmList.append([id,cx,cy])
                    '''
                    
                    '''
                    if draw :
                        cv2.circle(img, (cx,cy),10,(255,0,0),cv2.FILLED) #thumb tip

        return lmList

def main():
    cap = cv2.VideoCapture(0) #webcam is at 0
    detector = handDetector()

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

if __name__ == "__main__":
    main()