import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

num = 1
lock1 = threading.Lock()

def sumarUno():
    global num
    global lock1

    try:
        logging.info("Calculando suma")
        num += 1
    finally:
        lock1.release()

def multiplicarPorDos():
    global num
    global lock1

    lock1.acquire()
    try:
        logging.info("Calculando multiplicacion")
        num *= 2
    finally:
        lock1.release()

def dividirPorDos():
    global num
    global lock1

    lock1.acquire()
    try:
        logging.info("Calculando division")
        num /= 2
    finally:
        lock1.release()

thread1 = threading.Thread(target=sumarUno)
thread2 = threading.Thread(target=multiplicarPorDos)
thread3 = threading.Thread(target=dividirPorDos)

lock1.acquire()

thread2.start()
thread1.start()


thread1.join()
thread2.join()

# (1+1)* 2 = 4 sin importar el orden del codigo
logging.info(f"valor final de num es {num}")

    
