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

# --- Interpolación polinomial (Newton, grado 2) ---

# Diferencias divididas (coeficientes de Newton)
b0 = f_x0
b1 = (f_x1 - f_x0) / (x1 - x0)
b2 = (((f_x2 - f_x1) / (x2 - x1)) - ((f_x1 - f_x0) / (x1 - x0))) / (x2 - x0)

# Polinomio en el punto x
f2_x = b0 + b1*(x - x0) + b2*(x - x0)*(x - x1)

# Valor real
f_x_real = np.log(x)

# Curva real
x_real = np.arange(x0, x2 + 0.01, 0.01)
f_real = np.log(x_real)

# Polinomio de Newton en todo el intervalo
f_newton = b0 + b1*(x_real - x0) + b2*(x_real - x0)*(x_real - x1)

# --- Gráfica ---
plt.figure()
plt.plot(x_real, f_real, linewidth=2, label='Real')
plt.grid(True)
plt.title('Interpolación Polinomial (Newton, grado 2)')
plt.xlabel('X')
plt.ylabel('Log(x)')

# Puntos base
plt.plot(x0, f_x0, 'ro', linewidth=2)
plt.plot(x1, f_x1, 'ro', linewidth=2)
plt.plot(x2, f_x2, 'ro', linewidth=2)

x_vec = np.array([x0, x1, x2])
y_vec = np.array([f_x0, f_x1, f_x2])
plt.plot(x_vec, y_vec, 'r', linewidth=2, label='Línea base')

# Polinomio interpolante
plt.plot(x_real, f_newton, 'g--', linewidth=2, label='Polinomio Newton')

# Punto real vs interpolado
plt.plot(x, f_x_real, 'bo', linewidth=2, label='Real en x')
plt.plot(x, f2_x, 'go', linewidth=2, label='Interpolado')

plt.legend(loc='best')
plt.show()
