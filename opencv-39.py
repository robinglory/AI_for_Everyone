import cv2
import mediapipe as mp

print(cv2.__version__)

# Set up the webcam
width, height = 1280, 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Initialize MediaPipe FaceMesh
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=3,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mpDraw = mp.solutions.drawing_utils

font = cv2.FONT_HERSHEY_DUPLEX
fontSize = 0.3
fontColor = (0, 255, 255)
fontThick = 1

while True:
    success, frame = cam.read()
    if not success:
        print("Failed to capture frame")
        continue

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(frameRGB)

    if results.multi_face_landmarks:
        for faceLandmarks in results.multi_face_landmarks:
            mpDraw.draw_landmarks(
                frame,
                faceLandmarks,
                mpFaceMesh.FACEMESH_TESSELATION,  # Ensure landmarks are drawn
                mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                mpDraw.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1),
                # mp.solutions.face_mesh.FACE_CONNECTION
            )
            index = 0
            for lm in faceLandmarks.landmark:
                cv2.putText(frame,str(index),(int(width*lm.x),int(height*lm.y)),font,fontSize,fontColor,fontThick)
                index = index +1
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
