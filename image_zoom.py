import cv2
import numpy as np

#图像缩放

#cv2.resize(src,dsize=None,fx,fy,interpolation)
#src原图
#dsize输出图像尺寸,与比例因子二选一
#fx,fy沿水平轴,垂直轴的比例因子
#interpolation插值方法

#cv2.INTER_NEAREST  最邻近插值,默认值
#cv2.INTER_CUBIC    三次样条插值
#cv2.INTER_LANCZOS4 lanczos插值
#cv2.INTER_AREA     区域插值

img=cv2.imread("OpenCv/jk.jpg")
print(img.shape)
img_zoom=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)#线性插值
cv2.imshow("zoom",img_zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()