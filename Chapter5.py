'''
WARP PRESPECTIVE
'''
import cv2
import numpy as np

## WARP PRESPECTIVE
    # 1. Get the image
    # 2. Get the points of the image
    # 3. Get the points of the output
    # 4. Get the matrix
    # 5. Apply the matrix

img = cv2.imread('src/card.png')

print(np.shape(img)) # (450, 461, 3)


width, height = 250, 350


pts1 = np.float32([[225,93], [430, 137], [164,382], [368,426]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])


matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Original', img)
cv2.imwrite('Result/Chapter5/OriginalImg.png', img=img)
cv2.imshow('img Output', imgOutput)
cv2.imwrite('Result/Chapter5/ResultImg.png', imgOutput)



cv2.waitKey(0)

cv2.destroyAllWindows()