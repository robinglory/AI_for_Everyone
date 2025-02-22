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
            for hand in results.multi_handedness:
                handType = hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landmark in handLandMarks.landmark:
                    myHand.append((int(landmark.x * width), int(landmark.y * height)))
                myHands.append(myHand)
        return myHands, handsType

def findDistances(handData):
    distMatrix = np.zeros([len(handData), len(handData)], dtype='float')
    for row in range(0, len(handData)):
        for column in range(0, len(handData)):
            distMatrix[row][column] = ((handData[row][0]-handData[column][0])**2 + (handData[row][1]-handData[column][1]) ** 2)**(1./2.)
    return distMatrix

def findError(gestureMatrix, unknownMatrix, keyPoints):
    error = 0
    for row in keyPoints:
        for column in keyPoints:
            error = error + abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    return error

def findGesture(unknownGesture, knownGestures, keyPoints, gestNames, tol):
    errorArray = []
    for i in range(0, len(gestNames), 1):
        error = findError(knownGestures[i], unknownGesture, keyPoints)
        errorArray.append(error)
    errorMin = errorArray[0]
    minIndex = 0
    for i in range(0, len(errorArray), 1):
        if errorArray[i] < errorMin:
            errorMin = errorArray[i]
            minIndex = i
    if errorMin < tol:
        gesture = gestNames[minIndex]
    if errorMin > tol:
        gesture = "Unknown Gesture!"
    return gesture, errorMin

# Initialize camera properties
width = 1280
height = 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

findHands = mpHands()

keyPoints = [0, 4, 5, 9, 13, 17, 8, 12, 16, 20]

## Time
time.sleep(2)
train = True
tol = 1500
knownGestures = []
numGest = int(input("How Many Gestures Do You want to Train? "))
gestNames = []
trainCnt = 0
for i in range(0, numGest):
    prompt = "Name of the Gesture #" + str(i+1) + ": "
    name = input(prompt)
    gestNames.append(name)
print("Gestures to Train:", gestNames)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
        break

    hands_marks, handsType = findHands.Marks(frame, width, height)
    if train == True:
        if hands_marks != []:
            print("Please Show Gesture", gestNames[trainCnt], ": Press T key when ready")
            if cv2.waitKey(1) & 0xff == ord('t'):
                knownGesture = findDistances(hands_marks[0])
                knownGestures.append(knownGesture)
                trainCnt = trainCnt + 1
                if trainCnt == numGest:
                    train = False
                    print("Training Complete! Starting Gesture Recognition...")

    if train == False:
        if hands_marks != []:
            unknownGesture = findDistances(hands_marks[0])
            myGesture, errorMin = findGesture(unknownGesture, knownGestures, keyPoints, gestNames, tol)
            # Display Gesture and Confidence
            cv2.putText(frame, f"Gesture: {myGesture}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Confidence: {int(tol - errorMin)}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Draw Hand Landmarks and Bounding Box
    for hand, handType in zip(hands_marks, handsType):
        if handType == "Right":
            handColor = (255, 0, 0)
        if handType == "Left":
            handColor = (0, 0, 255)
        for point in hand:
            cv2.circle(frame, point, 10, handColor, cv2.FILLED)
        # Draw Bounding Box
        x_coords = [point[0] for point in hand]
        y_coords = [point[1] for point in hand]
        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), handColor, 2)

    # Display Instructions
    if train:
        cv2.putText(frame, f"Training Mode: Show {gestNames[trainCnt]}", (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        cv2.putText(frame, "Press Q to Quit", (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display Title
    cv2.putText(frame, "Sign Language Interpreter", (width // 2 - 200, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (100, 100, 255), 2)

    # Show Frame
    cv2.imshow('Sign Language Interpreter', frame)
    cv2.moveWindow('Sign Language Interpreter', 0, 0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()