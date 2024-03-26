import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)

cv2.ellipse(img,(256,256),(100,50),0,30,180,(255,0,255),-1)

winname="example"
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows()