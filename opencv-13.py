# Import OpenCV library for computer vision functions
import cv2

# Print the OpenCV version being used, helpful for debugging and compatibility
print(cv2.__version__)

# Callback function for the x-position trackbar
def myCallBack(val):
    global xPos  # Use global variable to store x-position
    print("X position: ", val)  # Print the updated x-position value
    xPos = val  # Update xPos with the value from the trackbar

# Callback function for the y-position trackbar
def myCallBack1(val):
    global yPos  # Use global variable to store y-position
    print("Y position: ", val)  # Print the updated y-position value
    yPos = val  # Update yPos with the value from the trackbar

# Callback function for the radius trackbar
def myCallBack2(val):
    global myRad  # Use global variable to store radius
    print("Radius:", myRad)  # Print the updated radius value
    myRad = val  # Update myRad with the value from the trackbar

# Set initial webcam resolution
width = 1920
height = 1080

# Set the size for the trackbar control window
width1 = 400
height1 = 150

# Initialize radius and position of the circle
myRad = 25  # Starting radius of the circle
xPos = int(width / 2)  # Initial x-position in the center of the frame width
yPos = int(height / 2)  # Initial y-position in the center of the frame height

# Initialize webcam capture with DirectShow compatibility for Windows
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set the width, height, and frame rate for the webcam feed
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)

# Set codec format to MJPG for video capture
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Create a window for the trackbar controls and set its size and position
cv2.namedWindow("MyTrackbar")
cv2.resizeWindow("MyTrackbar", width1, height1)
cv2.moveWindow("MyTrackbar", 1000, 0)  # Position the trackbar window on screen

# Create trackbars for x-position, y-position, and radius in the "MyTrackbar" window
cv2.createTrackbar("xPos", "MyTrackbar", xPos, 1920, myCallBack)  # Trackbar for x-position
cv2.createTrackbar("yPos", "MyTrackbar", yPos, 1920, myCallBack1)  # Trackbar for y-position
cv2.createTrackbar("radius", "MyTrackbar", myRad, int(height / 2), myCallBack2)  # Trackbar for radius

# Main loop to continuously capture frames from the webcam
while True:
    # Capture a frame from the webcam
    ignore, frame = cam.read()

    # Draw a circle on the frame using the position and radius from the trackbars
    cv2.circle(frame, (xPos, yPos), myRad, (255, 0, 22), 3)

    # Display the webcam frame with the circle overlay
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)  # Position the webcam window at the top-left corner

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the webcam and close all OpenCV windows upon program termination
cam.release()
