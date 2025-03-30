import numpy as np
import cv2

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\story_lena_lenna_1.jpg",1)

cv2.line(img,(20,400), (300,200), (0,255,0), 5)
cv2.rectangle(img,(200,100),(400,400),(255,0,0), 5)
cv2.circle(img,(80,80), 50, (0,0,255), -1)
cv2.ellipse(img,(400,300),(100,50),0,0,180,(255,255,0),-1)

cv2.imshow('img', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()