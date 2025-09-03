import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    row,col,ch = frame.shape
    cv2.line(frame,(0,0),(col,row),(255,0,0),5)
    cv2.line(frame,(0,row),(col,0),(255,0,0),5)

    cv2.imshow('Dibujar Formas', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break