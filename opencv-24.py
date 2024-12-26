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

waiFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\waiyan.jpg")
faceLoc = FR.face_locations(waiFace)[0]
waiFaceEncode = FR.face_encodings(waiFace)[0]

tokeFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\toke.jpg")
faceLoc = FR.face_locations(tokeFace)[0]
tokeFaceEncode = FR.face_encodings(tokeFace)[0]

knownEncodings = [yanFaceEncode, waiFaceEncode, tokeFaceEncode]
names = ["Yan Naing", "Wai Yan", "Myo Min Ko"]

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