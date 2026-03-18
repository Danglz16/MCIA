import random
import math

# Función de activación sigmoide y su derivada
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    sx = sigmoide(x)
    return sx * (1 - sx)

# Clase de una neurona individual
class Neurona:
    def __init__(self, num_entradas):
        self.pesos = [random.uniform(-1, 1) for _ in range(num_entradas)]
        self.bias = random.uniform(-1, 1)
    
    def activar(self, entradas):
        suma = sum(w * e for w, e in zip(self.pesos, entradas)) + self.bias
        return sigmoide(suma)

# Clase de una capa de la red
class Capa:
    def __init__(self, num_neuronas, num_entradas_por_neurona):
        self.neuronas = [Neurona(num_entradas_por_neurona) for _ in range(num_neuronas)]
    
    def activar(self, entradas):
        return [neurona.activar(entradas) for neurona in self.neuronas]

# Red neuronal con una capa oculta
class RedNeuronal:
    def __init__(self, num_entradas, num_ocultas, num_salidas):
        self.num_entradas = num_entradas
        self.capa_oculta = Capa(num_ocultas, num_entradas)
        self.capa_salida = Capa(num_salidas, num_ocultas)

    def predecir(self, entradas, guardar=False):
        if guardar:
            self.entrada = entradas
            self.z_oculta = []
            self.salida_oculta = []
            for neurona in self.capa_oculta.neuronas:
                z = sum(w * e for w, e in zip(neurona.pesos, entradas)) + neurona.bias
                self.z_oculta.append(z)
                self.salida_oculta.append(sigmoide(z))

            self.z_salida = []
            self.salida_final = []
            for neurona in self.capa_salida.neuronas:
                z = sum(w * h for w, h in zip(neurona.pesos, self.salida_oculta)) + neurona.bias
                self.z_salida.append(z)
                self.salida_final.append(sigmoide(z))

            return self.salida_final
        else:
            salida_oculta = self.capa_oculta.activar(entradas)
            salida_final = self.capa_salida.activar(salida_oculta)
            return salida_final

    def entrenar(self, datos, etiquetas, tasa_aprendizaje=0.1, epocas=1000):
        for epoca in range(epocas):
            error_total = 0
            for entrada, objetivo in zip(datos, etiquetas):
                # FORWARD almacenando valores
                salida = self.predecir(entrada, guardar=True)

                # BACKPROPAGATION
                # Errores en capa de salida
                errores_salida = [
                    (o - s) * derivada_sigmoide(z)
                    for s, o, z in zip(salida, objetivo, self.z_salida)
                ]

                # Errores en capa oculta
                errores_oculta = []
                for i, z in enumerate(self.z_oculta):
                    error = sum(
                        errores_salida[j] * self.capa_salida.neuronas[j].pesos[i]
                        for j in range(len(errores_salida))
                    )
                    errores_oculta.append(error * derivada_sigmoide(z))

                # Actualizar pesos capa salida
                for i, neurona in enumerate(self.capa_salida.neuronas):
                    for j in range(len(neurona.pesos)):
                        neurona.pesos[j] += tasa_aprendizaje * errores_salida[i] * self.salida_oculta[j]
                    neurona.bias += tasa_aprendizaje * errores_salida[i]

                # Actualizar pesos capa oculta
                for i, neurona in enumerate(self.capa_oculta.neuronas):
                    for j in range(len(neurona.pesos)):
                        neurona.pesos[j] += tasa_aprendizaje * errores_oculta[i] * self.entrada[j]
                    neurona.bias += tasa_aprendizaje * errores_oculta[i]

                # Acumular error
                error_total += sum((o - s)**2 for s, o in zip(salida, objetivo))

            if epoca % 100 == 0:
                print(f"Época {epoca}: Error total = {error_total:.4f}")


def evaluar_patron(red, etiqueta, patrones, etiquetas_codificadas):
    if etiqueta in patrones:
        entrada = patrones[etiqueta]
        salida = red.predecir(entrada, guardar=False)
        indice = salida.index(max(salida))
        letra_predicha = etiquetas_codificadas[indice]
        return letra_predicha, salida
    else:
        return None, None


def codificar_etiquetas(patrones):
    etiquetas = sorted(patrones.keys())
    codigos = {et: [1 if i == j else 0 for i in range(len(etiquetas))] for j, et in enumerate(etiquetas)}
    return codigos, etiquetas  # Regresar etiquetas en orden

def entrenar_red(red, patrones):
    codigos, etiquetas = codificar_etiquetas(patrones)
    datos = []
    salidas = []

    for etiqueta, vector in patrones.items():
        datos.append(vector)
        salidas.append(codigos[etiqueta])

    red.entrenar(datos, salidas, tasa_aprendizaje=0.1, epocas=1000)
    print("Entrenamiento finalizado.")
    return etiquetas  # Regresar etiquetas codificadas en orden

def guardar_pesos(red, etiquetas_codificadas, ruta="pesos.txt"):
    with open(ruta, "w") as f:
        # Guardar etiquetas codificadas como primera línea
        f.write(",".join(etiquetas_codificadas) + "\n")
        # Guardar pesos
        for capa in [red.capa_oculta, red.capa_salida]:
            for neurona in capa.neuronas:
                pesos = ",".join(map(str, neurona.pesos))
                f.write(f"{pesos}|{neurona.bias}\n")
    print("Pesos y etiquetas guardados exitosamente.")

def cargar_pesos(red, ruta="pesos.txt"):
    with open(ruta, "r") as f:
        lineas = f.readlines()

    # Leer etiquetas codificadas
    etiquetas_codificadas = lineas[0].strip().split(",")

    capas = [red.capa_oculta, red.capa_salida]
    idx = 1  # empieza en la segunda línea

    for capa in capas:
        for neurona in capa.neuronas:
            linea = lineas[idx].strip()
            pesos_str, bias_str = linea.split("|")
            neurona.pesos = list(map(float, pesos_str.split(",")))
            neurona.bias = float(bias_str)
            idx += 1

    print("Pesos y etiquetas cargados exitosamente.")
    return etiquetas_codificadas


def evaluar_todas(red, patrones, etiquetas_codificadas):
    correctas = 0
    total = len(patrones)

    for etiqueta, entrada in patrones.items():
        salida = red.predecir(entrada)
        indice = salida.index(max(salida))
        prediccion = etiquetas_codificadas[indice]
        if prediccion == etiqueta:
            correctas += 1

    porcentaje = (correctas / total) * 100
    print(f"Predicciones correctas: {correctas} de {total} ({porcentaje:.2f}%)")
    return correctas, total, porcentaje

############################################### Señales ###################################################

# Funciones para entrenar y evaluar una red neuronal para clasificación binaria
def entrenar_binario(red, X, Y, tasa=0.1, epocas=1000):
    red.entrenar(X, Y, tasa_aprendizaje=tasa, epocas=epocas)
    print("Entrenamiento binario finalizado.")

# Evaluar la precision
def evaluar_binario(red, X, Y):
    correctas = 0
    for entrada, etiqueta in zip(X, Y):
        salida = red.predecir(entrada)
        pred = 1 if salida[0] >= 0.5 else 0
        if pred == etiqueta[0]:
            correctas += 1
    total = len(Y)
    porcentaje = (correctas / total) * 100
    print(f"Correctas: {correctas}/{total} ({porcentaje:.2f}%)")
