import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)

image_cropped = image[:,:126]

plt.imshow(image_cropped, cmap='gray')
plt.axis('off')
plt.show()
