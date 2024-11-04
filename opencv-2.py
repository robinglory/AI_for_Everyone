#this is the homework from lesson 5
import cv2;
cam = cv2.VideoCapture(0);
while True:
    ignore, frame = cam.read();
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    hlsframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL);
    labframe = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB);

    cv2.imshow("This is original Color", frame);
    cv2.moveWindow("This is original Color", 0, 0);

    cv2.imshow("This is Gray Color",grayframe);
    cv2.moveWindow("This is Gray Color", 800, 0);

    cv2.imshow("This is HLS Color", hlsframe);
    cv2.moveWindow("This is HLS Color", 0, 500);

    cv2.imshow("This is LAB Color", labframe);
    cv2.moveWindow("This is LAB Color", 800, 500);

    if cv2.waitKey(1) & 0xff == ord("q"):
        break;
cam.release();

