import cv2

img=cv2.imread("OpenCv/code.png",1)#第二个参数是读取方式,0是灰度加载,1是彩色加载

print(img.shape)

#cv2.imshow()函数进行图像显示
cv2.imshow("image",img)#第一个参数是窗口的命名,第二个参数是显示的图像的数组

#waitKey()是一个键盘绑定函数,参数表示等待时间,单位是毫秒,0代表等待键盘输入
#cv2.waitKey(0)
k=cv2.waitKey(0)
if k==27:
    #输入ESC退出
    cv2.destroyAllWindows()
elif k==ord('s'):
    #输入S键保存图片并退出
    cv2.imwrite("OpenCv/split_.png",img)#第一个参数保存路径+名称,第二个参数是需要保存的图像的数组

#destroyAllWindows()删除窗口
#默认所有窗口,参数一为待删除窗口名
cv2.destroyAllWindows()