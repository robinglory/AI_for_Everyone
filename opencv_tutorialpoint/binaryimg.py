import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\A.png")
ret,img1= cv2.threshold(img,127,255,cv2.THRESH_BINARY)


plt.subplot(2,3,2),plt.imshow(img,'gray',vmin=0,vmax=255)
plt.title("Original")

plt.subplot(2,3,2),plt.imshow(img1,'gray',vmin=0,vmax=255)
plt.title("Binary Threshold")

plt.show()