import cv2
import numpy as np

image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\shapes.png")

cv2.imshow("original image",image)

#step 1: convert the image into gray space
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale image", gray_img)

#step 2: canny edge detection
edges = cv2.Canny(gray_img,100,150)
cv2.imshow('Edges', edges)

#step 3: finding the contours
#contours means area
contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE )
print(contours)
print ("Number of Contours found = ", len(contours))

# #Step 4 : Drawing Squares around each contour
imagecopy = image.copy()
cv2.drawContours(imagecopy,contours,-1,(0,255,0),3)
cv2.imshow("Image with squares Around Contours", imagecopy)

cv2.waitKey(0)



















