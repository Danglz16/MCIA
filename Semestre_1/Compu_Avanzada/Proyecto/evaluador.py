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
