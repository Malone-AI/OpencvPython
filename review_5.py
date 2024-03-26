import cv2

img=cv2.imread("OpenCv/jk.jpg")

b,g,r=cv2.split(img)

r[:]=0

img_merge=cv2.merge([b,g,r])
cv2.imshow("merge",img_merge)

cv2.waitKey(0)
cv2.destroyAllWindows()