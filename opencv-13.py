import cv2
print(cv2.__version__)


def myCallBack(val):
    global xPos
    print("X postion: ", val)
    xPos= val
def myCallBack1(val):
    global yPos
    print("Y position: ",  val)
    yPos = val
def myCallBack2(val):
    global myRad
    print("Radius" , myRad)
    myRad = val

width=1920
height=1080
width1 = 400
height1 = 150
myRad = 25
xPos = int(width/2)
yPos = int(height/2)

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("MyTrackbar");
cv2.resizeWindow("MyTrackbar", width1, height1);
cv2.moveWindow("MyTrackbar",1000,0)
cv2.createTrackbar("xPos", "MyTrackbar",xPos,1920,myCallBack)
cv2.createTrackbar("yPos","MyTrackbar",yPos,1920,myCallBack1)
cv2.createTrackbar("radius","MyTrackbar",myRad,int(height/2),myCallBack2)

while True:
    ignore,  frame = cam.read()
    cv2.circle(frame,(xPos,yPos),myRad,(255,0,22),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()