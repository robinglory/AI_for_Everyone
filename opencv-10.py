import cv2  # Import OpenCV library for video processing

print(cv2.__version__)  # Print the version of OpenCV being used

# Set the frame width and height for the video capture
width = 800
height = 540

# Set the dimensions of the region of interest (snip) that will move around
snipwidth = 180
snipheight = 90

# Define the center position of the snip (center of the frame)
boxCR = int(height / 2)  # box center row (vertical center)
boxCC = int(width / 2)   # box center column (horizontal center)

# Movement increments for the snip (this controls how fast it moves)
deltaRow = 1  # Row movement step
deltaColumn = 1  # Column movement step

# Initialize the video capture from the default camera, using DirectShow for Windows compatibility
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set the width of the frame
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set the height of the frame
cam.set(cv2.CAP_PROP_FPS, 30)  # Set frames per second for video feed
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set the codec for video capture

while True:
    # Capture a frame from the webcam
    ignore, frame = cam.read()

    # Calculate the top-left and bottom-right coordinates of the snip
    top_left_row = max(0, int(boxCR - snipheight / 2))
    bottom_right_row = min(height, int(boxCR + snipheight / 2))
    top_left_col = max(0, int(boxCC - snipwidth / 2))
    bottom_right_col = min(width, int(boxCC + snipwidth / 2))
    
    # Define the region of interest (ROI) (the snip) based on the center and dimensions
    frameROI = frame[top_left_row:bottom_right_row, top_left_col:bottom_right_col]

    # Convert the entire frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Convert the grayscale frame back to BGR format (to maintain the color structure)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    
    # Place the original color snip back onto the frame
    frame[top_left_row:bottom_right_row, top_left_col:bottom_right_col] = frameROI

    # Draw a green rectangle border around the snip to highlight it
    cv2.rectangle(frame, 
                  (top_left_col, top_left_row), 
                  (bottom_right_col, bottom_right_row), 
                  (0, 255, 0), 2)  # Green border with a thickness of 2

    # Animation logic to move the snip within the frame
    # Reverse direction if snip reaches the boundaries of the frame
    if boxCR - snipheight / 2 <= 0 or boxCR + snipheight / 2 >= height:
        deltaRow = -deltaRow  # Reverse vertical direction
    if boxCC - snipwidth / 2 <= 0 or boxCC + snipwidth / 2 >= width:
        deltaColumn = -deltaColumn  # Reverse horizontal direction

    # Update the position of the snip based on the movement increments
    boxCR = boxCR + deltaRow
    boxCC = boxCC + deltaColumn

    # Show the region of interest (snip) in a separate window
    if frameROI.size > 0:  # Only show if ROI has valid content
        cv2.imshow("My ROI", frameROI)
        cv2.moveWindow("My ROI", width, 0)  # Move the window to a different position

    # Show the modified frame with the moving snip
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)  # Move the webcam window to the top-left corner of the screen

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Break the loop when 'q' is pressed

# Release the camera and close all OpenCV windows
cam.release()



# Explanation of Key Parts:
# Webcam Capture: The video capture initializes with a width of 800 pixels and height of 540 pixels, and the frame rate is set to 30 FPS.
# Region of Interest (ROI): A rectangular snip (frameROI) is selected from the center of the frame, defined by the snipwidth and snipheight values.
# Grayscale Conversion: The entire frame is converted to grayscale, and then it is reconverted to BGR to maintain the original frame format. The region of interest is then inserted back into the frame.
# Snip Movement: The snip moves according to the deltaRow and deltaColumn values. When the snip reaches the edges of the frame, its movement direction is reversed.
# Rectangle for Visibility: A green rectangle is drawn around the snip to make it visually distinct.
# Display Windows: The original snip and the frame with the moving snip are displayed in separate windows.
# Exit: The program exits when the "q" key is pressed.
# This code shows how to extract and manipulate a region of interest (ROI) within a webcam feed and apply simple animation to it. The snip moves around the screen, bouncing off the edges, creating an animation effect.