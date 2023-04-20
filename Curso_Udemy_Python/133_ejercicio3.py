import numpy as np

lista1 = np.arange(0,30)
print(lista1)

lista2 =lista1[:10] #muestra un rango de valores en un array, primeros 10
print(lista2)

lista3 =lista1[-10:] #muestra un rango de valores en un array ultimos 10
print(lista3)

for bucle in(lista3):
    print(bucle)
