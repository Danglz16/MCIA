import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from scipy.signal import convolve2d

sobelX = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

sobelY = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]])

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3:
    A = rgb2gray(A)

Dx = convolve2d(A, sobelX, mode='same')
Dy = convolve2d(A, sobelY, mode='same')

Magnitud = np.sqrt(Dx**2 + Dy**2)
Angulo = np.arctan2(Dy, Dx)

plt.figure()
plt.imshow(A, cmap='gray')
plt.title('Imagen Original A')
plt.axis('off')

plt.figure()
plt.subplot(2,2,1); plt.imshow(Dx, cmap='gray');        plt.title('Derivada de X en A');           plt.axis('off')
plt.subplot(2,2,2); plt.imshow(Dy, cmap='gray');        plt.title('Derivada de Y en A');           plt.axis('off')
plt.subplot(2,2,3); plt.imshow(Magnitud, cmap='gray');  plt.title('Magnitud = sqrt(Dx^2 + Dy^2)'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(Angulo, cmap='gray');    plt.title('Angulo = atan2(Dy,Dx)');        plt.axis('off')

plt.tight_layout()
plt.show()
