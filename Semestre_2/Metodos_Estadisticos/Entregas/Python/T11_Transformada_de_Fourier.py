import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, buttord
import numpy as np
import matplotlib.pyplot as plt

def fft_signal(y, Fs):

    # Longitud de la señal
    L = len(y)

    # Siguiente potencia de 2
    NFFT = 1 << (L - 1).bit_length()   # nextpow2 equivalente

    # FFT normalizada
    Y = np.fft.fft(y, NFFT) / L

    # Rango de frecuencia unilateral
    f = (Fs / 2) * np.linspace(0, 1, NFFT//2 + 1)

    # Gráfica del espectro
    plt.plot(f, 2 * np.abs(Y[:NFFT//2 + 1]))
    plt.title('Espectro unilateral de y(t)')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('|Y(f)|')

    return f
# %% Selección del tipo de filtrado
# 1 -> Pasa bajo
# 2 -> Pasa alto
# 3 -> Pasa banda
# 4 -> Reprime banda
tipo = 2
cont = 0

# %% Crear señal de audio
f0 = 8e3      # 8 kHz
a = 3         # amplitud
fs = 44.1e3   # frecuencia de muestreo (Hz)
T = 1.5       # duración en segundos

t = np.linspace(0, T, int(T*fs))  # vector de tiempo

# Señales
# s1 = a * np.sin(2*np.pi*f0*t)
s1 = np.cos(2*np.pi*100*t) + 0.5*np.random.randn(len(t))
s2 = 0.75 * a * np.sin(2*np.pi*(1.5*f0)*t)
s3 = 0.5  * a * np.sin(2*np.pi*(2.0*f0)*t)

y = s1 + s2 + s3

plt.close('all')

# Señal original en el tiempo
plt.subplot(4, 1, 1)
plt.plot(t, y)
plt.title('señal ORIGINAL')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (V)')
plt.xlim([0, 20/f0])
plt.grid(True)

# %% FFT de la señal original
plt.subplot(4, 1, 2)
fft_signal(y, fs)
plt.title('ESPECTRO DE LA señal ORIGINAL')
plt.xlim([0, 3*f0])
plt.grid(True)

# %% Diseño del filtro según tipo
if tipo == 1:
    # Pasa bajas
    titulo = 'FILTRO PASA BAJAS'
    fNorm = 15e3 / (fs/2)
    b, a_f = butter(10, fNorm, btype='low')

elif tipo == 2:
    # Pasa altas
    titulo = 'FILTRO PASA ALTAS'
    fNorm = 15e3 / (fs/2)
    b, a_f = butter(10, fNorm, btype='high')

elif tipo == 3:
    # Pasa banda
    titulo = 'FILTRO PASA BANDA'
    Wp = np.array([11.5e3, 12.5e3])/(fs/2)
    Ws = np.array([11e3, 13e3])/(fs/2)
    Rp = 3
    Rs = 40
    n, Wn = buttord(Wp, Ws, Rp, Rs)
    b, a_f = butter(n, Wn, btype='band')

else:
    # Reprime banda (band-stop: combina low + high)
    titulo = 'FILTRO REPRIME BANDA'
    fNorm_1 = 11e3 / (fs/2)
    fNorm_2 = 13e3 / (fs/2)
    b_low,  a_low  = butter(10, fNorm_1, btype='low')
    b_high, a_high = butter(10, fNorm_2, btype='high')

    y_baja = filtfilt(b_low,  a_low,  y)
    y_alta = filtfilt(b_high, a_high, y)
    y_Low = y_baja + y_alta
    cont = 1

# %% Filtrado de la señal
if cont == 0:
    y_Low = filtfilt(b, a_f, y)
    cont = 0

# Señal filtrada en el tiempo
plt.subplot(4, 1, 3)
plt.plot(t, y_Low)
plt.title('señal FILTRADA — ' + titulo)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (V)')
plt.xlim([0, 20/f0])
plt.grid(True)

# Espectro de la señal filtrada
plt.subplot(4, 1, 4)
fft_signal(y_Low, fs)
plt.title('ESPECTRO DE LA señal FILTRADA')
plt.xlim([0, 3*f0])
plt.grid(True)

plt.tight_layout()
plt.show()


# %% Función auxiliar: FFT y gráfico de magnitud
def fft_signal(sig, fs):
    """
    Calcula y grafica el espectro de magnitud de 'sig' (similar a tu fft_signal de MATLAB).
    """
    N = len(sig)
    # FFT
    Y = np.fft.fft(sig)
    # Frecuencias asociadas
    freqs = np.fft.fftfreq(N, d=1/fs)
    # Considerar solo parte positiva
    mask = freqs >= 0
    freqs_pos = freqs[mask]
    Y_mag = np.abs(Y[mask]) * 2.0 / N  # magnitud normalizada

    plt.plot(freqs_pos, Y_mag)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
