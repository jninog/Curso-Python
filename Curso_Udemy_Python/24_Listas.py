colores = ['Rojo','Amarillo','Azul']

print(colores[0])
colores[0] = 'Negro'
print(colores)

print(len(colores))
colores.append('Naranja')
print(colores)
print(colores[3])
print(len(colores))

colores.remove('Amarillo')
print(colores)

for color in colores:
    print(color)