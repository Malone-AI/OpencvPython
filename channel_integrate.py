#将彩色图像,分成b,g,r 3个单通道图像方便我们对BGR三个通道进行单独操作
#用到的函数cv2.split(img)
#通道分离成B,G,R三个通道后对单通道进行修改,然后使用cv2.merge()进行合并,参数只有一个,即图像矩阵
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("OpenCv/girl.jpg",1)

#通道分离
b,g,r=cv2.split(img)

#修改b通道
g[:]=0

#合并修改后的通道
img_merge=cv2.merge([b,g,r])

cv2.imshow("merge",img_merge)

cv2.waitKey(0)
cv2.destroyAllWindows()