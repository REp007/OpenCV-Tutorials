'''
    CONTOURS / SHAPE DETECTION

    
    #*Contours are curves joining all the 
    continuous points (along the boundary), 
    having same color or intensity.*
'''
import cv2
import numpy as np

img = cv2.imread('src/Geometric.jpg')
imgContour = img.copy()
print(img.shape)
cv2.imshow('Original', img)




# ! 1- Convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ! 2- Blur the image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

# ! 3- Find the edges
imgCanny = cv2.Canny(imgBlur, 50, 50)

# ! 4- Find the contours


ret, thresh = cv2.threshold(imgCanny, 125, 255, cv2.THRESH_BINARY )

contours, hierarchies = cv2.findContours(imgCanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

# ! 5- Draw the contours
cv2.drawContours(imgContour, contours, -1, (0,255,0), 1)
cv2.imshow('Contour img', imgContour)
cv2.imwrite('Result/Chapter8/ContourImg.jpg', imgContour)





# cv2.imshow('Gray', imgGray)
# cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Contour img', imgContour)

cv2.waitKey(0)
cv2.destroyAllWindows()







