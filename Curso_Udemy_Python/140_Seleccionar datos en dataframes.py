#140. Seleccionar datos en dataframes

import pandas as pd
import numpy as np

lista_de_valores = np.arange(25).reshape(5,5)

print(lista_de_valores)


lista_de_indices = ['i1','i2','i3','i4','i5']

lista_de_columnas = ['c1','c2','c3','c4','c5']

dataframe = pd.DataFrame(lista_de_valores,index=lista_de_indices,columns=lista_de_columnas)
print(dataframe)

print(dataframe['c2']) # muestra todas as filas y no las columnas 
print(dataframe['c2']['i2']) # muestra el valor de las coordenadas brindadas
dataframe2=dataframe[['c1','c4','c2']] # muestra las columnas especificadas
print(dataframe2)

print(dataframe2[dataframe2['c2']>15]) # se pone condición para sacar los datos de dataframe

print(dataframe >20)

#selectcionar por indice

print(dataframe.loc['i3']) # seleciona por indice
print(dataframe.loc[['i3','i2']]) # seleciona por indice, teneidno en cuenta rango



