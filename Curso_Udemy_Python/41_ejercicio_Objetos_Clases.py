class coche:
    marca = ''
    color = ''
    combustible = ''
    cilindrada = ''
    
    def __init__(self,marca,color,combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    def mostrar_caracteristicas(self):    #instancio la clase completa para poder acceder a los atributos
        print('El carro tiene estas caracteristicas marca {},color {},Combustible {},cilindrada{}'
              .format(self.marca,self.color,self.combustible,self.cilindrada))


coche1 = coche('Opel','Azul','Gasolina','1,6')
coche2 = coche('1','1','1','1')

print(coche2.mostrar_caracteristicas())
print(coche1.marca)

print(coche1.mostrar_caracteristicas())
    
    
