import sqlite3

conexion =sqlite3.connect('basededatos1.bd')

cursor = conexion.cursor()
cursor.execute("select * from personas")

personas=cursor.fetchall()

for persona in personas:
    print(persona)
    
conexion.close()
 