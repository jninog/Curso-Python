#pickle - modulo para grabar ficheros binarios

import pickle

lista_colores = ["azul","Verde","Amarillo","rojo" ]

fichero = open("fichero_colores.pckl","wb") # se crea variable fichero ("Write binary")

pickle.dump(lista_colores,fichero)

fichero.close()
