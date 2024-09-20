import cv2

image =  cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\cards2.jpg")
image = cv2.resize(image,(540,540))

imgBlur = cv2.GaussianBlur(image,(7,7),0)  # Applying Gaussian Blur #the kernal must be odd numbers
# The kernel size is (7,7). This means the area of blurring will be 14x14 pixels in total.
# https://pytorch.org/vision/stable/generated/torchvision.transforms.GaussianBlur.html

cv2.imshow("Original Image", image)   # Displaying the original image

cv2.imshow("Blur image", imgBlur)   # Displaying the blurred image

cv2.waitKey(0)
