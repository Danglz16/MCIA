import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from skimage.feature import canny
from skimage.filters import sobel
from scipy.signal import convolve2d
from scipy.ndimage import maximum_filter, minimum_filter

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

if A.ndim == 3:
    A = rgb2gray(A)

Bordes_sobel = sobel(A)
Bordes_canny = canny(A)

kernel_lap = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])
Lap = convolve2d(A, kernel_lap, mode='same', boundary='symm')
Perfilado = A - Lap

eps = 1e-8
G = np.exp(convolve2d(np.log(A + eps),
                      np.ones((3, 3)) / 9.0,
                      mode='same',
                      boundary='symm'))

Maximo = maximum_filter(A, size=3)
Minimo = minimum_filter(A, size=3)

plt.figure(figsize=(8, 8))

plt.subplot(3,3,1); plt.imshow(A, cmap='gray');             plt.title('Original');          plt.axis('off')
plt.subplot(3,3,2); plt.imshow(Bordes_sobel, cmap='gray');  plt.title('Bordes Sobel');      plt.axis('off')
plt.subplot(3,3,3); plt.imshow(Bordes_canny, cmap='gray');  plt.title('Bordes Canny');      plt.axis('off')
plt.subplot(3,3,4); plt.imshow(Lap, cmap='gray');           plt.title('Laplaciano');        plt.axis('off')
plt.subplot(3,3,5); plt.imshow(Perfilado, cmap='gray');     plt.title('Perfilado');         plt.axis('off')
plt.subplot(3,3,6); plt.imshow(G, cmap='gray');             plt.title('Media geométrica');  plt.axis('off')
plt.subplot(3,3,7); plt.imshow(Maximo, cmap='gray');        plt.title('Filtro máximo');     plt.axis('off')
plt.subplot(3,3,8); plt.imshow(Minimo, cmap='gray');        plt.title('Filtro mínimo');     plt.axis('off')

plt.tight_layout()
plt.show()