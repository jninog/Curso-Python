#Valores nulos - NaN
import pandas as pd
import numpy as np

lista_valores = ['1','2',np.nan,'4'] #lista valores con un valor nulo NaN

serie = pd.Series(lista_valores,index=list('abcd'))
print(serie)

print(serie.isnull()) #muestra si tenemos valores nullos
print(serie.dropna()) #elimina valores nullos

lista_valores2 = [[1,2,3],[4,np.nan,5],[6,7,np.nan]]

lista_indices = list('123')

lista_columnas = list('abc')

dataframe = pd.DataFrame(lista_valores2,index=lista_indices,columns=lista_columnas)
print(dataframe)
print(dataframe.isnull()) # nos muestra si el valor es nulo
print(dataframe.dropna()) #elimina valores nullos

print(dataframe.fillna(0)) #llena los nulos con el valor especificado



