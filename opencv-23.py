# import face_recognition

# # Replace with a valid image path
# image_path = r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\justin bieber.jpeg"  
# try:
#     image = face_recognition.load_image_file(image_path)
#     face_locations = face_recognition.face_locations(image)
#     print("Face locations detected:", face_locations)
# except Exception as e:
#     print("Error:", e)

# import cv2

# print("OpenCV version:", cv2.__version__)
# image = cv2.imread(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\cleaned_image.jpg")
# if image is not None:
#     print("Image loaded successfully")
# else:
#     print("Failed to load image. Check the path.")

# import dlib

# print("dlib version:", dlib.__version__)
# face_detector = dlib.get_frontal_face_detector()
# print("Face detector initialized:", bool(face_detector))

# This is very important to check these script above if you face library errors.

import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX

donFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\Donald Trump.jpg")
faceLoc = FR.face_locations(donFace)[0]
donFaceEncode = FR.face_encodings(donFace)[0]

nancyFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\Nancy Pelosi.jpg")
faceLoc = FR.face_locations(nancyFace)[0]
nancyFaceEncode = FR.face_encodings(nancyFace)[0]

knownEncodings = [donFaceEncode, nancyFaceEncode]
names = ["Donald Trump", "Nancy Pelosi"]

unknownFace = FR.load_image_file(r"C:\Users\ASUS\Documents\Python\Programs\demoImages\unknown\u1.jpg")
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
cv2.waitKey(10000)
# print(faceLoc)

# top,right,bottom,left = faceLoc
# cv2.rectangle(donFace,(left,top),(right,bottom),(255,100,100),3)

# donFaceBGR = cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
# cv2.imshow("My Window",donFaceBGR)
# cv2.waitKey(3000)