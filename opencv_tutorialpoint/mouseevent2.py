import numpy as np
import cv2 as cv

drawing = True
shape = 'r'

def draw_circle(event, x, y, flags, param):
    global x1, y1, drawing  # Add 'drawing' to the global variables
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if shape == 'r':
            cv.rectangle(img, (x1, y1), (x, y), (0, 255, 0), -1)
        if shape == 'l':
            cv.line(img, (x1, y1), (x, y), (0, 255, 0), 5)
        if shape == 'c':
            cv.circle(img, (x, y), 5, (0, 255, 0), -1)

img = cv.imread(r'C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg')
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('r'):
        shape = 'r'
    elif k == ord('l'):
        shape = 'l'
    elif k == ord('c'):
        shape = 'c'
    elif k == 27:
        break
cv2.destroyAllWindows()