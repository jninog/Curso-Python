#crear tabla en SQLite

import sqlite3

conexion = sqlite3.connect('basededatos1.bd')

cursor = conexion.cursor()
cursor.execute('create table personas(nombre text, apellido1 text, apellido2 text,edad INTEGER)')

conexion.commit()

conexion.close()