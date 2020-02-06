import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def agregarUno(lista):
    lista.append(1)
    
def agregarDos(lista):
    lista.append(2)


lista = []

for i in range(25):
    t1 = threading.Thread(target=agregarUno, args=[lista])
    t2 = threading.Thread(target=agregarDos, args=[lista])
    t1.start()
    t2.start()

print(lista)