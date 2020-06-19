import cv2
Img = cv2.imread('sumedh.jpg',0)  #colured
Img1 = cv2.imread('sumedh.jpg',1)  #black and white

cv2.imshow('sumedh', Img)
cv2.waitKey(0)
cv2.destroyAllWindows()

