import cv2
from ffpyplayer.player import MediaPlayer

file = "output.avi"

video =cv2.VideoCapture(file)
player = MediaPlayer(file)
while True:
    ret, frame = video.read()
    audio_frame, val = player.get_frame()
    if not ret:
        print("End of the Video")
        break
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow("Video",frame)
    if val != "eof" and audio_frame is not None:
        #audio
        img, t = audio_frame

video.release()
cv2.destroyAllWindows()