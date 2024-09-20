import cv2

image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\face.png")
# cv2.imshow("output",image)

#setting the Threshold values
t_lower = 100
t_higher = 250
# Any gradient value greater than t_higher is considered an edge.
# Any gradient value below t_lower is considered non-edge.
# Gradient values between t_lower and t_higher are considered edges only if they are connected to pixels with gradients above t_higher.

edge = cv2.Canny(image,t_lower,t_higher)
cv2.imshow("output",edge)

cv2.waitKey(0)

