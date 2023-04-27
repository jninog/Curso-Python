#operaciones sobre dataframe y series

import pandas as pd
import numpy as np

serie1 = pd.Series([1,2,3],index=['a','b','c'])

serie2 = pd.Series([3,4,5,6],index=['a','b','c','d'])

suma_series = serie1 + serie2 #suama series

print(suma_series)

#-------------------- Dataframe------

lista_valores = np.arange(4).reshape(2,2) #reshape, es para decir la cantidad e filas y columnas en el array
#print(lista_valores)
lista_indice = list('ab') #forma diferente de construir una lista, separando los elementos
print(lista_indice)
lista_columnas = list('12') #forma diferente de construir una lista, separando los elementos
print(lista_columnas)

dataframe = pd.DataFrame(lista_valores,index=lista_indice,columns=lista_columnas)
print(dataframe)


lista_valores2 = np.arange(9).reshape(3,3)
print(lista_valores2)
lista_indice2 = list('abc') #forma diferente de construir una lista, separando los elementos
print(lista_indice)
lista_columnas2 = list('123') #forma diferente de construir una lista, separando los elementos
print(lista_columnas)

dataframe2 = pd.DataFrame(lista_valores2,index=lista_indice2,columns=lista_columnas2)
print(dataframe2)

suma_dataframe = dataframe+dataframe2
print(suma_dataframe)

no_null = suma_dataframe[suma_dataframe>=0]#operaciones entre dataframe
print(no_null)

#adicionar valores con el metodo add
print(dataframe)
print(dataframe2)
print(dataframe.add(dataframe2,fill_value=0))