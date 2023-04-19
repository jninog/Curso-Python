# Map, aplicar una función a una lista

def multiplicar(numero):
    return numero * 2;

#print(multiplicar(2))

numeros = [2,4,6]
mapeo = map(multiplicar,numeros)
print(mapeo)
resultado = list(mapeo)
print(resultado)

lista_resultado = list(map(multiplicar,numeros))
print(lista_resultado)

lista_resultado2 = list(map(lambda numero: numero*2,numeros))
print(lista_resultado2)