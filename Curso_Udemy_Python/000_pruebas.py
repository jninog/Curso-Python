import pandas as pd

def leer_csv(ruta):
    datos = pd.read_csv(ruta,sep=';')
    return datos.values.tolist()
    print(type(datos))
    
datos = leer_csv('C:/Users/Usuario/Documents/Raddar Studios/Curso Python/Curso_Udemy_Python/coches.csv')