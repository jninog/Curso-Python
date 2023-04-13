
import re

def buscar(palabra,texto):
    resultado = re.search(palabra,texto)
    return(resultado)

texto = 'Esta es una frase de prueba para hacer busqueda'
palabra = 'frase'

resultado  = buscar(palabra,texto)
print(resultado)

if (resultado):
    print('La frase encontrada es {}'.format(palabra))
    inicial = resultado.start()#saber la posición de la frase inicial
    termina = resultado.end() #saber la posición de la frase final
    print('la plabra empieza en la posición {} y termina en la posición {}'.format(inicial,termina))
else:
    print('No se encontro la palabra {}'.format(palabra))