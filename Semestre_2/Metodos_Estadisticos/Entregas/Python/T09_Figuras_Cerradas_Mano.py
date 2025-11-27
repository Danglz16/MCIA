import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd

# --- Leer archivo CSV ---
M = pd.read_csv('Semestre_2/Metodos_Estadisticos/Entregas/Datos/puntos_mano.csv', header=None).values
x = M[:, 0]
y = M[:, 1]

# --- Gráfica ---
plt.figure()
plt.plot(x, y, 'ob', linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Curva Paramétrica para Mano')
plt.grid(True)
plt.hold = True

# --- Generar parámetros t ---
tam = len(y)
t = np.linspace(0, 10, tam)
t2 = np.arange(0, 10.01, 0.01)

# --- Interpolación cúbica ---
cs_x = CubicSpline(t, x)
cs_y = CubicSpline(t, y)

xt = cs_x(t2)
yt = cs_y(t2)

# --- Graficar curva ---
plt.plot(xt, yt, linewidth=2)
plt.legend(['Puntos', 'Curva'])
plt.show()
