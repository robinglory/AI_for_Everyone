import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg")
kernel = np.ones((3,3),np.float32)/9
dst = cv.filter2D(img,-1,kernel)
dst1 = cv.filter2D(img,-1,kernel,anchor=(-1,-1),delta=0,borderType=cv.BORDER_DEFAULT)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(dst),plt.title('Convolved')
plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(dst1),plt.title("Testing")
plt.xticks([]), plt.yticks([])
plt.show()