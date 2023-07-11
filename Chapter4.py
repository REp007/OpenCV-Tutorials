'''
4- SHAPES AND TEXTS
'''
import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)  # Add the third dimension for color (3 channels)
print(np.shape(img))  # (512, 512, 3)

# Color the image

# img[:] = [255, 0, 0]  # Assign blue color as an array [B, G, R]



# How to get width and Height

width = img.shape[1]
height = img.shape[0]



# Create a line

cv2.line(img,(0,0),(300,300), (0,255,0), 6)  # (image, start point, end point, color, thickness)



# Draw a rectangle
cv2.rectangle(img, (0,0) , (250,350),(255,0,0), 2)  # (image, start point, end point, color, thickness)




# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()