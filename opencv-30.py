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
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks:
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landmark in handLandMarks.landmark:
                    myHand.append((int(landmark.x * width), int(landmark.y * height)))
                myHands.append(myHand)
        return myHands

# Initialize camera properties
width = 1280
height = 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

findHands = mpHands()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
        break

    hands_marks = findHands.Marks(frame, width, height)
    for hand in hands_marks:
        for point in hand:
            cv2.circle(frame, point, 10, (255, 0, 255), cv2.FILLED)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
