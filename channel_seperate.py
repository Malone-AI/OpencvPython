#将彩色图像,分成b,g,r 3个单通道图像方便我们对BGR三个通道进行单独操作
#用到的函数cv2.split(img)
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("OpenCv/girl.jpg",1)

b,g,r=cv2.split(img)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

cv2.waitKey(0)
cv2.destroyAllWindows()