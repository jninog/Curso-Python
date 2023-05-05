#Combinación de elementos

import numpy as np
import pandas as pd

lista_valores = np.arange(25).reshape(5,5)
print(lista_valores)
dataframe = pd.DataFrame(lista_valores)
#print(dataframe)

combinacion_aleatoria = np.random.permutation(5) #genera un array en este caso del 0 al 5 de forma aleatoria
print(combinacion_aleatoria)

print(dataframe.take(combinacion_aleatoria)) # Utilizamos el orden de combinacion_aleatoria para organizar el dataframe
