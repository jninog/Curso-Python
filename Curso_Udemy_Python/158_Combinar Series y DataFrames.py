# 158. Combinar Series y DataFrames

import pandas as pd #series y dataframes
import numpy as np #arrays

serie1 = pd.Series([1,2,np.nan])
print(serie1)
serie2 = pd.Series([4,5,6])
print(serie2)
serie3 = serie1.combine_first(serie2) # combina dos series y en los valores NaN remplaza por lo que encuentre en la otra serie
print(serie3)

### combinar dataframe

lista_valores=[1,2,np.nan]
dataframe = pd.DataFrame(lista_valores)
print(dataframe)

lista_valores2=[4,5,6]
dataframe2 = pd.DataFrame(lista_valores2)
print(dataframe2)

dataframe3 = dataframe.combine_first(dataframe2)
print(dataframe3)