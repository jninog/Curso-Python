import pandas as pd
import numpy as np

datos = pd.ExcelFile('C:/Users/Usuario/Downloads/poblacion (1).xlsx')
dataframedatos = datos.parse('Hoja 1')
print(dataframedatos['Ciudad más poblada'][3]) #muestra posición solicitada


#### Leer csv
datoscsv = pd.read_csv('C:/Users/Usuario/Downloads/poblacion.csv')
print(datoscsv['Ciudad más poblada'][1]) #muestra posición solicitada