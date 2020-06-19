import cv2
face_cas = sv2.CascadeClassifier("sumedh.jpg")
img = cv2.imread("sumedh.jpg")
gray_img = cv2.cvtColor(img,cv2,COLOR_BGR2GRAY)
