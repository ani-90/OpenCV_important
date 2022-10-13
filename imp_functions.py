import cv2 as cv

### converting image to grayscale

img=cv.imread('fudge.jpg')
cv.imshow('Color image',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)


## Blur an image
# gaussian blur
blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('blurred',blur)

### edge cascade

canny=cv.Canny(img,125,175)
cv.imshow('edges',canny)



### dilating an image

dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated',dilated)


#### cropping

cropped=img[200:400,200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)
