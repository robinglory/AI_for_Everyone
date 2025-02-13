import cv2
import mediapipe as mp

print(cv2.__version__)
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

# pose = mp.solutions.pose.Pose(False,False,True,0.5,0.5)  Wrong way or old way of identifying the pose\
pose = mp.solutions.pose.Pose(
    static_image_mode=False, 
    model_complexity=1,  # 0, 1, or 2 (higher means more accurate but slower)
    smooth_landmarks=True, 
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5
)
mpDraw = mp.solutions.drawing_utils
circleRaduis = 10
circleColor = (0,0,255)
circleThickness = 5
eyeColor = (255,0,0)
eyeRadius = 10
eyeThickness = -1

while True:
    ignore,  frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    # print(results)
    landMarks = []
    if results.pose_landmarks != None:
        # mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        # print(results.pose_landmarks)
        for lm in results.pose_landmarks.landmark:
            # print((landmark.x,landmark.y))
            landMarks.append((int(lm.x*width),int(lm.y*height)))

        cv2.circle(frame,landMarks[0],circleRaduis,circleColor,circleThickness)
        cv2.circle(frame,landMarks[2],eyeRadius,eyeColor,eyeThickness)
        cv2.circle(frame,landMarks[5],eyeRadius,eyeColor,eyeThickness)

        # print(landMarks)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()