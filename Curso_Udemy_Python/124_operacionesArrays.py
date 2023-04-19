# operaciones con Arrays(+,-,*,/,**)

import numpy as np

array1 = np.array([1,2,3,4,5])
print(array1)

print(array1+3)

array1 = array1 +3
print(array1)

lista = [1,2,3,4]
lista2 =[5,6,7,8]

lista_doble =(lista,lista2)
print(lista_doble)

array_doble = np.array(lista_doble)
print(array_doble)

suma =array_doble+4
print(suma)

div =array_doble/2
print(div)

exp =array_doble**2
print(exp)
