#163. Filtrar datos en DataFrames

import numpy as np
import pandas as pd

lista_valores = np.random.rand(10,3)
#print(lista_valores)

dataframe = pd.DataFrame(lista_valores)

columna0=dataframe[0] #filtra por la primer columna
#print(columna0)

print(columna0[columna0 > 0.40])

print(dataframe)
print(dataframe[dataframe >0.40]) #muestra lo que cumple y lo que no NaN
