import numpy as np
import matplotlib.pyplot as plt

# --- Orden del polinomio ---
n = int(input("Orden de la ecuacion: "))

# Datos
x = np.array([10, 20, 30, 40, 50, 60, 70, 80], dtype=float)
y = np.array([25, 70, 380, 550, 610, 1220, 830, 1450], dtype=float)

N = len(x)
x = x.reshape(-1, 1)  # columna
y = y.reshape(-1, 1)

# Precalcular sumas de potencias de x hasta 2n
Sx = np.zeros(2*n + 1)
for k in range(0, 2*n + 1):
    Sx[k] = np.sum(x**k)

# Matriz A (tamaño (n+1)x(n+1))
A = np.zeros((n+1, n+1))
for i in range(0, n+1):
    for j in range(0, n+1):
        A[i, j] = Sx[i + j]

# Vector b
b = np.zeros((n+1, 1))
for i in range(0, n+1):
    b[i] = np.sum(y * (x**i))

# Coeficientes p (en orden creciente: x^0, x^1, ..., x^n)
p = np.linalg.solve(A, b)

# y_hat en los puntos originales
y_hat = np.zeros_like(y)
for i in range(0, n+1):
    y_hat = y_hat + p[i] * (x**i)

# Métricas
SS_res = np.sum((y - y_hat)**2)
SS_tot = np.sum((y - np.mean(y))**2)
R2 = 1 - SS_res/SS_tot

k = n  # número de predictores (x, x^2, ..., x^n)
R2_adj = 1 - (1 - R2) * (N - 1) / (N - k - 1)

# Aplastamos a vectores 1D para corrcoef
r_matrix = np.corrcoef(y.ravel(), y_hat.ravel())
r_val = r_matrix[0, 1]

# Curva suave para graficar
x_aux = np.linspace(np.min(x), np.max(x), 500).reshape(-1, 1)
y_aux = np.zeros_like(x_aux)
for i in range(0, n+1):
    y_aux = y_aux + p[i] * (x_aux**i)


# Resultados
print("Coeficientes (x^0 .. x^n) en orden creciente de grado:")
print(p.ravel())
print(f"R^2         = {R2:.6f}")
print(f"R^2 ajustado = {R2_adj:.6f}")
print(f"Correlación  = {r_val:.6f}")

# Gráfica
plt.figure()
plt.plot(x, y, 'o', linewidth=3, label='Datos')
plt.plot(x_aux, y_aux, 'r', linewidth=2, label='Regresion Polinomica')
plt.grid(True)
plt.title(f'Regresion Polinomica de grado n = {n}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='best')
plt.show()

