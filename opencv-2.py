# This is the homework from Lesson 5, where we work with different color spaces in OpenCV
import cv2  # Import the OpenCV library for computer vision tasks

# Open a connection to the default camera (index 0)
cam = cv2.VideoCapture(0);

# Start an infinite loop to continuously read and display frames from the camera
while True:
    # Capture a frame from the camera
    ignore, frame = cam.read();  # `ignore` is a placeholder for a return value we don't need, `frame` contains the image

    # Convert the captured frame to grayscale
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    # Convert the frame from BGR to HLS_FULL color space
    # HLS_FULL separates hue, lightness, and saturation, often useful for color tracking
    hlsframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL);

    # Convert the frame from BGR to LAB color space
    # LAB separates lightness and color information, making it useful for more consistent color manipulation
    labframe = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB);

    # Display the original frame in a window titled "This is original Color"
    cv2.imshow("This is original Color", frame);

    # Position the original color window at the top-left corner of the screen (0, 0)
    cv2.moveWindow("This is original Color", 0, 0);

    # Display the grayscale frame in a window titled "This is Gray Color"
    cv2.imshow("This is Gray Color", grayframe);

    # Position the grayscale window at (800, 0), to the right of the original color window
    cv2.moveWindow("This is Gray Color", 800, 0);

    # Display the HLS color space frame in a window titled "This is HLS Color"
    cv2.imshow("This is HLS Color", hlsframe);

    # Position the HLS color window at (0, 500), below the original color window
    cv2.moveWindow("This is HLS Color", 0, 500);

    # Display the LAB color space frame in a window titled "This is LAB Color"
    cv2.imshow("This is LAB Color", labframe);

    # Position the LAB color window at (800, 500), to the right of the HLS color window
    cv2.moveWindow("This is LAB Color", 800, 500);

    # Wait for a key press for 1 millisecond; if the 'q' key is pressed, break the loop to end the program
    if cv2.waitKey(1) & 0xff == ord("q"):
        break;

# Release the camera to free up resources when done
cam.release();

# Explanation Summary
# This code:

# Opens a camera feed, captures frames in different color spaces, and displays them in separate windows.
# The cvtColor function converts frames into grayscale, HLS, and LAB formats.
# Windows are positioned for easy viewing, and the q key is used to exit the program.