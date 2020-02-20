import cv2
import numpy as np
import matplotlib.pyplot as plt

image_bgr = cv2.imread('images/NTNUME.png')
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

lower_blue = np.array([50, 100, 50])
upper_blue = np.array([130, 255, 255])
mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

image_bgr_masked = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)
image_rgb = cv2.cvtColor(image_bgr_masked, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb, cmap='gray')
plt.axis('off')
plt.show()
