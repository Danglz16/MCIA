import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from skimage.exposure import equalize_hist, equalize_adapthist

Tk().withdraw()
file_path = filedialog.askopenfilename(
    initialdir="C:\\Users\\death\\Documents\\Maestria\\MCIA\\Semestre_2\\Vision_Computadora\\img",
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path)

if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

A = A.astype(float) / 255.0

R2 = np.zeros_like(A)
R1 = equalize_hist(A)

if A.ndim == 3:
    R2[..., 0] = equalize_adapthist(A[..., 0])
    R2[..., 1] = equalize_adapthist(A[..., 1])
    R2[..., 2] = equalize_adapthist(A[..., 2])
else:
    R2 = equalize_adapthist(A)

plt.figure(figsize=(8,10))

plt.subplot(3,2,1); plt.imshow(A, cmap=None if A.ndim==3 else 'gray'); plt.title('Imagen Original'); plt.axis('off')
if A.ndim == 2:
    plt.subplot(3,2,2); plt.hist(A.ravel(), bins=256); plt.title('Histograma de A')
else:
    plt.subplot(3,2,2); plt.hist(rgb2gray(A).ravel(), bins=256); plt.title('Histograma de A')

plt.subplot(3,2,3); plt.imshow(R1, cmap=None if R1.ndim==3 else 'gray'); plt.title('Ecualizacion de histograma'); plt.axis('off')
if R1.ndim == 2:
    plt.subplot(3,2,4); plt.hist(R1.ravel(), bins=256); plt.title('Histograma de R1')
else:
    plt.subplot(3,2,4); plt.hist(rgb2gray(R1).ravel(), bins=256); plt.title('Histograma de R1')

plt.subplot(3,2,5); plt.imshow(R2, cmap=None if R2.ndim==3 else 'gray'); plt.title('Ecualizacion CLAHE'); plt.axis('off')
if R2.ndim == 2:
    plt.subplot(3,2,6); plt.hist(R2.ravel(), bins=256); plt.title('Histograma de R2')
else:
    plt.subplot(3,2,6); plt.hist(rgb2gray(R2).ravel(), bins=256); plt.title('Histograma de R2')

plt.show()
