import moduloficheros

nombre_fichero = 'fichero1.txt'
fichero = moduloficheros.fichero(nombre_fichero)

texto = 'Es la primera fila del fichero,\n Esta es la segunda fila.'
fichero.grabar_fichero(texto)

texto = '\nEsta es el texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)