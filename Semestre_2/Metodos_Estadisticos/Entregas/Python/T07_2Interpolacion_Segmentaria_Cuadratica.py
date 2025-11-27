import numpy as np
import matplotlib.pyplot as plt
import time

# Datos
xt = np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0,
               7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
f_x = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1,
                2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])

# Figura principal
plt.figure()
plt.plot(xt, f_x, 'o', linewidth=2)
plt.title('Interpolación Segmentaria Cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

length = len(xt)

# Segmentos cuadráticos
for n in range(length - 2):
    x0, y0 = xt[n],     f_x[n]
    x1, y1 = xt[n+1],   f_x[n+1]
    x2, y2 = xt[n+2],   f_x[n+2]

    A = np.array([
        [x0**2, x0, 1],
        [x1**2, x1, 1],
        [x2**2, x2, 1]
    ])

    coef = np.linalg.solve(A, np.array([y0, y1, y2]))

    a, b, c = coef

    x_seg = np.arange(x0, x1+0.01, 0.01)
    fx_seg = a*x_seg**2 + b*x_seg + c

    plt.plot(x_seg, fx_seg, 'r', linewidth=2)
    plt.pause(1)

plt.show()
