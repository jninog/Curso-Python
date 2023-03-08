class claseSilla:
    color = 'Blanco'
    precio  = 100
    
objetoSilla1 = claseSilla()

print(objetoSilla1.color)
print(objetoSilla1.precio)

objetoSilla2 = claseSilla()
objetoSilla2.color = 'Azul'
objetoSilla2.precio = 150

print(objetoSilla2.color)
print(objetoSilla2.precio)

class persona:
    #metodo
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print('Hola, me llamo {} y tengo {} años'.format(self.nombre,self.edad))
#se crea una persona

persona1 = persona('Juan',29)

print(persona1.edad)
print(persona1.nombre)

#invoco metodo saludar
print(persona1.saludar())