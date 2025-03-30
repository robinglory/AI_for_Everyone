import cv2
import numpy as np

width = 210
height = 160
img1 = cv2.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\A.png', 1)
img2 = cv2.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\B.png', 1)
img1 = cv2.resize(img1, (width, height))
img2 = cv2.resize(img2, (width, height))


if img1 is None or img2 is None:
    print("Error: Could not read one of the images.")
    exit()

dest1 = cv2.bitwise_and(img1,img2, mask=None)
dest2 = cv2.bitwise_or(img1,img2, mask=None)
dest3 = cv2.bitwise_xor(img1,img2, mask=None)


cv2.imshow("A",img1)
cv2.imshow("B",img2)
cv2.imshow("AND_Picture",dest1)
cv2.imshow("OR_Picture",dest2)
cv2.imshow("xOR_Picture",dest3)
cv2.imshow("NOT A", cv2.bitwise_not(img1))
cv2.imshow("NOT B", cv2.bitwise_not(img2))

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()