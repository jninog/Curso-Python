Dic_colores= {'red':'Rojo','Blue':'Azul','Yellow':'Amarillo'}
print(Dic_colores)

print(Dic_colores['Blue'])

valor = Dic_colores['Yellow']
print(valor)

#adiciona
Dic_colores['Black']='Negro'

print(Dic_colores)

#eliminar registros
Dic_colores.pop('red')
print(Dic_colores)
del(Dic_colores['Yellow'])
print(Dic_colores)

for color in Dic_colores:
 print(color)
    
for clave,valor in Dic_colores.items():
    print(clave,valor)