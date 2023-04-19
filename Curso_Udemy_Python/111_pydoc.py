#pydoc documentar desde la terminal

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
