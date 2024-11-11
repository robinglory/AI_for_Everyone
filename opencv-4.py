# Import the OpenCV library for video and image processing
import cv2
print(cv2.__version__)  # Print the OpenCV version to confirm it's installed correctly

# Set the initial video capture dimensions to 1280x720 pixels
width = 1280
height = 720

# Ask the user to specify the number of rows and columns for the video feed matrix
rows = int(input("Boss, how many rows do you want for this video feed? "))
columns = int(input("Boss, how many columns do you want too? "))

# Initialize the video capture from the default camera (index 0) with CAP_DSHOW for Windows compatibility
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set the capture properties for width, height, and FPS
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set the frame width to the initial value
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set the frame height to the initial value
cam.set(cv2.CAP_PROP_FPS, 10)  # Set frames per second to 10 for smoother playback
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))  # Set MJPG codec for better compression

# Start an infinite loop to capture and display the video frames in a grid format
while True:
    ignore, frame = cam.read()  # Capture a frame from the webcam; `ignore` is a placeholder

    # Resize the frame to fit each cell in the specified grid dimensions
    frame = cv2.resize(frame, (int(width / columns), int(height / rows)))

    # Loop through each row and column to create a video window matrix
    for i in range(0, rows):  # Iterate through each row
        for j in range(0, columns):  # Iterate through each column
            windowName = "Window " + str(i) + "x" + str(j)  # Create a unique window name based on position
            cv2.imshow(windowName, frame)  # Display the resized frame in the current window
            # Move each window to the appropriate position based on row and column
            cv2.moveWindow(windowName, int(width / columns) * j, int(height / rows) * i)

    # Wait for 1 ms; if 'q' is pressed, break the loop and stop the video feed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the camera resource when the loop ends
cam.release()
