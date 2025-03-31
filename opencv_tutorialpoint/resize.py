import numpy as np
import cv2

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg")
if img is None:
    print("Error: Could not read the image.")
    exit()

height, width = img.shape[:2]
res = cv2.resize(img,(int(width/2),int(height/2)), interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original", img)
cv2.imshow("Resized", res)
cv2.waitKey(0)
cv2.destroyAllWindows()