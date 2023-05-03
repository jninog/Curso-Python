import pandas as pd
import numpy as np

datos = pd.ExcelFile('C:/Users/Usuario/Downloads/poblacion (1).xlsx')
#print(datos)

dataframedatos = datos.parse('Hoja 1')
print(dataframedatos['Ciudad más poblada'][3])


#### Leer csv
datoscsv = pd.read_csv('C:/Users/Usuario/Downloads/poblacion.csv')
print(datoscsv['Ciudad más poblada'][1])