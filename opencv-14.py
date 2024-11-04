import cv2
print(cv2.__version__)

# Initial Setup
width = 640  # Starting width
height = int(width * 9 / 16)  # Starting height, maintaining 16:9 ratio
positionX = 0  # Initial X position for the window
positionY = 0  # Initial Y position for the window
resize_factor = 640  # Factor to resize (initial 640 to match width)

# Callback functions
def resize_callback(val):
    global width, height
    # Update width and height based on resize factor with 16:9 ratio
    width = val
    height = int(val * 9 / 16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    print(f"Resize Width: {width}, Height: {height}")

def move_x_callback(val):
    global positionX
    positionX = val
    print("X Position:", positionX)

def move_y_callback(val):
    global positionY
    positionY = val
    print("Y Position:", positionY)

# Webcam Setup
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Trackbar Window
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 400, 200)
cv2.createTrackbar("Resize", "Settings", resize_factor, 1920, resize_callback)  # Resize up to 1920 width
cv2.createTrackbar("Move X", "Settings", positionX, 1920, move_x_callback)
cv2.createTrackbar("Move Y", "Settings", positionY, 1080, move_y_callback)

while True:
    ignore, frame = cam.read()

    # Display the frame with updated window size and position
    cv2.imshow("Webcam", frame)
    cv2.moveWindow("Webcam", positionX, positionY)  # Position the frame based on trackbars

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
