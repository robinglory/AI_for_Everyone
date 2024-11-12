import cv2  # Import the OpenCV library to work with images and video

# Uncomment the following line to print the OpenCV version in use
# print(cv2.__version__);

# Open a connection to the default camera (usually the first one, index 0)
cam = cv2.VideoCapture(0);

# Start an infinite loop to read and process video frames
while True:
    # Capture a frame from the camera
    ignore, frame = cam.read();  # `ignore` is used to ignore the return value as we only need `frame`

    # Convert the captured frame from BGR to HLS_FULL color space
    # HLS is an alternative to RGB with separate channels for hue, lightness, and saturation
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL);

    # Display the converted frame in a window titled "My LaptopCam"
    cv2.imshow("My LaptopCam", grayframe);

    # Move the "My LaptopCam" window to position (500, 200) on the screen
    cv2.moveWindow("My LaptopCam", 500, 200);

    # Wait for a key press event for 1 millisecond, and check if it is the 'q' key
    # `0xff` is used to mask the bits of `waitKey` output to match ASCII for key checking
    if cv2.waitKey(1) & 0xff == ord("q"):
        break  # If 'q' is pressed, exit the loop and end the video feed

# Release the camera when done, freeing up system resources
cam.release()


# This is the homework from Lesson 5
# import cv2;

# cam = cv2.VideoCapture(0);  # Open the default camera

# Start another infinite loop to display different color space conversions
# while True:
    # Capture a frame from the camera
#     ignore, frame = cam.read();  # Again, only `frame` is used, `ignore` is a dummy variable

    # Convert the frame to grayscale
#     grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    # Convert the frame to HLS_FULL color space
#     hlsframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL);

    # Convert the frame to LAB color space, which separates lightness from color information
#     labframe = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB);

    # Display the original frame in a window titled "This is original Color"
#     cv2.imshow("This is original Color", frame);

    # Position the original color window at the top-left corner (0, 0)
#     cv2.moveWindow("This is original Color", 0, 0);

    # Display the grayscale frame in a window titled "This is Gray Color"
#     cv2.imshow("This is Gray Color", grayframe);

    # Position the grayscale window at (800, 0), to the right of the original color window
#     cv2.moveWindow("This is Gray Color", 800, 0);

    # Display the HLS_FULL frame in a window titled "This is HLS Color"
#     cv2.imshow("This is HLS Color", hlsframe);

    # Position the HLS window at (0, 500), below the original color window
#     cv2.moveWindow("This is HLS Color", 0, 500);

    # Display the LAB color frame in a window titled "This is LAB Color"
#     cv2.imshow("This is LAB Color", labframe);

    # Position the LAB window at (800, 500), to the right of the HLS window
#     cv2.moveWindow("This is LAB Color", 800, 500);

    # Wait for a key press event for 1 millisecond, and check if it is the 'q' key
#     if cv2.waitKey(1) & 0xff == ord("q"):
#         break;  # Exit the loop if 'q' is pressed

# Release the camera when done to free up resources
# cam.release();


# Explanation Summary
# The main code opens the camera and displays video in different color spaces:
# First, in the HLS_FULL color space, with an option to exit by pressing "q."
# The second section (homework) demonstrates converting the live video feed into grayscale, HLS, and LAB color spaces.
# Windows are created for each color space and moved to specific screen coordinates for organization.