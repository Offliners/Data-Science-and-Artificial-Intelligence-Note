import cv2
import numpy as np
import matplotlib.pyplot as plt

image_bgr = cv2.imread('images/NTNUME.png')

image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
image_rgb = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()
