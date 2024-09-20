import cv2
import numpy as np

width = 640
height = 700

def preprocess_img(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image,150,350)
    kernel = np.ones((7,7),np.uint8)
    dilation_image = cv2.dilate(canny_image,kernel,iterations=2)
    erosion_image = cv2.erode(dilation_image,kernel,iterations=1)
    return erosion_image


def draw_contours(image):
    contours, hirearchy = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print(len(contours))
    maxarea = 0
    biggest = np.array([]) 
    for cnt in contours: 
        area = cv2.contourArea(cnt)
        print("AREA: ",area)
        cv2.drawContours(image,cnt,-1,(255,0,0),3)
        if area > 10000:
            peri = cv2.arcLength(cnt,True)
            approx =  cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxarea and len(approx)==4:
                biggest = approx
    print("biggest: ",biggest)
    print("Biggest Shape", biggest.shape)
    cv2.drawContours(image,biggest,-1,(0,255,0),10)
    cv2.imshow("contours",image)
    return biggest 


def reorder (biggest):
    biggest = biggest.reshape((4,2))
    print("biggest\n",biggest)

    newbig = np.zeros((4,1,2),np.int32)

    add = biggest.sum(1)
    print(add)

    newbig[0]= biggest[np.argmin(add)]
    newbig[3]= biggest[np.argmax(add)]

    diff = np.diff(biggest,axis=1)
    print(diff)

    newbig[1] = biggest[np.argmin(diff)]
    newbig[2] = biggest[np.argmax(diff)]

    print("new: ",newbig)

    return newbig


def wrap_perspective(image,biggest):
    pts1=np.float32(biggest)
    pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    image_wrapped = cv2.warpPerspective(image,matrix, (width,height))
    
    # img_crop = wrapped[0:wrapped.shape[0]-10,20:wrapped.shape[1]-10]
    # img_crop = cv2.resize(img_crop,(width,height))
    return  image_wrapped


image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\documentscanner2.jpg")
image= cv2.resize(image,(width,height))
# cv2.imshow("resized",image)

image_copy=image.copy()

preprocessed_img = preprocess_img(image_copy)
# cv2.imshow("preprocessed",preprocessed_img)

contours = draw_contours(preprocessed_img)

new_biggest_contours = reorder(contours)
iamge_wrappeed = wrap_perspective(image,new_biggest_contours)

cv2.imshow("wrappedd",iamge_wrappeed)

cv2.waitKey(0)
cv2.destroyAllWindows()





