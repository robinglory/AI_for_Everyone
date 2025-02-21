import cv2
import mediapipe as mp

# Initialize OpenCV and MediaPipe FaceMesh
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=3,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open the webcam
width, height = 1280, 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Change to 'XVID' if needed

while True:
    success, frame = cam.read()
    if not success:
        print("Failed to read frame from camera")
        continue  # Skip this frame if the camera is not working

    # Convert the frame to RGB (MediaPipe uses RGB format)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process frame with FaceMesh
    results = faceMesh.process(frameRGB)

    if results.multi_face_landmarks:
        for faceLandmarks in results.multi_face_landmarks:
            # Draw landmarks on the face
            mpDraw.draw_landmarks(
                frame,  # Ensure drawing is done on the BGR frame
                faceLandmarks,
                mpFaceMesh.FACEMESH_TESSELATION,  # Use tesselation for better landmark visibility
                mpDraw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),  # Dots color
                mpDraw.DrawingSpec(color=(0,0,255), thickness=1, circle_radius=1)   # Lines color
            )

            # Debugging: Print landmark count
            print(f"Detected {len(faceLandmarks.landmark)} landmarks")

    # Display the frame
    cv2.imshow('Face Mesh', frame)
    cv2.moveWindow('Face Mesh', 0, 0)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
