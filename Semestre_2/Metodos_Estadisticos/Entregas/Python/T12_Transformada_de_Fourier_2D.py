import numpy as np
import cv2
import matplotlib.pyplot as plt
from imageio.v2 import imread

# Cerrar figuras previas
plt.close('all')

# --- Imagen 1 ---
ImagenA = imread('Semestre_2/Metodos_Estadisticos/Entregas/Datos/flor.jpeg')
# Convertir a gris si es RGB
if ImagenA.ndim == 3:
    imagenA = (0.2989 * ImagenA[..., 0] +
               0.5870 * ImagenA[..., 1] +
               0.1140 * ImagenA[..., 2])
else:
    imagenA = ImagenA.astype(float)
imagenA = imagenA.astype(float) / 255.0  # im2double

# --- Imagen 2 ---
ImagenB = imread('Semestre_2/Metodos_Estadisticos/Entregas/Datos/terry.png')
if ImagenB.ndim == 3:
    imagenB = (0.2989 * ImagenB[..., 0] +
               0.5870 * ImagenB[..., 1] +
               0.1140 * ImagenB[..., 2])
else:
    imagenB = ImagenB.astype(float)
imagenB = imagenB.astype(float) / 255.0

hA, wA = imagenA.shape
imagenB = cv2.resize(imagenB, (wA, hA))  # asegura mismo tamaño


# --- Mostrar imágenes ---
plt.figure()
plt.imshow(imagenA, cmap='gray')
plt.title('Image A - Flor')
plt.axis('off')

plt.figure()
plt.imshow(imagenB, cmap='gray')
plt.title('Image B - Perro')
plt.axis('off')

# --- FFT 2D ---
fftA = np.fft.fft2(imagenA)
fftB = np.fft.fft2(imagenB)

# ---------- Magnitud y fase de FFT A ----------
fftA_shift = np.fft.fftshift(fftA)
magA = np.abs(fftA_shift)
phaseA = np.angle(fftA_shift)

plt.figure()
plt.imshow(100 * np.log(1 + magA), cmap='gray')
plt.title('Image A FFT2 Magnitude')
plt.axis('off')

# Magnitud 3D
from mpl_toolkits.mplot3d import Axes3D  # necesario para 3D

X = np.arange(magA.shape[1])
Y = np.arange(magA.shape[0])
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, magA, cmap='bone', linewidth=0, antialiased=True)
ax.set_title('Image A FFT2 Magnitude 3D')

plt.figure()
plt.imshow(phaseA, cmap='gray', vmin=-np.pi, vmax=np.pi)
plt.title('Image A FFT2 Phase')
plt.axis('off')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, phaseA, cmap='bone', linewidth=0, antialiased=True)
ax.set_title('Image A FFT2 Phase 3D')

# ---------- Magnitud y fase de FFT B ----------
fftB_shift = np.fft.fftshift(fftB)
magB = np.abs(fftB_shift)
phaseB = np.angle(fftB_shift)

plt.figure()
plt.imshow(100 * np.log(1 + magB), cmap='gray')
plt.title('Image B FFT2 Magnitude')
plt.axis('off')

plt.figure()
plt.imshow(phaseB, cmap='gray', vmin=-np.pi, vmax=np.pi)
plt.title('Image B FFT2 Phase')
plt.axis('off')

# --- Intercambiar magnitud y fase ---
fftC = np.abs(fftA) * np.exp(1j * np.angle(fftB))
fftD = np.abs(fftB) * np.exp(1j * np.angle(fftA))

# --- IFFT ---
imageC = np.fft.ifft2(fftC)
imageD = np.fft.ifft2(fftD)

# --- Límites para ploteo ---
absC = np.abs(imageC)
absD = np.abs(imageD)

cmin, cmax = absC.min(), absC.max()
dmin, dmax = absD.min(), absD.max()

plt.figure()
plt.imshow(absC, cmap='gray', vmin=cmin, vmax=cmax)
plt.title('Image C Magnitude')
plt.axis('off')

plt.figure()
plt.imshow(absD, cmap='gray', vmin=dmin, vmax=dmax)
plt.title('Image D Magnitude')
plt.axis('off')

plt.show()
