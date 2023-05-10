from os import remove
import sys
import pandas as pd
import sqlite3
from sqlite3 import Error
from zipfile import ZipFile

basedatos = 'coches.bd'

def coche_economico(conexion):
    cursor = conexion.cursor()
    cursor.execute('select 	marca,modelo,min(precio) as precio from coches')
    dato = cursor.fetchall()
    return dato[0]

def suma_de_precio(conexion):
    cursor = conexion.cursor()
    cursor.execute('select 	sum(precio) as precio_total from coches ')
    dato = cursor.fetchone() #devuelve una tupla con un solo valor
    #numero= dato[0][0] # nos muestra en pantalla el valor sin ([])
    return dato[0]

def numero_coches_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('select count(*) from coches ')
    dato = cursor.fetchall() #devuelve como una lista
    numero = dato[0][0] # nos muestra en pantalla el valor sin ([])
    return(numero)

def consultar_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('select * from coches limit 20')
    filas=cursor.fetchall() # recupera todas las filas, las graba en filas
    for filas in filas:
        print(filas)

def borrar_datos():
    try:
        remove(basedatos)
    except FileNotFoundError:
        pass #no ejecuta nada

def insertar_tabla_coches(conexion,coche):
    cursor = conexion.cursor()
    cursor.execute('insert into coches(marca,modelo,conbustible,transmisión,estado,matricula,kilometraje,potencia,precio) values (?,?,?,?,?,?,?,?,?)',coche) # las interrogaciones se recogen de la variable coche
    conexion.commit()
    
# recoge los valores del fichero fila por fila y los aloja en la variable coche
def grabar_coche(conexion,datos):
    for fila in datos.itertuples():
        marca = fila[1]
        modelo = fila[2]
        conbustible = fila[3]
        transmision = fila[4]
        estado = fila[5]
        matriculacion = fila[6]
        kilometraje =fila[7]
        potencia = fila[8]
        precio = fila[9]
        
        coche=(marca,modelo,conbustible,transmision,estado,matriculacion,kilometraje,potencia,precio)
        
        insertar_tabla_coches(conexion,coche) #llama la función donde le pasa la variabe coche con los que capturo del fichero
        


def leer_csv(ruta):
    datos = pd.read_csv(ruta,sep=';')
    datos = pd.DataFrame(datos)
    return datos.values.tolist()
    
    
datos = leer_csv('C:/Users/Usuario/Documents/Raddar Studios/Curso Python/Curso_Udemy_Python/coches.csv')
datos = pd.DataFrame(datos)
print(datos)

def crear_conexio_bd():
    try:
        conexion = sqlite3.connect(basedatos)
        return conexion
    except Error:
        print(Error)
        
        

def crear_tabla_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('create table coches(marca text,modelo text,conbustible text, transmisión text,estado text,matricula text,kilometraje int,potencia real,precio real)')
    conexion.commit()
        

borrar_datos()
conexion = crear_conexio_bd()
crear_tabla_coches(conexion)
grabar_coche(conexion,datos)
print("\n Consultamos los datos de la tabla")
consultar_coches(conexion)

#Calcular numero de coches en la tabla
dato  = numero_coches_tabla(conexion)
print('\n El numero de coches es de {}'.format(dato))

#calcular el precio total de la tbl
dato = suma_de_precio(conexion)
dinero = '{:,.2f}'.format(dato).replace(',','.') #remplaza el tipo de dato y lo divide con puntos para saber que es dinero
print('\n El precio total de los coches es  ${}'.format(dinero))

dato = coche_economico(conexion)
marca = dato[0]
modelo = dato[1]
precio = dato[2]
dinero = '{:,.2f}'.format(precio).replace(',','.') #remplaza el tipo de dato y lo divide con puntos para saber que es dinero
print('\n El coche mas economico es, Marca {}, Modelo {}, Precio ${}'.format(marca,modelo,dinero))
