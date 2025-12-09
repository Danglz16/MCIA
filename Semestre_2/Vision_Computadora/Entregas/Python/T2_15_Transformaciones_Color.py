import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from tkinter import Tk, filedialog
from skimage.transform import resize

file_path1 = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)
A = imread(file_path1).astype(float) / 255.0

file_path2 = filedialog.askopenfilename(
    title='File Selector - Imagen B',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)
B = imread(file_path2).astype(float) / 255.0

if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]
if B.ndim == 3 and B.shape[-1] == 4:
    B = B[..., :3]

bx, by, bz = B.shape
A = resize(A, (bx, by, bz), preserve_range=True)

Rmax = np.maximum(A, B)
Rmin = np.minimum(A, B)

plt.figure()
plt.subplot(2,2,1); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(B); plt.title('B'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(Rmin); plt.title('Min(A,B)'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(Rmax); plt.title('Max(A,B)'); plt.axis('off')
plt.show()
