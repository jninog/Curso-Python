import numpy as np

lista1 =np.arange(10,20).reshape(2,5)
#print(lista1)

lista2 =np.arange(50,60).reshape(2,5)
#print(lista2)


array_unido = np.array((lista1,lista2)).reshape(2,10)
print(array_unido)

valor = array_unido.shape
print(valor)

arraymulti = array_unido *2
print(arraymulti)
