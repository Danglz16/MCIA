import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# ----- Variables iniciales -----
x = 0.5
nc = 5
e_x = 0
n = 6

Es = (0.5 * 10**(2-nc))

Vv = 1.648721271
Aprox_ant = 0

# ----- Primer término -----
e_x = e_x + (x**0) / factorial(0)
Aprox_act = e_x

Ev = [abs((Vv - e_x) / Vv) * 100]
Ea = [abs((Aprox_act - Aprox_ant) / Aprox_act) * 100]

# ----- Serie -----
for m in range(1, n):
    Aprox_ant = Aprox_act
    e_x = e_x + (x**m) / factorial(m)
    Aprox_act = e_x

    Ev_new = abs((Vv - e_x) / Vv) * 100
    Ea_new = abs((Aprox_act - Aprox_ant) / Aprox_act) * 100

    Ev.append(Ev_new)
    Ea.append(Ea_new)

# ----- Gráfica -----
plt.plot(Ev, 'r', linewidth=2)
plt.xlabel('Numero de terminos')
plt.ylabel('% error verdadero')
plt.title('Comportamiento del error')
plt.grid(True)

plt.plot(Ea, 'b', linewidth=2)
plt.legend(['ev(%)', 'ea(%)'])
plt.show()
