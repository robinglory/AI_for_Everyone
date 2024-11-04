# import cv2
# print(cv2.__version__)
# width=1280
# height=720

# evt = 0;
# #this is mouseClick function
# def mouseClick(event, xPos, yPos,flags,params):
#     global evt;
#     global pnt;
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         print("Mouse click event was: ", event)
#         print("at postion", xPos,yPos)
#         pnt = (xPos,yPos)
#         evt = event;

#     if event == cv2.EVENT_LBUTTONUP:
#         print("Mouse button up event was: ", event)
#         print("at postion", xPos,yPos)
#         evt = event;

# cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

# cv2.namedWindow("my WEBcam") #creating the window
# cv2.setMouseCallback('my WEBcam', mouseClick) #frame and function---which is mouseClick
# while True:

#     ignore,  frame = cam.read()
#     if evt == 1:
#         cv2.circle(frame,pnt,30,(255,0,0),3);

#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()


import cv2

# Check OpenCV version
print(cv2.__version__)

# Set the webcam resolution
width = 1280
height = 720

# Variables to store the event state and position
draw_circle = False
pnt = (0, 0)

# Mouse click event handler
def mouseClick(event, xPos, yPos, flags, params):
    global draw_circle, pnt
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Mouse click event was:", event)
        print("Position:", xPos, yPos)
        pnt = (xPos, yPos)
        draw_circle = True  # Set to true to indicate circle should be drawn

    if event == cv2.EVENT_RBUTTONUP:
        print("Right Button Up: ", event)
        pnt = (xPos,yPos);
        evt = event;

# Open the webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Set up the window and mouse callback
cv2.namedWindow("my WEBcam")
cv2.setMouseCallback("my WEBcam", mouseClick)

# Main loop
while True:
    # Capture frame-by-frame
    ignore, frame = cam.read()
    
    # Draw the circle if needed
    if draw_circle:
        cv2.circle(frame, pnt, 30, (255, 0, 0), 3)
    
    # Display the frame
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow("my WEBcam", 0, 0)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cam.release()
cv2.destroyAllWindows()
