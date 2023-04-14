import sqlite3

conexion =sqlite3.connect('basededatos1.bd')

cursor = conexion.cursor()
cursor.execute("select * from personas where edad <= 20")

personas_selecionada=cursor.fetchall()

for persona in personas_selecionada:
    print(persona)
    
conexion.close()
 