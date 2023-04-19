#Docstrings cadenas para documentación

def saludar(nombre):
    """
    Esto sera un comentario de la función saludar.
    esta funcipon tendra como parametro una cadena con el nombre e
    imprimira por pantalla un saludo con el nombre concatenado
    """
    print("Buenos dias "+ nombre)

saludar("Julian")

help(saludar)

#comentarios para una clase

class saludos:
    """
    Esta clase tendra dos funciones buenos dias 
    ambas funciones recibiran parametro nombre
    """
    def buenos_dias(self,nombre):
        """Este función sirver para decir buenos días      
        """
        print("Buenos dias {}".format(nombre))
    def adios(self,nombre):
        """Este función sirver para decir adios a una persona      
        """
        print("Adios {}".format(nombre))

saludo = saludos()
saludo.buenos_dias("Julian")
print(saludo)
help(saludos)

#help para funciones existentes

help(print)