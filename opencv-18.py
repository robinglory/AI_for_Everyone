#this is the homework assignment and in this assignment we are going to capture both red and yellow color from the HSV

# AI for Everyone Lesson 13: Tracking an object based on color in OpenCV

import cv2
import numpy as np

# Print the OpenCV version for reference
print(cv2.__version__)

# Define the dimensions for the webcam frame
width = 640
height = 360

# Trackbar callback functions to update HSV range values dynamically

def onTrack1(val):
    global hueLow
    hueLow = val
    print("Hue Low", hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh = val
    print("Hue High", hueHigh)

## Changes for red
def onTrack7(val):
    global hueLow2
    hueLow2 = val
    print("Hue Low 2", hueLow2)

def onTrack8(val):
    global hueHigh2
    hueHigh2 = val
    print("Hue High 2", hueHigh2)

def onTrack3(val):
    global satLow
    satLow = val
    print("Saturation Low", satLow)

def onTrack4(val):
    global satHigh
    satHigh = val
    print("Saturation High", satHigh)

def onTrack5(val):
    global valLow
    valLow = val
    print("Value Low", valLow)

def onTrack6(val):
    global valHigh
    valHigh = val
    print("Value High", valHigh)


# Initialize webcam capture with settings
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Set codec for capturing video

# Create a window for trackbars to adjust HSV ranges
cv2.namedWindow("my Tracker")
cv2.moveWindow("my Tracker", width, 0)

# Initialize HSV range values for tracking a specific color
hueLow = 164
hueHigh = 179
hueLow2 = 23
hueHigh2 = 35
satLow = 31
satHigh = 255
valLow = 179
valHigh = 255

# Create trackbars to adjust HSV range interactively
cv2.createTrackbar("Hue Low", "my Tracker", hueLow, 179, onTrack1)
cv2.createTrackbar("Hue High", "my Tracker", hueHigh, 179, onTrack2)
##Changes to capture the red value
cv2.createTrackbar("Hue Low 2", "my Tracker", hueLow2, 179, onTrack7)
cv2.createTrackbar("Hue High 2", "my Tracker", hueHigh2, 179, onTrack8)

cv2.createTrackbar("Sat Low", "my Tracker", satLow, 255, onTrack3)
cv2.createTrackbar("Sat High", "my Tracker", satHigh, 255, onTrack4)
cv2.createTrackbar("Val Low", "my Tracker", valLow, 255, onTrack5)
cv2.createTrackbar("Val High", "my Tracker", valHigh, 255, onTrack6)


# Main loop for reading webcam frames and processing color tracking
while True:
    ignore, frame = cam.read()  # Capture each frame from the webcam
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert frame to HSV color space

    # Define the lower and upper bounds for color detection based on trackbar values
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])

    # Define new upperbound and lowerbound for the red color
    lowerBound2 = np.array([hueLow2, satLow, valLow])
    upperBound2 = np.array([hueHigh2, satHigh, valHigh])

    # Create a mask to filter out pixels within the specified color range
    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    
    #Create a second mask for the new red color
    myMask2 = cv2.inRange(frameHSV, lowerBound2, upperBound2)

    ##Combine
    myMaskComp = myMask | myMask2

    #Anotherway
    #myMaskComp = cv2.add(myMask,myMask2)
 
    # myMask = cv2.bitwise_not(myMask)

    # Apply mask to the original frame to isolate the detected object
    myObject = cv2.bitwise_and(frame, frame, mask=myMaskComp)
    
    # Resize the result for easier display
    myObjectSmall = cv2.resize(myObject, (int(width / 2), int(height / 2)))
    cv2.imshow("my Object", myObjectSmall)
    cv2.moveWindow("my Object", width, int(height))

    # Resize the mask for easier display
    myMaskSmall = cv2.resize(myMask, (int(width / 2), int(height / 2)))
    cv2.imshow("my Mask", myMaskSmall)
    cv2.moveWindow("my Mask", int(width/2), height + 160)

    #my new mask for the red color
    myMaskSmall2 = cv2.resize(myMask2, (int(width / 2), int(height / 2)))
    cv2.imshow("my Mask 2", myMaskSmall2)
    cv2.moveWindow("my Mask 2", 0, height + int(height/2) +50)
    
    # Display the original webcam feed
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the webcam resources
cam.release()
