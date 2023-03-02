numeros =[1,2,3,4,5,6,7,8,9,10]
print(numeros)

print('Introduzca su número a validar en la lista')
dato = input()
numero = int(dato)

if(numero in numeros):
    print('El número si esta en la lista')
else:
   print('El número no esta en la lista')