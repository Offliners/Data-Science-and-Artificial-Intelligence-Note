import cv2
import matplotlib.pyplot as plt

image = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)

plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()
