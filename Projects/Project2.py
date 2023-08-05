#License : Plate Detection
import cv2
import numpy as np

img = cv2.imread(r'src\test3.PNG')

# cv2.imshow('Original Image',img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_img = cv2.bilateralFilter(gray_img, 11, 17, 17)

# cv2.imshow('Gray Image',gray_img)

edged_img = cv2.Canny(gray_img, 170, 200)

# find contours

cnts, new = cv2.findContours(edged_img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

images = img.copy()

cv2.drawContours(images, cnts, -1, (0, 255, 0), 3)

# cv2.imshow('Countours', images)


cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

screenCnt = None
image2 = img.copy()

cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
cv2.imshow('Top 30 Contours', image2)



i = 7
for c in cnts:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)


    if len(approx) == 4:
        screenCnt == approx
        x, y, w, h = cv2.boundingRect(c)
        new_img = images[y:y + h, x:x + w]
        cv2.imwrite(str(i) + '.png', new_img)
        i+=1
        break


# -1 signifies drawing all contours
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)


cv2.imshow('Final Image', img)

cv2.waitKey(0)

