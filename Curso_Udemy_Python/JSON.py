#JSON
#convertir datos de un diccionario a una estructura JSON
import json

producto1 = {'nombre':'silla','color':'blanco','precio':80}

print(producto1 ['nombre'])

estructurajson = json.dumps(producto1)

#print(estructurajson)

#print(estructurajson ['nombre'])
print(estructurajson [0])

#convertir un JSON en diccionario

producto2 = json.loads(estructurajson)
print(producto2)

print(producto2['nombre'])

