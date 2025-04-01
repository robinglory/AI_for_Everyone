import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\story_lena_lenna_1.jpg")
color = ('b','g','r')

for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()