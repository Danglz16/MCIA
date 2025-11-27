import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

plt.figure()
plt.plot(x, y, 'o', linewidth=3)
plt.grid(True)
plt.title('Regresión Cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')

# Elementos de A
n   = len(x)
Sx  = np.sum(x)
Sx2 = np.sum(x**2)
Sx3 = np.sum(x**3)
Sx4 = np.sum(x**4)
Sy  = np.sum(y)
Sxy = np.sum(x * y)
Sx2y = np.sum((x**2) * y)

# Matriz A y vector b
A = np.array([
    [n,   Sx,  Sx2],
    [Sx,  Sx2, Sx3],
    [Sx2, Sx3, Sx4]
])

b = np.array([Sy, Sxy, Sx2y])

# Coeficientes del polinomio
r = np.linalg.solve(A, b)
a0, a1, a2 = r[0], r[1], r[2]

# Curva ajustada
x_aux = np.linspace(x[0], x[-1], 500)
y_aux = a0 + a1*x_aux + a2*(x_aux**2)

plt.plot(x_aux, y_aux, linewidth=2)
plt.legend(['Datos', 'Regresión Cuadrática'], loc='best')

# Predicción para puntos reales
y_hat = a0 + a1*x + a2*(x**2)

# Cálculo de R²
SS_res = np.sum((y - y_hat)**2)
SS_tot = np.sum((y - np.mean(y))**2)
R2 = 1 - SS_res/SS_tot

# Correlación
r_val = np.corrcoef(y, y_hat)[0, 1]

print("Coeficientes:")
print(f"a0 = {a0}")
print(f"a1 = {a1}")
print(f"a2 = {a2}")
print(f"\nR^2 = {R2}")
print(f"Correlación = {r_val}")

plt.show()
