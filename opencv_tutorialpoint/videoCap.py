import cv2
cam = cv2.VideoCapture(0)

cc = cv2.VideoWriter_fourcc(*"XVID")
file = cv2.VideoWriter("Output.avi",cc,30,(640,480))

if not cam.isOpened():
    print("error opening camera")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("error in retrieving frame")
        exit()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('frame',img)
    file.write(img)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
file.release()
cv2.destroyAllWindows()