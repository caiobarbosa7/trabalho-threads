# importação de biblioteca
import threading # permite criar e controlar as threads
import time # criar as pausas

# estrutura da Thread
def estrutura(nome, inicio, fim): # def é quando vai fazer uma estrutura, como o function no js
    for i in range(inicio, fim +1): 
        print(f"{nome} -> {i}")

    # pausa entre as durações de contagem
    time.sleep(0.5) # pausa de 0.5 segundos entre cada número impresso

# criação das threads com argumentos
thread1 = threading.Thread(target=estrutura, args=("Thread-1", 1, 10)) # importa os números da thread1
thread2 = threading.Thread(target=estrutura, args=("Thread-2", 50, 60)) # args é argumento # importa os números da thread2

# inicia a execução das threads
thread1.start()
thread2.start()

# estado de espera, aguarda as threads terminarem antes de continuar
thread1.join()
thread2.join()

print("Todas as threads foram finalizadas.") # fechamento após as threads terminarem com uma mensagem final



