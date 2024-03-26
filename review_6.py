from matplotlib import pyplot as plt
import cv2

img=cv2.imread("OpenCv/jk.jpg")

img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

plt.imshow(img_gray,cmap=plt.cm.gray)
hist=cv2.calcHist([img],[2],None,[256],[0,256])

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixel")
plt.plot(hist)
plt.xlim([0,256])
plt.show()