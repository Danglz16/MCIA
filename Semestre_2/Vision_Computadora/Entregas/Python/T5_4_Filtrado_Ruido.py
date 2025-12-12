import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog

file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3:
    A = rgb2gray(A)

img = A

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
phase_spectrum = np.angle(fshift)

finv = np.fft.ifft2(f)
f_back = np.abs(finv)

rows, cols = img.shape
mask = np.ones((rows, cols))
band_width = 10
center_col = int(round(cols / 2))

mask[:, center_col-50:center_col-50+band_width] = 0
mask[:, center_col+50-band_width+1:center_col+50+1] = 0

fshift_masked = fshift * mask
magnitude_masked = 20 * np.log(np.abs(fshift_masked) + 1)

f_ishift = np.fft.ifftshift(fshift_masked)
img_restored = np.abs(np.fft.ifft2(f_ishift))

plt.figure()
plt.subplot(2,3,1); plt.imshow(img, cmap='gray');                plt.title('Imagen de entrada');        plt.axis('off')
plt.subplot(2,3,2); plt.imshow(magnitude_spectrum, cmap='gray'); plt.title('Espectro de magnitud');    plt.axis('off')
plt.subplot(2,3,3); plt.imshow(mask, cmap='gray');               plt.title('Mascara de bandas de ruido');plt.axis('off')
plt.subplot(2,3,4); plt.imshow(magnitude_masked, cmap='gray');   plt.title('Masked Spectrum');         plt.axis('off')
plt.subplot(2,3,5); plt.imshow(img_restored, cmap='gray');       plt.title('Imagen restaurada');       plt.axis('off')
plt.subplot(2,3,6); plt.imshow(phase_spectrum, cmap='gray');     plt.title('Espectro de fase');        plt.axis('off')
plt.tight_layout()
plt.show()
