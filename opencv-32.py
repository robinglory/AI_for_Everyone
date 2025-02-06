import cv2
import mediapipe as mp
print(cv2.__version__)

class mpHands:
    import mediapipe as mp
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
                    static_image_mode=False,
                    max_num_hands=max_num_hands,
                    min_detection_confidence=min_detection_confidence,
                    min_tracking_confidence=min_tracking_confidence,)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)

paddleWidth = 250
paddleHeight = 50
paddleColor = (0,0,0)
ballRadius = 50
ballColor = (16,16,247)
xPos = int(width/2)
yPos = int(height/2)
DeltaX = 10
DeltaY = 10
ScoreTxt = "Your Score"
score = 0
LivesTxt = "Your Lives"
lives = 2
font = cv2.FONT_HERSHEY_COMPLEX
txt_color = (17,233,247)
gameOverTxt = "This Game is Over!!"


while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    cv2.circle(frame,(xPos,yPos),ballRadius,ballColor,-1)
    cv2.putText(frame,str(ScoreTxt),(5,int(4* paddleHeight)),font,1,txt_color,3)
    cv2.putText(frame,str(score),(25,int(6* paddleHeight)),font,2,txt_color,5)
    cv2.putText(frame,str(LivesTxt),(width-255,int(4* paddleHeight)),font,1,txt_color,3)
    cv2.putText(frame,str(lives),(width-125,int(6* paddleHeight)),font,2,txt_color,5)

    handData=findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame,(hand[8][0]-int(paddleWidth/2),0),(hand[8][0]+int(paddleWidth/2),paddleHeight),paddleColor,-1)

    topEdgeBall = yPos-ballRadius
    bottomEdgeBall = yPos+ballRadius
    leftEdgeBall = xPos-ballRadius
    rightEgeBall = xPos+ballRadius

    if leftEdgeBall<= 0 or rightEgeBall >= width:
        DeltaX = DeltaX * (-1)
    if bottomEdgeBall>= height:
        DeltaY = DeltaY * (-1)

    if topEdgeBall <= paddleHeight:
        if xPos >= (handData[0][8][0]-int(paddleWidth/2)) and xPos <= (handData[0][8][0]+int(paddleWidth/2)):
            DeltaY = DeltaY * (-1)
            score = score + 1
            currentscore = score
        else:
            xPos = int(width/2)
            yPos = int(height/2)
            lives = lives -1

    if lives == 0 :
        DeltaX = width
        DeltaY = height
        cv2.putText(frame,str(gameOverTxt),(int(width/2)-150,int(height/2)),font,1,(0,0,255),3)
        cv2.putText(frame,str("Your Score: "),(int(width/2)-150,int(height/2)+50),font,1,(125,0,255),3)
        cv2.putText(frame,str(currentscore),(int(width/2)+ 50,int(height/2)+50),font,1,(125,0,255),3)

      
    xPos = xPos +DeltaX
    yPos = yPos + DeltaY
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()