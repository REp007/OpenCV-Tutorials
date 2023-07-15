import cv2
import numpy as np
'''
 Face and Eye Detection
'''

cap = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')


while True:
    ret, frame = cap.read()

    # Change to gray scale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_img, 1)

    cv2.imshow('frame', frame)


    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()
