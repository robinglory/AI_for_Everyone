#contour

# [[(x1,y1),(x2,y2),(x3,y3)],[(x11,y12),(x21,x22),(x31,y31)]]

import numpy as np
import cv2
print(cv2.__version__)
hueLow = 164
hueHigh = 179
hueLow2 = 23
hueHigh2 = 35
satLow = 31
satHigh = 255
valLow = 179
valHigh = 255
def onTrack1(val):
    global hueLow
    hueLow=val
    print('Low Hue: ',val)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('High Hue: ',val)
def onTrack3(val):
    global satLow
    satLow=val
    print('Low Sat: ',val)
def onTrack4(val):
    global satHigh
    satHigh=val
    print('High Sat: ',val)
def onTrack5(val):
    global valLow
    valLow=val
    print('Low Val: ',val)
def onTrack6(val):
    global valHigh
    valHigh=val
    print('High Val: ',val)
 
 
def onTrack7(val):
    global hueLow2
    hueLow2=val
    print('Low Hue2: ',val)
def onTrack8(val):
    global hueHigh2
    hueHigh2=val
    print('High Hue2: ',val)
 
 
width=960
height=540
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cv2.namedWindow('myTracker')
cv2.moveWindow('myTracker',width,0)
cv2.resizeWindow('myTracker',400,500)
cv2.createTrackbar('Hue Low','myTracker',15,180,onTrack1)
cv2.createTrackbar('Hue High','myTracker',30,180,onTrack2)
 
cv2.createTrackbar('Hue Low2','myTracker',50,180,onTrack7)
cv2.createTrackbar('Hue High2','myTracker',60,180,onTrack8)
 
cv2.createTrackbar('Sat Low','myTracker',10,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',10,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)
 
 
while True:
    ignore,  frame = cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
 
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
 
    lowerBound2=np.array([hueLow2,satLow,valLow])
    upperBound2=np.array([hueHigh2,satHigh,valHigh])
 
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
 
    myMask=myMask | myMask2
    #myMask=cv2.add(myMask,myMask2)
    #myMask=np.logical_or(myMask,myMask2)
    
    contours, junk = cv2.findContours(myMask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame,contours,-1,(255,0,0),3)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= 200:
            # myContour = [contour]
            # cv2.drawContours(frame,[contour],0,(255,0,0),3)
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    #myMask=cv2.bitwise_not(myMask)
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    mySelection=cv2.bitwise_and(frame,frame, mask=myMask)
    mySelection=cv2.resize(mySelection,(int(width/2),int(height/2)))
    cv2.imshow('My Selection', mySelection)
    cv2.moveWindow('My Selection',int(width/2),height)
 
    cv2.imshow('My Mask', myMaskSmall)
    cv2.moveWindow('My Mask',0,height)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()