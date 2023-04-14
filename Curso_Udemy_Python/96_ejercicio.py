# crear BD SQLite desde python
import sqlite3
#Crea BD y conexion
conexion = sqlite3.connect('basededatos.bd')
#crea tabla
cursor = conexion.cursor()
cursor.execute('create table productos(id integer, nombre text, precio integer)')
conexion.commit()

#inserta datos masivos
insertar = conexion.cursor()
lista_personas = [(1,'Impresora',300),(2,'Raton',20),(3,'Ordenador',600)]
cursor.executemany("INSERT INTO productos values (?,?,?,?)",lista_personas)
conexion.commit()

cursor = conexion.cursor()
cursor.execute("select * from productos")
productos=cursor.fetchall()

for producto in productos:
    print(producto)

conexion.close()