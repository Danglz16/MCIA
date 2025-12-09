import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    initialdir="C:\\Users\\death\\Documents\\Maestria\\MCIA\\Semestre_2\\Vision_Computadora\\img",
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

O = imread(file_path)

if O.shape[-1] == 4:
    O = O[..., :3]

A = rgb2gray(O)
A = A.astype(float)

L2 = 2**2
IQ2 = (A*(L2-1)).round()/(L2-1)

L3 = 2**3
IQ3 = (A*(L3-1)).round()/(L3-1)

L4 = 2**4
IQ4 = (A*(L4-1)).round()/(L4-1)

L5 = 2**5
IQ5 = (A*(L5-1)).round()/(L5-1)

plt.figure(figsize=(10,10))
plt.subplot(2,3,1); plt.imshow(O); plt.title('Original'); plt.axis('off')
plt.subplot(2,3,2); plt.imshow(A, cmap='gray'); plt.title('Escala de Grises'); plt.axis('off')
plt.subplot(2,3,3); plt.imshow(IQ2, cmap='gray'); plt.title('2 bits (4 niveles)'); plt.axis('off')
plt.subplot(2,3,4); plt.imshow(IQ3, cmap='gray'); plt.title('3 bits (8 niveles)'); plt.axis('off')
plt.subplot(2,3,5); plt.imshow(IQ4, cmap='gray'); plt.title('4 bits (16 niveles)'); plt.axis('off')
plt.subplot(2,3,6); plt.imshow(IQ5, cmap='gray'); plt.title('5 bits (32 niveles)'); plt.axis('off')
plt.show()
