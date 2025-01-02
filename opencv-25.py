import os
import cv2
import face_recognition as FR
print(cv2.__version__)

imageDir = r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known"

for root,dirs,files in os.walk(imageDir):
    print(f"My Working Folder (root) {root}")
    print(f"dirs in root: {dirs}")
    print(f"My files in root, {files}")
    for file in files:
        print(f"Your Guy is {file}")
        fullfilePath = os.path.join(root,file)
        print(fullfilePath)
        # print(f"{root}\{file}")
        name = os.path.splitext(file)[0]
        print(name)
        myPicture = FR.load_image_file(fullfilePath)
        myPicture = cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
        cv2.imshow(name,myPicture)
        cv2.moveWindow(name,0,0)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()