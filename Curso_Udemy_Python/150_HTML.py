# HTML con python recuperando datos

import pandas as pd
import numpy as np

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

dataframe = pd.io.html.read_html(url)
#print(dataframe)

dataframe_futbol = dataframe[0] # se le asigna la posición correcta
#print(dataframe_futbol)

dict(dataframe_futbol.loc[0])# se convierte en diccionario para modificar el dataframe y poner los titulos en su respectivo lugar

#dataframe_futbol = dataframe_futbol.rename(columns=dict(dataframe_futbol.loc[0]))
#print(dataframe_futbol)

dataframe_futbol = dataframe_futbol.drop('Notas',axis=1)# eliminamos una columna ,especificando cual
print(dataframe_futbol)