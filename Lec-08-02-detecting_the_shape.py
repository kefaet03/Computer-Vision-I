import cv2
import numpy as np

image = cv2.imread("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Pictures\\shapes.png")

cv2.imshow("original image",image)

#step 1: convert the image into gray space
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray scale image", gray_img)

#step 2: canny edge detection
edges = cv2.Canny(gray_img,100,150)
# cv2.imshow('Edges', edges)

#step 3: finding the contours
contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE )
print ("Number of Contours found = ", len(contours))

imagecopy = image.copy()
# cv2.imshow("trial",imagecopy)

#Step 4 : Drawing Squares around each contour
for cnt in contours:
    cv2.drawContours(imagecopy,cnt,-1,(0,255,0),3)
    area = cv2.contourArea(cnt)
    # print("AREA ",area)

    #step 4: drawing the arc length of our contous
    perimeter = cv2.arcLength(cnt,True)
    # print("PERIMETER ",perimeter)

    #step 5: finding corner points of each of the shapes
    approx = cv2.approxPolyDP(cnt,0.02*perimeter, True)

    print(approx)

    #step 6: length of the corner points 
    print("length of the corner points ", len(approx))

    objcor = len(approx)

    #step 7: creat bounding boxes around each of the shape in the image
    x,y,z,h = cv2.boundingRect(approx)

    print(x,y,z,h)

    cv2.rectangle(imagecopy,(x,y),(x+z,y+h),[0,255,0],2)

    if objcor==3:
        obj_typ = " Triangle "
    elif objcor == 4:
        aspect_ratio = z/float(h)
        if aspect_ratio > 0.98 and aspect_ratio < 1.03:
            obj_typ = " Square "
        else:
            obj_typ = " Rectangle "
    elif objcor > 4 :    
        obj_typ = "Circle"
    else:
        obj_typ = "NONE"

    
    cv2.putText(imagecopy,obj_typ,(x+(z//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_PLAIN,0.7,(0,0,0),2)
    cv2.imshow("Image with squares Around Contours", imagecopy)


cv2.waitKey(0)


