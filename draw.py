### painting on an image


import cv2 as cv
from cv2 import FILLED
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
blank[200:300,300:400]=10,2,32
### rectangle

### syntax: cv.rectangle(image,(start),(end),(colors),thickness)
cv.rectangle(blank,(0,0),(250,125),(0,255,0),thickness  =2)
cv.imshow('Blank Image',blank)

#### circle
## syntax: cv.circle(image,(midpoint),radius,(colors),thickness)
cv.circle(blank,(250,250),40,(0,0,255),thickness=1)


cv.imshow('Blank image',blank)



### line
### syntax: cv.line(image,(start),(end),(colors),thickness)
cv.line(blank,(0,0),(250,250),(255,0,255),thickness=3)
cv.imshow('BLank image',blank)




### text on image


### cv.putText(image,text,(position),fontstyle,fontsize,(colors),thickness)
cv.putText(blank,'Hello world',(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('BLank image',blank)
cv.waitKey(0)