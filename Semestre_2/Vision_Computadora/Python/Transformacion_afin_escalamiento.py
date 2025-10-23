import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

path = filedialog.askopenfilename()
img = cv2.imread(path)
cv2.imshow("Original Image", img)

# Duplicar tamaño
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scaled Image", res)
cv2.waitKey(0)