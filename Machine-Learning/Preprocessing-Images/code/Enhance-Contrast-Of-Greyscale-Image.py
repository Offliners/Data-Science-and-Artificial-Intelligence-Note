import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)

image_enhanced = cv2.equalizeHist(image)

plt.imshow(image_enhanced, cmap='gray')
plt.axis('off')
plt.show()
