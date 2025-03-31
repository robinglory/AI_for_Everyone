import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\A.png", 1)
edge = cv2.Canny(img,100,200)

plt.subplot(121), plt.imshow(img,cmap="rainbow"),plt.title("Original Image")
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edge,cmap="gray"),plt.title("Edge Image") 
plt.xticks([]), plt.yticks([])

plt.show()