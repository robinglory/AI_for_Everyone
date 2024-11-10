# import cv2
# import numpy
# print(cv2.__version__)
# width= 1800
# height= 1200
# myradius = 30;
# mycolor = (0,0,0);
# mythickness = 2;
# myText= "Geek Glory"
# cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# while True:
#     ignore,  frame = cam.read()
#     frame[int(height/2 -40):int(height/2 +40),int(width/2 -40):int(width/2 +40)] = (255,0,0)

#     cv2.rectangle(frame,(int(width/2 -40),int(height/2 -40)),(int(width/2 +40), int(height/2 +40)),(0,255,0),10);
#     cv2.circle(frame,(int(height/2),int(width/2)) ,25, (255,0,100) )
#     cv2.imshow('my WEBcam', frame) 
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()

import cv2
print(cv2.__version__)
width=640
height=360
myRadius=30
myColor=(0,0,0)
myThick=2
fontH=2
fontT=2
myText='Glory is Boss'
myFont=cv2.FONT_HERSHEY_DUPLEX
upperLeft=(250,140)
lowerRight=(390,220)
lineW=4
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    frame[140:220,250:390]=(255,0,0)
    cv2.rectangle(frame,upperLeft,lowerRight,(0,255,0),lineW)
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)
    cv2.putText(frame,myText,(100,90),myFont,fontH,(0,0,255),fontT)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()