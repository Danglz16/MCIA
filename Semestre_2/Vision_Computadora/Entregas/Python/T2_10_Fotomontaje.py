import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from tkinter import Tk, filedialog
from skimage.transform import resize

Tk().withdraw()

file_path_bg = filedialog.askopenfilename(
    title='File Selector - Fondo',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)
A = imread(file_path_bg).astype(float) / 255.0

file_path_fg = filedialog.askopenfilename(
    title='File Selector - Primer Plano',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)
B = imread(file_path_fg).astype(float) / 255.0
bx, by = B.shape[:2]

file_path_mask = filedialog.askopenfilename(
    title='File Selector - Mascara Binaria',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)
C = imread(file_path_mask).astype(float) / 255.0

if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]
if B.ndim == 3 and B.shape[-1] == 4:
    B = B[..., :3]
if C.ndim == 3 and C.shape[-1] == 4:
    C = C[..., :3]

if A.ndim == 3:
    A = resize(A, (bx, by, A.shape[2]), preserve_range=True)
else:
    A = resize(A, (bx, by), preserve_range=True)

if C.ndim == 3:
    C = rgb2gray(C)

C = C > threshold_otsu(C)
NOTC = ~C

if B.ndim == 3:
    NOTC_3 = NOTC[..., np.newaxis]
    C_3 = C[..., np.newaxis]
else:
    NOTC_3 = NOTC
    C_3 = C

T1 = B * NOTC_3
T2 = A * C_3
R = T1 + T2

plt.figure()
plt.subplot(3,3,1); plt.imshow(B); plt.title('B'); plt.axis('off')
plt.subplot(3,3,2); plt.imshow(NOTC, cmap='gray'); plt.title('B'); plt.axis('off')
plt.subplot(3,3,3); plt.imshow(T1); plt.title('B'); plt.axis('off')
plt.subplot(3,3,4); plt.imshow(A); plt.title('B'); plt.axis('off')
plt.subplot(3,3,5); plt.imshow(C, cmap='gray'); plt.title('B'); plt.axis('off')
plt.subplot(3,3,6); plt.imshow(T2); plt.title('B'); plt.axis('off')
plt.subplot(3,3,7); plt.imshow(T1); plt.title('B'); plt.axis('off')
plt.subplot(3,3,8); plt.imshow(T2); plt.title('B'); plt.axis('off')
plt.subplot(3,3,9); plt.imshow(R); plt.title('B'); plt.axis('off')

plt.figure(); plt.imshow(R); plt.axis('off'); plt.show()
