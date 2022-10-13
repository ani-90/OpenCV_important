## and or not xor:
## used a lot in image processing

### a pixel is turned off if value is 0, a pixel is turned on if value is 1

## we work with binary images:

from cmath import rect
import cv2 as cv
import numpy as np
from cv2 import bitwise_and
blank=np.zeros((500,500),dtype='uint8')
rectangle=cv.rectangle(blank,(55,55),(135,175),255,thickness=-1)
circle=cv.circle(blank,(100,100),50,255,thickness=-1)

bitwise_and=cv.bitwise_and(rectangle,circle)
bitwise_or=cv.bitwise_or(rectangle,circle)
bitwise_not_rectangle=cv.bitwise_not(rectangle)
bitwise_not_circle=cv.bitwise_not(circle)
bitwise_xor=cv.bitwise_xor(rectangle,circle)


cv.imshow('and',bitwise_and)
cv.imshow('or',bitwise_or)
cv.imshow('not_rect',bitwise_not_rectangle)
cv.imshow('not_circle',bitwise_not_circle)
cv.imshow('xor',bitwise_xor)

cv.waitKey(0)