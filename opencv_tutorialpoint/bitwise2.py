import cv2
import cv2 as cv
import numpy as np
width = 210
height = 160
img1 = cv2.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\story_lena_lenna_1.jpg')
img2 = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\opencv.png")
img1 = cv2.resize(img1, (width, height))
img2 = cv2.resize(img2, (width, height))
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI
dst = cv.add(img2_fg, img1_bg)
img1[0:rows, 0:cols ] = dst
cv.imshow("Result",img1)
cv.waitKey(0)
cv.destroyAllWindows()