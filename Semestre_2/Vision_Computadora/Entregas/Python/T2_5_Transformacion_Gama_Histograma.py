import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
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

plt.figure(figsize=(8,8))
plt.subplot(2,2,1); plt.imshow(A); plt.title('Imagen Original'); plt.axis('off')
plt.subplot(2,2,2); plt.hist(A.ravel(), bins=256); plt.title('Histograma de A')

for gamma in np.arange(0.1, 4.1, 0.1):
    R = (A ** (1/gamma))
    plt.subplot(2,2,3); plt.imshow(R); plt.title('Ajuste de Gamma'); plt.axis('off')
    plt.subplot(2,2,4); plt.hist(R.ravel(), bins=256); plt.title(str(round(gamma,1)))
    plt.pause(0.05)

plt.show()
