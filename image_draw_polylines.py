#绘制多边形
import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)

pts=np.array([[10,5],[50,10],[70,20],[20,30]])
print(pts)

pts=pts.reshape((-1,1,2))
print(pts)
cv2.polylines(img,[pts],True,(0,255,255))

winname="example"
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows()