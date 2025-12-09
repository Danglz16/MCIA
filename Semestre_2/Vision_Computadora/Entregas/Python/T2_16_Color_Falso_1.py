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

Agris = rgb2gray(A)
ax, ay = Agris.shape

sepia = np.zeros((ax, ay, 3))
verde = np.zeros((ax, ay, 3))
cian  = np.zeros((ax, ay, 3))

vr_sepia, vg_sepia, vb_sepia = 255/255.0, 150/255.0, 0/255.0
vr_verde, vg_verde, vb_verde =  30/255.0, 255/255.0, 0/255.0
vr_cian,  vg_cian,  vb_cian  =   0/255.0, 255/255.0, 255/255.0

for m in range(ax):
    for n in range(ay):
        v = Agris[m, n]
        if v < 0.5:
            sepia[m, n, 0] = (vr_sepia * v) / 0.5
            sepia[m, n, 1] = (vg_sepia * v) / 0.5
            sepia[m, n, 2] = (vb_sepia * v) / 0.5
        else:
            sepia[m, n, 0] = vr_sepia + ((1.0 - vr_sepia) * (v - 0.5)) / 0.5
            sepia[m, n, 1] = vg_sepia + ((1.0 - vg_sepia) * (v - 0.5)) / 0.5
            sepia[m, n, 2] = vb_sepia + ((1.0 - vb_sepia) * (v - 0.5)) / 0.5

for m in range(ax):
    for n in range(ay):
        v = Agris[m, n]
        if v < 0.5:
            verde[m, n, 0] = (vr_verde * v) / 0.5
            verde[m, n, 1] = (vg_verde * v) / 0.5
            verde[m, n, 2] = (vb_verde * v) / 0.5
        else:
            verde[m, n, 0] = vr_verde + ((1.0 - vr_verde) * (v - 0.5)) / 0.5
            verde[m, n, 1] = vg_verde + ((1.0 - vg_verde) * (v - 0.5)) / 0.5
            verde[m, n, 2] = vb_verde + ((1.0 - vb_verde) * (v - 0.5)) / 0.5

for m in range(ax):
    for n in range(ay):
        v = Agris[m, n]
        if v < 0.5:
            cian[m, n, 0] = (vr_cian * v) / 0.5
            cian[m, n, 1] = (vg_cian * v) / 0.5
            cian[m, n, 2] = (vb_cian * v) / 0.5
        else:
            cian[m, n, 0] = vr_cian + ((1.0 - vr_cian) * (v - 0.5)) / 0.5
            cian[m, n, 1] = vg_cian + ((1.0 - vg_cian) * (v - 0.5)) / 0.5
            cian[m, n, 2] = vb_cian + ((1.0 - vb_cian) * (v - 0.5)) / 0.5

plt.figure()
plt.subplot(2,3,1); plt.imshow(A); plt.title('Imagen Original'); plt.axis('off')
plt.subplot(2,3,2); plt.imshow(Agris, cmap='gray'); plt.title('Escala de grises'); plt.axis('off')
plt.subplot(2,3,3); plt.imshow(sepia); plt.title('Escala de sepias'); plt.axis('off')
plt.subplot(2,3,5); plt.imshow(verde); plt.title('Escala de (30,255,0)'); plt.axis('off')
plt.subplot(2,3,6); plt.imshow(cian); plt.title('Escala de (0,255,255)'); plt.axis('off')
plt.show()
