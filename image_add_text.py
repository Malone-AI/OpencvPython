import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"OpenCV",(0,200),font,2,(0,255,0),5,cv2.LINE_AA)

winname="example"
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows()