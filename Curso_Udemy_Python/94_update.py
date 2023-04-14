import sqlite3

conexion =sqlite3.connect('basededatos1.bd')

cursor = conexion.cursor()
cursor.execute("update personas set edad = 4 where nombre ='Zoe'")
    
conexion.commit()
conexion.close()