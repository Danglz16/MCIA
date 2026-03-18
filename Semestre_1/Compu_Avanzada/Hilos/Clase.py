import threading
import time

cuenta = 0

def tarea (nombre):
    for i in range(5):
        print(f"Hilo {nombre}: iteracion {i}\n")
        time.sleep(1)

#def tarea1 (nombre):
#    for i in range(5):
#        print(f"Hilo {nombre}: iteracion {i}")
#        time.sleep(4)

def contador():
    global cuenta
    for _ in range(5):
        cuenta = cuenta + 1
        print(f"Cuenta = {cuenta}\n")
        time.sleep(1)
    
# Crear Hilos
hilo1 = threading.Thread(target=tarea, args=("Charro",))
hilo2 = threading.Thread(target=contador, )

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()

if hilo1.isDaemon:
    print("El hilo 2 esta corriendo en segundo plano")
else:
    print("El hilo 2 termino de ejecutarse")

print("Hilos Finalizados")