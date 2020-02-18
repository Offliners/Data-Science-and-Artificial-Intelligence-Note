import cv2
import numpy as np
import matplotlib.pyplot as plt 

image_grey = cv2.imread('images/NTNUME.png', cv2.IMREAD_GRAYSCALE)

max_output_value = 255
neighborhood_size = 99
subtract_from_mean = 10
image_binarized = cv2.adaptiveThreshold(image_grey,
                                        max_output_value,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY,
                                        neighborhood_size,
                                        subtract_from_mean)

plt.imshow(image_binarized, cmap='gray')
plt.axis("off")
plt.show()
