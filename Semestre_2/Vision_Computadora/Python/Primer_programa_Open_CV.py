import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

path = filedialog.askopenfilename()
img = cv2.imread(path, 0)
#img = cv2.imread("X:\\img\\dg_4p.jpg")
cv2.imwrite("X:\\img\\dg_4p_bn.jpg", img)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()