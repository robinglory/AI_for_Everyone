import cv2
import face_recognition as FR
import numpy as np

# Load the image with OpenCV
image_path = r"C:\Users\ASUS\Documents\Python\Programs\demoImages\known\Donald-Trump-gray.jpg"
donFace = cv2.imread(image_path)

# Check if the image is loaded properly
if donFace is None:
    raise ValueError("Image not found. Check the file path and ensure the image exists.")

# Print image details for debugging
print(f"Original Image dtype: {donFace.dtype}, shape: {donFace.shape}")

# Convert the image to RGB (OpenCV loads images in BGR format by default)
donFace_rgb = cv2.cvtColor(donFace, cv2.COLOR_BGR2RGB)

# Ensure the image is 8-bit and RGB
if donFace_rgb.dtype != 'uint8':
    donFace_rgb = donFace_rgb.astype('uint8')

# Debugging step: Save and reload the image
cv2.imwrite("temp_image.jpg", cv2.cvtColor(donFace_rgb, cv2.COLOR_RGB2BGR))
donFace_rgb = cv2.imread("temp_image.jpg")
donFace_rgb = cv2.cvtColor(donFace_rgb, cv2.COLOR_BGR2RGB)

# Verify RGB format
print(f"Converted Image dtype: {donFace_rgb.dtype}, shape: {donFace_rgb.shape}")

# Detect face locations
try:
    faceLoc = FR.face_locations(donFace_rgb)
except RuntimeError as e:
    raise RuntimeError(f"Face recognition failed: {e}")

# Output face locations
print("Face Locations:", faceLoc)
