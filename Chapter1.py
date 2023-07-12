'''
    Created on 2023年07月11日
'''

# 1- Read Image, Video and Webcam
import cv2

img = cv2.imread('colorful.jpg')

cv2.imshow('img', img)

cv2.waitKey(0)



# For Video

cap = cv2.VideoCapture('src/vedio.mp4')

while True:
    success, img = cap.read()

    cv2.imshow('frmVedio', img)

    if cv2.waitKey(1) == ord('q'):
        break


# For Webcam

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow('frmWebcam', img)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()


# Save the image

cv2.imwrite('savedImage.jpg', img)  # (name, image)
