import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

yanFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\yan.jpg")
faceLoc = FR.face_locations(yanFace)[0]
yanFaceEncode = FR.face_encodings(yanFace)[0]

NiFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\Mom.jpg")
faceLoc = FR.face_locations(NiFace)[0]
NiFaceEncode = FR.face_encodings(NiFace)[0]

GuFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\Gugu.jpg")
faceLoc = FR.face_locations(GuFace)[0]
GuFaceEncode = FR.face_encodings(GuFace)[0]

knownEncodings = [yanFaceEncode, NiFaceEncode, GuFaceEncode]
names = ["Yan Naing", "Ni Ni Lwin", "Gu Gu"]

while True:
    ignore,  unknownFace = cam.read()
    unknownFaceRGB = cv2.cvtColor(unknownFace, cv2.COLOR_RGB2BGR)
    faceLocations = FR.face_locations(unknownFaceRGB)
    unknownEncodings = FR.face_encodings(unknownFaceRGB, faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left = faceLocation
        # print(faceLocation)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(100,255,100),3)
        name = "Unknown"
        matches = FR.compare_faces(knownEncodings, unknownEncoding)
        print(matches)
        if True in matches:
            matchIndex = matches.index(True)
            print(matchIndex)
            print(names[matchIndex])
            name = names[matchIndex]
        cv2.putText(unknownFace,name,(left,top),font,1,(0,0,255),2)

    cv2.imshow("My Faces",unknownFace)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


# while True:
#     ignore,  frame = cam.read()
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()