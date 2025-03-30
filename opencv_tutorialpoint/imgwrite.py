import numpy as np
import cv2

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\opencv_tutorialpoint\opencv.png", 0)
cv2.imshow("Graysclae Image", img)
key = cv2.waitKey(0) #wait indefinitely until a key is pressed
if key == ord('s'):
    cv2.imwrite("opencv_gray.png", img)
    print("Image saved as opencv_gray.png")
else:
    print("Image not saved")

cv2.destroyAllWindows()