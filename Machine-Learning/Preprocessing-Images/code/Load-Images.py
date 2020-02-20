import cv2
import matplotlib.pyplot as plt

image = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)

plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()

image_bgr = cv2.imread('images/NTNUME.png', cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()

print(image)
print(image.shape)
