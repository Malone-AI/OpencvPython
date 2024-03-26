import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)

cv2.rectangle(img,(384,0),(510,128),(0,255,255),1)#参数为1是不填充内部,为-1时填充内部

winname="example"
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows()