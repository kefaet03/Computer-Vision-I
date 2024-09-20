import cv2
import  numpy as np

image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\lambo.png")
imgHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lowerrange = (0,53,139)
upperrange = (179,255,255) 

mask=cv2.inRange(imgHSV,lowerrange,upperrange)

color_img = cv2.bitwise_and(image,imgHSV,mask=mask)

cv2.imshow("color detected",color_img)

cv2.waitKey(0)



