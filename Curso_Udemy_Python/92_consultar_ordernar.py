import sqlite3

conexion =sqlite3.connect('basededatos1.bd')

cursor = conexion.cursor()
cursor.execute("select * from personas order by edad asc")

personas_ordenadas=cursor.fetchall()

for persona in personas_ordenadas:
    print(persona)
    
conexion.close()
 