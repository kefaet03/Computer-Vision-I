import cv2
import numpy as np

image = cv2.imread("F:\\He_is_enough03 X UniqoXTech X Dreams\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\documentscanner2.jpg")

print(image.shape)

imgResize = cv2.resize(image,(480,640))
print(imgResize.shape)

cv2.imshow("original image" , image)
cv2.imshow("resized image", imgResize)

cv2.waitKey(0)
