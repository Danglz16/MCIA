import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print('Al inicio, las propiedades de la camara son: ')
print('El ancho de la imagen es: ', cap.get(3))
print('La altura de la imagen es: ', cap.get(4))
print('El numero de FPS es: ', cap.get(5))
w = cap.get(3)
h = cap.get(4)
FPS = cap.get(5)

cap.set(3, w*2)
cap.set(4, h*2)

print('Despues del cambio, las propiedades de la camara son: ')
print('El ancho de la imagen es: ', cap.get(3))
print('La altura de la imagen es: ', cap.get(4))
print('El numero de FPS es: ', cap.get(5))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Color',frame)
    cv2.imshow('Grayscale',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('./img/captured_image.png', frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()