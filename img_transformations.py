
from unittest.mock import NonCallableMagicMock
import cv2 as cv
from cv2 import warpAffine
import numpy as np

img=cv.imread('fudge.jpg')
cv.imshow('original',img)



### image translations:



def translate(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)



### rotation

def rotate(img,angle,rotpoint=None):
    (height,width)=(img.shape[0],img.shape[1])

    ## rotpoint,rotation matrix,dimensions

    if rotpoint==None:
        rotpoint=(width//2,height//2)

    rotmat=cv.getRotationMatrix2D(rotpoint,angle,1.0)

    dimensions=(width,height)


    return cv.warpAffine(img,rotmat,dimensions)






trans_img=translate(img,10,20)
cv.imshow('translated image',trans_img)

rot_img=rotate(img,-45,None)
cv.imshow('image_rotated',rot_img)



### flipping an image:

flip=cv.flip(img,-1)
cv.imshow('flipped',flip)


cv.waitKey(0)