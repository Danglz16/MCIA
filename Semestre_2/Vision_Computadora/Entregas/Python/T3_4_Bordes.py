import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from skimage.color import rgb2gray
from scipy.signal import convolve2d

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3:
    A = rgb2gray(A)

PrewittX = np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]])
PrewittY = PrewittX.T

Dx_prewitt = convolve2d(A, PrewittX, mode='same', boundary='symm')
Dy_prewitt = convolve2d(A, PrewittY, mode='same', boundary='symm')
Mag_prewitt = np.sqrt(Dx_prewitt**2 + Dy_prewitt**2)

ScharrX = np.array([[-3,  0,  3],
                    [-10, 0, 10],
                    [-3,  0,  3]])
ScharrY = ScharrX.T

Dx_scharr = convolve2d(A, ScharrX, mode='same', boundary='symm')
Dy_scharr = convolve2d(A, ScharrY, mode='same', boundary='symm')
Mag_scharr = np.sqrt(Dx_scharr**2 + Dy_scharr**2)

SobelX = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
SobelY = SobelX.T

Dx_sobel = convolve2d(A, SobelX, mode='same', boundary='symm')
Dy_sobel = convolve2d(A, SobelY, mode='same', boundary='symm')
Mag_sobel = np.sqrt(Dx_sobel**2 + Dy_sobel**2)

plt.figure(figsize=(8, 8))

plt.subplot(3,3,1); plt.imshow(A, cmap='gray');              plt.title('Imagen original');   plt.axis('off')

plt.subplot(3,3,2); plt.imshow(Dx_sobel, cmap='gray');       plt.title('Sobel Dx');          plt.axis('off')
plt.subplot(3,3,3); plt.imshow(Dy_sobel, cmap='gray');       plt.title('Sobel Dy');          plt.axis('off')

plt.subplot(3,3,4); plt.imshow(Dx_prewitt, cmap='gray');     plt.title('Prewitt Dx');        plt.axis('off')
plt.subplot(3,3,5); plt.imshow(Dy_prewitt, cmap='gray');     plt.title('Prewitt Dy');        plt.axis('off')

plt.subplot(3,3,6); plt.imshow(Dx_scharr, cmap='gray');      plt.title('Scharr Dx');         plt.axis('off')
plt.subplot(3,3,7); plt.imshow(Dy_scharr, cmap='gray');      plt.title('Scharr Dy');         plt.axis('off')

plt.subplot(3,3,8); plt.imshow(Mag_sobel, cmap='gray');      plt.title('Magnitud Sobel');    plt.axis('off')
plt.subplot(3,3,9); plt.imshow(Mag_prewitt, cmap='gray');    plt.title('Magnitud Prewitt');  plt.axis('off')

plt.tight_layout()
plt.show()
