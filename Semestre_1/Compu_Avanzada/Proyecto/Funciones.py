"""
Archivo unificado de funciones.

Incluye:
- Generación de funciones gaussianas y no gaussianas
- Evaluación segura de funciones desde strings
- Entrenamiento y evaluación de red neuronal para clasificación de funciones

Requiere: numpy, NN.py (para RedNeuronal y funciones asociadas)
"""

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


import numpy as np

def evaluar_funcion_str(funcion_str, puntos=50):
    """
    Evalúa una funciones escritas
    Regresa un vector y = f(x) con 50 puntos de evaluación entre -5 y 5.
    """
    x = np.linspace(-5, 5, puntos)
    
    # Diccionario de funciones
    contexto = {
        'x': x,
        'sin': np.sin,
        'cos': np.cos,
        'exp': np.exp,
        'tan': np.tan,
        'sqrt': np.sqrt,
        'abs': np.abs,
        'log': np.log,
        'pi': np.pi,
        'e': np.e
    }

    try:
        y = eval(funcion_str, contexto)
        if not isinstance(y, np.ndarray):
            raise ValueError("La función debe devolver un vector.")
        return np.array(y)
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")


from generador_funciones import generar_datos
from NN import RedNeuronal, entrenar_binario, evaluar_binario

# Crear red de 50 entradas, 10 ocultas, 1 salida
red = RedNeuronal(num_entradas=50, num_ocultas=10, num_salidas=1)

# Datos
X, Y = generar_datos(n=100, puntos=50)

# Entrenar
entrenar_binario(red, X, Y)

# Evaluar
evaluar_binario(red, X, Y)

# Guardar
from NN import guardar_pesos
guardar_pesos(red, ["No Gaussiana", "Gaussiana"], ruta="pesos_funcion.txt")
