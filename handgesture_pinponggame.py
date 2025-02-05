import cv2
import mediapipe as mp
import numpy as np
import random

print(cv2.__version__)

# Initialize MediaPipe Hands
class mpHands:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def Marks(self, frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks:
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x * width), int(landMark.y * height)))
                myHands.append(myHand)
        return myHands


# Window settings
width, height = 1280, 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Initialize Paddle
paddleWidth, paddleHeight = 125, 25
paddleColor = (0, 255, 0)

# Initialize Ball
ballRadius = 25
ballColor = (255, 0, 255)
ballX, ballY = width // 2, height // 2
ballSpeedX, ballSpeedY = random.choice([-6, 6]), 6  # Random start direction

# Create Hand Tracker
findHands = mpHands(2)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.resize(frame, (width, height))
    
    # Get hand data
    handData = findHands.Marks(frame)

    # Move paddle with hand (using index finger tip - hand[8])
    paddleX = width // 2  # Default paddle position
    if handData:
        paddleX = handData[0][8][0]  # Track x-coordinate of index finger tip

    # Draw paddle
    paddleLeft = max(0, paddleX - paddleWidth // 2)  # Prevent going out of bounds
    paddleRight = min(width, paddleX + paddleWidth // 2)
    cv2.rectangle(frame, (paddleLeft, height - paddleHeight), (paddleRight, height), paddleColor, -1)

    # Move ball
    ballX += ballSpeedX
    ballY += ballSpeedY

    # Ball collision with walls (left & right)
    if ballX - ballRadius <= 0 or ballX + ballRadius >= width:
        ballSpeedX = -ballSpeedX

    # Ball collision with top
    if ballY - ballRadius <= 0:
        ballSpeedY = -ballSpeedY

    # Ball collision with paddle
    if (ballY + ballRadius >= height - paddleHeight) and (paddleLeft <= ballX <= paddleRight):
        ballSpeedY = -ballSpeedY

    # Ball out of bounds (missed paddle)
    if ballY + ballRadius > height:
        ballX, ballY = width // 2, height // 2  # Reset ball position
        ballSpeedX, ballSpeedY = random.choice([-6, 6]), 6  # Restart ball

    # Draw ball
    cv2.circle(frame, (ballX, ballY), ballRadius, ballColor, -1)

    # Show frame
    cv2.imshow('Pong Game', frame)
    cv2.moveWindow('Pong Game', 0, 0)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
cam.release()
cv2.destroyAllWindows()
