# Cargar patrones desde el archivo
def cargar_patrones(ruta):
    patrones = {}
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if "//" in linea and "-" in linea:
                try:
                    etiqueta, datos = linea.strip().replace("//", "").split("-")
                    numeros = list(map(int, datos.split(",")))
                    if len(numeros) == 35:
                        patrones[etiqueta.strip()] = numeros
                except ValueError:
                    continue
    return patrones

# Función para actualizar la matriz de labels
def actualizar_matriz(patron, celdas):
    for i in range(7):  # filas
        for j in range(5):  # columnas
            valor = patron[i * 5 + j]
            color = "red" if valor == 1 else "white"
            celdas[i][j].configure(bg=color)

# Función que maneja la lógica del botón
def mostrar_texto(etiqueta, patrones, celdas):
    if etiqueta in patrones:
        patron = patrones[etiqueta]
        actualizar_matriz(patron, celdas)
    else:
        print("Etiqueta no encontrada.")

