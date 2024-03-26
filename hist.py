from matplotlib import pyplot as plt
import cv2
import numpy as np
#直方图是对像素图像的统计分布,他统计了每个像素(0,255)的数量

img=cv2.imread("OpenCv/girl.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img_gray,cmap=plt.cm.gray)
hist=cv2.calcHist([img],[0],None,[256],[0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])#刻度
plt.show()