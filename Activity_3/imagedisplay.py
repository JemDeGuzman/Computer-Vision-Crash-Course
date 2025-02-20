import cv2
import numpy as np

img = cv2.imread('OpenCV Crash Course/viktor.png')
cv2.imshow('Viktor', img)
cv2.waitKey()
cv2.destroyAllWindows()