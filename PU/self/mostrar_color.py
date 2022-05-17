from cv2 import cv2

image = cv2.imread("rgb.png")
B, G, R = cv2.split(image)
#se separan los canales correspondientes

cv2.imshow("original", image)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)

cv2.imshow("green", G)
cv2.waitKey(0)

cv2.imshow("red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()