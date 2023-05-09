#175. Regresiones lineales

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import seaborn as sns

#cargar dataset de propinas que trae serborn

propinas = sns.load_dataset('tips')
print(propinas.head(10))

#crear grafico de regresion lineal , teniendo en cuenta un dataset

sns.lmplot(x='total_bill',y='tip',data=propinas)
mpl.show()
#poner colores diferentes a la grafica, como linea y puntos
sns.lmplot(x='total_bill',y='tip',data=propinas,scatter_kws={'color':'blue'},line_kws={'color':'red'})
mpl.show()

#solo poner puntos y quitar linea
sns.lmplot(x='total_bill',y='tip',data=propinas,fit_reg=False)
mpl.show()

#crear porcentaje de propinas sobre total, se crea una nueva colimna a nuestro dataset llamada porcentaje
propinas['porcentaje']=100*propinas['tip']/propinas['total_bill']
print(propinas.head())

sns.lmplot(x='size',y='porcentaje',data=propinas) # se crea una grafica de regresion teniendo en cuenta el nuevo porcentaje
mpl.show()

sns.lmplot(x='total_bill',y='porcentaje',data=propinas,hue='sex',markers=['x','o']) # markers es para decirle qye le pnga a cada marcador en la grafica
mpl.show()

sns.lmplot(x='total_bill',y='porcentaje',data=propinas,hue='day')
mpl.show()

