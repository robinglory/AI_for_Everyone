import cv2
from PIL import Image
import pytesseract
import numpy as np

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open webcam
camera = cv2.VideoCapture(0)

while True:
    # Capture frame
    success, frame = camera.read()
    if not success:
        break

    # Convert frame to grayscale (better accuracy for OCR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to improve text detection
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Convert frame to PIL Image
    img_pil = Image.fromarray(thresh)

    # Extract text from the frame
    text = pytesseract.image_to_string(img_pil)

    # Print extracted text in the command line
    print("Extracted Text:", text.strip())

    # Display the text on the webcam feed
    for i, line in enumerate(text.split("\n")):
        cv2.putText(frame, line, (20, 50 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the processed webcam feed
    cv2.imshow("Live OCR", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
