import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

plt.plot(x, y, 'ob', linewidth=2)
plt.grid(True)

n = len(x)

sum_xi = np.sum(x)
sum_xi2 = np.sum(x**2)
sum_yi = np.sum(y)
sum_xiyi = np.sum(x * y)

A = np.array([
    [n, sum_xi],
    [sum_xi, sum_xi2]
])

d = np.array([sum_yi, sum_xiyi])

# Coeficientes del método manual
b = np.linalg.solve(A, d)
a0 = b[0]
a1 = b[1]

x_aprox = np.arange(10, 101)
y_aprox = a0 + a1 * x_aprox

plt.plot(x_aprox, y_aprox, 'r', linewidth=2)

# Método usando polyfit
p = np.polyfit(x, y, 1)
y_polyfit = np.polyval(p, x_aprox)

plt.plot(x_aprox, y_polyfit, '--k', linewidth=2)

plt.title('Regresión Lineal: Método Manual vs polyfit')
plt.legend(['Datos', 'Manual', 'polyfit'], loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
