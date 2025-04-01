import cv2
import numpy as np

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg",1)
cv2.imshow("Original Image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\ronaldo face.png",0)
cv2.imshow("Template", template)

w,h = template.shape[0], template.shape[1]
print(w,h)

matched = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
print(matched)
threshold = 0.8

loc = np.where(matched >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

cv2.imshow("Detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()