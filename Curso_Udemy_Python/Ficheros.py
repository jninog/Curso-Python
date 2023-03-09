#Leer el fichero de texto
#‘r’: Por defecto, para leer el fichero.
#‘w’: Para escribir en el fichero.
#‘x’: Para la creación, fallando si ya existe.
#‘a’: Para añadir contenido a un fichero existente.
#‘b’: Para abrir en modo binario.


fichero = open('ficherotexto.txt','rt')

datos_fichero = fichero.read()

print(datos_fichero)