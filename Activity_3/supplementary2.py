# Similar to activity #1, show an image of your favorite character on a window. Afterwards, slice so that only the character's face is displayed.
import cv2
import numpy as np

img = cv2.imread('OpenCV Crash Course/viktor.png')
img1 = img.copy()
img2 = img[75:325, 150:350]
images = [img1, img2]
names = ['Vik1', 'Vik2']
for i in range(2):
    cv2.imshow(names[i], images[i])
    cv2.waitKey()

cv2.destroyAllWindows()