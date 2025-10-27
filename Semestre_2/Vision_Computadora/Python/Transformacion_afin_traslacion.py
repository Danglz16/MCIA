import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

path = filedialog.askopenfilename()
img = cv2.imread(path)
cv2.imshow("Original Image", img)

rows, cols, ch = img.shape
for ii in range(10, 100, 2):
    M = np.float32([[1, 0, ii], [0, 1, ii]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.waitKey(100)
    cv2.imshow("Scaling Animation", dst)