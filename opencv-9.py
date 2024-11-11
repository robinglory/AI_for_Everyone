import cv2  # Import OpenCV library for video processing
print(cv2.__version__)  # Print the version of OpenCV being used

# Set the frame width and height for the video capture
width = 640
height = 360

# Initialize the video capture from the webcam, using DirectShow for Windows compatibility
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set the width of the frame
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set the height of the frame
cam.set(cv2.CAP_PROP_FPS, 30)  # Set the FPS (frames per second) for the video feed
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set the codec for video capture

while True:
    # Capture a frame from the webcam
    ignore, frame = cam.read()

    # Define a Region of Interest (ROI) in the captured frame (100 to 310 for rows, 150 to 490 for columns)
    frameROI = frame[100:310, 150:490]
    
    # Convert the ROI to grayscale
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)

    # Reconvert the grayscale ROI back to BGR (to maintain the original frame format)
    frameROIBGR = cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR)
    
    # Replace the original ROI in the frame with the new BGR image (after grayscale conversion and reconversion)
    frame[100:310, 150:490] = frameROIBGR

    # Display the original ROI (grayscale frame) in a separate window
    cv2.imshow("This is my frame region of interest", frameROI)
    cv2.moveWindow("This is my frame region of interest", 650, 0)  # Move the window to a specific position

    # Display the grayscale ROI in a separate window
    cv2.imshow("This is my GRAY region of interest", frameROIGray)
    cv2.moveWindow("This is my GRAY region of interest", 0, 500)  # Move the window to a specific position

    # Display the reconverted BGR ROI in a separate window
    cv2.imshow("This is reconverting the gray frame to BGR region of interest", frameROIBGR)
    cv2.moveWindow("This is reconverting the gray frame to BGR region of interest", 650, 500)  # Move the window

    # Display the entire frame (with the modified ROI) in the main webcam window
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)  # Move the main webcam window to the top-left corner

    # Wait for a key press. If 'q' is pressed, break the loop and close the video feed.
    if cv2.waitKey(1) & 0xff == ord('q'):
        break  # Exit the loop when 'q' is pressed

# Release the camera and close all OpenCV windows
cam.release()


# Explanation:
# Video Capture: Captures video frames from the webcam and sets properties like frame size and FPS.
# Region of Interest (ROI): The section of the frame between rows 100 to 310 and columns 150 to 490 is selected as the ROI. This region is further processed to demonstrate how you can manipulate specific sections of the frame.
# Gray Conversion: The ROI is converted to grayscale using cv2.cvtColor(). Afterward, it is converted back to BGR (color) format to fit the original frame's color scheme.
# Display Windows: Multiple cv2.imshow() windows are created to display the original ROI, grayscale ROI, and the reconverted BGR ROI. Each window is positioned using cv2.moveWindow().
# Exit: The loop runs continuously until the 'q' key is pressed, which stops the webcam feed and releases the camera.
# The program effectively demonstrates how to work with specific regions of a video frame and apply color space conversions in OpenCV.