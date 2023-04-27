# crear un dataframe con datos copiados de una pagina web

import pandas as pd
import webbrowser

#website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
#webbrowser.open(website)  #Abre pagina web medisnte el open

#dataframe = pd.read_clipboard()
#print(dataframe)
#print(dataframe.columns)

#print(dataframe.loc[5])
#print(dataframe.head(5))  # muestra los primero 5 registros del frame
#print(dataframe.tail(5))  # muestra los ultimos 5 registros del frame
#--------------------

lista_asignatura = ['Matematicas','Fisica','Historia']
lista_notas = [8,7,9]

diccionario={'Asignatura':lista_asignatura,'Notas':lista_notas}

print(diccionario)

dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)