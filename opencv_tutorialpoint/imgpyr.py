import sys
import cv2

filename = r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg"

src = cv2.imread(filename)

while True:
    print("Press 'i' to zoom in, 'o' to zoom out, 'esc' to exit")
    rows, cols, _channels = map(int, src.shape)

    cv2.imshow("Pyramids", src)
    k = cv2.waitKey(0) & 0xFF  # Wait for a key press and get the key code

    if k == 27:  # ESC key
        break
    elif k == ord('i'):  # Check if the key is 'i'
        src = cv2.pyrUp(src)  # Zoom in (double the size)
    elif k == ord('o'):  # Check if the key is 'o'
        src = cv2.pyrDown(src)  # Zoom out (halve the size)

cv2.destroyAllWindows()