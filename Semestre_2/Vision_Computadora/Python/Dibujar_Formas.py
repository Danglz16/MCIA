import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

# Cargar Imagen
#path = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")])
#img = cv2.imread(path)
#img = cv2.resize(img, (512, 512))  # Escala la imagen a 512x512 píxeles

# INFO de la Imagen
#print(img.shape) # Dimensiones de la imagen
#row,col,ch = img.shape
#print(img.size)  # Total de pixeles
#print(img.dtype) # Tipo de dato de la imagen

# Create a black image
img = np.zeros((512,512,3), np.uint8)
#img.fill(255) # Cambiar Color del fondo

# Draw a diagonal blue line with thickness of 5 px
#                             B, G, R
cv2.line(img,(0,0),(511,511),(255,0,0),5) # Diagonal
cv2.line(img,(0,511),(511,0),(0,255,0),5) # Diagonal Inversa (X = linea 9 + linea 10)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) # Rectangulo
cv2.circle(img,(447,63), 63, (0,0,255), -1) # Circulo
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) # Elipse
cv2.ellipse(img,(256,256),(50,100),90,0,180,255,-1) # Elipse

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255)) # Dibujo Figura Amarilla

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('Dibujar Formas',img)
cv2.waitKey(0)
cv2.destroyAllWindows()