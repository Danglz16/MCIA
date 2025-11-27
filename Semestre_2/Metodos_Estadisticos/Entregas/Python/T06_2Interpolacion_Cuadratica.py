import numpy as np
import matplotlib.pyplot as plt

# Puntos
x0 = 1
f_x0 = np.log(x0)

x1 = 3
f_x1 = np.log(x1)

x2 = 6
f_x2 = np.log(x2)

# Punto a interpolar
x = 2

# Interpolación cuadrática (Lagrange)
L0 = ((x - x1)*(x - x2)) / ((x0 - x1)*(x0 - x2))
L1 = ((x - x0)*(x - x2)) / ((x1 - x0)*(x1 - x2))
L2 = ((x - x0)*(x - x1)) / ((x2 - x0)*(x2 - x1))

f2_x = f_x0*L0 + f_x1*L1 + f_x2*L2

# Valor real
f_x_real = np.log(x)

# Curva real
x_real = np.arange(x0, x2 + 0.01, 0.01)
f_real = np.log(x_real)

# --- Gráfica ---
plt.figure()
plt.plot(x_real, f_real, linewidth=2)
plt.title('Interpolación Cuadrática')
plt.xlabel('X')
plt.ylabel('Log(x)')
plt.grid(True)

# Puntos base
plt.plot(x0, f_x0, 'ro', linewidth=2)
plt.plot(x1, f_x1, 'ro', linewidth=2)
plt.plot(x2, f_x2, 'ro', linewidth=2)

x_vec = np.array([x0, x1, x2])
y_vec = np.array([f_x0, f_x1, f_x2])
plt.plot(x_vec, y_vec, 'r', linewidth=2)

# Punto real e interpolado
plt.plot(x, f_x_real, 'bo', linewidth=2)
plt.plot(x, f2_x, 'go', linewidth=2)

plt.legend(['Real', 'Puntos base', 'Línea base', 'Real en x', 'Interpolado'])
plt.show()
