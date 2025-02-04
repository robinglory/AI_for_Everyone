##Old file
import cv2
from PIL import Image
import pytesseract
import numpy as np

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open webcam
camera = cv2.VideoCapture(0)

# Create or open the text file
output_file = r"C:\Users\ASUS\Documents\Python\Programs\OCR Python\extracted_text.txt"

while True:
    # Capture frame
    success, frame = camera.read()
    if not success:
        break

    # Convert frame to grayscale for better OCR accuracy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text readability
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Convert frame to PIL Image
    img_pil = Image.fromarray(thresh)

    # Extract text from the frame
    text = pytesseract.image_to_string(img_pil).strip()

    # Filter out empty or unreadable text
    if text and any(char.isalnum() for char in text):  # Ensures text is not just spaces or symbols
        print("Extracted Text:", text)  # Print in the command line

        # Save only meaningful text to the file
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(text + "\n")

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
