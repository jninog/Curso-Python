# series

import pandas as pd

serie1 = pd.Series([3,4,7])
print(serie1)
print(serie1[1])#muestra posición

asignaturas = ['matematicas','historia','fisica','literatura']

notas= [8,6,9,7]

serie_notas_daniel= pd.Series(notas,index=asignaturas) # une las listas en una serie
print(serie_notas_daniel)

print(serie_notas_daniel['fisica']) #muestra resultado de un solo valor especifico

print(serie_notas_daniel[serie_notas_daniel>=8]) #filtra por valor
name=serie_notas_daniel.name = 'Notas de daniel'# pone nombre a la serie
print(name)

serie_notas_daniel.index.name = 'Asignaturas Daniel' # poner nombre a los indices
print(serie_notas_daniel)