import numpy as np
import matplotlib.pyplot as plt

# Datos
x0 = 1
f_x0 = np.log(x0)

x1 = 6
f_x1 = np.log(x1)

x = 2

# Interpolación lineal
f1_x = f_x0 + ((f_x1 - f_x0) / (x1 - x0)) * (x - x0)

# Valor real
f1_x_ver = np.log(x)

# Curva real
x_real = np.arange(x0, x1 + 0.01, 0.01)
f_real = np.log(x_real)

# Gráfica
plt.figure()
plt.plot(x_real, f_real, linewidth=2)
plt.title("Interpolación Lineal")
plt.xlabel("X")
plt.ylabel("Log(x)")
plt.grid(True)

# Puntos x0 y x1
plt.plot(x0, f_x0, 'ro', linewidth=2)
plt.plot(x1, f_x1, 'ro', linewidth=2)

# Línea entre los puntos
plt.plot([x0, x1], [f_x0, f_x1], color='red')

# Punto real del valor interpolado
plt.plot(x, f1_x_ver, 'bo', linewidth=2)

# Punto aproximado con interpolación
plt.plot(x, f1_x, 'ro', linewidth=2)

plt.show()
