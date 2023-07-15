'''
JOINING IMAGES
'''
import cv2
import numpy as np


img = cv2.imread('src/colorful.jpg')

# Horizontal Stacking

hor = np.hstack((img, img))

cv2.imshow('Horizontal', hor)
cv2.imwrite('Resources/Chapter6/hor.jpg', hor)


# Vertical Stacking

ver = np.vstack((img,img))

cv2.imshow('Vertical', ver)
cv2.imwrite('Result/Chapter6/ver.jpg', ver)


cv2.waitKey(0)
cv2.destroyAllWindows()


# TODO : Function StackingImages()

def StackingImages():
    pass
