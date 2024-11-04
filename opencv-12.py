# import cv2
# start_point = None;
# end_point = None;
# drawing = False;
# roi_window_open = False;

# def mouse_callback(event,x,y,flags,params):
#     global start_point,end_point,drawing,roi_window_open

#     if event == cv2.EVENT_LBUTTONDOWN:
#         start_point = (x,y);
#         drawing = True;
#         roi_window_open = False;
    
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing: 
#             end_point = (x,y);
    
#     elif event == cv2.EVENT_LBUTTONUP:
#         end_point = (x,y);
#         drawing = False;
#         roi_window_open = True;

#     elif event == cv2.EVENT_RBUTTONDOWN:
#         cv2.destroyWindow("Live ROI")
#         roi_window_open = False;

# cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# cv2.namedWindow("Webcam")
# cv2.setMouseCallback("Webcam", mouse_callback)

# while True:
#     ret, frame = cam.read()
#     if not ret:
#         break

#     if drawing and start_point and end_point:
#         cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)

#     if roi_window_open and start_point and end_point:
#         x1, y1 = start_point
#         x2, y2 = end_point
#         roi = frame[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
#         if roi.size > 0:
#             cv2.imshow("Live ROI", roi)

#     cv2.imshow("Webcam", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cam.release()
# cv2.destroyAllWindows()


import cv2
print(cv2.__version__)
width=900
height=600
evt = 0;
def mouseClick(event, xPos,yPos, flags, params):
    global pnt1;
    global pnt2;
    global evt;
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event);
        pnt1 = (xPos,yPos);
        evt = event;

    if event == cv2.EVENT_LBUTTONUP:
        print(event);
        pnt2 = (xPos,yPos);
        evt = event;

    if event == cv2.EVENT_RBUTTONUP:
        print(event);
        evt = event

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('my WEBcam');
cv2.setMouseCallback("my WEBcam", mouseClick);

while True:
    ignore,  frame = cam.read()

    if evt == 4: 
        cv2.rectangle(frame,pnt1, pnt2, (255,0,100), 2);
        ROI = frame[pnt1[1]:pnt2[1], pnt1[0]:pnt2[0]]
        cv2.imshow("ROI", ROI)
        cv2.moveWindow("ROI", int(width*1.1),0)

    if evt == 5:
        cv2.destroyWindow("ROI");
        evt = 0;

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()