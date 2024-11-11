import cv2  # Import OpenCV library for video processing
import time  # Import time module to measure frame rate (FPS)

print(cv2.__version__)  # Print the OpenCV version

# Set the video capture properties
width = 640  # Set the frame width
height = 360  # Set the frame height
myRadius = 30  # Circle radius for visual elements
myColor = (0, 0, 0)  # Color of circle (black)
myThick = 2  # Thickness of circle border
fontH = 2  # Font scale for text
fontT = 2  # Text thickness
myText = 'Glory is Boss'  # Text to display
myFont = cv2.FONT_HERSHEY_DUPLEX  # Font type for text
upperLeft = (250, 140)  # Upper-left corner of a rectangle
lowerRight = (390, 220)  # Lower-right corner of the rectangle
lineW = 4  # Line thickness for the rectangle

# Initialize video capture from default camera, using DirectShow for Windows compatibility
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set frame height
cam.set(cv2.CAP_PROP_FPS, 30)  # Set frames per second
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set video codec to MJPG

# Variables for calculating frames per second (FPS)
prev_time = 0  # Store time of previous frame
fps = 0  # Variable to store current FPS
fps_filter = 30  # Initialize filtered FPS for smoother display

# Main loop to capture and display frames
while True:
    # Capture a frame from the webcam
    ignore, frame = cam.read()
    
    # Calculate FPS by measuring the time difference between frames
    current_time = time.time()  # Get the current time
    fps = 1 / (current_time - prev_time)  # FPS = 1 / time taken for one frame
    prev_time = current_time  # Update the previous time for the next loop

    # Apply a simple low-pass filter to smooth the FPS value over time
    fps_filter = fps_filter * 0.9 + fps * 0.1  # Weighted average for smoothing

    # Prepare the FPS text to display
    fps_text = f"{int(fps_filter)} Fps"  # Convert filtered FPS to integer for display

    # Draw a white rectangle to serve as the FPS background in the upper-left corner
    cv2.rectangle(frame, (10, 10), (150, 50), (255, 255, 255), -1)  # White-filled rectangle
    # Place the FPS text over the rectangle
    cv2.putText(frame, fps_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)  # Black text for FPS
    
    # Additional drawing elements can be added here (commented out for now)
    # frame[140:220, 250:390] = (255, 0, 0)  # Fill area with blue
    # cv2.rectangle(frame, upperLeft, lowerRight, (0, 255, 0), lineW)  # Draw green rectangle
    # cv2.circle(frame, (int(width / 2), int(height / 2)), myRadius, myColor, myThick)  # Draw black circle
    # cv2.putText(frame, myText, (100, 90), myFont, fontH, (0, 0, 255), fontT)  # Display custom text
    
    # Show the frame with FPS in a window titled 'my WEBcam'
    cv2.imshow('my WEBcam', frame)
    # Move the window to the top-left corner of the screen
    cv2.moveWindow('my WEBcam', 0, 0)
    
    # Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Break the loop if 'q' is pressed

# Release the camera and close all OpenCV windows after exiting the loop
cam.release()
cv2.destroyAllWindows()

# Video Capture Setup:

# Initializes the webcam and sets the frame width, height, FPS, and video codec (MJPG). MJPG provides a good balance of compression and image quality for live webcam feeds.
# FPS Calculation:

# prev_time and current_time are used to measure the time taken to capture and display each frame. The reciprocal of this time difference gives the FPS.
# A simple low-pass filter (fps_filter) smooths the FPS value over time, making it more readable by dampening fluctuations.
# Drawing Elements on the Frame:

# A white rectangle is drawn in the top-left corner to act as a background for the FPS counter.
# cv2.putText overlays the FPS value on top of the rectangle.
# Additional elements, such as text, rectangles, and circles, are drawn on the frame, though these are commented out in this code block.
# Display Loop:

# The frame is displayed in a window titled my WEBcam.
# The window is positioned in the top-left corner of the screen.
# The loop continues until the user presses the "q" key, at which point the program exits gracefully by releasing the camera and closing the display window.
# Smooth FPS Calculation:

# By combining the current FPS with the previous filtered FPS value at a 0.9:0.1 ratio, this line smooths sudden jumps in FPS values for a more stable display.