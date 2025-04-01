import numpy as np
import cv2

img1 = cv2.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg')
img2 = cv2.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\ronaldo face.png')

# Convert it to grayscale
img1_bw = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2_bw = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()

queryKeypoints, queryDescriptors = orb.detectAndCompute(img1_bw,None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(img2_bw,None)

matcher = cv2.BFMatcher()
matches = matcher.match(queryDescriptors,trainDescriptors)

img = cv2.drawMatches(img1, queryKeypoints,
img2, trainKeypoints, matches[:20],None)

img = cv2.resize(img, (1000,650))

cv2.imshow("Feature Match", img)
cv2.waitKey(0)
cv2.destroyAllWindow()