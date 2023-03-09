numero1 = 5
numero2 = 6
cadena1='Hola'
cadena2='Hola'

print(numero1 == numero2)
print(cadena1 == cadena2)

print(numero1 <= numero2)

cadena1 = 'Holaa'
if(cadena1 == 'Hola'):
    print('Dijo si')
else:
    print('Dijo no')
    
    
cadena1 = 'Holaa'
if(cadena1 != 'Hola'):
    print('Dijo si')
else:
    print('Dijo no')
    
print('Digite los numeros a comparar')

numero1= input()
numero2= input()

if(numero1 != numero2):
    print('son diferentes')
else:
    print('No son diferentes')
    
if(numero1 > numero2):
    print('el numero '+str(numero1)+' es mayor que el número'+ str(numero2))
else:
    print('El número '+str(numero2)+' es mayor que el número '+str(numero1))