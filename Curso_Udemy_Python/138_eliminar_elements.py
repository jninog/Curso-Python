#138_eliminar_elementos en series y en dataframe

import pandas as pd
import numpy as np

print(np.arange(3))

series = pd.Series(np.arange(4),index=['a','b','c','d'])
print(series)

print(series.drop('c')) # elimina un elemento

#------------dataframe-----------

lista_valores = np.arange(9).reshape(3,3) # devuelve 9 valores
lista_indices = ['a','b','c']
lista_columnas = ['columna1','columna2','columna3']

datafrane= pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)
print(datafrane)
print(datafrane.drop('b')) #Elimina fila
print(datafrane.drop('columna1',axis=1)) #Elimina columna 

datafrane = datafrane.drop('b') #Así se hacen permanentes los cambios
print(datafrane)