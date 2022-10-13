#### splitting image into its b,g,r components


import cv2 as cv
import numpy as np


img=cv.imread('fudge.jpg')
cv.imshow('original',img)

### splitting an image into blue,green and red


b,g,r=cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)


### converting the b,g,r grayscale components into their respective colors: using a blank image


blank=np.zeros(img.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])



cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)



cv.waitKey(0)