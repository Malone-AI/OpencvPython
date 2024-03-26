import cv2
from matplotlib import pyplot as plt

img=cv2.imread("OpenCv/girl.jpg",1)
shape=img.shape
cv2.imshow("colorful",shape)

img_cv_method=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)#这个是OpenCv自带的方法RGB转BGR

img_numpy_method=img[:,:,::-1]#这个是python自带的list方法

img_cv_gray=cv2.cvtColor(img_numpy_method,cv2.COLOR_RGB2BGR)

plt.subplot(2,2,1)#plt.subplot()是在同一框下绘制多图,plt(2,2,1)是把图像窗口分成2行2列，当前位置为1
plt.axis("off")#关闭坐标轴
plt.imshow(img_cv_method)

plt.subplot(2,2,2)
plt.axis("off")#关闭坐标轴
plt.imshow(img_numpy_method)

plt.subplot(2,2,3)
plt.axis("off")#关闭坐标轴
plt.imshow(img_cv_gray)

plt.subplot(2,2,4)
plt.axis("off")#关闭坐标轴
plt.imshow(img[:,:,::-1])#如果不做这一步转化,显示异常

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()