import cv2
import time

print(cv2.__version__)

# Set the video capture properties
width = 640
height = 360
myRadius = 30
myColor = (0, 0, 0)
myThick = 2
fontH = 2
fontT = 2
myText = 'Glory is Boss'
myFont = cv2.FONT_HERSHEY_DUPLEX
upperLeft = (250, 140)
lowerRight = (390, 220)
lineW = 4

# Initialize video capture
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Initialize variables to calculate FPS
prev_time = 0
fps = 0
fps_filter = 30;
while True:
    # Read frame from webcam
    ignore, frame = cam.read()
    
    # Get current time and calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    fps_filter= fps_filter*.9+fps*.1;
    # Format FPS to be displayed
    fps_text = f"{int(fps_filter)} Fps"
    
    # Add the rectangle and text box for FPS in the upper left corner
    cv2.rectangle(frame, (10, 10), (150, 50), (255, 255, 255), -1)  # White box for FPS
    cv2.putText(frame, fps_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)  # FPS text in black
    
    # Draw the other elements
    # frame[140:220, 250:390] = (255, 0, 0)
    # cv2.rectangle(frame, upperLeft, lowerRight, (0, 255, 0), lineW)
    # cv2.circle(frame, (int(width / 2), int(height / 2)), myRadius, myColor, myThick)
    # cv2.putText(frame, myText, (100, 90), myFont, fontH, (0, 0, 255), fontT)
    
    # Display the frame
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    
    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
cam.release()
cv2.destroyAllWindows()
