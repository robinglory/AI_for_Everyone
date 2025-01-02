import os
import cv2
import face_recognition as FR
import pickle

print(cv2.__version__)
encodings = []
names = []
imageDir = r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known"
for root,dirs,files in os.walk(imageDir):
    # print(root)
    # print(dirs)
    # print(files)
    for file in files:
        # print(file)
        fullfilepath = os.path.join(root,file)
        print(fullfilepath)
        myPicture = FR.load_image_file(fullfilepath)
        encoding = FR.face_encodings(myPicture)[0]
        name = os.path.splitext(file)[0]
        encodings.append(encoding)
        names.append(name)

with open('train.pkl','wb') as f:
    pickle.dump(names,f)
    pickle.dump(encodings,f)
