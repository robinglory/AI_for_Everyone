import numpy as np
import cv2

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\opencv.png", 1)
print(img.shape)  # (height, width, channels)
print(img.size)  # total number of pixels (height * width * channels)

p = img[50,50]
print(p)  # pixel value at (50, 50) in BGR format

for i in range(100):
    for j in range(100):
        img[i,j] = [255, 255, 255]  # set pixel value to white

cv2.imshow("image", img)  # display the modified image
cv2.waitKey(0)  # wait for a key event
cv2.destroyAllWindows()  # close all windows
# This code reads an image, prints its shape and size, modifies a portion of the image to white, and displays it.