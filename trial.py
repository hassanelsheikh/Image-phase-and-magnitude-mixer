import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread('bahey.jpeg', cv2.IMREAD_COLOR)
print(img.size)
# Compute 2D FFT
# fft = np.fft.fft2(img)

# # Shift zero frequency component to center of spectrum
# fft = np.fft.fftshift(fft)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))


phase = np.angle(fshift)

# # Take the logarithm of the magnitude for display purposes
# # magnitude = np.log(magnitude)

# # Display results
cv2.imshow('hmm', img)

cv2.imshow('Magnitude', magnitude_spectrum)
cv2.imshow('Phase', phase)
cv2.waitKey(0)
cv2.destroyAllWindows()