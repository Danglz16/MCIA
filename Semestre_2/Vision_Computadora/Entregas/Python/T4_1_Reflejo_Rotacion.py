import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

ax, ay = A.shape[0], A.shape[1]

R1 = A[:, ::-1, :]          # Espejo horizontal
R2 = A[::-1, :, :]          # Espejo vertical
R3 = np.rot90(A, k=1)       # 90°
R4 = np.rot90(A, k=2)       # 180°
R5 = np.rot90(A, k=3)       # 270°

plt.figure()
plt.subplot(2,3,1); plt.imshow(A);  plt.title('Imagen Original A');  plt.axis('off')
plt.subplot(2,3,2); plt.imshow(R1); plt.title('Espejo Horizontal');  plt.axis('off')
plt.subplot(2,3,4); plt.imshow(R2); plt.title('Espejo Vertical');    plt.axis('off')
plt.subplot(2,3,3); plt.imshow(R3); plt.title('Rotacion 90 Grados'); plt.axis('off')
plt.subplot(2,3,5); plt.imshow(R4); plt.title('Rotacion 180 Grados');plt.axis('off')
plt.subplot(2,3,6); plt.imshow(R5); plt.title('Rotacion 270 Grados');plt.axis('off')
plt.show()
