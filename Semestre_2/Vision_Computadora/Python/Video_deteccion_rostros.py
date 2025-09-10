import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('Vision_Computadora/Python/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    print(faces)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    # Display the resulting frame
    cv2.imshow('Color',frame)
    cv2.imshow('ROI Color',roi_color)
    cv2.imshow('ROI Gris',roi_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()