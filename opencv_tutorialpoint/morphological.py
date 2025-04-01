import cv2
import numpy as np

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\story_lena_lenna_1.jpg", 0)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations= 1)

# img = cv2.resize(img, (200,400))
# erosion = cv2.resize(erosion, (200,400))
# dilation = cv2.resize(dilation, (200,400))
cv2.imshow("Dilation", dilation)
cv2.imshow("Original Image", img)
cv2.imshow("Erosion", erosion)


cv2.waitKey(0)
cv2.destroyAllWindows()