#Mapas de calor (heatmap)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mlp

#documentacion de seaborn.heatmap (https://seaborn.pydata.org/generated/seaborn.heatmap.html)


vuelos = sns.load_dataset('flights')#traer el dataset, de vuelos
#print(vuelos.head())

#convertir en matriz el dataset
vuelos = vuelos.pivot(index='month',columns='year',values='passengers')
print(vuelos)

sns.heatmap(vuelos) #crea mapa de calor teniendo encuenta la matriz
mlp.show()

sns.heatmap(vuelos,annot=True,fmt='d')# muestra los valores de la matriz en el mapa de calor 
mlp.show()

#El argumento fmt en sns.heatmap() especifica el formato de la anotación de los valores en la celda. Por ejemplo, si tienes el valor 123.45, con 'g' se mostrará como '123.45' y con 'd' se mostrará como '123'
#en annot muestra los valores en cada celda cuando se especifica true
#se especifica la cariable valore_central como el punto de medición del mapa de calor
valor_central = vuelos.loc['May'][1956]
sns.heatmap(vuelos,center=valor_central,annot=True,fmt='d')
mlp.show()

#mover la barra de valores
sns.heatmap(vuelos,center=valor_central,annot=True,fmt='d',cbar_kws={'orientation':'horizontal'})
mlp.show()
