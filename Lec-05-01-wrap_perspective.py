import cv2
import numpy as np

img = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\cards.jpg")

cv2.imshow("original image", img)

width,height = 350,500

cv2.circle(img,(111,219),3,(0,255,0),2)
cv2.circle(img,(287,188),3,(0,255,0),2)
cv2.circle(img,(154,482),3,(0,255,0),2)
cv2.circle(img,(352,440),3,(0,255,0),2)
cv2.imshow("points",img)


pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])

pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

# calculate the perspective transform matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)

outputimg= cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("output",outputimg)

cv2.waitKey(0)

