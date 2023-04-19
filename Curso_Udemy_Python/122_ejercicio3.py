
lista = [1,2,3,4,5,6,7,8,9,10]

def multiplicar(numero):
    return numero +10

mapeo = map(multiplicar,lista)
#print(mapeo)
resultado = list(mapeo)
print(resultado)

