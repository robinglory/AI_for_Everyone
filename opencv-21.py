import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier(r'C:\Users\ASUS\Documents\Python\Programs\haar\haarcascade_frontalface_default.xml')

while True:
    ignore,  frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.3,5)

    # print(faces)
    for face in faces:
        x,y,width,height = face
        print(f"x = {x} and y = {y} and width = {width} and height = {height}")
        cv2.rectangle(frame, (x,y), (x+width,y+height), (255,0,0), 3)
        
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()