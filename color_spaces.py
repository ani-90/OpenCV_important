### colro spaces: system of representing an array of pixel colors
### eg: RGB,HSV
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('fudge.jpg')
cv.imshow('actual',img)


# BGR to Gray

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)


# BGR TO HSV

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv image',hsv)


rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)