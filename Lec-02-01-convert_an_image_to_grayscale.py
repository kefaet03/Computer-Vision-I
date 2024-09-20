import cv2

image =  cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\cards2.jpg")
image = cv2.resize(image,(540,540))
# cv2.imshow("Output show", image)

imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to BGR

cv2.imshow("Output show" , imgGray)

cv2.waitKey(0)

