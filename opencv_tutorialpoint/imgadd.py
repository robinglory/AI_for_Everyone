import cv2

cristino = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg")
lena = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\story_lena_lenna_1.jpg")

lena_resized = cv2.resize(lena, (cristino.shape[1], cristino.shape[0]))
img = cv2.add(cristino, lena_resized)
cv2.imshow("Addition of Images", img)

img2 = cv2.addWeighted(cristino, 0.5, lena_resized, 0.5, 0)
cv2.imshow("Using Weighted",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()