##ဒါက အလုပ်လုပ်တဲ့ Code 

import cv2
from PIL import Image
import pytesseract
import time
import os

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open webcam
camera = cv2.VideoCapture(0)

# For tracking detected text stability
last_detected_word = ""
detection_start_time = None

# Paths for saving images and extracted text
image_save_path = r"C:\Users\ASUS\Documents\Python\Programs\OCR Python\caputred_picture"
text_save_path = r"C:\Users\ASUS\Documents\Python\Programs\OCR Python\captured_text.txt"

# Ensure the image save directory exists
os.makedirs(image_save_path, exist_ok=True)

# OCR Configuration
ocr_config = r'--oem 3 --psm 6'

while True:
    success, frame = camera.read()
    if not success:
        break

    original_frame = frame.copy()  # Keep the original frame for saving

    # Preprocessing for better OCR
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Detect text boxes with pytesseract
    data = pytesseract.image_to_data(thresh, config=ocr_config, output_type=pytesseract.Output.DICT)

    detected_words = []

    # Loop through detected text regions
    for i in range(len(data['text'])):
        word = data['text'][i].strip()
        conf = int(data['conf'][i])

        # Only consider high-confidence detections
        if conf >= 93 and word != "":
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]

            # Draw bounding box around detected text
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, word, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            detected_words.append(word)
            # print(word)

    # Text stability check (for 0.1 seconds)
    if detected_words:
        for word in detected_words:
            if word == last_detected_word:
                if detection_start_time and (time.time() - detection_start_time >= 0.05):
                    print("Stable Word Detected:", word)

                    # Save the original frame
                    timestamp = int(time.time() * 1000)
                    image_filename = f"{image_save_path}/capture_{timestamp}.jpg"
                    cv2.imwrite(image_filename, original_frame)

                    # OCR on the saved image
                    img_pil = Image.open(image_filename)
                    extracted_text = pytesseract.image_to_string(img_pil, config=ocr_config).strip()

                    if extracted_text:
                        print("Captured Text:", extracted_text)

                        # Save the extracted text
                        with open(text_save_path, "a", encoding="utf-8") as file:
                            file.write(f"Time Data Collected {timestamp} {extracted_text}" + "\n")

                    # Reset after processing
                    last_detected_word = ""
                    detection_start_time = None
                    break  # Prevent multiple captures for the same detection
            else:
                # New word detected, start timer
                last_detected_word = word
                detection_start_time = time.time()
    else:
        # No text detected, reset tracking
        last_detected_word = ""
        detection_start_time = None

    # Show the webcam feed with bounding boxes
    cv2.imshow("Live OCR (Bounding Box)", frame)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
