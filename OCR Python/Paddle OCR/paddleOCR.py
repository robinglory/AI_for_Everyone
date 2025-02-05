import cv2
import threading
import time
import os
import numpy as np
from paddleocr import PaddleOCR

# Initialize webcam
camera = cv2.VideoCapture(0)

# Set OCR model (English, digits, symbols)
ocr = PaddleOCR(use_angle_cls=True, lang="en")

# Create OpenCV window
cv2.namedWindow("OCR Live", cv2.WINDOW_NORMAL)

# Flags
ocr_running = False
user_requested_ocr = False

def preprocess_image(image):
    """Apply preprocessing to improve OCR accuracy."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Adaptive Thresholding (for better contrast)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 41, 10)

    # Denoising (removes background noise)
    denoised = cv2.fastNlMeansDenoising(binary, None, 30, 7, 21)

    # Sharpen Image for OCR clarity
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(denoised, -1, kernel)

    return sharpened

def run_ocr(image_path):
    """Runs OCR and saves results to a text file."""
    global ocr_running

    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        ocr_running = False
        return

    # Read and preprocess the captured image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Failed to read image '{image_path}'")
        ocr_running = False
        return

    processed_image = preprocess_image(image)

    # Convert back to 3-channel RGB for PaddleOCR
    image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2RGB)

    # Run OCR
    results = ocr.ocr(image_rgb, cls=True)

    if not results or all(not result for result in results):
        print("⚠️ No text detected.")
        ocr_running = False
        return

    detected_texts = []
    for result in results:
        for line in result:
            detected_texts.append(line[1][0])  # Extract recognized text

    if detected_texts:
        with open("ocr_result.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(detected_texts))
        print("✅ OCR result saved to ocr_result.txt")

    ocr_running = False

def listen_for_user_input():
    """Thread function to listen for user input."""
    global user_requested_ocr
    while True:
        user_input = input().strip().lower()
        if user_input == "r":
            user_requested_ocr = True

# Start a thread to handle user input
input_thread = threading.Thread(target=listen_for_user_input, daemon=True)
input_thread.start()

while True:
    success, frame = camera.read()
    if not success:
        print("⚠️ Failed to capture frame from webcam.")
        break

    # Show live camera feed
    cv2.imshow("OCR Live", frame)

    if user_requested_ocr and not ocr_running:
        ocr_running = True
        user_requested_ocr = False  # Reset user request flag

        print("Focusing on text... Please hold still for 3 seconds.")
        time.sleep(3)  # Give time for the user to adjust the camera

        # Capture and save image
        image_path = "captured_image.jpg"
        cv2.imwrite(image_path, frame)
        print(f"✅ Image captured and saved as {image_path}")

        # Start OCR in a separate thread
        threading.Thread(target=run_ocr, args=(image_path,)).start()

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()
