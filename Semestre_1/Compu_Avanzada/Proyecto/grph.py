import customtkinter as ctk 
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
import random 
from sympy import symbols, sympify
import os

def generarEntrenamiento(canFunciones, numMuestras):
    sigma,mu = random.randint(0,100),random.randint(0,100)
    for i in range(canFunciones//2): 
        for j in range(numMuestras): 
            x = [(random.random()-0.5)*20 for _ in range(50)]
            y = [np.exp(-((valor-mu)*2)/(2*sigma*2)) for valor in x]
            plt.plot(x,y,color="blue")
    for i in range(canFunciones//2): 
        for j in range(numMuestras): 
            x = [(random.random()-0.5)*20 for _ in range(50)]
            y = [random.randint(-100,100) for _ in range(50)]
            #plt.plot(x,y,color="red")
    plt.show()

def generarImagen(x,y,mX,mY):
    plt.axis('off')
    plt.tight_layout()
    plt.plot(x, y, color="white", linewidth=1)
    plt.scatter(mX, mY, color="yellow", s=20)
    plt.savefig("grafico.png",transparent=True)
    plt.close()

def calcular(minimo,maximo): 
    minimo = 0 
    funcion = entrada.get()
    x = symbols('x')
    dominio = np.linspace(minimo, maximo, 1000)
    try:
        funcion = sympify(funcion)
        imagenes = [funcion.subs(x,valor) for valor in dominio]
        #muestraX = [(random.random()-0.5)*20 for _ in range(50)]
        muestraX = np.linspace(minimo, maximo, puntos)
        muestraY = [funcion.subs(x,valor) for valor in muestraX]
        generarImagen(dominio, imagenes, muestraX, muestraY)
        imagen = Image.open("grafico.png")
        imagen = imagen.resize((260, 260))
        imagenTk = ctk.CTkImage(imagen,size=(260,260))
        etiquetaImagen.configure(image=imagenTk)
        etiquetaImagen.update()
        ventana.update()
    except:
        print("Error al evaluar la función:")

#generarEntrenamiento(10, 10)

puntos = 50
minimo,maximo = 1,100

os.system("cls")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ventana = ctk.CTk()
ventana.geometry("300x400")
ventana.title("Señales Gausianas")
ventana.resizable(False, False)

etiqueta1 = ctk.CTkLabel(ventana, text="Ingrese la función a evaluar:")
etiqueta1.place(x=20,y=10)
entrada = ctk.CTkEntry(ventana, width=260,border_color="#FFFF00", placeholder_text="(1/x)*sin(x)")
entrada.place(x=20,y=35)
boton1 = ctk.CTkButton(ventana, width=260, text_color="#000000", hover_color = "#DDDD00", fg_color ="#FFFF00",  text="Generar patrón", command=lambda:[calcular(minimo,maximo)])
boton1.place(x=20,y=80)
etiquetaImagen= ctk.CTkLabel(ventana, text="",width=260, height=260)
etiquetaImagen.place(x=20,y=120)

ventana.mainloop()