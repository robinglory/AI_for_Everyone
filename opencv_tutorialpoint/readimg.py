# imread to read an image
# imshow to display an image
# waitKey to wait for a key event
# destroyAllWindows to close all windows

import numpy as np  
import cv2 as cv

img =cv.imread(r"C:\Users\ASUS\Documents\Python\opencv_tutorialpoint\opencv.png",1) # 1 for color, 0 for grayscale, -1 for unchanged
cv.imshow("image", img) # window name is "image"
cv.waitKey(0) # wait for a key event, 0 means wait indefinitely
cv.destroyAllWindows()