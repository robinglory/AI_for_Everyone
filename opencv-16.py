# Import necessary libraries: OpenCV for image processing and NumPy for numerical operations
import cv2
import numpy as np 

# Create a blank image array 'x' with a size of 256x640 pixels and 3 color channels (for HSV colors)
x = np.zeros([256, 640, 3], dtype=np.uint8)

# Fill in each pixel in 'x' with HSV values that vary based on column and row positions
for row in range(0, 256, 1):  # Loop through each row
    for column in range(0, 640, 1):  # Loop through each column
        # Set HSV values where the hue is based on the column, saturation is based on row, and value is max (255)
        x[row, column] = (int(column / 4), row, 255)

# Convert the HSV image to BGR (blue-green-red) color space, as OpenCV's `imshow` expects BGR images
x = cv2.cvtColor(x, cv2.COLOR_HSV2BGR)

# Create another blank image array 'y' with a size of 256x640 pixels and 3 color channels (for HSV colors)
y = np.zeros([256, 640, 3], dtype=np.uint8)

# Fill in each pixel in 'y' with HSV values where saturation is max (255) and value varies based on row
for row in range(0, 256, 1):  # Loop through each row
    for column in range(0, 640, 1):  # Loop through each column
        # Set HSV values where the hue is based on column, saturation is max (255), and value is based on row
        x[row, column] = (int(column / 4), 255, row)

# Convert the HSV image to BGR color space for display
y = cv2.cvtColor(x, cv2.COLOR_HSV2BGR)

# Display loop for showing both images
while True:
    # Show the first HSV-based image ('x')
    cv2.imshow('my HSV', x)
    # Position the window at the top-left corner
    cv2.moveWindow('my HSV', 0, 0)

    # Show the second HSV-based image ('y')
    cv2.imshow('my HSV2', y)
    # Position this window slightly below the first one
    cv2.moveWindow('my HSV2', 0, row + 60)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break;

# Close all OpenCV windows after breaking the loop
cv2.destroyAllWindows();
