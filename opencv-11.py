# Import OpenCV library for computer vision and image processing tasks
import cv2

# Check and print the current OpenCV version for compatibility reference
print(cv2.__version__)

# Set the width and height for the webcam resolution
width = 1280
height = 720

# Variables to store the event state and position for drawing a circle
draw_circle = False  # This flag indicates whether a circle should be drawn
pnt = (0, 0)  # Stores the coordinates for the circle's center

# Define the mouseClick function to handle mouse events on the webcam window
def mouseClick(event, xPos, yPos, flags, params):
    global draw_circle, pnt  # Access global variables within the function

    # If a double left-click is detected, store the position and set the draw flag
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Mouse click event was:", event)  # Output the event type (double-click)
        print("Position:", xPos, yPos)  # Output the coordinates of the click
        pnt = (xPos, yPos)  # Save the position as the center for the circle
        draw_circle = True  # Enable the draw flag to indicate circle should be drawn

    # If the right mouse button is released, record the event type and position
    if event == cv2.EVENT_RBUTTONUP:
        print("Right Button Up: ", event)  # Output the event type (right button up)
        pnt = (xPos, yPos)  # Save the position as the center for the circle
        evt = event  # Store the event (this line currently has no further effect)

# Initialize the webcam feed from the default camera using DirectShow for Windows compatibility
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Configure the webcam resolution and frame rate
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set frame height
cam.set(cv2.CAP_PROP_FPS, 30)  # Set frames per second
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set codec for video capture

# Create a window named "my WEBcam" for displaying the webcam feed
cv2.namedWindow("my WEBcam")

# Set the mouse callback for "my WEBcam" window to the mouseClick function
cv2.setMouseCallback("my WEBcam", mouseClick)

# Main loop to continuously capture frames from the webcam
while True:
    # Capture a single frame from the webcam
    ignore, frame = cam.read()
    
    # If the draw_circle flag is set, draw a blue circle on the frame
    if draw_circle:
        cv2.circle(frame, pnt, 30, (255, 0, 0), 3)  # Draw circle at `pnt` with radius 30 and color blue (BGR format)

    # Display the modified frame in the "my WEBcam" window
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow("my WEBcam", 0, 0)  # Move the window to the top-left corner of the screen

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam resources and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
