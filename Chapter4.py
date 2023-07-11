'''
4- SHAPES AND TEXTS
'''
import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)  # Add the third dimension for color (3 channels)
print(np.shape(img))  # (512, 512, 3)

# Color the image
img[200:300, 100:300] = [255, 0, 0]  # Assign blue color as an array [B, G, R]

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()