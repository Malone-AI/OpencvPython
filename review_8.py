import cv2
from matplotlib import pyplot as plt

img=cv2.imread("OpenCv/jk.jpg")
cv2.imshow("jk",img)
color=['b','g','r']

for i,color in enumerate(color):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.title("jk")
    plt.xlabel("Bins")
    plt.ylabel("num of perplex")
    label="bgr"
    plt.plot(hist,color=color,label=label[i])
    plt.xlim([0,256])

plt.legend()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()