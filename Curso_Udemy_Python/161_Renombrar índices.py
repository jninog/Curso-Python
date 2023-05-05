# Renombrar indices

import pandas as pd
import numpy as np

lista_valores = np.arange(9).reshape(3,3)
#print(lista_valores)

lista_indices = list('abc')

dataframe = pd.DataFrame(lista_valores,index=lista_indices)
print(dataframe)

new_indices = dataframe.index.map(str.upper) #cambia de minuscula a mayuscula los indices
dataframe.index = new_indices
print(dataframe)

#metodo rename(para Renombrar los indices)
dataframe = dataframe.rename(index=str.lower)
print(dataframe)

new_indices = {'a':'f','b':'g','c':'h'}

dataframe = dataframe.rename(index=new_indices)
print(dataframe)
new_indices = {'f':'j'}
print(dataframe.rename(index=new_indices, inplace=True))