import sqlite3

conexion =sqlite3.connect('basededatos1.bd')

cursor = conexion.cursor()
cursor.execute("delete from personas where nombre ='pepito'")
    
conexion.commit()
conexion.close()