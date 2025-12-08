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

O = imread(file_path)

if O.shape[-1] == 4:
    O = O[..., :3]

R = O[..., 0]
G = O[..., 1]
B = O[..., 2]

allBlack = np.zeros_like(R)

justR = np.stack([R, allBlack, allBlack], axis=2)
justG = np.stack([allBlack, G, allBlack], axis=2)
justB = np.stack([allBlack, allBlack, B], axis=2)

full = np.stack([R, G, B], axis=2)
Neg = 255 - full

plt.figure(figsize=(10,6))
plt.subplot(2,3,1); plt.imshow(justR); plt.title('Canal Rojo'); plt.axis('off')
plt.subplot(2,3,2); plt.imshow(justG); plt.title('Canal Verde'); plt.axis('off')
plt.subplot(2,3,3); plt.imshow(justB); plt.title('Canal Azul'); plt.axis('off')
plt.subplot(2,3,4); plt.imshow(full); plt.title('Imagen Completa'); plt.axis('off')
plt.subplot(2,3,5); plt.imshow(Neg); plt.title('Imagen Negativa'); plt.axis('off')
plt.show()
