import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd

# --- Leer archivo CSV ---
x =([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,
    9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3,13,12.6,12,11.5,
    10.8,10,9,8.5,8.25,8,7.5,7,6,5,4.8,5,5.25,5.35,5.5,5.65,5,
    4.35,4,3,2.15,1.5,1,0.9])

y =([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3,
    2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25, 0.15,0.16,0,0.1,
    0,-0.25,-0.45,-0.4,-1,-2,-3,-4,-5,-5.25,-5.25,-4.5,-3,-2,-1,0,
    0.25,1,1,1,1.15,1,1,1.3])

# --- Gráfica ---
plt.figure()
plt.plot(x, y, 'ob', linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Curva Paramétrica para Pato')
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
