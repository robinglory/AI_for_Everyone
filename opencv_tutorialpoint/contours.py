import cv2
import numpy as np

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\A.png")
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 30,200)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of contours found: ", len(contours))

cv2.imshow("Canny", canny)
cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()