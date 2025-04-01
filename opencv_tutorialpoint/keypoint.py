import numpy as np
import cv2 as cv
img = cv.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\scale.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\keypoints.jpg',img)