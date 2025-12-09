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

if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

A = A.astype(float) / 255.0

plt.figure()
plt.subplot(2,3,1); plt.imshow(A); plt.title('Imagen A'); plt.axis('off')

hist_A, _ = np.histogram(A.ravel(), bins=256, range=(0,1))
plt.subplot(2,3,2); plt.bar(np.arange(256), hist_A); plt.title('Histograma de A')

tipo_histograma = 'gaussiano'

if tipo_histograma.lower() == 'uniforme':
    hist_ref = np.ones(256) / 256.0
elif tipo_histograma.lower() == 'gaussiano':
    x = np.arange(256)
    mu = 180
    sigma = 30
    hist_ref = np.exp(-((x - mu)**2) / (2 * sigma**2))
    hist_ref = hist_ref / hist_ref.sum()
elif tipo_histograma.lower() == 'exponencial':
    x = np.arange(256)
    lam = 0.02
    hist_ref = lam * np.exp(-lam * x)
    hist_ref = hist_ref / hist_ref.sum()
else:
    hist_ref = np.ones(256) / 256.0

cdf_A = np.cumsum(hist_A) / hist_A.sum()
cdf_ref = np.cumsum(hist_ref)

T = np.zeros(256)
for g in range(256):
    idx = np.argmin(np.abs(cdf_ref - cdf_A[g]))
    T[g] = idx / 255.0

idx_img = np.round(A * 255).astype(int)
idx_img = np.clip(idx_img, 0, 255)
R = T[idx_img]

plt.subplot(2,3,3); plt.bar(np.arange(256), hist_ref); plt.title('Histograma de referencia'); plt.xlim(0,255)
plt.subplot(2,3,4); plt.imshow(R); plt.title('A transformada'); plt.axis('off')

hist_R, _ = np.histogram(R.ravel(), bins=256, range=(0,1))
plt.subplot(2,3,5); plt.bar(np.arange(256), hist_R); plt.title('Histograma transformado')

plt.tight_layout()
plt.show()
