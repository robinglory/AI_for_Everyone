##Parsing Mediapipe Pose, Face and Hand LandMarks, facemesh also!


import cv2
import mediapipe as mp
print(cv2.__version__)

class mpFaceMesh:
    import mediapipe as mp
    def __init__(self, still=False, max_num_faces=3, min_detection_confidence=0.5, min_tracking_confidence=0.5, drawMesh=True):
        self.myFaceMesh = self.mp.solutions.face_mesh.FaceMesh(
            static_image_mode=still,
            max_num_faces=max_num_faces,
            refine_landmarks=False,  # This should be a bool (not 0.5)
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        self.mpDraw = self.mp.solutions.drawing_utils
        self.draw = drawMesh
    # def Marks(self,frame):
    #     global width
    #     global height
    #     frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #     results = self.myFaceMesh.process(frameRGB)
    #     facesMeshLandmarks = []
    #     if results.multi_face_landmarks != None:
    #         for faceMesh in results.multi_face_landmarks:
    #             faceMeshLandmarks = []
    #             for lm in faceMesh.landmark:
    #                 loc = (int(lm.x*width),int(lm.y*height))
    #                 faceMeshLandmarks.append(loc)
    #             facesMeshLandmarks.append(faceMeshLandmarks)
    #             if self.draw == True:
    #                 self.myDraw.draw_landmarks(frame,faceMesh)
    def Marks(self, frame):
        global width, height
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.myFaceMesh.process(frameRGB)

        facesMeshLandmarks = []  # ✅ Initialize this list properly before using it

        if results.multi_face_landmarks:  # Check if any face mesh landmarks are detected
            for faceMesh in results.multi_face_landmarks:
                faceMeshLandmarks = []  # Store landmarks for one face
                for lm in faceMesh.landmark:
                    loc = (int(lm.x * width), int(lm.y * height))  # Convert to pixel coordinates
                    faceMeshLandmarks.append(loc)
                facesMeshLandmarks.append(faceMeshLandmarks)  # ✅ Append the detected face landmarks

                if self.draw:
                    self.mpDraw.draw_landmarks(frame, faceMesh)  # ✅ Corrected "self.myDraw" to "self.mpDraw"

        return facesMeshLandmarks  # ✅ Return the list correctly


class mpFace:
    import mediapipe as mp
    def __init__(self):
        self.myFace = self.mp.solutions.face_detection.FaceDetection()

    def Marks(self,frame):
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.myFace.process(frameRGB)
        faceBoundBoxs = []
        if results.detections != None:
            for face in results.detections:
                bBox = face.location_data.relative_bounding_box
                topLeft = (int(width*bBox.xmin),int(height * bBox.ymin))
                bottomRight = (int((bBox.xmin+bBox.width) * width ),int((bBox.ymin+bBox.height)* height))
                faceBoundBoxs.append((topLeft,bottomRight))
        return faceBoundBoxs


class mpPose:
    import mediapipe as mp
    def __init__(self, still=False, smoothData=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.myPose=self.mp.solutions.pose.Pose(
            static_image_mode=still,
            model_complexity=1,  # Default is 1, can be 0 (faster) or 2 (more accurate)
            smooth_landmarks=smoothData,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence)
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands = mp.solutions.hands.Hands(
                        static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5
                    )                          
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                #print(hand)
                #print(hand.classification)
                #print(hand.classification[0])
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands()
findFace = mpFace()
findPose = mpPose()
findMesh = mpFaceMesh(drawMesh=False)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fontColor = (0,0,255)
fontSize = .5
fontThick = 1

lowerLimit = 0
upperLimit = 468

def setLower(value):
    global lowerLimit
    lowerLimit = value
def setHigher(value):
    global upperLimit
    upperLimit = value

cv2.namedWindow("TrackBars")
cv2.moveWindow("TrackBars",width+50,0)
cv2.resizeWindow("TrackBars",400,150)

cv2.createTrackbar("LowerLimit","TrackBars",0,468,setLower)
cv2.createTrackbar("UpperLimit","TrackBars",468,468,setHigher)
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))

    handLM,handsType = findHands.Marks(frame)
    faceLoc = findFace.Marks(frame)
    poseLM = findPose.Marks(frame)
    facesMeshLM = findMesh.Marks(frame)

    if poseLM != None:
        for ind in [13,14,15,16]:
            cv2.circle(frame,poseLM[ind],20,(0,255,0),-1)

    for face in faceLoc:
        cv2.rectangle(frame,face[0],face[1],(255,0,0),3)

    for hand,handType in zip(handLM,handsType):
        if handType == "Right":
            lbl = "Right Hand"
            cv2.putText(frame,lbl,hand[8],font,2,fontColor,2)
        if handType == "Left":
            lbl = "Left Hand"
            cv2.putText(frame,lbl,hand[8],font,2,fontColor,2)
    for faceMeshLM in facesMeshLM:
        cnt = 0
        for lm in faceMeshLM:
            if cnt >= lowerLimit and cnt <= upperLimit:
                cv2.putText(frame,str(cnt),lm,font,fontSize,fontColor,fontThick)
            cnt = cnt+1

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()