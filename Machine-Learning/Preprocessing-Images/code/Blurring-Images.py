import cv2
import numpy as np
import matplotlib.pyplot as plt

images = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)
images_blurry = cv2.blur(images, (5, 5))

plt.imshow(images_blurry, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()
