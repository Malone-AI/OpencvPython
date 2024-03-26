import cv2

img=cv2.imread("OpenCv/jk.jpg",cv2.IMREAD_UNCHANGED)

shape=img.shape
print(img.shape)

if shape[2]==3 or shape[2]==4:
    img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cv2.imshow("Gray",img_gray)

cv2.imshow("Before",img)
cv2.waitKey(0)
cv2.destroyAllWindows()