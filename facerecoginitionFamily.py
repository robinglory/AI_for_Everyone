import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX

#Yan Naing Face
YanFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\yannaing.jpg")
faceLoc = FR.face_locations(YanFace)[0]
YanFaceEncode = FR.face_encodings(YanFace)[0]

#Mother Face
NiFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\mother.jpg")
faceLoc = FR.face_locations(NiFace)[0]
NiFaceEncode = FR.face_encodings(NiFace)[0]

#Father Face
KyawFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\father.jpg")
faceLoc = FR.face_locations(KyawFace)[0]
KyawFaceEncode = FR.face_encodings(KyawFace)[0]

#Sister Face
GuFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\gugu.jpg")
faceLoc = FR.face_locations(GuFace)[0]
GuFaceEncode = FR.face_encodings(GuFace)[0]

knownEncodings = [YanFaceEncode, NiFaceEncode, KyawFaceEncode, GuFaceEncode]
names = ["Yan Naing", "Mother", "Father", "Sister"]

unknownFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\father.jpg")
unknownFaceBGR = cv2.cvtColor(unknownFace, cv2.COLOR_RGB2BGR)
faceLocations = FR.face_locations(unknownFace)
unknownEncodings = FR.face_encodings(unknownFace, faceLocations)

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(100,255,100),3)
    name = "Unknown"
    matches = FR.compare_faces(knownEncodings, unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex = matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name = names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,0.7,(0,0,255),1)

cv2.imshow("My Faces",unknownFaceBGR)
cv2.waitKey(15000)
# print(faceLoc)

# top,right,bottom,left = faceLoc
# cv2.rectangle(donFace,(left,top),(right,bottom),(255,100,100),3)

# donFaceBGR = cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
# cv2.imshow("My Window",donFaceBGR)
# cv2.waitKey(3000)