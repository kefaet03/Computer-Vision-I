import cv2
import numpy as np

width = 600
height = 700

def preprocess_img(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image,275,350)
    kernel = np.ones((5,5),np.uint8)
    dilation_image = cv2.dilate(canny_image,kernel,iterations=2)
    erosion_image = cv2.erode(dilation_image,kernel,iterations=1)
    return erosion_image


def reorder (corners):
    corners = corners.reshape((4,2))
    newbig = np.zeros((4,1,2),np.int32)

    add = corners.sum(1)
    print(add)

    newbig[0]= corners[np.argmin(add)]
    newbig[3]= corners[np.argmax(add)]

    diff = np.diff(corners,axis=1)
    newbig[1] = corners[np.argmin(diff)]
    newbig[2] = corners[np.argmax(diff)]

    print(newbig)

    return newbig


def draw_contours(image):
    contours, hirearchy = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    corners = [] 
    for cnt in contours: 
        area = cv2.contourArea(cnt)
        cv2.drawContours(image,cnt,-1,(255,0,0),3)
        if area-2223.0 <= 50 :
            peri = cv2.arcLength(cnt,True)
            approx =  cv2.approxPolyDP(cnt,0.02*peri,True)
            if len(approx) == 4 :
                print(area)
                corners.append(approx)
    print("corners: ",corners)
    # ultimate_corners = [arr[0][0] for arr in corners]
    # print(ultimate_corners)
    # # print(np.array(ultimate_corners).shape)
    # ultimate_corners = reorder(np.array(ultimate_corners))
    image = cv2.resize(image,(540,540))
    cv2.drawContours(image,corners,-1,(0,255,0),10)
    cv2.imshow("hell",image)
    # return image_copy , ultimate_corners


def wrap_perspective(image,corners):
    pts1=np.float32(corners)
    pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    image_wrapped = cv2.warpPerspective(image,matrix, (width,height))
    
    # img_crop = wrapped[0:wrapped.shape[0]-10,20:wrapped.shape[1]-10]
    # img_crop = cv2.resize(img_crop,(width,height))
    return  image_wrapped



image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\documentscanner2.jpg")
image_copy = image.copy()
preprocessed_img = preprocess_img(image)
# img_contours,corners =  draw_contours(preprocessed_img)
draw_contours(preprocessed_img)
# image_wrap = wrap_perspective(image_copy,corners)



# cv2.imshow("original",image)
# cv2.imshow("preproccessed", preprocessed_img)
# cv2.imshow("contours", img_contours)
# cv2.imshow("Warped Image", image_wrap)



cv2.waitKey(0)
cv2.destroyAllWindows()