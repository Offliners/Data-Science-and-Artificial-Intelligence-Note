import cv2
import numpy as np
import matplotlib.pyplot as plt

image_bgr = cv2.imread('images/NTNUME.png')
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

corners_to_detect = 10
minimum_quality_score = 0.05
minimum_distance = 25

corners = cv2.goodFeaturesToTrack(image_gray,
                                  corners_to_detect,
                                  minimum_quality_score,
                                  minimum_distance)

corners = np.float32(corners)

for corner in corners:
    x, y = corner[0]
    cv2.circle(image_bgr, (x, y), 10, (255, 255, 255), -1)

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

plt.imshow(image_gray, cmap='gray')
plt.axis('off')
plt.show()
