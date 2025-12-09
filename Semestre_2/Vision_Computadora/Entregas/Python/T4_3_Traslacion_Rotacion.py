import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

esColor = (A.ndim == 3)
filas_original, columnas_original = A.shape[:2]
num_canales = A.shape[2] if esColor else 1

total_plots = 8
num_filas_subplot = 3
num_columnas_subplot = 3
plot_idx = 1

plt.figure()
plt.subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx += 1
plt.imshow(A); plt.title('Imagen Original'); plt.axis('off')

dx_tras = 50
dy_tras = 30

R_traslacion_manual = np.zeros_like(A)
for m_nueva in range(dy_tras, filas_original):
    for n_nueva in range(dx_tras, columnas_original):
        m_original = m_nueva - dy_tras
        n_original = n_nueva - dx_tras
        if esColor:
            R_traslacion_manual[m_nueva, n_nueva, :] = A[m_original, n_original, :]
        else:
            R_traslacion_manual[m_nueva, n_nueva] = A[m_original, n_original]

plt.subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx += 1
plt.imshow(R_traslacion_manual); 
plt.title(f'Traslación (dx={dx_tras}, dy={dy_tras})'); 
plt.axis('off')

angulos_rotacion = [-10, 10]

theta_rad_max = np.deg2rad(max(abs(a) for a in angulos_rotacion))
cos_theta = abs(np.cos(theta_rad_max))
sin_theta = abs(np.sin(theta_rad_max))

nueva_filas_rot = int(np.ceil(filas_original * cos_theta + columnas_original * sin_theta))
nueva_columnas_rot = int(np.ceil(filas_original * sin_theta + columnas_original * cos_theta))

centro_orig_x = columnas_original / 2.0
centro_orig_y = filas_original / 2.0
centro_nueva_x = nueva_columnas_rot / 2.0
centro_nueva_y = nueva_filas_rot / 2.0

for angulo in angulos_rotacion:
    theta_rad = np.deg2rad(angulo)
    if esColor:
        R_rotacion_NN = np.zeros((nueva_filas_rot, nueva_columnas_rot, num_canales), dtype=A.dtype)
    else:
        R_rotacion_NN = np.zeros((nueva_filas_rot, nueva_columnas_rot), dtype=A.dtype)

    for m_out in range(nueva_filas_rot):
        for n_out in range(nueva_columnas_rot):
            x_out_c = n_out - centro_nueva_x
            y_out_c = m_out - centro_nueva_y

            x_orig_c = x_out_c * np.cos(theta_rad) + y_out_c * np.sin(theta_rad)
            y_orig_c = -x_out_c * np.sin(theta_rad) + y_out_c * np.cos(theta_rad)

            x_orig = x_orig_c + centro_orig_x
            y_orig = y_orig_c + centro_orig_y

            x_pixel = int(round(x_orig))
            y_pixel = int(round(y_orig))

            if 0 <= x_pixel < columnas_original and 0 <= y_pixel < filas_original:
                if esColor:
                    R_rotacion_NN[m_out, n_out, :] = A[y_pixel, x_pixel, :]
                else:
                    R_rotacion_NN[m_out, n_out] = A[y_pixel, x_pixel]

    plt.subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx += 1
    plt.imshow(R_rotacion_NN)
    if angulo == -10:
        plt.title('Rotar -10º (Vecino Más Próximo)')
    elif angulo == 10:
        plt.title('Rotar 10º (Vecino Más Próximo)')
    plt.axis('off')

print('Calculando rotación con interpolación Bilineal...')
angulo_bilinear = -10
theta_rad_bilinear = np.deg2rad(angulo_bilinear)

if esColor:
    R_rotacion_Bilinear = np.zeros((nueva_filas_rot, nueva_columnas_rot, num_canales), dtype=A.dtype)
else:
    R_rotacion_Bilinear = np.zeros((nueva_filas_rot, nueva_columnas_rot), dtype=A.dtype)

for m_out in range(nueva_filas_rot):
    for n_out in range(nueva_columnas_rot):
        x_out_c = n_out - centro_nueva_x
        y_out_c = m_out - centro_nueva_y

        x_orig_c = x_out_c * np.cos(theta_rad_bilinear) + y_out_c * np.sin(theta_rad_bilinear)
        y_orig_c = -x_out_c * np.sin(theta_rad_bilinear) + y_out_c * np.cos(theta_rad_bilinear)

        x_orig = x_orig_c + centro_orig_x
        y_orig = y_orig_c + centro_orig_y

        x1 = int(np.floor(x_orig))
        y1 = int(np.floor(y_orig))
        x2 = x1 + 1
        y2 = y1 + 1

        a = x_orig - x1
        b = y_orig - y1

        if x1 >= 0 and x2 < columnas_original and y1 >= 0 and y2 < filas_original:
            if esColor:
                for canal in range(num_canales):
                    val11 = A[y1, x1, canal]
                    val21 = A[y1, x2, canal]
                    val12 = A[y2, x1, canal]
                    val22 = A[y2, x2, canal]
                    R_rotacion_Bilinear[m_out, n_out, canal] = (
                        val11 * (1-a) * (1-b) +
                        val21 * a * (1-b) +
                        val12 * (1-a) * b +
                        val22 * a * b
                    )
            else:
                val11 = A[y1, x1]
                val21 = A[y1, x2]
                val12 = A[y2, x1]
                val22 = A[y2, x2]
                R_rotacion_Bilinear[m_out, n_out] = (
                    val11 * (1-a) * (1-b) +
                    val21 * a * (1-b) +
                    val12 * (1-a) * b +
                    val22 * a * b
                )

