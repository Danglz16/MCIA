import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import time

# ----- Inicio -----
start = time.time()

x = np.pi / 6
nc = 5
sen_x = 0
n = 6

Es = (0.5 * 10**(2 - nc))

Vv = 0.5
Aprox_ant = 0

# ----- Primer término -----
sen_x = sen_x + x
Aprox_act = sen_x

Ev = [abs((Vv - sen_x) / Vv) * 100]
Ea = [abs((Aprox_act - Aprox_ant) / Aprox_act) * 100]

# ----- Serie seno -----
for m in range(1, n):
    Aprox_ant = Aprox_act

    sen_x = sen_x + ((-1)**m) * (x**(2*m + 1)) / factorial(2*m + 1)
    Aprox_act = sen_x

    Ev_new = abs((Vv - sen_x) / Vv) * 100
    Ea_new = abs((Aprox_act - Aprox_ant) / Aprox_act) * 100

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
plt.legend(['ev(%)','ea(%)'])
plt.show()
