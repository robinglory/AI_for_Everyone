# import cv2
# print(cv2.__version__);

# square_size = 100;
# board_size = 1000;
# import numpy as np
# while True:
#     frame = np.zeros([1000,1000,3],dtype=np.uint8)
#     # frame[:,:] = (0,0,255);
#     # frame[:,:125] = (0,255,0);
#     # frame[:125,:0] = (255, 0,0);

#     # frame[:100,:] = (0,0,0);
#     # frame[100:200,:] = (255,255,255);
#     # frame[200:300,:] = (0,0,0);
#     # frame[300:400,:] = (255,255,255);
#     # frame[400:500,:] = (0,0,0);
#     # frame[500:600,:] = (255,255,255);    
#     # frame[600:700,:] = (0,0,0);
#     # frame[700:800,:] = (255,255,255);
#     # frame[800:900,:] = (0,0,0);
#     # frame[900:1000,:] = (255,255,255);

#     # frame[:,:100] = (0,0,0);
#     # frame[:,100:200] = (255,255,255);
#     # frame[:,200:300] = (0,0,0);
#     # frame[:,300:400] = (255,255,255);

#     for row in range(0, 1000, 100):
#         for col in range(0, 1000, 100):
#             # Alternate colors based on the row and column indices
#             if (row // 100 + col // 100) % 2 == 0:
#                 color = (0, 0, 0)  # Black
#             else:
#                 color = (255, 255, 255)  # White
            
#             # Draw the square
#             frame[row:row+1000, col:col+1000] = color

#     cv2.imshow("My Window", frame)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break


import cv2
print(cv2.__version__);
import numpy as np

board_size = int(input("What size is you Board, Yan Naing?"));
numSquare = int(input("Yan Naing, how many square do you want too?"));

square_size = int(board_size/numSquare);

darkColor = (0,0,0);
ligthColor = (125,125,125);
nowColor = darkColor


while True:
    x = np.zeros([board_size,board_size, 3], dtype=np.uint8);

    for row in range(0,numSquare):
        for col in range(0,numSquare):
            x[square_size*row:square_size*(row+1), square_size*col:square_size
            *(col+1)] = nowColor;
            if nowColor == darkColor:
                nowColor = ligthColor;
            else:
                nowColor = darkColor;
        if nowColor == darkColor:
            nowColor = ligthColor;
        else:
            nowColor = darkColor;
    cv2.imshow("My CheckerBox ", x)
    if cv2.waitKey(1) == ord("q"):
        break