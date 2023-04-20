import numpy as np

lista=[1,30]

def pares(inicio,fin):
    for numero in range(inicio,fin):
        if (numero % 2 == 0):
            yield numero

inicio = 1
fin = 30

for numero in pares(inicio,fin):
    #print(numero)
    array = np.array(numero)
    print(array)
print(type(array))

#-------------------------

def pares2(inicio,fin):
    if(inicio % 2==0):
        array = np.arange(inicio,fin,2)
    else:
        inicio=inicio+1
        array=np.arange(inicio,fin,2)
    return array

print(pares2(1,30))

