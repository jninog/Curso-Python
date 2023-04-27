#funciones con arrays

import numpy as np

array = np.arange(5)
print(array)
raiz = np.sqrt(array)
#print(raiz)

aletorio=  np.random.rand(5)
#print(aletorio)

lista =[5,6,7,8,9]
array2 = np.array(lista)
print(array2)

#sumar array
suma=np.add(array,array2)
print(suma)

#multiplicar
multi = np.multiply(array,array2)
print(multi)

peque = np.minimum(array, array2) # saca el array mas pequeño
print(peque)

grande = np.maximum(array, array2) # saca el array mas grande
print(grande)