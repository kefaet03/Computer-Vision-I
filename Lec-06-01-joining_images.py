import cv2
import numpy as np

img1= cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\cards.jpg")
print(img1.shape)
img2= cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\car.jpg")
img2_resize = cv2.resize(img2, (477, 500)) # resize img2 to match the
print(img2_resize.shape)

imageHorizontalStack = np.hstack ((img1, img2_resize)) # horizontal stacking of images
cv2.imshow("horizontal", imageHorizontalStack)

imageVerticleStack = np.vstack((img1,img2_resize))
imageVerticleStack_resize = cv2.resize(imageVerticleStack,(554,639))# resize vertically stacked image
cv2.imshow("verticle", imageVerticleStack_resize)

cv2.waitKey(0)  &  0xFF == ord('s')

