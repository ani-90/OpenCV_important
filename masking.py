## masking is a concept which helps us in focussing on certain parts of the image

 
import cv2 as cv
from cv2 import circle
import numpy as np

img=cv.imread('cat1.jpg')
cv.imshow('cat',img)
print(img.shape)


### masking: to focus on the face of a cat

blank=np.zeros((img.shape[0],img.shape[1]),dtype='uint8')
## mask:
mask1=cv.circle(blank.copy(),(img.shape[1]//2-100,img.shape[0]//2+180),100,255,-1)



mask2=cv.rectangle(blank.copy(),(120,190),(300,390),255,thickness=-1)

weird_shape=cv.bitwise_and(mask1,mask2)
cv.imshow('weird mask',weird_shape)

masked_img=cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('masked part',masked_img)


cv.waitKey(0)