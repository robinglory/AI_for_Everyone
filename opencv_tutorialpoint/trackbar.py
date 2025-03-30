import numpy as np
import cv2

img = np.zeros((300,400,3), np.uint8)#Create a black image
cv2.namedWindow("Image")

def nothing(x):
    pass

cv2.createTrackbar("R", "Image", 0, 255, nothing)
cv2.createTrackbar("G", "Image", 0, 255, nothing)
cv2.createTrackbar("B", "Image", 0, 255, nothing)

while True:
    cv2.imshow("Image", img)
    k = cv2.waitKey(1) & 0xFF # Wait for a key press
    if k == 27: # ESC key to exit
        break
    # Get the current positions of the trackbars
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")

    #s = cv2.getTrackbarPos("S", "Image")
    #img[:] = [b, g, r] # Set the image to the selected color

    cv2.rectangle(img,(100,100),(200,200),(b,g,r),-1)

cv2.destroyAllWindows()