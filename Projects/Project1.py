#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:08:04 2019
"""


# Colors and Color Detection
# Detect blue in video

import cv2
import numpy as np


# img = cv2.imread('..\src\colorful.jpg', 0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width= int(cap.get(3))
    height= int(cap.get(4))
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue sat value
    # whats this do if blue is 110-130 will it detect blue?
    # if its blue will keep it if not will make it black
    lower_blue = np.array([110, 50,50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('frame', result)

    
    if cv2.waitKey(1) == ord('q'):
        break






