#Jerarquía en los índices

import pandas as pd
import numpy as np

lista_valores = np.random.rand(6)
print(lista_valores)

lista_indices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]

serie = pd.Series(lista_valores,index  =lista_indices)
print(serie)
print(serie[1]['b']) #muestra el valor alojado en las coordenadas enviadas
dataframe = serie.unstack() # crea dataframe a partir de una serie que tiene doble indice
print(dataframe)

lista_valores2 = np.arange(16).reshape(4,4)
lista_indices2 = list('1234')
lista_columnas = list('abcd')

#crear un lista con varios indices teniendo en cuenta un dataframe
dataframe2 = pd.DataFrame(lista_valores2,index=lista_indices2,columns=lista_columnas)
print(dataframe2)

serie2 = dataframe2.stack() #
print(serie2)