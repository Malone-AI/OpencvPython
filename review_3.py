import cv2

def color_space_demo(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    cv2.imshow("gray",gray)
    hsv=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    cv2.imshow("hsv",hsv)

src=cv2.imread("OpenCv/jk.jpg")
cv2.imshow("before",src)
color_space_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()