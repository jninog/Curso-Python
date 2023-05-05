#166. Agregación en DataFrames (operaciones que dan un valor, como la media)

import pandas as pd
import numpy as np

lista_valores = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.nan,np.nan]]
#print(lista_valores)
lista_columnas = list('abc')

dataframe = pd.DataFrame(lista_valores,columns=lista_columnas)
print(dataframe)

#agregación
print(dataframe.agg(['sum','min'])) # muestra el maximo valor y el minimo valor de cada columna del dataframe

print(dataframe.agg('sum',axis=1)) #sumar filas