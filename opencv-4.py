# import cv2
# print(cv2.__version__)

# width = 320;
# height = 180;

# cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width);
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height);
# cam.set(cv2.CAP_PROP_FPS, 10);
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

# while True:
#     ignore,  frame = cam.read()
#     grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
#     hlsframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL);
#     labframe = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB);

# # i will add 4 row 6 coloums video matrix
# #this is the first row of the video feeds
#     cv2.imshow("This is original Color", frame);
#     cv2.moveWindow("This is original Color", 0, 0);

#     cv2.imshow("This is Gray Color",grayframe);
#     cv2.moveWindow("This is Gray Color", 320, 0);
    
#     cv2.imshow("This is HLS Color", hlsframe);
#     cv2.moveWindow("This is HLS Color", 640, 0);

#     cv2.imshow("This is LAB Color", labframe);
#     cv2.moveWindow("This is LAB Color", 960, 0);


# #this is the second row of the column
#     cv2.imshow("This is original Color", frame);
#     cv2.moveWindow("This is original Color", 0, 400);

#     cv2.imshow("This is Gray Color",grayframe);
#     cv2.moveWindow("This is Gray Color", 320, 400);
    
#     cv2.imshow("This is HLS Color", hlsframe);
#     cv2.moveWindow("This is HLS Color", 320, 400);

#     cv2.imshow("This is LAB Color", labframe);
#     cv2.moveWindow("This is LAB Color", 320, 400);


#     # cv2.imshow("This is HLS Color", hlsframe);
#     # cv2.moveWindow("This is HLS Color", 1280, 900);

#     # cv2.imshow("This is LAB Color", labframe);
#     # cv2.moveWindow("This is LAB Color", 1600, 1080);
    
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()



#Homework soultion from Paul Macwhorter

import cv2
print(cv2.__version__)

width = 1280;
height = 720;

rows = int(input("Boss, How many rows do you want for this video feed!! "));
columns = int(input("Boss, How many coloum do you want too? "));


cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width);
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height);
cam.set(cv2.CAP_PROP_FPS, 10);
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
while True:
    ignore,  frame = cam.read()
    frame = cv2.resize(frame, (int(width/columns), int(height/rows)));
    for i in range(0, rows):
        for j in range(0, columns):
            windowName = "Window "  + str(i) + "x" + str(j);
            cv2.imshow(windowName,frame);
            cv2.moveWindow(windowName,int(width/columns) * j, int(height/rows) * i)


    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()