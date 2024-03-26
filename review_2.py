from matplotlib import pyplot as plt
import cv2

img=cv2.imread("OpenCv/girl.jpg")

img_cv2_method=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

img_numpy_method=img[:,:,::-1]

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.subplot(2,2,1)
plt.axis("off")
plt.title("Colorful")
plt.imshow(img)

plt.subplot(2,2,2)
plt.axis("off")
plt.title("BGR")
plt.imshow(img_cv2_method)

plt.subplot(2,2,3)
plt.axis("off")
plt.title("BGR")
plt.imshow(img_numpy_method)

plt.subplot(2,2,4)
plt.axis("off")
plt.title("GRAY")
plt.imshow(img_gray)

plt.show()