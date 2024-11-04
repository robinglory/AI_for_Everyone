import cv2
print(cv2.__version__);

import numpy as np
while True:
    frame = np.zeros([250,250,3],dtype=np.uint8)
    frame[:,:] = (0,0,255);
    frame[:,:125] = (0,255,0);
    frame[:125,:0] = (255, 0,0);
    cv2.imshow("My Window", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break