import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import time

# ----- Inicio -----
start = time.time()

x = np.pi / 3
nc = 5
n = 6

Es = (0.5 * 10**(2 - nc))

Vv = 0.5
Aprox_ant = 0

cos_x = 1
Aprox_act = cos_x

Ev = [abs((Vv - cos_x) / Vv) * 100]
Ea = [abs((Aprox_act - Aprox_ant) / Aprox_act) * 100]

# ----- Serie de Taylor para cos(x) -----
for m in range(1, n):
    Aprox_ant = Aprox_act
    
    cos_x = cos_x + ((-1)**m) * (x**(2*m)) / factorial(2*m)
    Aprox_act = cos_x

    Ev_new = abs((Vv - cos_x) / Vv) * 100
    Ea_new = abs((Aprox_act - Aprox_ant) / Aprox_act) * 100

    # Igual que MATLAB:
    if Ea_new > 100:
        Ea_new = Ea_new - (Ea_new - 80)

    Ev.append(Ev_new)
    Ea.append(Ea_new)

# ----- Tiempo -----
end = time.time()
print(f"Tiempo de ejecución: {end - start:.6f} segundos")

# ----- Gráfica -----
plt.plot(Ev, 'r', linewidth=2)
plt.xlabel('Numero de terminos')
plt.ylabel('% error verdadero')
plt.title('Comportamiento del error')
plt.grid(True)

plt.plot(Ea, 'b', linewidth=2)
plt.legend(['ev(%)', 'ea(%)'])

plt.show()
