#insertar varias filas SQLite desde python

import sqlite3

conexion = sqlite3.connect('basededatos1.bd')

curso = conexion.cursor()

lista_personas = [('pepito','perez','rodiguez',18),('Zoe','Niño','Gonzalez',14),('Daniela','Zuñiga','Garzon',26)]

curso.executemany("INSERT INTO personas values (?,?,?,?)",lista_personas)

conexion.commit()

conexion.close()