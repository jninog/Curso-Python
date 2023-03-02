minimo = 20
maximo = 500

print('Inserte un valor')
dato = input()

numero = int(dato)

if(numero<minimo):
    print('Valor bajo')
elif(numero>maximo):
    print('Valor alto')
else:
    print('Valor Medio')