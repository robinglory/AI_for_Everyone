import cv2
import time
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier(r'C:\Users\ASUS\Documents\Python\Programs\haar\haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(r'C:\Users\ASUS\Documents\Python\Programs\haar\haarcascade_eye.xml')

fps = 10
timeStamp = time.time()
while True:
    ignore,  frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ##Face Detection Start Here
    faces = faceCascade.detectMultiScale(frameGray,1.3,5)
    # print(faces)
    for face in faces:
        x,y,width,height = face
        # print(f"x = {x} and y = {y} and width = {width} and height = {height}")
        cv2.rectangle(frame, (x,y), (x+width,y+height), (255,0,0), 3)
        #This is the solution that I have came up by myself.
        # cv2.rectangle(frame, (x+30,y+50),(int(x+width)-30,int(y+height/2)), (0,0,255), 1)
        ##another method
        # Region of interest (ROI) for eyes (inside detected face)
        frameROI = frame[y:y+height, x:x+width]
        frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(frameROIGray, 1.3, 5)
        for eye in eyes:
            xeye, yeye, weye, heye = eye
            cv2.rectangle(frame[y:y+height, x:x+width], (xeye,yeye),(xeye+weye,yeye+heye), (255,0,0),3)



    ## Eye Detection Start Here
    ## it is very computational intense so we gonna approach another way
    # eyes = eyeCascade.detectMultiScale(frameGray,1.3,5)
    # for eye in eyes:
    #     x,y,width,height = eye
    #     cv2.rectangle(frame, (x,y), (x+width,y+height), (255,0,0), 3)


    loopTime = time.time()-timeStamp
    timeStamp = time.time()
    fpsNEW = 1/loopTime
    fps = .9*fps + .1*fpsNEW
    fps = int(fps)
    cv2.putText(frame,str(fps) +" Frame Per Second", (5,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,100,0), 2)
    # print(fps)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()