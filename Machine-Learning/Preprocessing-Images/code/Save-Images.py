import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)

plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()

cv2.imwrite('images/NTNUME_new.png', image)
