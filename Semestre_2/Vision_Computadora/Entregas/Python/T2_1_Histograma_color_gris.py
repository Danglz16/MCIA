import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
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

plt.figure()
plt.subplot(1,2,1); plt.imshow(A); plt.title('Imagen A'); plt.axis('off')
plt.subplot(1,2,2); plt.hist(A.ravel(), bins=256, color='gray'); plt.title('Histograma de A')

Agris = rgb2gray(A)

plt.figure()
plt.subplot(1,2,1); plt.imshow(Agris, cmap='gray'); plt.title('Imagen gris'); plt.axis('off')
plt.subplot(1,2,2); plt.hist(Agris.ravel(), bins=256, color='gray'); plt.title('Histograma de A gris')

A_r = A[..., 0]
A_g = A[..., 1]
A_b = A[..., 2]

plt.figure()
plt.subplot(2,3,2); plt.imshow(A); plt.title('Imagen A'); plt.axis('off')
plt.subplot(2,3,4); plt.hist(A_r.ravel(), bins=256, color='red'); plt.title('Histograma canal rojo')
plt.subplot(2,3,5); plt.hist(A_g.ravel(), bins=256, color='green'); plt.title('Histograma canal verde')
plt.subplot(2,3,6); plt.hist(A_b.ravel(), bins=256, color='blue'); plt.title('Histograma canal azul')
plt.show()
