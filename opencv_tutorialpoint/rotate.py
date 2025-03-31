import cv2
import numpy as np

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\opencv.png")
if img is None:
    print("Error: Could not read the image.")
    exit()
height, width = img.shape[:2]
img = cv2.resize(img,(int(width/2),int(height/2)), interpolation=cv2.INTER_CUBIC)

center = (width/2, height/2)
mat = cv2.getRotationMatrix2D(center, 45, 1)
rotimg = cv2.warpAffine(img, mat,(width,height))
rotimg = cv2.resize(rotimg, (400,300),interpolation=cv2.INTER_CUBIC)
# rotimg = cv2.resize(rotimg, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotimg)
cv2.waitKey(0)
cv2.destroyAllWindows()