plt.subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx += 1
plt.imshow(R_rotacion_Bilinear)
plt.title('Rotación -10º (Bilineal)')
plt.axis('off')

ax1, ay1 = 0.8, 0.8
ax2, ay2 = 2.0, 0.5

nueva_filas_R1 = int(round(filas_original * ay1))
nueva_columnas_R1 = int(round(columnas_original * ax1))

if esColor:
    R_escala_R1 = np.zeros((nueva_filas_R1, nueva_columnas_R1, num_canales), dtype=A.dtype)
else:
    R_escala_R1 = np.zeros((nueva_filas_R1, nueva_columnas_R1), dtype=A.dtype)

for m_out in range(nueva_filas_R1):
    for n_out in range(nueva_columnas_R1):
        x_orig = n_out / ax1
        y_orig = m_out / ay1

        x1 = int(np.floor(x_orig))
        y1 = int(np.floor(y_orig))
        x2 = x1 + 1
        y2 = y1 + 1
        a = x_orig - x1
        b = y_orig - y1

        if x1 >= 0 and x2 < columnas_original and y1 >= 0 and y2 < filas_original:
            if esColor:
                for canal in range(num_canales):
                    val11 = A[y1, x1, canal]
                    val21 = A[y1, x2, canal]
                    val12 = A[y2, x1, canal]
                    val22 = A[y2, x2, canal]
                    R_escala_R1[m_out, n_out, canal] = (
                        val11 * (1-a) * (1-b) +
                        val21 * a * (1-b) +
                        val12 * (1-a) * b +
                        val22 * a * b
                    )
            else:
                val11 = A[y1, x1]
                val21 = A[y1, x2]
                val12 = A[y2, x1]
                val22 = A[y2, x2]
                R_escala_R1[m_out, n_out] = (
                    val11 * (1-a) * (1-b) +
                    val21 * a * (1-b) +
                    val12 * (1-a) * b +
                    val22 * a * b
                )

plt.subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx += 1
plt.imshow(R_escala_R1)
plt.title('Escala R1- Reducir al 80%')
plt.axis('off')

nueva_filas_R2 = int(round(filas_original * ay2))
nueva_columnas_R2 = int(round(columnas_original * ax2))

if esColor:
    R_escala_R2 = np.zeros((nueva_filas_R2, nueva_columnas_R2, num_canales), dtype=A.dtype)
else:
    R_escala_R2 = np.zeros((nueva_filas_R2, nueva_columnas_R2), dtype=A.dtype)

for m_out in range(nueva_filas_R2):
    for n_out in range(nueva_columnas_R2):
        x_orig = n_out / ax2
        y_orig = m_out / ay2

        x1 = int(np.floor(x_orig))
        y1 = int(np.floor(y_orig))
        x2 = x1 + 1
        y2 = y1 + 1
        a = x_orig - x1
        b = y_orig - y1

        if x1 >= 0 and x2 < columnas_original and y1 >= 0 and y2 < filas_original:
            if esColor:
                for canal in range(num_canales):
                    val11 = A[y1, x1, canal]
                    val21 = A[y1, x2, canal]
                    val12 = A[y2, x1, canal]
                    val22 = A[y2, x2, canal]
                    R_escala_R2[m_out, n_out, canal] = (
                        val11 * (1-a) * (1-b) +
                        val21 * a * (1-b) +
                        val12 * (1-a) * b +
                        val22 * a * b
                    )
            else:
                val11 = A[y1, x1]
                val21 = A[y1, x2]
                val12 = A[y2, x1]
                val22 = A[y2, x2]
                R_escala_R2[m_out, n_out] = (
                    val11 * (1-a) * (1-b) +
                    val21 * a * (1-b) +
                    val12 * (1-a) * b +
                    val22 * a * b
                )

plt.subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx += 1
plt.imshow(R_escala_R2)
plt.title(f'Escala R2 (ax={ax2:.1f}, ay={ay2:.1f})')
plt.axis('off')

plt.tight_layout()
plt.show()
