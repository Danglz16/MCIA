import numpy as np
import pandas as pd
from sympy import symbols, sin, series, lambdify

# Variable simbólica
x = symbols('x')

# --- Función polinómica ---
f_poly = x**4 - 3*x**2 + 2
a1 = 1          # punto de expansión
n1 = 4          # orden

# Serie de Taylor
t_poly = series(f_poly, x, a1, n1+1).removeO()

print(f"Polinómica: f(x) = x^4 - 3x^2 + 2, expandida en a = {a1}, orden = {n1}")
print(t_poly)

# Tabla polinómica
x_vals = np.arange(-2, 3.5, 0.5)

f_poly_num = lambdify(x, f_poly, 'numpy')
t_poly_num = lambdify(x, t_poly, 'numpy')

f_real_vals = f_poly_num(x_vals)
f_taylor_vals = t_poly_num(x_vals)
error_abs = np.abs(f_real_vals - f_taylor_vals)

tab_poly = pd.DataFrame({
    'x': x_vals,
    'f_real': f_real_vals,
    'f_taylor': f_taylor_vals,
    'error_abs': error_abs
})

print("\nTabla polinómica:")
print(tab_poly)

# --- Función trigonométrica ---
f_trig = sin(x)
a2 = 0
n2 = 9

t_trig = series(f_trig, x, a2, n2+1).removeO()

print(f"\nTrigonométrica: f(x) = sin(x), expandida en a = {a2}, orden = {n2}")
print(t_trig)

# Tabla trigonométrica
x_vals2 = np.arange(-np.pi, np.pi + np.pi/6, np.pi/6)

f_trig_num = lambdify(x, f_trig, 'numpy')
t_trig_num = lambdify(x, t_trig, 'numpy')

f_real_vals2 = f_trig_num(x_vals2)
f_taylor_vals2 = t_trig_num(x_vals2)
error_abs2 = np.abs(f_real_vals2 - f_taylor_vals2)

tab_trig = pd.DataFrame({
    'x': x_vals2,
    'f_real': f_real_vals2,
    'f_taylor': f_taylor_vals2,
    'error_abs': error_abs2
})

print("\nTabla trigonométrica:")
print(tab_trig)
