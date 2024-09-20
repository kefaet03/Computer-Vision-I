import cv2

cap = cv2.VideoCapture("E:\\He_is_enough03 X UniqoXTech X Dreams\\Click_here\\Computer Vision\\Udemy Course\\Basics of OpenCV\\Videos\\bikes.mp4")       


while True:
    success, frame = cap.read()  # Read the video frame
    if success:
        cv2.imshow("output",frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()








