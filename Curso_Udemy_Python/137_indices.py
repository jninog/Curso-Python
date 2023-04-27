#indices

import numpy as np
import pandas as pd

lista_valores = [1,2,3]
lista_indices = ['a','b','c']
serie = pd.Series(lista_valores,index=lista_indices)

#print(serie)
#print(serie.index)  # saber los indices 
#print(serie.index[0])  # saber los indices en esa posición  

lista_valores = [[6,7,8],[8,9,5],[6,9,7]] 

lista_indices = ['Matematicas','Fisia','Historia']
lista_nombres = ['Julian','Pedro','Roberto']

datafreame = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_nombres )
print(datafreame)

print(datafreame.index)
print(datafreame.index[0])