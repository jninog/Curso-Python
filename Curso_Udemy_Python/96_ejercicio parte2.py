import sqlite3

conexion = sqlite3.connect('basededatos.bd')

cursor = conexion.cursor()
cursor.execute("select * from productos")
productos=cursor.fetchall()

for producto in productos:
    print(producto)

conexion.close()