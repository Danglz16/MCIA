import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    initialdir="C:\\Users\\death\\Documents\\Maestria\\MCIA\\Semestre_2\\Vision_Computadora\\img",
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path)

if A.shape[-1] == 4:
    A = A[..., :3]

A = A.astype(float) / 255.0

plt.figure(figsize=(10,12))
plt.subplot(5,2,1); plt.imshow(A); plt.title('Imagen Original A (x,y)'); plt.axis('off')
plt.subplot(5,2,2); plt.hist(A.ravel(), bins=256); plt.title('Histograma de A')

for a in np.arange(0.0, 1.1, 0.1):
    R1 = a + A
    plt.subplot(5,2,3); plt.imshow(R1); plt.title('Imagen Resultante de A+a (x,y)'); plt.axis('off')
    plt.subplot(5,2,4); plt.hist(R1.ravel(), bins=256); plt.title(str(a))
    plt.pause(1)

    R2 = a - A
    plt.subplot(5,2,5); plt.imshow(R2); plt.title('Imagen Resultante de A-a (x,y)'); plt.axis('off')
    plt.subplot(5,2,6); plt.hist(R2.ravel(), bins=256); plt.title(str(a))
    plt.pause(1)

    R3 = a * A
    plt.subplot(5,2,7); plt.imshow(R3); plt.title('Imagen Resultante de A*a (x,y)'); plt.axis('off')
    plt.subplot(5,2,8); plt.hist(R3.ravel(), bins=256); plt.title(str(a))
    plt.pause(1)

    if a != 0:
        R4 = A / a
    else:
        R4 = np.zeros_like(A)

    plt.subplot(5,2,9); plt.imshow(R4); plt.title('Imagen Resultante de A/a (x,y)'); plt.axis('off')
    plt.subplot(5,2,10); plt.hist(R4.ravel(), bins=256); plt.title(str(a))
    plt.pause(1)

plt.show()
