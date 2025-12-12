import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from tkinter import Tk, filedialog
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity

file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]
elif A.ndim == 2:
    A = np.dstack([A, A, A])

M_rgb2xyz = np.array([[0.41, 0.36, 0.18],
                      [0.21, 0.72, 0.07],
                      [0.02, 0.12, 0.95]])

M_xyz2rgb = np.array([[ 3.24, -1.5 , -0.5 ],
                      [-0.9 ,  1.88,  0.04],
                      [ 0.06, -0.2 ,  1.05]])

m, n, _ = A.shape

rgb = A.reshape(-1, 3)
xyz = rgb @ M_rgb2xyz.T
img_xyz = xyz.reshape(m, n, 3)

xyz2 = img_xyz.reshape(-1, 3)
rgb2 = xyz2 @ M_xyz2rgb.T
img_rgb2 = rgb2.reshape(m, n, 3)
img_rgb2 = np.clip(img_rgb2, 0, 1)

plt.figure()
plt.subplot(1,3,1); plt.imshow(A);        plt.title('Original RGB');     plt.axis('off')
plt.subplot(1,3,2); plt.imshow(img_xyz);  plt.title('Convertida a XYZ'); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(img_rgb2); plt.title('RGB restaurada');   plt.axis('off')
plt.show()

print('Métricas de Calidad de Imagen')

mse = mean_squared_error(A, img_rgb2)
print(f'IMMSE: {mse:.6f}')

peaksnr = peak_signal_noise_ratio(A, img_rgb2, data_range=1.0)
print(f'PSNR: {peaksnr:.2f} dB')

ssimval = structural_similarity(A, img_rgb2, channel_axis=2, data_range=1.0)
print(f'SSIM: {ssimval:.4f}')
