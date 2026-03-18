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
