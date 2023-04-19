import numpy as np

def pares(inicio,fin):
    for numero in range(inicio,fin):
        if (numero % 2 == 0):
            yield numero

inicio = 1
fin = 3

for numero in pares(inicio,fin):
    print(numero)
    
