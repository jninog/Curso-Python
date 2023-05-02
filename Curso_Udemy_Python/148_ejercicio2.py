import pandas as pd
import numpy as np


datos = pd.read_clipboard() # recoger los datos que se copian "porta papeles"
print(datos)


print(datos.columns)
#print(datos.head(1))#muestra la primera fila
#print(datos.loc[0]) #muestra la información del primer registro
#print(datos['Continente']) #muestra el valor de la columna
print(datos.loc[0:3,['Continente','Población']]) # selecionar filas y columas a nuestro gusto
print(datos.head(3))#muestra las 3 primeras filas
print(datos.tail(2))#muestra la2 dos ultimas filas