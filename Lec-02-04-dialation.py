import cv2
import numpy as np

image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\documentscanner2.jpg")
cv2.imshow("outputR",image)

#setting the Threshold values
t_lower = 225
t_higher = 350

imgCanny = cv2.Canny(image,t_lower,t_higher)

kernel = np.ones((7,7),np.uint8)
# print(kernel)
#why we use array of ones in case of kernel in opencv?
imageDialation = cv2.dilate(imgCanny, kernel , iterations=1)

cv2.imshow("outputD",imageDialation)
cv2.imshow("outputC",imgCanny)

cv2.waitKey(0)