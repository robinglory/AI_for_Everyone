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

paddleWidth = 125
paddleHeight = 25
paddleColor = (0,255,0)

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame,(hand[8][0]-int(paddleWidth/2),0),(hand[8][0]+int(paddleWidth/2),paddleHeight),paddleColor,-1)
            
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()