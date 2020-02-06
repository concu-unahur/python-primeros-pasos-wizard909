import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def agregarPares(lista):
    for i in range(100):
        lista.append(2*i)
    
def agregarImpares(lista):
    for i in range(100):
        lista.append(2*i+1)


lista = []

for i in range(20):
    t1 = threading.Thread(target=agregarPares, args=[lista])
    t2 = threading.Thread(target=agregarImpares, args=[lista])
    t1.start()
    t2.start()

print(lista)