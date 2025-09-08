# importação de biblioteca
import threading
import time
import math

# estrutura da Thread
def estrutura(nome, inicio, fim): # def é quando vai fazer uma estrutura, como o function no js
    for i in range(inicio, fim +1): # .tofixed() é para limitar os números, como por exp. número infinito
        print(f"{nome} -> {i}")

    # pausa entre as durações de contagem
    time.sleep(1) 

# criar thread
thread1 = threading.Thread(target=estrutura, args=("Thread-1", 1, 10))
thread2 = threading.Thread(target=estrutura, args=("Thread-2", 50, 60)) # args é argumento

# rodar
thread1.start()
thread2.start()

# estado de espera
thread1.join()
thread2.join()

print("Todas as threads foram finalizadas.")

