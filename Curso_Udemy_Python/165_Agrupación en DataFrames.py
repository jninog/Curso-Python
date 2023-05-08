#165. Agrupación en DataFrames

import numpy as np
import pandas as pd

lista_valores = {'clave1':['x','x','y','y','z'],'clave2':['a','b','a','b','a'],
                 'datos1':np.random.rand(5),'datos2':np.random.rand(5)}
#print(lista_valores)


dataframe = pd.DataFrame(lista_valores)
print(dataframe)

grupo1 = dataframe['datos1'].groupby(dataframe['clave1']) #agrupar valores en función de lo que se requiera, aqui se va agrupar datos1, en función de clave1
print(grupo1.mean()) #el mean muestra la media delos valores agrupados anteriormente 