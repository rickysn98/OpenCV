# python program to illustrate
# arithmetic operation of
# substraction of two images

# organizing imports
from cv2 import cv2
import numpy as np

# path to input images are specified and 
# images are loaded with imread command
image1 = cv2.imread('inp1.jpg')
image2 = cv2.imread('inp2.jpg')

# cv2.subtract is applied over the 
# image inputs with applied parameters
sub = cv2.subtract(image1, image2)

# the window showing output image
# with the substracted image
cv2.imshow('Substracted image', sub)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()