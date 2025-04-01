import cv2

img = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.resize(img, (500, 500))
img3 = cv2.resize(img1, (500, 500))
img4 = cv2.resize(img2, (500, 500))

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", img3)
cv2.imshow("HSV Image", img4)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()