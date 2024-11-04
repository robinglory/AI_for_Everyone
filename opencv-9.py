import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frameROI = frame[100:310,150:490]
    frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)


    frameROIBGR = cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR)
    frame[100:310,150:490] = frameROIBGR

    cv2.imshow("This is my frame region of interest",frameROI)
    cv2.moveWindow("This is my frame region of interest", 650, 0)

    cv2.imshow("This is my GRAY region of interest",frameROIGray)
    cv2.moveWindow("This is my GRAY region of interest", 0, 500)

    cv2.imshow("This is reconverting the gray frame to BGR region of interest",frameROIBGR)
    cv2.moveWindow("This is reconverting the gray frame to BGR region of interest", 650, 500)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()