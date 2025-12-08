import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from tkinter import Tk, filedialog
from skimage.exposure import equalize_hist, equalize_adapthist
from skimage.transform import resize

Tk().withdraw()
file_path1 = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path1).astype(float) / 255.0
A_color = A.copy()
A_Gris = rgb2gray(A)
A_bin = A_Gris > threshold_otsu(A_Gris)

file_path2 = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

B = imread(file_path2).astype(float) / 255.0
B_color = B.copy()
B_Gris = rgb2gray(B)
B_bin = B_Gris > threshold_otsu(B_Gris)

bx, by, _ = B_color.shape

if A_color.ndim == 2:
    A_color = np.dstack([A_color, A_color, A_color])
if B_color.ndim == 2:
    B_color = np.dstack([B_color, B_color, B_color])

A_color = resize(A_color, (bx, by), preserve_range=True)

mask = (A_color > 0) & (B_color > 0)

C_color = A_color.copy()
C_color[~mask] = 0

plt.figure()
plt.subplot(1,3,1); plt.imshow(A_color); plt.title('Imagen A (color)'); plt.axis('off')
plt.subplot(1,3,2); plt.imshow(B_color); plt.title('Imagen B (color)'); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(C_color); plt.title('A & B (color)'); plt.axis('off')

bx, by = B_Gris.shape
A_Gris_res = resize(A_Gris, (bx, by), preserve_range=True)
C_Gris = (A_Gris_res > 0) & (B_Gris > 0)

plt.figure()
plt.subplot(1,3,1); plt.imshow(A_Gris_res, cmap='gray'); plt.title('Imagen A (gris)'); plt.axis('off')
plt.subplot(1,3,2); plt.imshow(B_Gris, cmap='gray'); plt.title('Imagen B (gris)'); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(C_Gris, cmap='gray'); plt.title('A & B (gris)'); plt.axis('off')

bx, by = B_bin.shape
A_bin_res = resize(A_bin.astype(float), (bx, by), preserve_range=True) > 0.5
C_bin = A_bin_res & B_bin

plt.figure()
plt.subplot(1,3,1); plt.imshow(A_bin_res, cmap='gray'); plt.title('Imagen A (binaria)'); plt.axis('off')
plt.subplot(1,3,2); plt.imshow(B_bin, cmap='gray'); plt.title('Imagen B (binaria)'); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(C_bin, cmap='gray'); plt.title('A & B (binaria)'); plt.axis('off')
plt.show()
