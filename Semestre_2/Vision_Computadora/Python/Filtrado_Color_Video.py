import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # define range of blue color in HSV
    lower_skin = np.array([0,44,0])
    upper_skin = np.array([255,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_skin = cv2.inRange(hsv, lower_skin, upper_skin)

    mask = mask + mask_skin

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res_skin = cv2.bitwise_and(frame,frame, mask= mask_skin)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask_skin)
    cv2.imshow('res',res_skin)

    k = cv2.waitKey(5) & 0xFF # Esc key to stop
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()