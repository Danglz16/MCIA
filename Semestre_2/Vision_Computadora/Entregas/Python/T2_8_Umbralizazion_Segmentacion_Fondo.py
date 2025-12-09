import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    initialdir="C:\\Users\\death\\Documents\\Maestria\\MCIA\\Semestre_2\\Vision_Computadora\\img",
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

I = imread(file_path)

if I.ndim == 3 and I.shape[-1] == 4:
    I = I[..., :3]

I = I.astype(float) / 255.0

if I.ndim == 3:
    A = rgb2gray(I)
else:
    A = I

ax, ay = A.shape

u1 = 42 / 255.0
u2 = 180 / 255.0

R1 = np.zeros_like(A)
R2 = np.zeros_like(A)

R1[A > u1] = 1.0
R2[A > u2] = 1.0

low = 192 / 255.0
high = 255 / 255.0

mask = (A >= low) & (A <= high)

C = I.copy()
if I.ndim == 3:
    C[~mask] = 0.0
else:
    C[~mask] = 0.0

plt.figure()

plt.subplot(2,2,1); plt.imshow(I, cmap=None if I.ndim == 3 else 'gray'); plt.title('Imagen de entrada'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(R1, cmap='gray'); plt.title('Umbralizar, u = 42'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(R2, cmap='gray'); plt.title('Umbralizar, u = 180'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(C, cmap=None if I.ndim == 3 else 'gray'); plt.title('Cortar rango (192, 255)'); plt.axis('off')

plt.show()