import numpy as np
import cv2 

def drawfunction(event,x,y,flags,param):
   if event == cv2.EVENT_LBUTTONDOWN:  # Corrected constant
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg",1)
img = cv2.resize(img, (400, 450))
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", drawfunction)

while True:
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()