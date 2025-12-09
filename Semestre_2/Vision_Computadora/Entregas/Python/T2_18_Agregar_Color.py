import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog

file_path = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0

if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]
elif A.ndim == 2:
    A = np.dstack([A, A, A])

Agris = rgb2gray(A)
ax, ay = Agris.shape

R1 = np.zeros((ax, ay, 3))
R2 = np.zeros((ax, ay, 3))
R3 = np.zeros((ax, ay, 3))
R4 = np.zeros((ax, ay, 3))

vr_1, vg_1, vb_1 = -20/255.0,  8/255.0, 60/255.0   # azul (suma)
vr_2, vg_2, vb_2 = 1.4,        0.9,      0.9       # rojo (multi)
vr_3, vg_3, vb_3 = 1.4,        1.15,     1.0       # naranja (multi)
vr_4, vg_4, vb_4 = -10/255.0, 40/255.0, -10/255.0  # verde (suma)

R1[..., 0] = vr_1 + A[..., 0]
R1[..., 1] = vg_1 + A[..., 1]
R1[..., 2] = vb_1 + A[..., 2]

R2[..., 0] = vr_2 * A[..., 0]
R2[..., 1] = vg_2 * A[..., 1]
R2[..., 2] = vb_2 * A[..., 2]

R3[..., 0] = vr_3 * A[..., 0]
R3[..., 1] = vg_3 * A[..., 1]
R3[..., 2] = vb_3 * A[..., 2]

R4[..., 0] = vr_4 + A[..., 0]
R4[..., 1] = vg_4 + A[..., 1]
R4[..., 2] = vb_4 + A[..., 2]

plt.figure()
plt.subplot(2,3,1); plt.imshow(A);  plt.title('Imagen Original');          plt.axis('off')
plt.subplot(2,3,2); plt.imshow(R1); plt.title('Suma(-20,8,60)');          plt.axis('off')
plt.subplot(2,3,3); plt.imshow(R2); plt.title('Multi(1.4,0.9,0.9)');      plt.axis('off')
plt.subplot(2,3,5); plt.imshow(R3); plt.title('Multi(1.4,1.15,1)');       plt.axis('off')
plt.subplot(2,3,6); plt.imshow(R4); plt.title('Suma(-10,40,-10)');       plt.axis('off')
plt.show()
