import numpy as np
import cv2
img=np.zeros((512,512,3),np.uint8)

cv2.circle(img,(447,63),63,(255,255,0),1)

winname="example"
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows()