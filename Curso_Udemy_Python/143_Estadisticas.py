# Estadisticas en dataframes
import pandas as pd
import numpy as np

array = np.array([[1,8,3],[5,6,7]])
print(array)

dataframe = pd.DataFrame(array, index=['a','b'],columns=list('123'))

print(dataframe)
print(dataframe.sum()) #suma columnas
print(dataframe.sum(axis=1)) #suma filas
print(dataframe.min()) # minimo valor por columnas
print(dataframe.max()) #maximo valor por columnas

print(dataframe.min(axis=1)) # minimo valor por fila
print(dataframe.max(axis=1)) #maximo valor por fila
print(dataframe)
print(dataframe.idxmin())
print(dataframe.describe())