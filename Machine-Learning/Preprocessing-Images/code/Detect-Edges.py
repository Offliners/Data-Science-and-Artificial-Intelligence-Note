import cv2
import numpy as np
import matplotlib.pyplot as plt

image_gray = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)

median_intensity = np.median(image_gray)
lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)

plt.imshow(image_canny, cmap='gray')
plt.axis('off')
plt.show()
