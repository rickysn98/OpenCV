import cv2

# cargar imagen
img = cv2.imread("lena.jpg",0)

cv2.imshow("curso dia uno",img)

cv2.waitKey(4000)
cv2.destroyAllWindows()