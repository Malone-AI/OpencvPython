import cv2

#读入原始图像,使用cv2.IMREAD_UNCHANGED
img=cv2.imread("OpenCv/girl.jpg",cv2.IMREAD_UNCHANGED)

#查看打印图像的shape
shape=img.shape
print(shape)

#判断三通道还是四通道
if shape[2]==3 or shape[2]==4:
    #将彩色图转化为三通道图
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("img_gray",img_gray)
    #cv2.waitKey(0)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()