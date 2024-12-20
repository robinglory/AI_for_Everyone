import cv2
import os
import time

# Ensure output folder exists
output_folder = "LicencePlateDatabasePhotos"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize webcam
width, height = 1280, 1080
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Load Haar cascades for license plate detection
plateCascade = cv2.CascadeClassifier(r'C:\Users\ASUS\Documents\Python\Programs\haar\haarcascade_russian_plate_number.xml')

fps = 10
timeStamp = time.time()

while True:
    # Capture frame
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # License plate detection
    # Adjust parameters for higher accuracy (scaleFactor and minNeighbors)
    plates = plateCascade.detectMultiScale(frameGray, scaleFactor=1.1, minNeighbors=10, minSize=(50, 50))
    for plate in plates:
        x, y, w, h = plate
        # Draw a rectangle around the license plate
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        
        # Extract the plate region
        plateROI = frame[y:y+h, x:x+w]
        
        # Save the detected plate image
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(output_folder, f"detected_plate_{timestamp}.jpg")
        cv2.imwrite(filename, plateROI)

    # Display FPS
    loopTime = time.time() - timeStamp
    timeStamp = time.time()
    fpsNEW = 1 / loopTime
    fps = .9 * fps + .1 * fpsNEW
    fps = int(fps)
    cv2.putText(frame, f"{fps} FPS", (5, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 100, 0), 2)

    # Display the frame
    cv2.imshow('License Plate Detection', frame)
    cv2.moveWindow('License Plate Detection', 0, 0)

    # Break loop with 'q' key
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the webcam and close windows
cam.release()
cv2.destroyAllWindows()
