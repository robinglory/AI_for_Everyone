import cv2
import numpy as np
height =450
width = 400
img = cv2.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg')
img = cv2.resize(img,(width,height))
txt = "CR7 The GOAT"
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
thickness = 5
color = (255,0,0)


cv2.putText(img,txt,(100,350),font,fontScale,color,thickness,cv2.LINE_AA)
cv2.imshow("Cristino Ronaldo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()