import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import time

# %% Funciones Newton

def newton_coeffs_improved(x, f_x):
    x = np.asarray(x, dtype=float)
    f_x = np.asarray(f_x, dtype=float)
    n = len(x)
    F = np.zeros((n, n), dtype=float)
    F[:, 0] = f_x
    for j in range(1, n):
        for i in range(0, n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x[i+j] - x[i])
    coef_new = np.diag(F)
    return coef_new


def newton_eval(coef, x_data, x_val):
    x_data = np.asarray(x_data, dtype=float)
    coef = np.asarray(coef, dtype=float)
    n = len(coef)
    result = coef[-1]
    for k in range(n-2, -1, -1):
        result = result * (x_val - x_data[k]) + coef[k]
    return result
# Interpolación polinomial con una señal de ECG

x_mat = loadmat('Semestre_2/Metodos_Estadisticos/Entregas/Datos/100m.mat')

ecg_val = x_mat['val']          # matriz tal como en MATLAB
ecg = (ecg_val - 0) / 200.0     # normalización
ecg = ecg.T                     # transponer

fs = 360.0
ts = 1.0 / fs

ecg = ecg[:, 1]                 # canal 2 (índice 1 en Python)
t = np.arange(len(ecg)) * ts

n_puntos = 512
x_data_ecg = t[:n_puntos]
y_data_ecg = ecg[:n_puntos]

plt.figure()
plt.plot(t, ecg)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.title('Señal de ECG Original')
plt.grid(True)

# %% Interpolación de Newton y tiempo de ejecución

start = time.perf_counter()

newton_coef_ecg = newton_coeffs_improved(x_data_ecg, y_data_ecg)
x_interp_ecg = np.linspace(x_data_ecg[0], x_data_ecg[-1], 512)

y_interp_ecg = np.zeros_like(x_interp_ecg)
for i in range(len(x_interp_ecg)):
    y_interp_ecg[i] = newton_eval(newton_coef_ecg, x_data_ecg, x_interp_ecg[i])

tiempo_ejecucion = time.perf_counter() - start
print(f'Tiempo de ejecución de la interpolación: {tiempo_ejecucion:.4f} segundos')

# %% Gráfica completa

plt.figure()
plt.plot(t, ecg, 'b', linewidth=0.5)
plt.plot(x_interp_ecg, y_interp_ecg, 'r', linewidth=1.2)
plt.plot(x_data_ecg, y_data_ecg, 'go', markersize=3)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.title('Interpolación polinómica de Newton sobre señal ECG')
plt.legend(['ECG original', 'Interpolación Newton', 'Puntos de interpolación'])
plt.grid(True)

# %% Zoom 512 puntos

plt.figure()
plt.plot(x_data_ecg, y_data_ecg, 'go-', markersize=3)
plt.plot(x_interp_ecg, y_interp_ecg, 'r-')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.title('Zoom: primeros 512 puntos con interpolación')
plt.grid(True)

margen_x = 0.2 * (x_data_ecg[-1] - x_data_ecg[0])
plt.xlim([x_data_ecg[0] - margen_x, x_data_ecg[-1] + margen_x])

y_min = np.min(y_data_ecg)
y_max = np.max(y_data_ecg)
margen_y = 0.5 * (y_max - y_min)
plt.ylim([y_min - margen_y, y_max + margen_y])

# %% Zoom primeros 30 puntos

segmento_zoom = 30
margen_x_100 = 0.05 * (x_data_ecg[segmento_zoom-1] - x_data_ecg[0])

y_min_100 = np.min(y_data_ecg[:segmento_zoom])
y_max_100 = np.max(y_data_ecg[:segmento_zoom])
margen_y_100 = 0.1 * (y_max_100 - y_min_100)

plt.figure()
plt.plot(x_data_ecg[:segmento_zoom], y_data_ecg[:segmento_zoom],
         'go-', markersize=3)

idx_zoom = (x_interp_ecg >= x_data_ecg[0]) & (x_interp_ecg <= x_data_ecg[segmento_zoom-1])
plt.plot(x_interp_ecg[idx_zoom], y_interp_ecg[idx_zoom], 'r-')

plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.title(f'Zoom detallado: primeros {segmento_zoom} puntos')
plt.grid(True)
plt.xlim([x_data_ecg[0] - margen_x_100,
          x_data_ecg[segmento_zoom-1] + margen_x_100])
plt.ylim([y_min_100 - margen_y_100, y_max_100 + margen_y_100])

plt.show()



