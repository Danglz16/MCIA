import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from scipy.signal import convolve2d

file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0

if A.ndim == 3:
    A = rgb2gray(A)

Mx      = np.array([[-1, 1]])
My      = Mx.T
Mdiag1  = np.array([[-2, -1, 0],
                    [-1,  0, 1],
                    [ 0,  1, 2]])
Mdiag2  = np.array([[ 0,  1,  2],
                    [-1,  0,  1],
                    [-2, -1,  0]])
Msmooth = np.array([[1, 2, 1],
                    [2, 4, 2],
                    [1, 2, 1]]) / 16.0
Memboss = np.array([[-2, -1, 0],
                    [-1,  1, 1],
                    [ 0,  1, 2]])

Rx        = convolve2d(A, Mx,      mode='same')
Ry        = convolve2d(A, My,      mode='same')
Rdiag1    = convolve2d(A, Mdiag1,  mode='same')
Rdiag2    = convolve2d(A, Mdiag2,  mode='same')
Remboss   = convolve2d(A, Memboss, mode='same')
A_smooth  = convolve2d(A, Msmooth, mode='same')
Rx_smooth = convolve2d(A_smooth, Mx, mode='same')

plt.figure(); plt.imshow(A, cmap='gray');      plt.title('Original');                 plt.axis('off')

plt.figure(); plt.imshow(Rx, cmap='gray');     plt.title('Derivada en X');            plt.axis('off')
plt.figure(); plt.imshow(Ry, cmap='gray');     plt.title('Derivada en Y');            plt.axis('off')
plt.figure(); plt.imshow(Rdiag1, cmap='gray'); plt.title('Derivada diagonal 1');      plt.axis('off')
plt.figure(); plt.imshow(Rdiag2, cmap='gray'); plt.title('Derivada diagonal 2');      plt.axis('off')

Remboss_norm = (Remboss - Remboss.min()) / (Remboss.max() - Remboss.min() + 1e-8)
plt.figure(); plt.imshow(Remboss_norm, cmap='gray'); plt.title('Emboss');             plt.axis('off')
plt.figure(); plt.imshow(Rx_smooth, cmap='gray'); plt.title('Suavizado + Derivada X'); plt.axis('off')
plt.show()
