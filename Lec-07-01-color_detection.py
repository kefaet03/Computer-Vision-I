import cv2
import  numpy as np

def empty(a):
    pass

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",640,240)

cv2.createTrackbar("Hue Min","trackbars",0,179,empty)
cv2.createTrackbar("Hue Max", "trackbars", 179,179,empty)
cv2.createTrackbar("Sat Min", "trackbars", 0,255,empty)
cv2.createTrackbar("Sat Max", "trackbars", 255,255,empty)
cv2.createTrackbar("Val Min", "trackbars", 0,255,empty)
cv2.createTrackbar("Val Max", "trackbars", 255,255,empty)

while True:
    image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\lambo.png")
    
    imgHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("Hue Min","trackbars")
    s_min=cv2.getTrackbarPos("Sat Min","trackbars")
    v_min=cv2.getTrackbarPos("Val Min","trackbars")
    h_max=cv2.getTrackbarPos("Hue Max","trackbars")
    s_max=cv2.getTrackbarPos("Sat Max","trackbars")
    v_max=cv2.getTrackbarPos("Val Max","trackbars") 
    
    # print(h_max,h_min,s_max,s_min,v_max,v_min)
    lower =  np.array([h_min,s_min,v_min])
    upper =  np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("original",image)

    cv2.imshow("hsv",imgHSV)

    cv2.imshow("mask",mask)

    cv2.waitKey(1)
