import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from scipy.signal import convolve2d

file_path = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

if A.ndim == 2:
    A_gray = A
else:
    A_gray = rgb2gray(A)

ax, ay = A_gray.shape

k33 = np.ones((3, 3)) / (3 * 3)
k55 = np.ones((5, 5)) / (5 * 5)
k77 = np.ones((7, 7)) / (7 * 7)

kernel_horizontal = np.ones((1, 10)) / 10
kernel_vertical   = np.ones((10, 1)) / 10

if A.ndim == 3:
    R33 = np.zeros_like(A)
    R55 = np.zeros_like(A)
    R77 = np.zeros_like(A)
    R_horizontal = np.zeros_like(A)
    R_vertical = np.zeros_like(A)

    for i in range(A.shape[2]):
        R33[..., i] = convolve2d(A[..., i], k33, mode='same')
        R55[..., i] = convolve2d(A[..., i], k55, mode='same')
        R77[..., i] = convolve2d(A[..., i], k77, mode='same')

        R_horizontal[..., i] = convolve2d(A[..., i], kernel_horizontal, mode='same')
        R_vertical[..., i]   = convolve2d(A[..., i], kernel_vertical, mode='same')
else:
    R33 = convolve2d(A, k33, mode='same')
    R55 = convolve2d(A, k55, mode='same')
    R77 = convolve2d(A, k77, mode='same')

    R_horizontal = convolve2d(A, kernel_horizontal, mode='same')
    R_vertical   = convolve2d(A, kernel_vertical, mode='same')

plt.figure(1)
plt.subplot(2,2,1); plt.imshow(A, cmap='gray' if A.ndim == 2 else None); plt.title('Imagen Original'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(R33, cmap='gray' if A.ndim == 2 else None); plt.title('Media 3x3'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(R55, cmap='gray' if A.ndim == 2 else None); plt.title('Media 5x5'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(R77, cmap='gray' if A.ndim == 2 else None); plt.title('Media 7x7'); plt.axis('off')

plt.figure(2)
plt.subplot(1,3,1); plt.imshow(A, cmap='gray' if A.ndim == 2 else None); plt.title('Imagen Original'); plt.axis('off')
plt.subplot(1,3,2); plt.imshow(R_horizontal, cmap='gray' if A.ndim == 2 else None); plt.title('Media Horizontal 1x10'); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(R_vertical, cmap='gray' if A.ndim == 2 else None); plt.title('Media Vertical 10x1'); plt.axis('off')

plt.show()
