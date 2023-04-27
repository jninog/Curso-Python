#142. Ordenación y clasificación

import numpy as np
import pandas as pd

#print(range(4))
lista_de_valores = range(4)
lista_indices = list('CADB')
serie = pd.Series(lista_de_valores,index=lista_indices)
print(serie)

print(serie.sort_index()) #ordena la serio por los indices 
print(serie.sort_values()) #ordena la serio por los valores
print(serie.rank()) #ordena la serio por los valores, pero muestra la posición en la que queda


#creo una serie con valores aleatorios

serie2 = pd.Series(np.random.randn(10))
print(serie2)
print(serie2.rank()) #ordena la serio por los valores, pero muestra la posición en la que queda
print(serie2.sort_values()) #ordena la serio por los valores