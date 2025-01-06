import cv2
import mediapipe as mp
print(cv2.__version__)
width=640
height=480
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

hands = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mpDraw = mp.solutions.drawing_utils


while True:
    myHands = []
    ignore,  frame = cam.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            myHand=[]
            # mpDraw.draw_landmarks(frame,handLandMarks, mp.solutions.hands.HAND_CONNECTIONS)
            for Landmark in handLandMarks.landmark:
                # print((Landmark.x,Landmark.y))
                myHand.append((int(Landmark.x*width),int(Landmark.y*height)))
            cv2.circle(frame,myHand[20],15,(255,0,0),-1)
            # cv2.circle(frame,myHand[17],35,(255,0,0),-1)
            # cv2.circle(frame,myHand[18],15,(255,0,0),-1)
            # cv2.circle(frame,myHand[19],15,(255,0,0),-1)

            myHands.append(myHand)
            myHands.append(myHand)
            print(myHands)
            print(" ")



    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()

