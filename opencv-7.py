import cv2  # Import OpenCV for video processing
print(cv2.__version__)  # Print the OpenCV version

# Define constants for video frame dimensions, shapes, colors, and text
width = 640  # Frame width
height = 360  # Frame height
myRadius = 30  # Radius for the circle to be drawn
myColor = (0, 0, 0)  # Color of the circle in BGR (black)
myThick = 2  # Thickness of the circle outline
fontH = 2  # Font scale for the text
fontT = 2  # Thickness of the text
myText = 'Glory is Boss'  # Text to be displayed on the frame
myFont = cv2.FONT_HERSHEY_DUPLEX  # Font type for the text
upperLeft = (250, 140)  # Upper-left corner coordinates for the rectangle
lowerRight = (390, 220)  # Lower-right corner coordinates for the rectangle
lineW = 4  # Thickness of the rectangle outline

# Initialize the video capture from the default camera (0) with DirectShow for Windows compatibility
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set video capture properties: resolution, frames per second, and codec
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set the frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set the frame height
cam.set(cv2.CAP_PROP_FPS, 30)  # Set frames per second
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set video codec to MJPG

# Main loop to capture and process video frames
while True:
    ignore, frame = cam.read()  # Read a frame from the camera (ignore the first return value)

    # Set a region of the frame (rectangle area) to blue by directly assigning pixel values
    frame[140:220, 250:390] = (255, 0, 0)  # Fill a specific area with blue (BGR format)

    # Draw a green rectangle around the defined area with a specific thickness
    cv2.rectangle(frame, upperLeft, lowerRight, (0, 255, 0), lineW)

    # Draw a black circle in the center of the frame with specified radius and thickness
    cv2.circle(frame, (int(width / 2), int(height / 2)), myRadius, myColor, myThick)

    # Place text on the frame at the specified location, with color, font type, and thickness
    cv2.putText(frame, myText, (100, 90), myFont, fontH, (0, 0, 255), fontT)

    # Display the modified frame in a window titled 'my WEBcam'
    cv2.imshow('my WEBcam', frame)

    # Move the window to the top-left corner of the screen
    cv2.moveWindow('my WEBcam', 0, 0)

    # Check for 'q' key press to exit the loop and close the camera
    if cv2.waitKey(1) & 0xff == ord('q'):
        break  # Exit the loop if 'q' is pressed

# Release the camera resource after exiting the loop
cam.release()


# Summary of the Code
# This code opens a live camera feed and applies a series of visual modifications to each frame.
# It adds a blue rectangle area within the frame, a green rectangle border, a black circle centered in the frame, and a red text label.
# The camera feed with these modifications is displayed in real time until the user presses the 'q' key to stop the feed and close the camera.