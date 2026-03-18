import tkinter as tk
from tkinter import ttk
from GUI import *
from NN import *


# Cargar patrones desde archivo
patrones = cargar_patrones("caract.txt")

# Crear ventana
raiz = tk.Tk()
raiz.title("Proyecto Final")
raiz.geometry("500x400")

# Combobox con etiquetas desde archivo
Combo = ttk.Combobox(raiz, values=list(patrones.keys()))
Combo.set("Selecciona una letra")
Combo.place(x=10, y=10)

def on_seleccion_cambio(event):
    mostrar_texto(Combo.get(), patrones, celdas)

Combo.bind("<<ComboboxSelected>>", on_seleccion_cambio)


# Frame para la matriz
frame_matriz = tk.Frame(raiz)
frame_matriz.place(x=10, y=50)

# Crear matriz 5x7 de labels
celdas = []
for i in range(7):
    fila = []
    for j in range(5):
        etiqueta = tk.Label(frame_matriz, width=2, height=1, bg="white", relief="solid", borderwidth=1)
        etiqueta.grid(row=i, column=j, padx=1, pady=1)
        fila.append(etiqueta)
    celdas.append(fila)

etiquetas_codificadas = []

def evaluar():
    global etiquetas_codificadas
    etiqueta = Combo.get().strip()
    letra, salida = evaluar_patron(red, etiqueta, patrones, etiquetas_codificadas)
    if letra is not None:
        print(f"Letra seleccionada: {etiqueta}")
        print(f"Predicción de la red: {letra}")
        print(f"Salida (vector): {salida}")
        label_prediccion.config(text=f"Predicción: {letra}")
    else:
        print("Etiqueta no encontrada o red sin entrenar.")
        label_prediccion.config(text="Predicción: ---")



boton_eval = tk.Button(raiz, text="Evaluar", command=evaluar)
boton_eval.place(x=160, y=7)

def entrenar():
    global etiquetas_codificadas
    etiquetas_codificadas = entrenar_red(red, patrones)

boton_train = tk.Button(raiz, text="Entrenar", command=entrenar)
boton_train.place(x=230, y=7)

def guardar():
    guardar_pesos(red, etiquetas_codificadas)
boton_guardar = tk.Button(raiz, text="Guardar", command=guardar)
boton_guardar.place(x=10, y=350)

def cargar():
    global etiquetas_codificadas
    etiquetas_codificadas = cargar_pesos(red)
boton_cargar = tk.Button(raiz, text="Cargar", command=cargar)
boton_cargar.place(x=100, y=350)

# Etiqueta para mostrar la predicción
label_prediccion = tk.Label(raiz, text="Predicción: ---", font=("Arial", 14), fg="blue")
label_prediccion.place(x=10, y=310)

def evaluar_todo():
    global etiquetas_codificadas
    if not etiquetas_codificadas:
        print("Primero entrena la red.")
        return
    correctas, total, porcentaje = evaluar_todas(red, patrones, etiquetas_codificadas)
    label_prediccion.config(text=f"Aciertos: {correctas}/{total} = {porcentaje:.1f}%")

boton_eval_todo = tk.Button(raiz, text="Evaluar todo", command=evaluar_todo)
boton_eval_todo.place(x=200, y=350)


# Crear la red con 35 entradas, 10 ocultas, y 16 salidas
# Cada letra tiene 35 características y 16 posibles letras
red = RedNeuronal(35, 10, 16)

raiz.mainloop()
