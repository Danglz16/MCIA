import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

path = filedialog.askopenfilename()
img = cv2.imread(path)
cv2.imshow("Original Image", img)
rows, cols, ch = img.shape

for angle in range(0, 360, 1):
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow(f"Rotated Image {angle} degrees", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()