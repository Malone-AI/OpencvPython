from matplotlib import pyplot as plt
import cv2

img=cv2.imread("OpenCv/girl.jpg")

print(img.shape)

cv2.imshow("image",img)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("OpenCv/1.png",img)

cv2.destroyAllWindows()