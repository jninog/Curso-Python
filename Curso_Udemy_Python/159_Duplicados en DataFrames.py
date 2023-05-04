import pandas as pd #series y dataframes
import numpy as np #arrays

lista_valores = [[1,2],[1,2],[5,6],[5,8]]
print(lista_valores)

lista_indices = list('mnop')
print(lista_indices)
lista_columnas = ['valor1','valor2'] 
print(lista_columnas)

dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)
print(dataframe)

dataframe2 = dataframe.drop_duplicates()# elimina duplicados de todo el dataframe
print(dataframe2)

dataframe3 = dataframe2.drop_duplicates(['valor1'])# elimina duplicados por columna de un dataframe
print(dataframe3)

dataframe4 = dataframe2.drop_duplicates(['valor1'],keep='last')# elimina duplicados en la columna especifica indicando cual duplicado dejar en un dataframe
print(dataframe4)
