import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg',0)
# global thresholding
ret1,img1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu's thresholding
ret2,img2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.subplot(2,2,1),plt.imshow(img,'gray',vmin=0,vmax=255)
plt.title('Original')
plt.subplot(2,2,2),plt.imshow(img1,'gray')

plt.title('Binary')
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.title('OTSU')
plt.show()