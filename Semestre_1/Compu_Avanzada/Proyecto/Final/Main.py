
import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from GUI import *
from NN import *
from Funciones import *

# ---------------------- Inicialización de red de caracteres ----------------------
patrones = cargar_patrones("caract.txt")
# 35 entradas (5x7), 10 neuronas ocultas, 16 salidas (letras A-H mas minusculas a-h)
red_caracteres = RedNeuronal(35, 10, 16)
etiquetas_codificadas = []

# ---------------------- Inicialización de red de funciones ----------------------
# 50 entradas (puntos de 0 a 0.1), 10 neuronas ocultas, 1 salida (gaussiana/no gaussiana)
red_funciones = RedNeuronal(50, 10, 1)

# ---------------------- Ventana Principal ----------------------
root = tk.Tk()
root.title("Proyecto Final")
root.geometry("700x500")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ---------------------- Parte 1: Caracteres ----------------------
frame_caracteres = ttk.Frame(notebook)
notebook.add(frame_caracteres, text="Reconocimiento de Caracteres")

# Combobox
combo_letras = ttk.Combobox(frame_caracteres, values=list(patrones.keys()))
combo_letras.set("Selecciona una letra")
combo_letras.place(x=10, y=10)

# Matriz 5x7
frame_matriz = tk.Frame(frame_caracteres)
frame_matriz.place(x=10, y=50)

celdas = []
for i in range(7):
    fila = []
    for j in range(5):
        celda = tk.Label(frame_matriz, width=2, height=1, bg="white", relief="solid", borderwidth=1)
        celda.grid(row=i, column=j, padx=1, pady=1)
        fila.append(celda)
    celdas.append(fila)

def on_letra_seleccionada(event):
    mostrar_texto(combo_letras.get(), patrones, celdas)

# Seleccionar letra
combo_letras.bind("<<ComboboxSelected>>", on_letra_seleccionada)

# Label Resultado Predicción
label_prediccion = tk.Label(frame_caracteres, text="Predicción: ---", font=("Arial", 14), fg="blue")
label_prediccion.place(x=10, y=310)

def evaluar_caracter():
    global etiquetas_codificadas
    etiqueta = combo_letras.get().strip()
    letra, salida = evaluar_patron(red_caracteres, etiqueta, patrones, etiquetas_codificadas)
    if letra is not None:
        label_prediccion.config(text=f"Predicción: {letra}")
    else:
        label_prediccion.config(text="Predicción: ---")

def entrenar_caracteres():
    global etiquetas_codificadas
    etiquetas_codificadas = entrenar_red(red_caracteres, patrones)

def guardar_caracteres():
    guardar_pesos(red_caracteres, etiquetas_codificadas)

def cargar_caracteres():
    global etiquetas_codificadas
    etiquetas_codificadas = cargar_pesos(red_caracteres)

def evaluar_todos():
    global etiquetas_codificadas
    if etiquetas_codificadas:
        correctas, total, porcentaje = evaluar_todas(red_caracteres, patrones, etiquetas_codificadas)
        label_prediccion.config(text=f"Aciertos: {correctas}/{total} = {porcentaje:.1f}%")

tk.Button(frame_caracteres, text="Evaluar", command=evaluar_caracter).place(x=160, y=7)
tk.Button(frame_caracteres, text="Entrenar", command=entrenar_caracteres).place(x=230, y=7)
tk.Button(frame_caracteres, text="Guardar", command=guardar_caracteres).place(x=10, y=350)
tk.Button(frame_caracteres, text="Cargar", command=cargar_caracteres).place(x=100, y=350)
tk.Button(frame_caracteres, text="Evaluar todo", command=evaluar_todos).place(x=200, y=350)

# ========== Parte 2: Funciones ==========
frame_funciones = ttk.Frame(notebook)
notebook.add(frame_funciones, text="Clasificación de Funciones")

# Label y entrada para función
tk.Label(frame_funciones, text="Función f(x):").place(x=10, y=10)
entrada = tk.Entry(frame_funciones, width=40)
entrada.place(x=100, y=10)

tk.Label(frame_funciones, text="Predefinidas:").place(x=10, y=40)
combo_func = ttk.Combobox(frame_funciones, values=list(lista_funciones_predefinidas().keys()), width=37)
combo_func.place(x=100, y=40)


def cargar_funcion():
    funciones = lista_funciones_predefinidas()
    seleccion = combo_func.get()
    if seleccion in funciones:
        entrada.delete(0, tk.END)
        entrada.insert(0, funciones[seleccion])
combo_func.bind("<<ComboboxSelected>>", lambda e: cargar_funcion())

# Label y Grafica para resultado
resultado_func = tk.Label(frame_funciones, text="Resultado: ", font=("Arial", 14))
resultado_func.place(x=10, y=90)

fig, ax = plt.subplots(figsize=(6, 3))
canvas = FigureCanvasTkAgg(fig, master=frame_funciones)
canvas.get_tk_widget().place(x=10, y=120)

def evaluar_funcion():
    funcion_str = entrada.get()
    try:
        puntos = 5000
        x = np.linspace(0, 0.1, puntos)

        # Evaluar para la red (usar pocos puntos fijos)
        y_red = evaluar_funcion_str(funcion_str, puntos=50)
        salida = red_funciones.predecir(y_red)
        pred = "Gaussiana" if salida[0] >= 0.5 else "No gaussiana"
        resultado_func.config(text=f"Resultado: {pred} ({salida[0]:.2f})")

        # Evaluar para graficar
        y_interp = evaluar_funcion_str(funcion_str, x=x)
        ax.clear()
        ax.plot(x, y_interp)
        ax.grid(True)
        canvas.draw()
    except Exception as e:
        resultado_func.config(text=f"Error: {str(e)}")


def entrenar_red_funciones():
    X, Y = generar_datos(n=100, puntos=50)
    red_funciones.entrenar(X, Y, tasa_aprendizaje=0.1, epocas=1000)
    resultado_func.config(text="Red entrenada correctamente.")

def guardar_funcion_pesos():
    guardar_pesos(red_funciones, ["No Gaussiana", "Gaussiana"], ruta="pesos_funcion.txt")
    resultado_func.config(text="Pesos guardados como 'pesos_funcion.txt'.")

def cargar_funcion_pesos():
    cargar_pesos(red_funciones, ruta="pesos_funcion.txt")
    resultado_func.config(text="Pesos cargados desde 'pesos_funcion.txt'.")

# Botones para funciones
tk.Button(frame_funciones, text="Evaluar función", command=evaluar_funcion).place(x=360, y=7)
tk.Button(frame_funciones, text="Entrenar red para funciones", command=entrenar_red_funciones).place(x=500, y=7)
tk.Button(frame_funciones, text="Guardar pesos", command=guardar_funcion_pesos).place(x=500, y=37)
tk.Button(frame_funciones, text="Cargar pesos", command=cargar_funcion_pesos).place(x=500, y=67)

# ========== Lanzar GUI ==========
root.mainloop()