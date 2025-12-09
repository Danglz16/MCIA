import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from skimage.exposure import equalize_hist
from skimage.transform import resize

Tk().withdraw()

# Cartel
file_path1 = filedialog.askopenfilename(
    title='File Selector - Cartel',
    filetypes=[("Images", "*.png;*.jpeg;*.jpg")]
)
M = imread(file_path1).astype(float) / 255.0

# Persona
file_path2 = filedialog.askopenfilename(
    title='File Selector - Persona',
    filetypes=[("Images", "*.png;*.jpeg;*.jpg")]
)
A = imread(file_path2).astype(float) / 255.0

if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

if A.ndim == 3:
    A = np.stack([equalize_hist(A[..., c]) for c in range(A.shape[-1])], axis=-1)
else:
    A = equalize_hist(A)

A = A ** (1/1.8)

# Fondo
file_path3 = filedialog.askopenfilename(
    title='File Selector - Fondo',
    filetypes=[("Images", "*.png;*.jpeg;*.jpg")]
)
F = imread(file_path3).astype(float) / 255.0

if F.ndim == 3 and F.shape[-1] == 4:
    F = F[..., :3]
if M.ndim == 3 and M.shape[-1] == 4:
    M = M[..., :3]

fx, fy = F.shape[:2]
M = resize(M, (fx, fy), preserve_range=True)
A = resize(A, (fx, fy), preserve_range=True)

D = np.abs(M - A)

if D.ndim == 3:
    Dgris = rgb2gray(D)
else:
    Dgris = D

umbral = 0.225
U = Dgris >= umbral

U_f = U.astype(float)
NOT_U = 1.0 - U_f

if F.ndim == 3:
    U_f3 = U_f[..., np.newaxis]
    NOT_U3 = NOT_U[..., np.newaxis]
else:
    U_f3 = U_f
    NOT_U3 = NOT_U

parte1 = F * NOT_U3
parte2 = A * U_f3
R = parte1 + parte2

plt.figure()
plt.subplot(3,2,1); plt.imshow(M); plt.title('M'); plt.axis('off')
plt.subplot(3,2,2); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(3,2,3); plt.imshow(Dgris, cmap='gray'); plt.title('D'); plt.axis('off')
plt.subplot(3,2,4); plt.imshow(U, cmap='gray'); plt.title('U'); plt.axis('off')
plt.subplot(3,2,5); plt.imshow(F); plt.title('F'); plt.axis('off')
plt.subplot(3,2,6); plt.imshow(R); plt.title('R'); plt.axis('off')
plt.show()
