#creando array

import numpy as np

vacia=np.zeros(4)
print(vacia)

vacia=np.ones(4)
print(vacia)

vacia=np.arange(4)
print(vacia)

vacia=np.arange(2,20,3)
print(vacia)

lista = [1,2,3,4]
array1 = np.array(lista)
print(array1)
print(type(array1))
print(lista)
print(type(lista))

lista = [1,2,3,4]
lista2 =[5,6,7,8]
lista_doble = (lista,lista2)
print(lista_doble)

array_doble = np.array(lista_doble)
print(array_doble)

resul=array_doble.shape # nos dice cuantas filas y columnas tiene nuestro array
print(resul)

