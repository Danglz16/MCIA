import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from tkinter import Tk, filedialog
from scipy.ndimage import convolve
import time

file_path = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

def aplicar_filtro(img, kernel):
    if img.ndim == 3:
        R = np.zeros_like(img)
        for c in range(img.shape[2]):
            R[..., c] = convolve(img[..., c], kernel, mode='nearest')
    else:
        R = convolve(img, kernel, mode='nearest')
    return R

def gauss2d(size, sigma):
    n = size
    ax = np.linspace(-(n-1)/2, (n-1)/2, n)
    xx, yy = np.meshgrid(ax, ax)
    k = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    k /= k.sum()
    return k

media11 = np.ones((11, 11)) / (11 * 11)
media21 = np.ones((21, 21)) / (21 * 21)
gauss21 = gauss2d(21, 5)
gauss41 = gauss2d(41, 10)

R1 = aplicar_filtro(A, media11)
R2 = aplicar_filtro(A, media21)
R3 = aplicar_filtro(A, gauss21)
R4 = aplicar_filtro(A, gauss41)

plt.figure()
plt.subplot(2,2,1); plt.imshow(R1); plt.title('Media 11x11'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(R2); plt.title('Media 21x21'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(R3); plt.title('Gaussiana 21x21'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(R4); plt.title('Gaussiana 41x41'); plt.axis('off')

media_horiz = np.ones((1, 31)) / 31
media_vert  = np.ones((31, 1)) / 31

ax = np.linspace(-(61-1)/2, (61-1)/2, 61)
g1d = np.exp(-ax**2 / (2 * 10**2))
g1d /= g1d.sum()
gauss_horiz = g1d.reshape(1, -1)
gauss_vert  = g1d.reshape(-1, 1)

R5 = aplicar_filtro(A, media_horiz)
R6 = aplicar_filtro(A, media_vert)
R7 = aplicar_filtro(A, gauss_horiz)
R8 = aplicar_filtro(A, gauss_vert)

plt.figure()
plt.subplot(2,2,1); plt.imshow(R5); plt.title('Media 31x1 (horizontal)'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(R6); plt.title('Media 1x31 (vertical)'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(R7); plt.title('Gaussiana 61x1 (horizontal)'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(R8); plt.title('Gaussiana 1x61 (vertical)'); plt.axis('off')
plt.show()

t0 = time.time()
T1 = aplicar_filtro(A, media11)
t_media11 = time.time() - t0

t0 = time.time()
T2 = aplicar_filtro(A, media21)
t_media21 = time.time() - t0

t0 = time.time()
T3 = aplicar_filtro(A, gauss21)
t_gauss21 = time.time() - t0

t0 = time.time()
T4 = aplicar_filtro(A, gauss41)
t_gauss41 = time.time() - t0

t0 = time.time()
T5 = aplicar_filtro(A, media_horiz)
t_mediaH = time.time() - t0

t0 = time.time()
T6 = aplicar_filtro(A, media_vert)
t_mediaV = time.time() - t0

t0 = time.time()
T7 = aplicar_filtro(A, gauss_horiz)
t_gaussH = time.time() - t0

t0 = time.time()
T8 = aplicar_filtro(A, gauss_vert)
t_gaussV = time.time() - t0

print('\nTiempos de ejecución (en segundos):')
print(f'Media 11x11         : {t_media11:.6f}')
print(f'Media 21x21         : {t_media21:.6f}')
print(f'Gaussiana 21x21     : {t_gauss21:.6f}')
print(f'Gaussiana 41x41     : {t_gauss41:.6f}')
print(f'Media 31x1 (H)      : {t_mediaH:.6f}')
print(f'Media 1x31 (V)      : {t_mediaV:.6f}')
print(f'Gaussiana 61x1 (H)  : {t_gaussH:.6f}')
print(f'Gaussiana 1x61 (V)  : {t_gaussV:.6f}')
