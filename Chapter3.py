'''
3- Resizing and cropping and Rotating Images
'''
import cv2
import numpy as np

img = cv2.imread('src/colorful.jpg')


print(img.shape)

imgResize = cv2.resize(img,(150,150))
cv2.imshow('Image Resize', imgResize)
cv2.imshow('Image', img)


imgCropped = img[0:100, 0:100]

imgRoated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Image Cropped', imgCropped)
cv2.imshow('Image Rotated', imgRoated)
cv2.waitKey(0)
