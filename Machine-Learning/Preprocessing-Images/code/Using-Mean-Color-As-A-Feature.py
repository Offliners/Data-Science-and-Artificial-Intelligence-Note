import cv2
import numpy as np
import matplotlib.pyplot as plt

image_bgr = cv2.imread('images/NTNUME.png', cv2.IMREAD_COLOR)

channels = cv2.mean(image_bgr)
observation = np.array([(channels[2], channels[1], channels[0])])
print(observation)

plt.imshow(observation)
plt.axis('off')
plt.show()
