import numpy as np

def generar_funcion_gaussiana(puntos=50):
    A = np.random.uniform(0.5, 2)
    mu = np.random.uniform(-1, 1)
    sigma = np.random.uniform(0.5, 1.5)
    x = np.linspace(-5, 5, puntos)
    y = A * np.exp(-((x - mu)**2) / (2 * sigma**2))
    return y, 1  # Etiqueta 1 para gaussiana

def generar_funcion_no_gaussiana(puntos=50):
    x = np.linspace(-5, 5, puntos)
    tipo = np.random.choice(['lineal', 'seno', 'cuadratica'])
    if tipo == 'lineal':
        m = np.random.uniform(-2, 2)
        b = np.random.uniform(-1, 1)
        y = m * x + b
    elif tipo == 'seno':
        freq = np.random.uniform(0.5, 2)
        y = np.sin(freq * x)
    elif tipo == 'cuadratica':
        a = np.random.uniform(-1, 1)
        b = np.random.uniform(-2, 2)
        c = np.random.uniform(-1, 1)
        y = a * x**2 + b * x + c
    return y, 0  # Etiqueta 0 para no gaussiana

def generar_datos(n=100, puntos=50):
    datos = []
    for _ in range(n):
        datos.append(generar_funcion_gaussiana(puntos))
        datos.append(generar_funcion_no_gaussiana(puntos))
    np.random.shuffle(datos)
    X = np.array([d[0] for d in datos])
    Y = np.array([[d[1]] for d in datos])
    return X, Y

def lista_funciones_predefinidas():
    return {
        "Gaussiana": "exp(-x**2)",
        "Lineal": "x",
        "Cuadrática": "x**2",
        "Seno": "sin(x)",
        "Coseno": "cos(x)",
        "Señal 1":"sin(20*pi*x)",
        "Señal 2":"1/(1 + e**(-200*(x-0.05)))",
        "Señal 3":"0.5 * e**(-5000*(x-0.05)**2)",
        "Señal 4":"0.5 * (exp(-5000 * (x - 0.1)**2) + exp(-5000 * x**2))",
        "Señal 5":"0.8*e**(-5000*(x-0.05)**2) + 0.5*e**(-5000*(x-0.09)**2)",
        "Señal 6":"sin(20*pi*x) + 0.5*cos(60*pi*x)",
        "Señal 7":"sin(20*pi*x) + 0.5*cos(60*pi*x) + 0.3*sin(120*pi*x)",
        "Señal 8":"0.7*e**(-5000*(x-0.02)**2)",
        "Señal 9":"1.8*e**(-500*(x-0.07)**2) - 1",
        "Señal 10":"sin(100*pi*x) * (1.8*e**((-(x-0.07)**2) / 0.0018) - 1)"
    }
