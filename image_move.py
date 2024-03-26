#仿射变换函数
#cv2.warpAffine(src,M,dsize,flags,borderMode,borderValue)
#src输入图像
#M变换矩阵
#dsize输出图像的大小
#flags插值方法的组合(int)
#flags默认为flags=cv2.INTER_LINEAR,即线性插值
#此外还有
#cv2.INTER_NEAREST      最邻近插值
#cv2.INTER_AREA     区域插值
#cv2.INTER_CUBIC    三次样条插值
#cv2.INTER_LANCZOS4     Lanczos插值

#borderMode边界像素模式(int类型！)
#borderValue(!!!!重点)      边界填充值,默认为0

#M作为仿射变换矩阵,一般反映平移或旋转的关系,为InputArray类型的2x3的变换矩阵

import cv2
import numpy as np

img=cv2.imread("OpenCv/jk.jpg")
#变换矩阵M的构造
#第一行元素表示在x轴方向移动距离,第二行是y轴方向
H=np.float32([[1,0,50],[0,1,25]])
rows,cols=img.shape[:2]
print(img.shape)
print(rows,cols)

#rows和cols需要反置
res=cv2.warpAffine(img,H,(2*cols,2*rows))
cv2.imshow("Orignal",img)
cv2.imshow("New",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
