# Import the OpenCV library for computer vision functions
import cv2

# Print the version of OpenCV in use, helpful for debugging and compatibility
print(cv2.__version__)

# Initial Setup
width = 640  # Set initial width of the webcam frame
height = int(width * 9 / 16)  # Set initial height to maintain a 16:9 aspect ratio
positionX = 0  # Initial X position of the display window
positionY = 0  # Initial Y position of the display window
resize_factor = 640  # Initial resize factor to match starting width

# Callback function for resizing the window
def resize_callback(val):
    global width, height  # Access the global width and height variables
    # Update the width and height based on the resize factor (16:9 ratio)
    width = val
    height = int(val * 9 / 16)  # Calculate new height to maintain the aspect ratio
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Update the camera's frame width
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Update the camera's frame height
    print(f"Resize Width: {width}, Height: {height}")  # Print the new dimensions for debugging

# Callback function for moving the window along the X-axis
def move_x_callback(val):
    global positionX  # Access the global X position variable
    positionX = val  # Update the X position
    print("X Position:", positionX)  # Print the new X position for debugging

# Callback function for moving the window along the Y-axis
def move_y_callback(val):
    global positionY  # Access the global Y position variable
    positionY = val  # Update the Y position
    print("Y Position:", positionY)  # Print the new Y position for debugging

# Webcam Setup
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Open the webcam with DirectShow for Windows
# Set initial frame dimensions for the camera
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)  # Set frames per second to 30
# Set the codec format for video capture to MJPG
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Trackbar Window for controlling settings
cv2.namedWindow("Settings")  # Create a window named "Settings" for the trackbars
cv2.resizeWindow("Settings", 400, 200)  # Set the size of the trackbar window

# Create trackbars in the "Settings" window
cv2.createTrackbar("Resize", "Settings", resize_factor, 1920, resize_callback)  # Trackbar to adjust width up to 1920
cv2.createTrackbar("Move X", "Settings", positionX, 1920, move_x_callback)  # Trackbar for X-axis window position
cv2.createTrackbar("Move Y", "Settings", positionY, 1080, move_y_callback)  # Trackbar for Y-axis window position

# Main loop for capturing and displaying frames
while True:
    # Capture a frame from the webcam
    ignore, frame = cam.read()

    # Display the frame and apply the current window position and size
    cv2.imshow("Webcam", frame)  # Show the webcam feed in a window named "Webcam"
    cv2.moveWindow("Webcam", positionX, positionY)  # Set the window's position using trackbar values

    # Break the loop and close program when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows after exiting the loop
cam.release()
cv2.destroyAllWindows()
