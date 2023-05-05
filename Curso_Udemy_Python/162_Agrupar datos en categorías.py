#162. Agrupar datos en categorías

import numpy as np
import pandas as pd

precios = [42,55,48,23,5,21,88,34,26]
#print(precios)
rango = [10,20,30,40,50,60,70,80,90,100]

precios_con_rango = pd.cut(precios,rango),#muestra en que rango esta cada valor de precios
print(precios_con_rango)

print(pd.value_counts(precios_con_rango)) #contar cuantos hay en cada categoria
