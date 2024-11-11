# Import OpenCV library and NumPy for creating and manipulating images
import cv2
print(cv2.__version__)  # Print the OpenCV version for confirmation

import numpy as np  # Import NumPy for array handling

# Start an infinite loop to continuously create and display the frame
while True:
    # Create a blank 250x250 image with 3 color channels (RGB), all initialized to zero (black)
    frame = np.zeros([250, 250, 3], dtype=np.uint8)
    
    # Set the entire frame to red (0, 0, 255 in BGR format) as the default color
    frame[:, :] = (0, 0, 255)
    
    # Set the left half of the frame (columns 0 to 124) to green (0, 255, 0 in BGR format)
    frame[:, :125] = (0, 255, 0)
    
    # Set the top left quarter of the frame (rows 0 to 124 and columns 0 onward) to blue (255, 0, 0 in BGR format)
    frame[:125, :] = (255, 0, 0)

    # Display the frame in a window titled "My Window"
    cv2.imshow("My Window", frame)
    
    # Wait for 1 ms; if 'q' is pressed, break the loop and close the window
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


# Explanation Summary
# This code creates a 250x250 pixel image that combines three color sections: red, green, and blue.
# The entire frame is initially set to red, then the left half is changed to green, and finally, the top half is set to blue, creating an overlapping effect of colors in specific regions.
# The image is displayed in a loop until the user presses 'q' to exit.