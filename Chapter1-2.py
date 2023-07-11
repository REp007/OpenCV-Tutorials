'''
1- Read Image, Video and Webcam
2- Basic Functions
'''
import cv2
import numpy as np

# image Reader

img = cv2.imread('colorful.jpg')
kernel = np.ones((5,5), np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7,7),0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny,kernel=kernel, iterations=1)
imgEroded = cv2.erode(imgDialation,kernel=kernel,iterations=1)
# print(img.shape)
# cv2.imshow('Gray', imgGrey)
# cv2.imshow('Blur', imgBlur)
# cv2.imshow('imgCanny', imgCanny)
# cv2.imshow('imgDialation', imgDialation)
cv2.imshow('imgEroded', imgEroded)

cv2.waitKey(0)


# For Video

# cap = cv2.VideoCapture(0)

# while True:

#     success, img = cap.read()

#     cv2.imshow('vedio', img)


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break