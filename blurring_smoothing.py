# blurring and smoothing is done to remove noise from the image

import cv2 as cv

img=cv.imread('fudge.jpg')
cv.imshow('original',img)


#  averaging: divide the image into n*n, compute the
## pixel of center grid as average of surrounding grids


avg_blur=cv.blur(img,(5,5))
cv.imshow('average',avg_blur)

## gaussian blur: similar to the above, blurring is less

gauss_blur=cv.GaussianBlur(img,(5,5),0)
cv.imshow('gaussian_blur',gauss_blur)


## median blur: find median of surrounding pixels->most effective in removing noise

median=cv.medianBlur(img,5)
cv.imshow('median blur',median)



## bilateral blurring: best method, used in lot of cv projects, retians the edges while the other methods mentioned above do  not

## syntax: cv.bilateralFilter(image,diameter of pixel neighbourhood,sigma_color,sigma_space)
bilateral_blur=cv.bilateralFilter(img,15,35,25)
cv.imshow('bilateral',bilateral_blur)


cv.waitKey(0)


