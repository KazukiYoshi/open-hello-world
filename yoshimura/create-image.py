import numpy as np 
import cv2 

img = np.zeros((400,400,3), np.uint8)
img[:,:] = [250 , 0, 0]
cv2.imwrite('c:/temp/buleImage1.jpg', img)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllwindows()


