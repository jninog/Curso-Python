#from Curso_Udemy_Python.ejercicio_Objetos_Clases import coche
#from Curso_Udemy_Python.ejecicio_Lambda import media
class coche:
      
    def __init__(self,marca,color,combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    def mostrar_caracteristicas(self):    #instancio la clase completa para poder acceder a los atributos
        print('El carro tiene estas caracteristicas marca {},color {},Combustible {},cilindrada {}'
              .format(self.marca,self.color,self.combustible,self.cilindrada))

media = lambda nota1, nota2,nota3: (nota1 + nota2 +nota3) /3
