import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread(r"C:\Users\ASUS\Documents\Python\Programs\opencv_tutorialpoint\CR7.jpg",0)

# Perform the Discrete Fourier Transform (DFT)
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)  # Shift the zero frequency component to the center

# Compute the magnitude spectrum
magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

plt.subplot(121)
plt.imshow(img,cmap = "gray")
plt.title("Input Image")
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(magnitude_spectrum,cmap="gray")
plt.title("Magnitude Spectrum")
plt.xticks([])
plt.yticks([])

plt.show()