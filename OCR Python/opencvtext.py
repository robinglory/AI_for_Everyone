import cv2
from PIL import Image  # Corrected import
from pytesseract import pytesseract

# Open camera
camera = cv2.VideoCapture(0)

while True:
    _, image = camera.read()
    cv2.imshow("Text Detection", image)
    
    # Press 's' to capture and save the image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("test1.jpg", image)
        break

# Release camera and close windows
camera.release()
cv2.destroyAllWindows()

# Function to extract text from the captured image
def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = 'test1.jpg'
    
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    
    print("Extracted Text:\n", text.strip())  # .strip() removes unnecessary whitespace

tesseract()
