import cv2
Img = cv2.imread('sumedh.jpg',0)  #colured
Img1 = cv2.imread('sumedh.jpg',1)  #black and white

resized = cv2.resize(Img,(650,500))
cv2.imshow('sumedh', resized)
 
cv2.waitKey(0)
 
cv2.destroyAllWindows()
