import matplotlib.pyplot as plt
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
G = rgb2gray(A)
B = G > threshold_otsu(G)

plt.figure(figsize=(12,4))
plt.subplot(1,3,1); plt.imshow(A); plt.title('Original'); plt.axis('off')
plt.subplot(1,3,2); plt.imshow(G, cmap='gray'); plt.title('Escala de Grises'); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(B, cmap='gray'); plt.title('Binario'); plt.axis('off')
plt.show()
