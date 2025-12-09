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

B = resize(B, A.shape, preserve_range=True)

plt.figure()
plt.suptitle('Media Ponderada de A y B')
plt.subplot(1,3,1); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(1,3,2); plt.imshow(B); plt.title('B'); plt.axis('off')

for a in np.arange(0.1, 1.1, 0.1):
    R3 = a * A + (1 - a) * B
    plt.subplot(1,3,3); plt.imshow(R3); plt.title(str(round(a,1))); plt.axis('off')
    plt.pause(0.2)

plt.show()