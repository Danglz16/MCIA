import numpy as np
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

path = filedialog.askopenfilename()
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img = cv2.imread("X:\\img\\dg_4p.jpg")
#cv2.imwrite("X:\\img\\dg_4p_bn.jpg", img)

plt.imshow(img, interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()