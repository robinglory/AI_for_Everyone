# Import OpenCV for video and image processing
import cv2
print(cv2.__version__)  # Print the OpenCV version to confirm it's installed correctly

# Set the desired width and height for the video capture frames
width = 320  # Frame width in pixels
height = 180  # Frame height in pixels

# Initialize the video capture from the default camera (index 0)
# The 'cv2.CAP_DSHOW' parameter helps with compatibility on Windows to avoid certain errors
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set the video capture properties
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set the frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set the frame height
cam.set(cv2.CAP_PROP_FPS, 10)  # Set the frames per second (FPS) to 10
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))  # Set the codec to MJPG for better compression

# Start an infinite loop to capture and display video frames in real-time
while True:
    ignore, frame = cam.read()  # Read a frame from the camera; `ignore` is a placeholder for an unused return value

    # Display the current frame in a window titled "my WEBcam"
    cv2.imshow('my WEBcam', frame)

    # Move the window to position (0, 0) on the screen for a fixed viewing position
    cv2.moveWindow('my WEBcam', 0, 0)

    # Wait 1 ms for a key press; if 'q' is pressed, break the loop to end the video capture
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the camera resource when the loop ends
cam.release()
