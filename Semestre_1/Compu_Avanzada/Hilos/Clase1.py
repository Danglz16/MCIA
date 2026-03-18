import threading
import time

class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        
    def run(self):
        for i in range(5):
        print(f"[{self.nomnre}] iteracion {i}")
        time.sleep(1)
        
h1 = MiHilo("Hilo1")
h2 = MiHilo("Hilo2")
h1.start()
h2.start()
h1.join()
h2.join()