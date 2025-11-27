import numpy as np
import matplotlib.pyplot as plt

# Parámetros
mul = 2
w0 = 1.0   # frecuencia fundamental

t  = np.arange(-np.pi,  np.pi+0.01, 0.01)
t2 = np.arange(-3*np.pi, -np.pi+0.01, 0.01)
t3 = np.arange( np.pi,   3*np.pi+0.01, 0.01)

ytotal  = np.zeros_like(t)
ytotal2 = np.zeros_like(t2)
ytotal3 = np.zeros_like(t3)

N = 50

for n in range(1, N+1):
    y  = (2/n) * (-1)**(n+1) * np.sin(n*t)
    y2 = (2/n) * (-1)**(n+1) * np.sin(n*t2)
    y3 = (2/n) * (-1)**(n+1) * np.sin(n*t3)

    ytotal  += y
    ytotal2 += y2
    ytotal3 += y3

ytotal[0:3]   = ytotal[3]
ytotal2[0:3]  = ytotal2[3]
ytotal3[0:3]  = ytotal3[3]
ytotal[624:629]   = ytotal[624]
ytotal2[624:629]  = ytotal2[624]
ytotal3[624:629]  = ytotal3[624]

# --------- Serie de Fourier truncada ---------
plt.figure()
plt.plot(t,  ytotal,  'k', linewidth=2)
plt.plot(t2, ytotal2, 'k', linewidth=2)
plt.plot(t3, ytotal3, 'k', linewidth=2)
plt.title('Serie de Fourier truncada (N = 50)')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)

# --------- Espectro de amplitud ---------
n  = np.arange(1, N+1)
Bn = (2.0/n) * (-1)**(n+1)
wn = n * w0

plt.figure()
plt.stem(wn, np.abs(Bn), basefmt=" ")
plt.title('Espectro de amplitud |B_n| vs ω_n')
plt.xlabel('ω_n')
plt.ylabel('|B_n|')
plt.grid(True)

plt.show()
