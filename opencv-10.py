import cv2
print(cv2.__version__)
width=800;
height=540;


snipwidth = 180;
snipheight = 90;

#center position of the snip
boxCR = int(height/2)#box center row
boxCC = int(width/2)#box center column

#Move the  snip
deltaRow = 1;
delataColumn = 1;


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()

    #our snip frame
    frameROI = frame[int(boxCR-snipheight/2): int(boxCR+snipheight/2), int(boxCC-snipwidth/2):int(boxCC+snipwidth/2)]
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxCR-snipheight/2): int(boxCR+snipheight/2), int(boxCC-snipwidth/2):int(boxCC+snipwidth/2)] = frameROI

    # Draw a border around the snip for visibility
    cv2.rectangle(frame, 
                  (int(boxCC - snipwidth / 2), int(boxCR - snipheight / 2)), 
                  (int(boxCC + snipwidth / 2), int(boxCR + snipheight / 2)), 
                  (0, 255, 0), 2)  # Green border with thickness of 2
    #animation part

    if boxCR -snipheight/2 <= 0 or boxCR + snipheight/2 >=height:
        deltaRow = deltaRow * (-2)
    if boxCC-snipwidth/2 <= 0 or boxCC + snipwidth/2 >= width:
        delataColumn = delataColumn * (-2)
        
    boxCR = boxCR + deltaRow
    boxCC = boxCC + delataColumn

    cv2.imshow("My ROI", frameROI);
    cv2.moveWindow("My ROI",width,0)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()