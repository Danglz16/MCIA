import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    initialdir="C:\\Users\\death\\Documents\\Maestria\\MCIA\\Semestre_2\\Vision_Computadora\\img",
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path)

if A.shape[-1] == 4:
    A = A[..., :3]

A = A.astype(float) / 255.0

m = 0.05
M = 0.90

R = (A - m) / (M - m)
R = np.clip(R, 0, 1)

plt.figure(figsize=(8,8))

plt.subplot(2,2,1); plt.imshow(A); plt.title('Imagen Original'); plt.axis('off')

if A.ndim == 2:
    plt.subplot(2,2,2); plt.hist(A.ravel(), bins=256); plt.title('Histograma de A')
else:
    plt.subplot(2,2,2); plt.hist(rgb2gray(A).ravel(), bins=256); plt.title('Histograma de A')

plt.subplot(2,2,3); plt.imshow(R); plt.title('Ajuste Lineal'); plt.axis('off')

if R.ndim == 2:
    plt.subplot(2,2,4); plt.hist(R.ravel(), bins=256); plt.title('Histograma de R')
else:
    plt.subplot(2,2,4); plt.hist(rgb2gray(R).ravel(), bins=256); plt.title('Histograma de R')

plt.show()
