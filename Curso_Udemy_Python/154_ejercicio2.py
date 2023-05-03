import pandas as pd
import numpy as np

url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'

datos = pd.io.html.read_html(url)
#print(datos)

paises = datos[0] # se le asigna la posición correcta
print(paises)

#paises = paises.rename(columns=dict(paises.loc[0]))
#print(paises)