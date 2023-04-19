
def primos(maximo):
    if (maximo <= 50):
        return True
    else:
        return False

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

filtro = filter(primos,numeros_primos)
resultado  = list(filtro)
print(resultado)

#Solución 2

def primos(maximo):
    for numero in range(maximo):
        if (numero in numeros_primos):
            yield numero
        if(numero>30):
            break

maximo = 150
for nuemero in primos(maximo):
    print(nuemero)