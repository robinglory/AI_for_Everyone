import cv2
import mediapipe as mp
import numpy as np
import time

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

def findDistances(handData):
    distMatrix = np.zeros([len(handData),len(handData)],dtype='float')
    palmSize =((handData[0][0]-handData[9][0])**2 + (handData[0][1]-handData[9][1]) ** 2)**(1./2.)

    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            distMatrix[row][column] = (((handData[row][0]-handData[column][0])**2 + (handData[row][1]-handData[column][1]) ** 2)**(1./2.))/palmSize

    return distMatrix

def findError(gestureMatrix,unknownMatrix,keyPoints):
    error  = 0
    for row in keyPoints:
        for column in keyPoints:
            error = error + abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    # print(error)
    return error

def findGesture(unkownGesture,knownGestures,keyPoints,gestNames,tol):
    errorArray = []
    for i in range(0,len(gestNames),1):
        error = findError(knownGestures[i],unkownGesture,keyPoints)
        errorArray.append(error)
    errorMin = errorArray[0]
    minIndex = 0
    for i in range(0,len(errorArray),1):
        if errorArray[i] < errorMin:
            errorMin = errorArray[i]
            minIndex = i
    if errorMin < tol:
        gesture = gestNames[minIndex]
    if errorMin > tol:
        gesture = "Unkown Gesture!"
    return gesture


# Initialize camera properties
width = 1280
height = 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

findHands = mpHands()

keyPoints = [0,4,5,9,13,17,8,12,16,20]

##time
time.sleep(2)
train = True
tol = 10
knownGestures = []
numGest = int(input("How Many Gestures Do You want to Train!! "))
gestNames = []
trainCnt = 0
for i in range(0,numGest):
    prompt = "Name of the Gesture # " + str(i+1) + "  "
    name = input(prompt)
    gestNames.append(name)
print(gestNames)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
        break

    hands_marks,handsType = findHands.Marks(frame, width, height)
    if train == True:
        if hands_marks != []:
            print("Please Show Gesture ", gestNames[trainCnt], ": Press T key when you are ready")
            if cv2.waitKey(1) & 0xff==ord('t'):
                knownGesture = findDistances(hands_marks[0])               
                # print(knownGesture)
                knownGestures.append(knownGesture)
                trainCnt = trainCnt +1
                if trainCnt == numGest:
                    train = False 
    
    if train == False:
        if hands_marks != []:
            unkownGesture =  findDistances(hands_marks[0])
            # error = findError(knownGesture,unkownGesture,keyPoints)
            myGesture = findGesture(unkownGesture,knownGestures,keyPoints,gestNames,tol)
            cv2.putText(frame,myGesture,(100,175),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),8)


    for hand,handType in zip(hands_marks,handsType):
        if handType == "Right":
            handColor = (255,0,0)
        if handType ==  "Left":
            handColor = (0,0,255)
        for point in hand:
            cv2.circle(frame, point, 10, handColor, cv2.FILLED)
    cv2.rectangle(frame, (100,100),(500,500),(100,255,0),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
