import threading
import time
import logging
from tiempo import Contador


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir():
    time.sleep()


tiempo = Contador()
tiempo.iniciar
lista = []
for i in range(10):
    
    print("creando thread" + i)
    #thread = threading.Thread(target=dormir, nombre = "thread" + i )

    print("lanzando thread" + i)
    #thread.start()


tiempo.finalizar()
tiempo.imprimir()