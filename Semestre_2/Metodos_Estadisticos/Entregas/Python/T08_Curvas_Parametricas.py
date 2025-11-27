import numpy as np
import matplotlib.pyplot as plt

# Datos
xi = np.array([-1, 0, 1, 0, 1])
yi = np.array([0, 1, 0.5, 0, -1])

n = len(xi)
t = np.linspace(0, 1, 100)

# Curvas paramétricas x(t) y y(t)
x_t = ((((((64*t) - (352/3))*t) + 60)*t) - (14/3))*t - 1
y_t = ((((((-64/3)*t) + 48)*t) - (116/3))*t + 11)*t

# --- Gráfica paramétrica x(t) y y(t) ---
plt.figure()

plt.subplot(1, 2, 1)
plt.plot(t, x_t, 'r', linewidth=2)
plt.title('Curva Paramétrica x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(1, 2, 2)
plt.plot(t, y_t, 'b', linewidth=2)
plt.title('Curva Paramétrica y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')

# --- Gráfica final de la curva en el plano ---
plt.figure()
plt.plot(xi, yi, 'o', linewidth=2)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curva Paramétrica en el Plano')
plt.plot(x_t, y_t, 'r', linewidth=2)

plt.show()
