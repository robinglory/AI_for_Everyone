# Import necessary libraries: OpenCV for video capture and manipulation, and NumPy for numerical operations
import cv2
import numpy as np

# Print OpenCV version, helpful for debugging and ensuring compatibility
print(cv2.__version__)

# Set initial configurations
width = 1000  # Width of the webcam window
height = 400  # Height of the webcam window
evt = 0  # Event variable to track mouse events
xVal = 0  # X-coordinate for color picking
yVal = 0  # Y-coordinate for color picking

# Define the mouse callback function for handling mouse events
def mouseClick(event, xPos, yPos, flag, params):
    global evt, xVal, yVal  # Use global variables to store the event type and position
    
    # Check if the left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)  # Print the event code (1 for left button down)
        evt = event  # Set event type to left button down
        xVal = xPos  # Store the X-coordinate of the click
        yVal = yPos  # Store the Y-coordinate of the click

    # Check if the right mouse button is released
    if event == cv2.EVENT_RBUTTONUP:
        evt = event  # Set event type to right button up
        print(event)  # Print the event code (5 for right button up)

# Initialize webcam video capture
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow for Windows
# Set camera properties such as frame width, height, FPS, and format
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set the codec format

# Create a window for displaying the webcam feed
cv2.namedWindow("my WEBcam")
# Assign the mouse callback function to the webcam window
cv2.setMouseCallback("my WEBcam", mouseClick)

# Main loop to continuously capture frames from the webcam
while True:
    # Capture a frame from the webcam
    ignore, frame = cam.read()
    
    # Check if left mouse button down event has occurred
    if evt == 1:
        # Create a new image (250x250 pixels) for displaying the selected color
        x = np.zeros([250, 250, 3], dtype=np.uint8)
        clr = frame[yVal][xVal]  # Retrieve the color of the pixel at the clicked position
        print(clr)  # Print the BGR color values
        
        # Set all pixels in the new image to the selected color
        x[:, :] = clr
        # Display the BGR color values as text on the color display window
        cv2.putText(x, str(clr), (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        # Label the channels as "BLUE, GREEN, RED" for clarity
        cv2.putText(x, "BLUE, GREEN, RED", (0, 90), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        
        # Show the color display window with the selected color
        cv2.imshow("Color Picker", x)
        # Position the color display window to the right of the main webcam window
        cv2.moveWindow("Color Picker", width, 0)
        
        # Reset the event variable to prevent repeated color picking on the same frame
        evt = 0

    # Display the webcam feed
    cv2.imshow('my WEBcam', frame)
    # Position the main webcam window at the top-left of the screen
    cv2.moveWindow('my WEBcam', 0, 0)
    
    # Exit loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the webcam resource and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
