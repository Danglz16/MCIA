import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import time

# Datos
xt = np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0,
               7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
f_x = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25,
                2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])

# -------- Interpolación segmentaria lineal --------
plt.close('all')

plt.figure()
plt.plot(xt, f_x, 'o', linewidth=2)
plt.title('Interpolacion Segmentaria Lineal')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

length = len(xt)

for n in range(length - 1):
    m = (f_x[n+1] - f_x[n]) / (xt[n+1] - xt[n])
    x_seg = np.arange(xt[n], xt[n+1] + 0.01, 0.01)
    fx_seg = f_x[n] + m * (x_seg - xt[n])

    plt.plot(x_seg, fx_seg, 'r', linewidth=2)

    if n > 4:
        plt.plot(x_seg, fx_seg, 'r', linewidth=2)

    plt.pause(1)
plt.show()
