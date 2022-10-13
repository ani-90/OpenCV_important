
import cv2 as cv
from cv2 import scaleAdd

# img=cv.imread('fudge.jpg')
# cv.imshow('Fudge',img)
# cv.waitKey(0)

capture=cv.VideoCapture('"C:/Users/bala/Videos/RealPlayer Downloads/A.R. Rahman - Tere Bina Best Video  Guru Aishwarya Rai Abhishek Bachchan Chinmayi.mp4"')



def rescale(frame,scale=0.3):
    
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


while True:
    istrue,frame=capture.read()
    
    frame_resized=rescale(frame,scale=0.1)
    cv.imshow('video',frame_resized)

    if cv.waitkey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()