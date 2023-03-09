import modulo1

coche1 = modulo1.coche('Mazda','Azul','Gasolina','1.5')
print(coche1.mostrar_caracteristicas())

print('Ingrese su nota de matematicas, por favor')
media1 = input()
print('Ingrese su nota de Fisica, por favor')
media2 = input()
print('Ingrese su nota de ingles, por favor')
media3 = input()

media1 = (modulo1.media(float(media1),float(media2),float(media3)))
print('El promedio de notas es {}'.format(media1))