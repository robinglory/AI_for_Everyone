import cv2  # Import OpenCV for image handling
print(cv2.__version__)  # Display OpenCV version

import numpy as np  # Import NumPy for creating the checkerboard array

# Prompt the user for the board size and the number of squares
board_size = int(input("What size is your board, Yan Naing? "))  # Total board dimension
numSquare = int(input("Yan Naing, how many squares do you want? "))  # Number of squares along one row/column

# Calculate the size of each square based on board size and number of squares
square_size = int(board_size / numSquare)

# Define colors for the checkerboard: dark and light colors
darkColor = (0, 0, 0)  # Black color in BGR format
lightColor = (125, 125, 125)  # Light gray color in BGR format
nowColor = darkColor  # Start with the dark color

# Infinite loop to generate and display the checkerboard
while True:
    # Create a blank board (image) with 3 color channels, initialized to black
    x = np.zeros([board_size, board_size, 3], dtype=np.uint8)

    # Loop through rows and columns to fill in each square
    for row in range(0, numSquare):
        for col in range(0, numSquare):
            # Set each square in the checkerboard pattern
            x[square_size * row:square_size * (row + 1), square_size * col:square_size * (col + 1)] = nowColor
            
            # Alternate the color for each square in the row
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor

        # Alternate the starting color of each new row for a checkerboard effect
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor

    # Display the checkerboard in a window titled "My CheckerBox"
    cv2.imshow("My CheckerBox", x)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break


# Explanation Summary
# This code creates a dynamic checkerboard pattern where the board size and the number of squares are user-defined.
# Each square alternates between a dark color (black) and a light color (gray) to form the checkerboard pattern, with each row reversing the starting color for the alternating effect.
# The checkerboard updates continuously in a window until 'q' is pressed to exit.





