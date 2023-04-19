#funcion filter filtra resultados segun condición

def positivo(numero):
    if (numero >0):
        return True
    else:
        return False

#resultado = positivo(-4)
#print(resultado)

numeros = [4,-2,8,-3,-5,-7,1,9]
filtro = filter(positivo,numeros)
resultado  = list(filtro)

print(resultado)

