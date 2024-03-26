from matplotlib import pyplot as plt
import cv2
girl=cv2.imread("OpenCv/girl.jpg")
cv2.imshow("girl",girl)
color=("b","g","r")

#使用for 循环遍历color列表,enumerate枚举返回索引和值
for i,color in enumerate(color):
    hist=cv2.calcHist([girl],[i],None,[256],[0,256])
    plt.title("girl")
    plt.xlabel("Bins")
    plt.ylabel("num of perplex")
    label="bgr"
    plt.plot(hist,color=color,label=label[i])
    plt.xlim([0,256])

plt.legend()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()