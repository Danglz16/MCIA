import threading
import time

lock = threading.Lock()

contador = 0

def incrementar():
    global contador
    for _ in range (200000):
        with lock:
            contador += 1
            
h1 = threading.Thread(target=incrementar)
h2 = threading.Thread(target=incrementar)
h1.start()
h2.start()
h2.join()
h1.join()

print(f"Contador Final {contador}")