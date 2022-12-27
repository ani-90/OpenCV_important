import cv2 as cv
import mediapipe as mp
import numpy as np

blank=np.zeros((1900,1000,3),dtype="uint8")


mpHands=mp.solutions.hands
human_hand=mpHands.Hands()

mpDraw=mp.solutions.drawing_utils

vid=cv.VideoCapture(0)
lmlist=[]
while True:
    flag,img=vid.read()
    print(flag)
    imgrgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

    result=human_hand.process(imgrgb)
    cx=0
    cy=0
    i=0

    if result.multi_hand_landmarks is not None:
        for handlmarks in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handlmarks,mpHands.HAND_CONNECTIONS)

            for id,lm in enumerate(handlmarks.landmark):

                #print(id,lm)
                h,w,c=img.shape

                cx,cy=int(lm.x*w),int(lm.y*h)
                #print(id,cx,cy)
                
                temp=[]
                temp.append(id)
                temp.append(cx)
                temp.append(cy)
                lmlist.append(temp)
                temp=[]
                

                if id==8:
                  
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    dx,dy=int(lm.x*w),int(lm.y*h)
                    cv.circle(img,(cx,cy),20,(100,200,222),cv.FILLED)
    cv.line(blank,(cx,cy),(cx+20,cy+20),(100,100,100),thickness=4)
    
    cv.imshow("hands",img)
    cv.imshow("frame",blank)
    cv.waitKey(1)
