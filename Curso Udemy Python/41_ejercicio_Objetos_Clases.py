class coche:
    def __init__(self,marca,color,combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    def mostrar_caracteristicas(self):    
        print('El carro tiene estas caracteristicas marca {},color {},Combustible {},cilindrada{}'
              .format(self.marca,self.color,self.combustible,self.cilindrada))

coche1 = coche('Opel','Azul','Gasolina','1,6')

print(coche1.marca)

print(coche1.mostrar_caracteristicas())
    