import cv2
import mediapipe as mp
import numpy as np
import time
import pickle
import serial

# print(cv2.__version__)
arudinoData = serial.Serial('COM9',115200)

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
train = int(input("Enter 1 to Train, Enter 0 to Recognize! "))
if train == 1:
    trainCnt = 0
    knownGestures = []
    numGest = int(input("How Many Gestures Do You want to Train!! "))
    gestNames = []
    for i in range(0,numGest):
        prompt = "Name of the Gesture # " + str(i+1) + "  "
        name = input(prompt)
        gestNames.append(name)
    print(gestNames)
    trainName = input("Filename for Training Data? (Press Enter for Default!) ")
    if trainName == "":
        trainName = "default"
    trainName = trainName+".pkl"
if train == 0:
    trainName = input("What Training Data Do you want to Use? (Press Enter for Default!!) ")
    if trainName == "":
        trainName = "default"
    trainName = trainName + ".pkl"
    with open(trainName,'rb') as f:
        gestNames = pickle.load(f)
        knownGestures = pickle.load(f)
tol = 10
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
        break

    hands_marks,handsType = findHands.Marks(frame, width, height)
    if train == 1:
        if hands_marks != []:
            print("Please Show Gesture ", gestNames[trainCnt], ": Press T key when you are ready")
            if cv2.waitKey(1) & 0xff==ord('t'):
                knownGesture = findDistances(hands_marks[0])               
                # print(knownGesture)
                knownGestures.append(knownGesture)
                trainCnt = trainCnt +1
                if trainCnt == numGest:
                    train = 0
                    with open(trainName,'wb') as f:
                        pickle.dump(gestNames,f)
                        pickle.dump(knownGestures,f)
    
    if train == 0:
        if hands_marks != []:
            unkownGesture =  findDistances(hands_marks[0])
            # error = findError(knownGesture,unkownGesture,keyPoints)
            myGesture = findGesture(unkownGesture,knownGestures,keyPoints,gestNames,tol)
            cv2.putText(frame,myGesture,(100,175),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),8)
            myGesture = myGesture+'\n'
            arudinoData.write(myGesture.encode())

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

# My Arduino Code:
# String cmd;
# int LED1 = 2;
# int LED2 = 3;
# int LED3 = 4;
# int LED4 = 5;
# int LED5 = 6;

# void setup() {
#   // put your setup code here, to run once:
# pinMode(LED1, OUTPUT);
# pinMode(LED2, OUTPUT);
# pinMode(LED3, OUTPUT);
# pinMode(LED4, OUTPUT);
# pinMode(LED5, OUTPUT);

# Serial.begin(115200);

# }

# void loop() {
#   if (Serial.available()) {
#     cmd = Serial.readStringUntil('\n');  
#     cmd.trim();  
#     Serial.println("Received: " + cmd);  // Debugging output

#     if (cmd == "One") {
#       Serial.println("Turning LED1 ON");
#       digitalWrite(LED1, HIGH);
#     } 
#     else if (cmd == "Two") {
#       Serial.println("Turning LED2 ON");
#       digitalWrite(LED2, HIGH);
#     } 
#     else if (cmd == "Three") {
#       Serial.println("Turning LED3 ON");
#       digitalWrite(LED3, HIGH);
#     }
#     else if (cmd == "Four") {
#       Serial.println("Turning LED4 ON");
#       digitalWrite(LED4, HIGH);
#     } 
#     else if (cmd == "Five") {
#       Serial.println("Turning LED5 ON");
#       digitalWrite(LED5, HIGH);
#     } 
#     else {
#       Serial.println("Unknown command!");
#     }
#   }
# }

