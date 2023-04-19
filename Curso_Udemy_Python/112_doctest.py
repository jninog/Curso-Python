#genera pruebas dentro de la documentación

def sumar (numero1, numero2):
    """Esa es la documentación de esta función
    Recibe dos numeros como parametros y devuelve su suma
    >>> sumar(4,3)
    7
    >>> sumar(4,5)
    9
    >>> sumar(1,3)
    7
    """
    return numero1+numero2
resultado = sumar(2,4)
print(resultado)

import doctest
prueba = doctest.testmod() # permite que la prueba sumar se ejecute y de el resultado

print(prueba)