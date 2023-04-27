#Seleccionar datos en series

import pandas as pd
import numpy as np

lista_valores = np.arange(3) # crea un rango de valores

lista_indices = ['i1','i2','i3']

serie = pd.Series(lista_valores,index=lista_indices)
print(serie)

serie = serie*2 #multiplica todos los valores
print(serie)

#print(serie['i2']) #muestra un elemento, respecto a la indice 
#print(serie[1]) #muestra un elemento, respecto a la posición
#print(serie[0:2]) #muestra un todos elementos, teniendo en cuenta el rango pasado
#print(serie[0:3]) #muestra un todos elementos, teniendo en cuenta el rango pasado
print(serie['i1':'i2']) #muestra un todos elementos, teniendo en cuenta el rango pasado

print(serie[serie>2]) # Se pueden realizar condiciones

serie[serie>3] = 6 # Se pueden realizar condiciones
print(serie)
