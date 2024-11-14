# Import the OpenCV library
import cv2

# Print the OpenCV version being used, useful for compatibility reference
print(cv2.__version__)

# Set the desired width and height of the webcam capture window
width = 900
height = 600

# Initialize the event variable to store mouse events
evt = 0

# Define the mouseClick function to handle mouse events on the webcam window
def mouseClick(event, xPos, yPos, flags, params):
    global pnt1, pnt2, evt  # Declare global variables to store points and event status

    # Check if the left mouse button is pressed down
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)  # Output the event type (left button down)
        pnt1 = (xPos, yPos)  # Store the initial point (start of rectangle)
        evt = event  # Update event state

    # Check if the left mouse button is released
    if event == cv2.EVENT_LBUTTONUP:
        print(event)  # Output the event type (left button up)
        pnt2 = (xPos, yPos)  # Store the endpoint (end of rectangle)
        evt = event  # Update event state

    # Check if the right mouse button is released
    if event == cv2.EVENT_RBUTTONUP:
        print(event)  # Output the event type (right button up)
        evt = event  # Update event state to indicate right button release

# Initialize the webcam feed with DirectShow compatibility for Windows
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set webcam frame width, height, and frames per second
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set codec to MJPG for video capture

# Create a named window "my WEBcam" for the webcam display
cv2.namedWindow('my WEBcam')

# Set up the mouse callback for "my WEBcam" window, linking it to the mouseClick function
cv2.setMouseCallback("my WEBcam", mouseClick)

# Main loop to continuously capture frames from the webcam
while True:
    # Capture a frame from the webcam
    ignore, frame = cam.read()

    # If the left mouse button was released, draw a rectangle on the frame
    if evt == 4:  # Event 4 corresponds to `cv2.EVENT_LBUTTONUP`
        # Draw a rectangle from pnt1 to pnt2 with color and thickness
        cv2.rectangle(frame, pnt1, pnt2, (255, 0, 100), 2)
        
        # Extract the Region of Interest (ROI) based on the defined rectangle
        ROI = frame[pnt1[1]:pnt2[1], pnt1[0]:pnt2[0]]

        # Display the extracted ROI in a separate window named "ROI"
        cv2.imshow("ROI", ROI)
        
        # Move the "ROI" window to a position on the screen offset from the main window
        cv2.moveWindow("ROI", int(width * 1.1), 0)

    # If the right mouse button was released, close the ROI window
    if evt == 5:  # Event 5 corresponds to `cv2.EVENT_RBUTTONUP`
        cv2.destroyWindow("ROI")  # Close the "ROI" window
        evt = 0  # Reset the event status to avoid repeated closure

    # Display the webcam frame with the optional rectangle overlay
    cv2.imshow('my WEBcam', frame)
    
    # Move the webcam window to the top-left corner of the screen
    cv2.moveWindow('my WEBcam', 0, 0)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the webcam and close all OpenCV windows upon program termination
cam.release()
cv2.destroyAllWindows()
