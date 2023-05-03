#ficheros formato excel

import pandas as pd
import numpy as np

fichero_excel = pd.ExcelFile('C:/Users/Usuario/Documents/Raddar Studios/Curso Python/Curso_Udemy_Python/fichero_Excel.xlsx')
#print(fichero_excel)

misdatos = fichero_excel.parse('Hoja1')#recoge los datos de la hoja que le enviamos y crea un dataframe
print(misdatos)