
lista = [1,2,3,4,5,6,7,8,9,10]

def incrementar(numero):
    return numero +10

mapeo = map(incrementar,lista)
#print(mapeo)
resultado = list(mapeo)
print(resultado)

