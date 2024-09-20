import cv2
import numpy as  np

#this is a gray scale image
image = np.ones((300,512,3))
# cv2.imshow("Output",image)

#color functionality
image[75:225,128:384]=0,255,0
cv2.imshow("Ouput is here",image)

#drawing a line in the frame
# cv2.line(image,(0,0),(image.shape[1],image.shape[0]),(0,0,255),2)
cv2.line(image,(128,75),(384,75),(0,0,255),2)
cv2.line(image,(128,75),(128,225),(0,0,255),2)
cv2.line(image,(128,225),(384,225),(0,0,255),2)
cv2.line(image,(384,225),(384,75),(0,0,255),2)

# #drawing a rectangle in the frame
cv2.rectangle(image,(125,72),(387,228),(0,0,0),1)

# #drawing a circle in the frame
cv2.circle(image,(256,150),50,(0,0,255),3)

# #adding text to the frame
cv2.putText(image,"Bangladesh !!!",(128,245),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)

cv2.imshow("Ouput is here",image)
cv2.waitKey(0)

