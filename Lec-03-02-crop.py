import cv2
import numpy as np

image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\documentscanner2.jpg")
# cv2.imshow("original",image)

imgResize = cv2.resize(image,(480,640))
cv2.imshow("resized",imgResize)

imgCrop = imgResize[100:600,15:450]

print(imgCrop.shape)

cv2.imshow("cropped",imgCrop)
cv2.waitKey(0) & 0xFF == ord('q')



