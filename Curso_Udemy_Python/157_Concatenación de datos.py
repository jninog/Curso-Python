#concatenación de array, series y dataframes

import pandas as pd #series y dataframes
import numpy as np #arrays

array1 = np.arange(9).reshape(3,3)
#print(array1)
array_concat  = np.concatenate([array1,array1]) #concatenar Arrays
print(array_concat)

## Concatenar Series

serie1 = pd.Series([1,2,3],index=['a','b','c'])
serie2 = pd.Series([4,5,6],index=['d','e','f'])

serie_concat = pd.concat([serie1,serie2]) # Concatena series
print(serie_concat)
serie_concat1 = pd.concat([serie1,serie2],keys=['serie1','serie2']) # Concatena series, pero identificando cada una mediante la función (keys)
print(serie_concat1)

#concatenar dataframes
dataframe = pd.DataFrame(np.random.rand(3,3),columns=['a','b','c'])
print(dataframe)

dataframe2 = pd.DataFrame(np.random.rand(2,3),columns=['a','b','c'])
print(dataframe2)

dataframe_concat = pd.concat([dataframe,dataframe2])#concatena dataframe
print(dataframe_concat)

dataframe_concat = pd.concat([dataframe,dataframe2],keys=['d1','d2'])
print(dataframe_concat)