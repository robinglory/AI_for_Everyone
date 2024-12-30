import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX

# Optimized resolution
width = 320
height = 180
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Load and encode known faces
yanFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\yan.jpg")
yanFaceEncode = FR.face_encodings(yanFace)[0]

NiFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\Mom.jpg")
NiFaceEncode = FR.face_encodings(NiFace)[0]

GuFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\Gugu.jpg")
GuFaceEncode = FR.face_encodings(GuFace)[0]

knownEncodings = [yanFaceEncode, NiFaceEncode, GuFaceEncode]
names = ["Yan Naing", "Ni Ni Lwin", "Gu Gu"]

# Frame processing interval
frame_count = 0
process_interval = 5  # Process every 5th frame

while True:
    ret, unknownFace = cam.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(unknownFace, (0, 0), fx=0.5, fy=0.5)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    frame_count += 1
    if frame_count % process_interval == 0:
        # Detect and encode faces in the resized frame
        faceLocations = FR.face_locations(rgb_small_frame, model='hog')  # Use 'hog' for faster detection
        unknownEncodings = FR.face_encodings(rgb_small_frame, faceLocations)

        # Process detected faces
        for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
            matches = FR.compare_faces(knownEncodings, unknownEncoding)
            name = "Unknown"
            if True in matches:
                matchIndex = matches.index(True)
                name = names[matchIndex]

            # Scale face locations back to original frame size
            top, right, bottom, left = [int(coord * 2) for coord in faceLocation]
            cv2.rectangle(unknownFace, (left, top), (right, bottom), (100, 255, 100), 3)
            cv2.putText(unknownFace, name, (left, top - 10), font, 0.6, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("My Faces", unknownFace)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()