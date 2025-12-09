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

A_f = A.astype(float) / 255.0

A_R = A_f[..., 0] * 255
A_G = A_f[..., 1] * 255
A_B = A_f[..., 2] * 255

num_puntos = 600
idx = np.random.permutation(A_R.size)[:num_puntos]

R = A_R.flatten()[idx]
G = A_G.flatten()[idx]
B = A_B.flatten()[idx]

plt.figure(figsize=(12,4))
plt.subplot(1,4,1); plt.imshow(A/255); plt.title('Imagen original'); plt.axis('off')

plt.subplot(1,4,2); plt.scatter(R, G, s=10, c='k')
plt.xlabel('Canal Rojo (0-255)', color='red')
plt.ylabel('Canal Verde (0-255)', color='green')
plt.title('Canales R y G')
plt.grid(True)
plt.xlim(0,255); plt.ylim(0,255)
ax = plt.gca()
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('green')
ax.xaxis.label.set_weight('bold')
ax.yaxis.label.set_weight('bold')
ax.invert_yaxis()

plt.subplot(1,4,3); plt.scatter(G, B, s=10, c='k')
plt.xlabel('Canal Verde (0-255)', color='green')
plt.ylabel('Canal Azul (0-255)', color='blue')
plt.title('Canales G y B')
plt.grid(True)
plt.xlim(0,255); plt.ylim(0,255)
ax = plt.gca()
ax.spines['bottom'].set_color('green')
ax.spines['left'].set_color('blue')
ax.xaxis.label.set_weight('bold')
ax.yaxis.label.set_weight('bold')
ax.invert_yaxis()

plt.subplot(1,4,4); plt.scatter(R, B, s=10, c='k')
plt.xlabel('Canal Rojo (0-255)', color='red')
plt.ylabel('Canal Azul (0-255)', color='blue')
plt.title('Canales R y B')
plt.grid(True)
plt.xlim(0,255); plt.ylim(0,255)
ax = plt.gca()
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('blue')
ax.xaxis.label.set_weight('bold')
ax.yaxis.label.set_weight('bold')
ax.invert_yaxis()

plt.show()
