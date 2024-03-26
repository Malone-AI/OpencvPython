import cv2
from matplotlib import pyplot as plt

img1=cv2.imread("OpenCv/an.jpg",cv2.IMREAD_UNCHANGED)
img2=cv2.imread("OpenCv/liang.jpg",cv2.IMREAD_UNCHANGED)

color=["b","g","r"]

for i,color in enumerate(color):
    hist=cv2.calcHist([img1],[i],None,[256],[0,256])
    plt.figure()
    plt.title(color)
    plt.xlabel("Bins")
    plt.ylabel("num of perplex")
    plt.xlim([0,256])
    label="bgr"
    plt.plot(hist,label=label[i])
plt.show()

color=list(color)

for i,color in enumerate(color):
    hist=cv2.calcHist([img2],[i],None,[256],[0,256])
    plt.figure()
    plt.title(color)
    plt.xlabel("Bins")
    plt.ylabel("num of perplex")
    plt.xlim([0,256])
    label="bgr"
    plt.plot(hist,label=label[i])
plt.show()
