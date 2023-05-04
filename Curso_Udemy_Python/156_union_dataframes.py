#union de dataframes

import pandas as pd

dataframe1 = pd.DataFrame({'c1':['1','2','3'],'clave':['a','b','c']})
#print(dataframe1)

dataframe2 = pd.DataFrame({'c2':['4','5','6'],'clave':['c','b','e']})
#print(dataframe2)

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2) #merge, une por las claves eb comun 
print(dataframe3)

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave') #se especifica por que campo hacer la union
print(dataframe3)

dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave',how='left') # muestra la información del dataframe de la izq, en este caso datframa1 y lo que cruza
print(dataframe4)

dataframe5 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave',how='right') # muestra la información del dataframe de la izq, en este caso datframa1 y lo que cruza
print(dataframe5)