#insertar fila SQLite

import sqlite3

conexion = sqlite3.connect('basededatos1.bd')

insertar = conexion.cursor()
insertar.execute("INSERT INTO personas(nombre, apellido1, apellido2, edad) VALUES ('Julian','Niño','Gonzalez',29)")

conexion.commit()

conexion.close()