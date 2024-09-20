import cv2

cap = cv2.VideoCapture(0) 

cap.set(3,640)    # set the width of capture (640 is default)
cap.set(4,480)    # set the resolution to be 640x480
cap.set(10,150)   # brightness

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
