import cv2
import mediapipe as mp

print(cv2.__version__)

class mpHands:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
                    static_image_mode=False,
                    max_num_hands=max_num_hands,
                    min_detection_confidence=min_detection_confidence,
                    min_tracking_confidence=min_tracking_confidence,
                )
    def Marks(self, frame, width, height):
        myHands = []
        handsType =[]
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)

        if results.multi_hand_landmarks:
            # print(results.multi_handedness)
            for hand in results.multi_handedness:
                # print(hand.classification)
                # print(hand.classification[0].label) ##Extracting the left or right hand. Handling the data structure!
                handType = hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landmark in handLandMarks.landmark:
                    myHand.append((int(landmark.x * width), int(landmark.y * height)))
                myHands.append(myHand)
        return myHands,handsType

# Initialize camera properties
width = 1280
height = 800
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

findHands = mpHands()
paddleWidth = 25
paddleHeight = 125
paddleColor = (255,0,255)
ballRadiu = 30
ballColor = (0,0,255)
xPos = int(width/2)
yPos = int(height/2)
deltaX = 9
deltaY = 9
font = cv2.FONT_HERSHEY_COMPLEX
fontHeight = 2
fontWeight = 3
fontColor = (255,100,100)
yLeftTip = 0
yRightTip = 0
scoreLeft = 0
scoreRight = 0
LScoreTxt = "Left Player Score"
LLivesTxt = "Left Player Lives"
RScoreTxt = "Right Player Score"
RLivesTxt = "Right Player Lives"
Llives = 3
Rlives = 3
gameOverTxt = "Game Over!!"

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
        break
    frame = cv2.resize(frame,(width,height))
    cv2.circle(frame,(xPos,yPos),ballRadiu,ballColor,-1)
    ##LeftPlayerTextandScore and stuffs
    cv2.putText(frame,str(LScoreTxt),(1,50),font,1,fontColor,fontWeight)
    cv2.putText(frame,str(scoreLeft),(100,135),font,fontHeight,(33,33,33),fontWeight)
    cv2.putText(frame,str(LLivesTxt),(1,200),font,1,fontColor,fontWeight)
    cv2.putText(frame,str(Llives),(100,265),font,fontHeight,(33,33,33),fontWeight)

    ##Right Player Text and Score and Stuffs
    cv2.putText(frame,str(RScoreTxt),(width-425,50),font,1,fontColor,fontWeight)
    cv2.putText(frame,str(scoreRight),(width-200,135),font,fontHeight,(33,33,33),fontWeight)
    cv2.putText(frame,str(RLivesTxt),(width-425,200),font,1,fontColor,fontWeight)
    cv2.putText(frame,str(Rlives),(width-200,265),font,fontHeight,(33,33,33),fontWeight)

    hands_marks,handsType = findHands.Marks(frame, width, height)
    for hand,handType in zip(hands_marks,handsType):    
        if handType ==  "Left":
            yLeftTip = hand[8][1]
        if handType == "Right":
            yRightTip = hand[8][1]
    cv2.rectangle(frame,(0,yLeftTip-int(paddleHeight/2)),(paddleWidth,int(yLeftTip+paddleHeight)),paddleColor,-1)
    cv2.rectangle(frame,(width-paddleWidth,yRightTip-int(paddleHeight/2)),(width,int(yRightTip+paddleHeight)),paddleColor,-1)
    topBallEdge = yPos-ballRadiu
    bottomEdgeBall = yPos+ballRadiu
    leftEdgeBall = xPos-ballRadiu
    rightEdgeBall = xPos+ballRadiu

### Moving the Ball
    if Llives > 0 and Rlives > 0:
        if topBallEdge <= 0 :
            deltaY = deltaY *(-1)
        if bottomEdgeBall >= height:
            deltaY = deltaY*(-1)
        ##Bouncing the ball on the paddle on both sides
        if leftEdgeBall <= paddleWidth:
            if yPos >= yLeftTip-int(paddleHeight/2) and yPos <= yLeftTip+int(paddleHeight/2):
                deltaX = deltaX * (-1)
            else:
                xPos = int(width/2)
                ypos = int(height/2)
                scoreRight = scoreRight+1
                Llives = Llives -1
        if rightEdgeBall >= width - paddleWidth:
            if yPos >= yRightTip-int(paddleHeight/2) and yPos <= yRightTip+int(paddleHeight/2):
                deltaX = deltaX * (-1)
            else:
                xPos = int(width/2)
                ypos = int(height/2)
                scoreLeft = scoreLeft+1
                Rlives = Rlives -1
        xPos = xPos + deltaX
        yPos = yPos + deltaY
            ##Bouncing the ball on the top and bottom of the frame

##Game Over text and Display the score
    if Llives == 0 or Rlives == 0 :
        xPos = int(width/2)
        yPos = int(height/2 - 300)
        deltaX = 0
        deltaY = 0
        cv2.putText(frame,str(gameOverTxt),(int(width/2)-350,int(height/2)),font,3,(0,0,255),7)
        if scoreLeft > scoreRight:
            cv2.putText(frame,str("Left Player Win with Score "),(int(width/2)-300,int(height/2)+100),font,1,(0,0,230),fontWeight)
            cv2.putText(frame,str(scoreLeft),(int(width/2)+ 200,int(height/2)+100),font,1,(0,0,230),fontWeight)
        if scoreRight > scoreLeft:
            cv2.putText(frame,str("Right Player Win with Score "),(int(width/2)-300,int(height/2)+100),font,1,(0,0,230),fontWeight)
            cv2.putText(frame,str(scoreRight),(int(width/2)+ 200,int(height/2)+100),font,1,(0,0,230),fontWeight)

    cv2.imshow('Double Player Ping Pong Game', frame)
    cv2.moveWindow('Double Player Ping Pong Game',0,0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
